import random
import fpdf
import cv2
from tkinter import messagebox
import os
import win32api 
import win32print
from mis_herramientas import animaciones as anim
from mis_herramientas import panel_de_control as pan

def pdf(ev, can_plantillas,direccion_envio,lista_pdf):
        global contador
        contador = contador + 1
        if contador > can_plantillas-1:
            contador = 0
        
        print("\t\tINICIA EL METODO DE PDF")

        while anim.escuchador.is_alive():

            # numero_al = random.randint(0,5)
            numero_al = contador
            print(f"SE USO LA PLANTILLA NO. {numero_al+1}")

            pdf = fpdf.FPDF()
            pdf.add_page()
            # Agregamos una imagen


            pdf.image(f"{direccion_envio}/secion "+ str(ev) + "/imagen 0.jpg",13,11,89,67)

            pdf.image(f"{direccion_envio}/secion "+ str(ev) + "/imagen 1.jpg",108,11,89,67)

            pdf.image(f"{direccion_envio}/secion "+ str(ev) + "/imagen 2.jpg",13,84,89,67)

            pdf.image(f"{direccion_envio}/secion "+ str(ev) + "/imagen 3.jpg",108,84,89,67)

            pdf.image(f"{direccion_envio}/secion "+ str(ev) + "/imagen 4.jpg",13,157,89,67)

            pdf.image(f"{direccion_envio}/secion "+ str(ev) + "/imagen 5.jpg",108,157,89,67)

            # pdf.image("plantillas/Plantilla cabina " + str(numero_al) + ".png", 0, 0)

            pdf.image(lista_pdf[numero_al], 0, 0)


            cadena = f"{direccion_envio}/secion "+ str(ev) + "/documento.pdf"
            # Guardamos el documento
            pdf.output(cadena)
            print(f"EL PDF SE GUARDO EN: {cadena}")
            break

def plantilla_face(ev, direccion_de_envio,plantilla_de_face):

        print("\t\tINICIA EL METODO DE PANTILLA FACEBOOK")

        while anim.escuchador.is_alive():
            for k in range(6):
                img_foto = cv2.imread(f"{direccion_de_envio}/secion {ev}/imagen " + str(k) + ".jpg")
                img_face = cv2.imread(plantilla_de_face,cv2.IMREAD_UNCHANGED)
                alto, ancho, _ = img_foto.shape
                img_face = cv2.resize(img_face,(ancho,alto))
                img_foto = cv2.cvtColor(img_foto,cv2.COLOR_BGR2BGRA)
                for i in range(img_face.shape[0]):
                    for j in range(img_face.shape[1]):
                        if (img_face[i,j][3]!=0):
                            img_foto[i,j] = img_face[i,j]

                img_foto = cv2.cvtColor(img_foto,cv2.COLOR_BGRA2BGR)
                cadena = f"{direccion_de_envio}/secion "+ str(ev)+ f"/imagen face no {k+1}.jpg"
                cv2.imwrite(cadena,img_foto) 
                print(f"DIRECCION DE LA FOTO CON PLANTILLA DE FECEBBOK {k+1}: {cadena}")           

            break

def video_face (ev, direccion_de_envio,plantilla_red):
        img_array = []
        print("\t\tINICIO DEL METODO DEL VIDEO DE FECEBOOK")
        while anim.escuchador.is_alive():
            for k in range(6):
                img_foto = cv2.imread(f"{direccion_de_envio}/secion {ev}/imagen " + str(k) + ".jpg")
                alto, ancho, _ = img_foto.shape
                img_face = cv2.imread(plantilla_red,cv2.IMREAD_UNCHANGED)
                img_face = cv2.resize(img_face,(ancho,alto))
                img_foto = cv2.cvtColor(img_foto,cv2.COLOR_BGR2BGRA)
                for i in range(img_face.shape[0]):
                    for j in range(img_face.shape[1]):
                        if (img_face[i,j][3]!=0):
                            img_foto[i,j] = img_face[i,j]

                img_foto = cv2.cvtColor(img_foto,cv2.COLOR_BGRA2BGR)
                img_array.append(img_foto)

            alto, ancho = img_foto.shape[:2]

            cadena = f"{direccion_de_envio}/secion {ev}/video face.mp4"

            video = cv2.VideoWriter(cadena,cv2.VideoWriter_fourcc(*'mp4v'),2,(ancho,alto))
            
            for i in range(6):
                video.write(img_array[i])

            print(f"VIDEO YA CREADO EN: {cadena}")
            video.release()

            break

def exit():
    os.system("cls")
    messagebox.showinfo(message="Pocesos y sistemas apagados", title="on/off")            
    print("programa cerrado")


def entrega_prod(opcion, ev ):
    if opcion == "1":
        plantilla_face(ev = ev,
                    direccion_de_envio = pan.ruta_de_secion,
                    plantilla_de_face = pan.pla_face)

    elif opcion == "2":
        video_face(ev = ev,
                    direccion_de_envio = pan.ruta_de_secion,
                    plantilla_red = pan.pla_face)

    elif opcion == "3":
        plantilla_face(ev = ev,
                    direccion_de_envio = pan.ruta_de_secion,
                    plantilla_de_face = pan.pla_face)

        video_face(ev = ev,
                    direccion_de_envio = pan.ruta_de_secion,
                    plantilla_red = pan.pla_face)

def imprimir(ev, direccion_de_envio):
    print("\t\tINICIA EL METODO IMPRIMIR")
    ruta_de_impresion =f"{direccion_de_envio}/secion "+ str(ev) + "/documento.pdf"
    while anim.escuchador.is_alive():

        win32api.ShellExecute(0,
                            'print',
                            ruta_de_impresion,
                            win32print.GetDefaultPrinter(),
                            '.',
                            0)
        impresora_pred = win32print.GetDefaultPrinter()
        print(f"EL PDF YA SE MANDO A IMPRIMIR A LA IMPRESORA: {impresora_pred}")
        break

def impresion_no(ev):
    
    file = open("imp_no_validas.txt", "a")
    file.write(f"\nLA SECION NO. {ev} NO SE IMPRIMIO")
    file = open("imp_no_validas.txt")
    print(file.read())
    file.close()

contador = -1

def actualizar():
    file = open("imp_no_validas.txt", "w")
    file.write("")
    file.close()