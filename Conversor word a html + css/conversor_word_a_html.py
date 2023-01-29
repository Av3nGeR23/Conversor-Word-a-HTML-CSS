import os
import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup
from docx import Document

# Crear una ventana selección de archivos múltiples
root = tk.Tk()
root.withdraw()
file_paths = filedialog.askopenfilenames()

# Recorrer cada archivo seleccionado
for file_path in file_paths:
    # Abre el documento
    document = Document(file_path)
    # Crear un objeto BeautifulSoup
    soup = BeautifulSoup('', 'html.parser')
    # Crear una estructura básica de HTML
    doctype = soup.new_tag("!DOCTYPE")
    doctype.string = ""
    html = soup.new_tag('html')
    html.attrs = {'lang': 'en'}
    head = soup.new_tag('head')
    body = soup.new_tag('body')
    meta1 = soup.new_tag('meta')
    meta1.attrs = {'charset': 'UTF-8'}
    meta2 = soup.new_tag('meta')
    meta2.attrs = {'http-equiv': 'X-UA-Compatible', 'content': 'IE=edge'}
    meta3 = soup.new_tag('meta')
    meta3.attrs = {'name': 'viewport',
                   'content': 'width=device-width, initial-scale=1.0'}
    title = soup.new_tag('title')
    title.string = 'Document'
    soup.append(doctype)
    soup.append(html)
    html.append(head)
    head.append(meta1)
    head.append(meta2)
    head.append(meta3)
    head.append(title)
    html.append(body)
    # Agregar el contenido del Word en la etiqueta <body>
    for para in document.paragraphs:
        p = soup.new_tag('p')
        p.string = para.text
        body.append(p)
    # Obtiene  el nombre del archivo original
    file_name = os.path.splitext(file_path)[0]

    # Crear un nombre de archivo para el HTML
    html_file = file_name + '.html'

    # Escribir el contenido HTML en el archivo
    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
    print(f'File {html_file} created')
print('Transformacion OK')
