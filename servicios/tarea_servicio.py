from modelos.tarea import Tarea


class TareaServicio:
    def __init__(self):
        # Lista interna encapsulada — nadie la toca directamente
        self._tareas = []

    def agregar(self, descripcion):
        """Crea y agrega una nueva tarea a la lista."""
        nueva = Tarea(descripcion)
        self._tareas.append(nueva)
        return nueva

    def completar(self, tarea_id):
        """Cambia el estado de una tarea a completada."""
        for tarea in self._tareas:
            if tarea.id == tarea_id:
                tarea.completada = True
                return True
        return False

    def eliminar(self, tarea_id):
        """Elimina una tarea por su ID."""
        for tarea in self._tareas:
            if tarea.id == tarea_id:
                self._tareas.remove(tarea)
                return True
        return False

    def listar(self):
        """Devuelve una copia de la lista de tareas."""
        return list(self._tareas)