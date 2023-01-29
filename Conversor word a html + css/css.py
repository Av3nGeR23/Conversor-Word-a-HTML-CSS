import os
import tkinter as tk
from tkinter import filedialog

# Crear una ventana selección de archivos múltiples
root = tk.Tk()
root.withdraw()
file_paths = filedialog.askopenfilenames()

#  plantilla de estilo CSS
hoja_estilo = '''
<style>
  body {
    font-family: Comic Sans;
    font-size: 16px;
    color: #A9A9A9;
    background-color:#008B8B;
  }

  h1, h2, h3 {
    font-weight: bold;
  }

  h1 {
    font-size: 36px;
  }

  h2 {
    font-size: 28px;
  }

  h3 {
    font-size: 24px;
  }
</style>
'''

# Recorrer cada archivo seleccionado
for file_path in file_paths:
    # Leer el contenido del archivo HTML
    with open(file_path, 'r',encoding="utf-8") as file:
        content = file.read()
    # Insertar el estilo CSS en la cabecera del HTML
    content = content.replace('</head>', hoja_estilo + '\n</head>')
    # Escribir el contenido modificado en el archivo HTML
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(content)
    print(f'Archivo {file_path} css cargado ')
print('Proceso OK')