# GUI-APP

Aplicación de escritorio desarrollada con Python y Tkinter para gestionar tareas diarias.

## Requisitos
- Python 3.x (sin librerías externas para ejecutar)
- PyInstaller (solo para generar el ejecutable)

## Cómo ejecutar
```bash
python main.py
```

## Generar ejecutable
```bash
pip install pyinstaller
pyinstaller --noconsole --onefile --name TkMiApp main.py
```

El ejecutable se generará en la carpeta `dist/`.

## Arquitectura
- `modelos/` → Clase Tarea
- `servicios/` → Lógica CRUD de tareas
- `ui/` → Interfaz gráfica con Tkinter y manejo de eventos
- `main.py` → Punto de entrada
```

**Archivo:** `.gitignore`
```
# PyInstaller
build/
dist/
*.spec

# Python
__pycache__/
*.pyc