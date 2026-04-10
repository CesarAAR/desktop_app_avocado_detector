import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog
import threading
import os
import zipfile
import csv
import shutil
import tempfile

from .components.imageView import ImageCanvas
from .components.image_sidebar import ImageSideBar
from .components.metricsTable import MetricsTable

class MainWindow(ttk.Frame):
    def __init__(self, root, detector):
        self.root = root
        self.detector = detector
        self.processed_images = {} 
        self.temp_dir = tempfile.mkdtemp(prefix="fruit_app_")

        self.__setup_ui()

    def __setup_ui(self):
        top_bar = ttk.Frame(self.root, padding=10)
        top_bar.pack(fill=X)

        self.btn_load = ttk.Button(
            top_bar,
            text="+ Cargar Imagen",
            command=self._on_upload_click,
            bootstyle="success"
        )

        self.btn_load.pack(side=LEFT, padx=5)

        self.btn_export_zip = ttk.Button(
            top_bar, text="Exportar Imágenes (ZIP)", 
            command=self._on_export_zip, bootstyle="info-outline"
        )
        self.btn_export_zip.pack(side=LEFT, padx=5)

        self.btn_export_csv = ttk.Button(
            top_bar, text="Exportar Métricas (CSV)", 
            command=self._on_export_csv, bootstyle="info-outline"
        )
        self.btn_export_csv.pack(side=LEFT, padx=5)

        main_layout = ttk.Frame(self.root)
        main_layout.pack(fill=BOTH, expand=True, padx=5, pady=5)
        
        self.sidebar = ImageSideBar(main_layout, on_select_callback=self._on_item_selected)
        self.sidebar.config(width=250)
        self.sidebar.pack(side=LEFT, fill=Y)
        self.sidebar.pack_propagate(False)

        self.canvas = ImageCanvas(main_layout)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True, padx=5)

        self.table = MetricsTable(main_layout)
        self.table.config(width=400)
        self.table.pack(side=LEFT, fill=Y)
        self.table.pack_propagate(False)

    def _on_upload_click(self):

        file_path = filedialog.askopenfilename(
            title="Seleccionar imagen",
            filetypes=[("Imágenes", "*.jpg *.jpeg *.png *.webp")]
        )
        
        if not file_path:
            return

        self.btn_load.config(state=DISABLED)
        self.canvas.show_loading()

        hilo_deteccion = threading.Thread(
            target=self._procesar_en_segundo_plano, 
            args=(file_path,),
            daemon=True 
        )
        hilo_deteccion.start()

    def _procesar_en_segundo_plano(self, file_path):

        try:
            results = self.detector.detect(file_path)
 
            self.root.after(0, self._finalizar_procesamiento, file_path, results)
            
        except Exception as e:
            print(f"Error en detección: {e}")
            self.root.after(0, lambda: self.btn_load.config(state=NORMAL))

    def _finalizar_procesamiento(self, file_path, results):
        filename = os.path.basename(file_path)
        processed_path = os.path.join(self.temp_dir, f"detected_{filename}")
        
        results["annotated_image"].save(processed_path)
        
        self.processed_images[processed_path] = results

        stats = [
            results["count"], 
            results["avg_conf"], 
            results["min_conf"], 
            results["max_conf"]
        ]
        
        self.sidebar.add_image_item(filename, processed_path)
        self.table.add_row(filename, stats, processed_path) 
        
        self.canvas.display_image(results["annotated_image"])
        self.btn_load.config(state=NORMAL)

    def _on_item_selected(self, path):
        if path in self.processed_images:
            data = self.processed_images[path]
            self.canvas.display_image(data["annotated_image"])

    def _on_export_csv(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV file", "*.csv")],
            title="Guardar métricas como..."
        )
        if not file_path:
            return

        try:
            tree = self.table.tree
            with open(file_path, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["Archivo", "Conteo", "Conf. Promedio", "Conf. Mínima", "Conf. Máxima"])
                
                for item in tree.get_children():
                    row = tree.item(item)['values']
                    writer.writerow(row[:-1])
            
            ttk.dialogs.Messagebox.show_info("Exportación exitosa", "El archivo CSV se ha guardado correctamente.")
        except Exception as e:
            ttk.dialogs.Messagebox.show_error(f"Error al exportar CSV: {e}", "Error")

    def _on_export_zip(self):
        zip_path = filedialog.asksaveasfilename(
            defaultextension=".zip",
            filetypes=[("ZIP file", "*.zip")]
        )
        if not zip_path: return

        try:
            tree = self.table.tree
            with zipfile.ZipFile(zip_path, 'w') as zip_file:
                for item in tree.get_children():
                    row = tree.item(item)['values']
                    img_processed_path = row[5] 
                    clean_name = row[0] 
                    
                    if os.path.exists(img_processed_path):
                        zip_file.write(img_processed_path, arcname=f"RESULTADO_{clean_name}")
            
            ttk.dialogs.Messagebox.show_info("Se generó y exportó el ZIP exitosamente", "ZIP generado con imágenes etiquetadas.")
        except Exception as e:
            ttk.dialogs.Messagebox.show_error(f"Error: {e}", "Error")

    def on_closing(self):
        try:
            if hasattr(self, 'temp_dir') and os.path.exists(self.temp_dir):
                import shutil
                shutil.rmtree(self.temp_dir) 
                print("Carpeta temporal eliminada con éxito.")
        except Exception as e:
            print(f"No se pudo limpiar la carpeta temporal: {e}")
        finally:
            self.root.destroy()