import ttkbootstrap as ttk
from src.gui.main_window import MainWindow
from src.core.detector import FruitDetector 
import os
import sys

def get_resource_path(relative_path):
    
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    root = ttk.Window(title="Fruit Detection", themename="darkly")
    root.geometry("1200x700")

    path_al_modelo = get_resource_path("models/best.pt")

    detector = FruitDetector(model_path=path_al_modelo)

    app = MainWindow(root, detector)

    root.protocol("WM_DELETE_WINDOW", app.on_closing)

    root.mainloop()