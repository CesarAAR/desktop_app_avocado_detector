import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class MetricsTable(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        container = ttk.Frame(self)
        container.pack(fill=BOTH, expand=True)

        self.columns = ("file_name", "count", "avg_conf", "min_conf", "max_conf", "path")
        
        self.tree = ttk.Treeview(
            container, 
            columns=self.columns, 
            show="headings", 
            bootstyle="primary"
        )

        v_scrollbar = ttk.Scrollbar(container, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=v_scrollbar.set)
        
        h_scrollbar = ttk.Scrollbar(self, orient=HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscrollcommand=h_scrollbar.set)

        v_scrollbar.pack(side=RIGHT, fill=Y)
        self.tree.pack(side=TOP, fill=BOTH, expand=True)
        h_scrollbar.pack(side=BOTTOM, fill=X) 

        self.tree.heading("file_name", text="Archivo")
        self.tree.column("file_name", width=200, minwidth=150)

        self.tree.heading("count", text="Conteo")
        self.tree.column("count", width=100, minwidth=80, anchor=CENTER)

        self.tree.heading("avg_conf", text="Conf. Promedio")
        self.tree.column("avg_conf", width=150, minwidth=120, anchor=CENTER)

        self.tree.heading("min_conf", text="Conf. Mínima")
        self.tree.column("min_conf", width=150, minwidth=120, anchor=CENTER)

        self.tree.heading("max_conf", text="Conf. Máxima")
        self.tree.column("max_conf", width=150, minwidth=120, anchor=CENTER)

        self.tree.column("path", width=0, stretch=NO)

    def add_row(self, file_name, stats_list, file_path):
        row_data = (file_name, *stats_list, file_path)
        self.tree.insert("", END, values=row_data)