import tkinter as tk
from tkinter import ttk, messagebox


class AppTkinter:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio
        self.root.title("Lista de Tareas")
        self.root.geometry("580x420")
        self.root.resizable(False, False)

        self._construir_formulario()
        self._construir_botones()
        self._construir_tabla()
        self._configurar_estilos()

    # ── Estilos visuales ────────────────────────────────────
    def _configurar_estilos(self):
        """Define el estilo visual para las tareas completadas (texto gris)."""
        self.style = ttk.Style()
        # Tag para tareas completadas: texto gris y con prefijo [Hecho]
        self.tabla.tag_configure("completada", foreground="gray")

    # ── Formulario ──────────────────────────────────────────
    def _construir_formulario(self):
        frame = tk.LabelFrame(self.root, text="Nueva Tarea", padx=10, pady=8)
        frame.pack(fill="x", padx=15, pady=10)

        tk.Label(frame, text="Descripción:").grid(row=0, column=0, sticky="w")
        self.entry_descripcion = tk.Entry(frame, width=45)
        self.entry_descripcion.grid(row=0, column=1, padx=10)

        # EVENTO DE TECLADO: agregar tarea al presionar Enter en el Entry
        self.entry_descripcion.bind("<Return>", self._agregar_desde_teclado)

    # ── Botones ─────────────────────────────────────────────
    def _construir_botones(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=5)

        tk.Button(frame, text="Añadir Tarea", width=14, bg="#4CAF50", fg="white",
                  command=self._agregar).grid(row=0, column=0, padx=6)

        tk.Button(frame, text="Marcar Completada", width=16, bg="#2196F3", fg="white",
                  command=self._completar).grid(row=0, column=1, padx=6)

        tk.Button(frame, text="Eliminar", width=14, bg="#f44336", fg="white",
                  command=self._eliminar).grid(row=0, column=2, padx=6)

    # ── Tabla ────────────────────────────────────────────────
    def _construir_tabla(self):
        frame = tk.LabelFrame(self.root, text="Mis Tareas", padx=10, pady=8)
        frame.pack(fill="both", expand=True, padx=15, pady=10)

        columnas = ("id", "descripcion", "estado")
        self.tabla = ttk.Treeview(frame, columns=columnas, show="headings", height=10)

        self.tabla.heading("id", text="ID")
        self.tabla.heading("descripcion", text="Descripción")
        self.tabla.heading("estado", text="Estado")

        self.tabla.column("id", width=40, anchor="center")
        self.tabla.column("descripcion", width=370)
        self.tabla.column("estado", width=90, anchor="center")

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)

        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # EVENTO DE RATÓN: doble clic sobre una fila marca la tarea como completada
        self.tabla.bind("<Double-1>", self._completar_doble_clic)

    # ── Acciones ─────────────────────────────────────────────
    def _agregar(self):
        descripcion = self.entry_descripcion.get().strip()
        if not descripcion:
            messagebox.showwarning("Campo vacío", "Escribe una descripción para la tarea.")
            return
        self.servicio.agregar(descripcion)
        self._actualizar_tabla()
        self.entry_descripcion.delete(0, tk.END)
        self.entry_descripcion.focus()

    def _agregar_desde_teclado(self, evento):
        """Manejador del evento <Return>: llama al mismo método de agregar."""
        self._agregar()

    def _completar(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Sin selección", "Selecciona una tarea de la lista.")
            return
        tarea_id = int(self.tabla.item(seleccion[0])["values"][0])
        self.servicio.completar(tarea_id)
        self._actualizar_tabla()

    def _completar_doble_clic(self, evento):
        """Manejador del evento <Double-1>: marca como completada con doble clic."""
        seleccion = self.tabla.selection()
        if seleccion:
            tarea_id = int(self.tabla.item(seleccion[0])["values"][0])
            self.servicio.completar(tarea_id)
            self._actualizar_tabla()

    def _eliminar(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Sin selección", "Selecciona una tarea de la lista.")
            return
        tarea_id = int(self.tabla.item(seleccion[0])["values"][0])
        descripcion = self.tabla.item(seleccion[0])["values"][1]
        confirmar = messagebox.askyesno("Confirmar", f"¿Eliminar la tarea '{descripcion}'?")
        if confirmar:
            self.servicio.eliminar(tarea_id)
            self._actualizar_tabla()

    def _actualizar_tabla(self):
        """Borra y recarga todas las filas de la tabla desde el servicio."""
        for row in self.tabla.get_children():
            self.tabla.delete(row)
        for tarea in self.servicio.listar():
            estado = "[Hecho]" if tarea.completada else "Pendiente"
            # Aplica el tag 'completada' para cambiar el color a gris si está hecha
            tag = "completada" if tarea.completada else ""
            self.tabla.insert("", "end",
                              values=(tarea.id, tarea.descripcion, estado),
                              tags=(tag,))