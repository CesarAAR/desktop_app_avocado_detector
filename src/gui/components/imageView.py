import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

class ImageCanvas(ttk.Frame):
    def __init__(self, master, **kwargs):
            super().__init__(master, bootstyle="secondary", **kwargs)

            self.image_label = ttk.Label(self, text="Seleccione una imagen para procesar", anchor=CENTER)
            self.image_label.pack(fill=BOTH, expand=True, padx=10, pady=10)

            self.current_image_tk = None

    def display_image(self, image_source):
        try:
            if isinstance(image_source, str):
                img = Image.open(image_source)
            else:
                img = image_source

            self.update_idletasks() 
            container_width = self.winfo_width()
            container_height = self.winfo_height()

            if container_width < 10: container_width = 800
            if container_height < 10: container_height = 600

            img.thumbnail((container_width, container_height), Image.Resampling.LANCZOS)

            self.current_image_tk = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.current_image_tk, text="")
            
        except Exception as e:
            self.image_label.config(text=f"Error al cargar imagen: {e}")

    def show_loading(self):
        self.image_label.config(image="", text="Analizando imagen...\nPor favor, espere.")
        self.update_idletasks()

    def clear(self):
        self.current_image_tk = None # Liberamos la imagen de la RAM
        self.image_label.config(image="", text="Seleccione una imagen para procesar")