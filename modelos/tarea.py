class Tarea:
    # Contador de clase para generar IDs únicos automáticamente
    _contador_id = 1

    def __init__(self, descripcion):
        self.id = Tarea._contador_id
        self.descripcion = descripcion
        self.completada = False  # Estado inicial: pendiente
        Tarea._contador_id += 1