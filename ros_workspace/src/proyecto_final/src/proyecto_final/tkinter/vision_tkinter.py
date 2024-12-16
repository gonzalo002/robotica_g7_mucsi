#!/usr/bin/python3

import os
# Configurar la variable de entorno para que no aparezcan mensajes de error de index de camara
os.environ["OPENCV_LOG_LEVEL"] = "FATAL"

import ttkbootstrap as ttk
from vision_tab import VisionTab
#from TKINTER.camera_controller import CameraController

class DynamicTabsApp:
    def __init__(self):
        # --- ROOT ---
        self.root = ttk.Window(title="", themename="custom-vision")
        self.root.resizable(True, True)  # Permitir redimensionar la ventana
        self.root.attributes('-zoomed', True) 
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)


        #Al finalizar
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)

        # Crear un notebook (pestañas)
        self.estilo()
        self.create_notebook()
        #self.vision_tab()
        self.root.mainloop()

    
    def create_notebook(self):

        # --- NOTEBOOK FRAME: Visión ---
        self.tab_vision = ttk.Frame(self.root)
        self.tab_vision.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
        self.tab_vision.grid_columnconfigure(0, weight=1)
        self.tab_vision.grid_rowconfigure(0, weight=1)
        self.VisionTab = VisionTab(self.root, self.tab_vision, True)



    def estilo(self):
        style = ttk.Style()
        style.configure("Custom.TNotebook.Tab",
            font= ("Montserrat Medium", 12), 
            background= "white",
            )

        style.configure("Custom.TNotebook",
            background= "white",
            )

        style.configure("Custom.TFrame",
            font= ("Montserrat Medium", 12), 
            background= "white",
            borderwidth=0,  # Grosor del borde
            )

        style.map(
            "Custom.TNotebook.Tab",
            background=[("selected", "#8C85F7"), ("active", "#8C85F7"), ("!selected", "white")],     # Background color when hovered
            foreground=[("selected", "black"), ("active", "black"), ("!selected", "black")],   # Text color when hovered
        )

        style.configure("Vision.TNotebook.Tab",
            font= ("Montserrat Medium", 10), 
            background= "white",
            borderwidth=0,  # Grosor del borde
            )

        style.configure("Vision.TNotebook",
            background= "white",
            borderwidth=0
            )

        style.configure("Custom.TFrame",
            font= ("Montserrat Medium", 12), 
            background= "white",
            borderwidth=0,  # Grosor del borde
            )

        style.map(
            "Vision.TNotebook.Tab",
            background=[("selected", "#C5C1F7"), ("active", "#C5C1F7"), ("!selected", "white")],     # Background color when hovered
            foreground=[("selected", "black"), ("active", "black"), ("!selected", "black")],   # Text color when hovered
        )

        style.configure(
        "TCheckbutton",  # Nombre del estilo
        font=("Montserrat", 10),  # Fuente personalizada
        )

        style.configure(
        "TButton",  # Nombre del estilo
        font=("Montserrat", 10),  # Fuente personalizada
        )

        style.configure(
        "TLabelframe.Label",  # Nombre del estilo
            font=("Montserrat", 10),
        )


    def _on_closing(self):
        """Esta función se ejecuta cuando la ventana se cierra."""
        self.VisionTab.camera_controller.stop()
        
        # Cerrar la ventana de Tkinter
        self.root.destroy()
        exit()

if __name__ == "__main__":

    app = DynamicTabsApp()
    