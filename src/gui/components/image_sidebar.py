import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class ImageSideBar(ttk.Frame):
    def __init__(self, master, on_select_callback, **kwargs):

        super().__init__(master, bootstyle="light", **kwargs)
        self.on_select_callback = on_select_callback

        lbl = ttk.Label(
            self, 
            text="IMÁGENES PROCESADAS", 
            font=("Helvetica", 10, "bold"),
            bootstyle="inverse-light",
            anchor=CENTER
        )
        lbl.pack(fill=X, pady=10, padx=5)

        container = ttk.Frame(self)
        container.pack(fill=BOTH, expand=True, padx=5, pady=5)


        scrollbar = ttk.Scrollbar(container, bootstyle="round")
        scrollbar.pack(side=RIGHT, fill=Y)

        self.tree = ttk.Treeview(
            container, 
            columns=("filename"), 
            show="tree", 
            selectmode="browse",
            yscrollcommand=scrollbar.set,
            bootstyle="primary"
        )
        self.tree.pack(side=LEFT, fill=BOTH, expand=True)
        

        scrollbar.config(command=self.tree.yview)

        self.tree.bind("<<TreeviewSelect>>", self._on_item_selected)

    def add_image_item(self, filename, full_path):

        self.tree.insert("", END, iid=full_path, text=f" 📄 {filename}")

    def _on_item_selected(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            path = selected_item[0]
            self.on_select_callback(path)

    def clear(self):
        for item in self.tree.get_children():
            self.tree.delete(item)