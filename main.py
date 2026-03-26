import tkinter as tk
from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import AppTkinter


def main():
    # Inyección de dependencias: el servicio se crea aquí y se pasa a la UI
    servicio = TareaServicio()
    root = tk.Tk()
    AppTkinter(root, servicio)
    root.mainloop()


if __name__ == "__main__":
    main()