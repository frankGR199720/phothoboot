"""from pynput.keyboard import Listener
from pywinauto import application

def on_press(key):
    if key.char == 'p':
        # Simular la acción de imprimir (ajusta según tu aplicación)
        app = application.Application().connect(path="C:/Users/ATM-DESING4/Documents/evento3/secion 1/documento.pdf")  # Reemplaza 'acrobat.exe' con la ruta correcta
        dlg = app.window(title_re=".Adobe Acrobat DC.")
        dlg.menu_select("File->Print")

        # Configurar Adobe Acrobat para guardar como PDF (ajusta según tu configuración)
        print_dlg = dlg.child_window(title_re=".Print.")
        print_dlg.child_window(title="Printer", control_type="ComboBox").select("Adobe PDF")
        print_dlg.child_window(title="Properties", control_type="Button").click()
        # ... Otras configuraciones necesarias ...
        print_dlg.child_window(title="OK", control_type="Button").click()

        # Simular la impresión (ajusta según tu configuración)
        print_dlg.child_window(title="Print", control_type="Button").click()

# Escuchar por las pulsaciones del teclado
with Listener(on_press=on_press) as listener:
    listener.join()"""
from pynput.keyboard import Listener
from pywinauto import application

def guardar_como_pdf(ruta_pdf):
    """Simula la impresión y guarda el documento como PDF en la ruta especificada.

    Args:
        ruta_pdf (str): Ruta completa donde se guardará el PDF.
    """
    # ... (Código para simular la impresión y configurar Adobe Acrobat, similar al código anterior)
    # Asegúrate de ajustar la configuración de Adobe Acrobat para guardar en la ruta especificada

def cambiar_modo_impresion():
    """Cambia el modo de impresión entre imprimir físicamente y guardar como PDF."""
    global modo_impresion  # Variable global para rastrear el modo actual
    modo_impresion = not modo_impresion  # Invierte el modo
    if modo_impresion:
        print("Modo impresión activado.")
    else:
        print("Modo guardar PDF activado.")

def on_press(key):
    if key.char == 'p':
        cambiar_modo_impresion()
        if not modo_impresion:
            
            guardar_como_pdf("C:/Users/ATM-DESING4/Documents/evento3/secion 1/documento.pdf")

# Variable global para rastrear el modo de impresión
modo_impresion = True

with Listener(on_press=on_press) as listener:
    listener.join()