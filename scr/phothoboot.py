import cv2                                  #pip install opencv-contrib-python
import fpdf                                 #pip install fpdf
import random                               
import win32api                             #pip install win-api
import win32print
from pynput import keyboard as kb           #pip install pynput
from tkinter import messagebox, ttk
import tkinter as tk
import os
import datetime as dt
import shutil as sh
import serial
import time

direccion_de_seciones_guardadas = "seciones guardadas/"
nombre_secion = dt.datetime.now().strftime('secion %d-%m-%y-%H-%M')
direccion_de_seciones_en_album = "album de fotos/carpeta "

class Panel_control():
    def init_arduino ():
        com = input("pon el puerto com del arduino: ")

        return com

    def creacion_de_evento ():
        
        while True:
            letrero = """
//                              _                   _      _                        _         
//      ___ _ __ ___  __ _  ___(_) ___  _ __     __| | ___| |   _____   _____ _ __ | |_ ___   
//     / __| '__/ _ \/ _` |/ __| |/ _ \| '_ \   / _` |/ _ | |  / _ \ \ / / _ | '_ \| __/ _ \  
//    | (__| | |  __| (_| | (__| | (_) | | | | | (_| |  __| | |  __/\ V |  __| | | | || (_) | 
//     \___|_|  \___|\__,_|\___|_|\___/|_| |_|  \__,_|\___|_|  \___| \_/ \___|_| |_|\__\___/  
//                                                                                            """
            print(letrero)
            rut_de_event = input("ruta de almacenamiento: ")
            nom_eve = input("nombre del evento:")
            rut_de_carpeta = rut_de_event + '/' + nom_eve
            print(rut_de_carpeta)
            if os.path.exists(rut_de_carpeta):
                print("El directorio ya fue creada favor de crear un nuevo directorio")
                time.sleep(2)
            os.system("cls")
            if not os.path.exists(rut_de_carpeta):
                os.makedirs(rut_de_carpeta)
                time.sleep(2)
                os.system("cls")
                return rut_de_carpeta
                break    

    def cal_camara ():
        no_cam = 0
        letrero = """
//                                              _                  _ _ _                    _                   _                                            
//   _ __  _ __ ___   ___ ___ ___  ___     __| | ___    ___ __ _| (_| |__  _ __ __ _  ___(_) ___  _ __     __| | ___    ___ __ _ _ __ ___   __ _ _ __ __ _ 
//  | '_ \| '__/ _ \ / __/ _ / __|/ _ \   / _` |/ _ \  / __/ _` | | | '_ \| '__/ _` |/ __| |/ _ \| '_ \   / _` |/ _ \  / __/ _` | '_ ` _ \ / _` | '__/ _` |
//  | |_) | | | (_) | (_|  __\__ | (_) | | (_| |  __/ | (_| (_| | | | |_) | | | (_| | (__| | (_) | | | | | (_| |  __/ | (_| (_| | | | | | | (_| | | | (_| |
//  | .__/|_|  \___/ \___\___|___/\___/   \__,_|\___|  \___\__,_|_|_|_.__/|_|  \__,_|\___|_|\___/|_| |_|  \__,_|\___|  \___\__,_|_| |_| |_|\__,_|_|  \__,_|
//  |_|                                                                                                                                                                                                                                                                                                               """
        print(letrero)
        print("Presione ENTER para seleccionar la camara o preisone SPACE para pasar a la siguiente camara")
        while True:
            isclosed_1 = 0
            isclosed_2 = 0
            
            camara=cv2.VideoCapture(no_cam,cv2.CAP_DSHOW)
            print(f"Camara no. {no_cam+1}")
            while True:
                ret, frames = camara.read()
                
                if ret == True:
                    frames = cv2.flip(frames,1)
                    cv2.imshow("vista previa de la camara",frames)
                    opcion = cv2.waitKey(1)
                    if opcion == 13:
                        print("opcion aceptada")
                        isclosed_1 = 1
                        isclosed_2 = 1
                        
                        break    
                    elif opcion == 32:
                        print("opcion no aceptada")
                        isclosed_2 = 1
                        no_cam = no_cam + 1
                        
                        break

                elif ret == False:
                    print(f"no xiste la camara no {no_cam+1} se regresa al inicio")
                    no_cam = 0
                    break   
            
                elif isclosed_2:
                    
                    break
            
            if isclosed_1:
                
                break
            
        cv2.destroyAllWindows()
        time.sleep(2)
        os.system("cls")
        return no_cam

    
        return direc_de_assets, list_de_archivos

    def pdf_start():
        while True:
            letrero = """
//                                            _        _       _      _             _                  _  __ 
//   _ __  _ __ ___   ___ ___ ___  ___     __| | ___  (_)_ __ (_) ___(_) ___     __| | ___   _ __   __| |/ _|
//  | '_ \| '__/ _ \ / __/ _ / __|/ _ \   / _` |/ _ \ | | '_ \| |/ __| |/ _ \   / _` |/ _ \ | '_ \ / _` | |_ 
//  | |_) | | | (_) | (_|  __\__ | (_) | | (_| |  __/ | | | | | | (__| | (_) | | (_| |  __/ | |_) | (_| |  _|
//  | .__/|_|  \___/ \___\___|___/\___/   \__,_|\___| |_|_| |_|_|\___|_|\___/   \__,_|\___| | .__/ \__,_|_|  
//  |_|                                                                                     |_|           """
            print(letrero)
            direc_de_assets = input("ingresa la  direccion de busqueda de los assets: ")
            list_de_archivos = os.listdir(direc_de_assets)
            valor = 1
            for i in list_de_archivos:
                print(f"opcion {valor}: ",i)
                valor = valor+1
            opcion2 = input("¿Desea hacer una nueva consulta? Si/No: ")
            if opcion2 == "Si":
                
                time.sleep(2)
                os.system("cls")
            elif opcion2 == "No":
                break
            else:
                print("nop es la opcion deseada")
                time.sleep(2)
                os.system("cls")
                time.sleep(2)

        cant_fotos = int(input("cuantas plantillas deseas; 1, 3 y/o 5: "))

        list_pla = []
        for x in range(cant_fotos):
            opcion = int(input(f"escoge la opcion de la lista para la plantilla no {x+1}: "))
            url_plant= direc_de_assets + "/" + list_de_archivos[opcion-1]
            print(url_plant)
            list_pla.append(url_plant)

        os.system("cls")

        return cant_fotos,list_pla

    def nombre_impresora():
        letrero = """  
//                       _                    _        _         _                                               
// _ __   ___  _ __ ___ | |__  _ __ ___    __| | ___  | | __ _  (_)_ __ ___  _ __  _ __ ___  ___  ___  _ __ __ _ 
//| '_ \ / _ \| '_ ` _ \| '_ \| '__/ _ \  / _` |/ _ \ | |/ _` | | | '_ ` _ \| '_ \| '__/ _ \/ __|/ _ \| '__/ _` |
//| | | | (_) | | | | | | |_) | | |  __/ | (_| |  __/ | | (_| | | | | | | | | |_) | | |  __/\__ \ (_) | | | (_| |
//|_| |_|\___/|_| |_| |_|_.__/|_|  \___|  \__,_|\___| |_|\__,_| |_|_| |_| |_| .__/|_|  \___||___/\___/|_|  \__,_|
//                                                                          |_|                                  """
        print(letrero)
        impresora_pred = win32print.GetDefaultPrinter()
        print("la impresora es: ", impresora_pred)
        time.sleep(4)
        os.system("cls")

    def entrega_digital():
        while True:
            letrero = """
//                    __       _                            _            _           __ _             _ 
//    ___ ___  _ __  / _|   __| | ___   _ __  _ __ ___   __| |_   _  ___| |_ ___    / _(_)_ __   __ _| |
//   / __/ _ \| '_ \| |_   / _` |/ _ \ | '_ \| '__/ _ \ / _` | | | |/ __| __/ _ \  | |_| | '_ \ / _` | |
//  | (_| (_) | | | |  _| | (_| |  __/ | |_) | | | (_) | (_| | |_| | (__| || (_) | |  _| | | | | (_| | |
//   \___\___/|_| |_|_|    \__,_|\___| | .__/|_|  \___/ \__,_|\__,_|\___|\__\___/  |_| |_|_| |_|\__,_|_|
//                                     |_|                                                              """
            print(letrero)
            OPCION = 0
            menu = """
            Selecciona la opcion para la entrega de producto final
            [1] FOTOS 
            [2] VIDEO
            [3] FOTOS Y VIDEO
            si no desea una opcion poner otro numero 
            """
          
            print(menu)
            opcion = int(input("escribe la opcion deseada: "))
            seleccion = ""
            if opcion == 1:
                seleccion = "1"
                letrero = "FOTOS"
                break
            elif opcion == 2:
                seleccion = "2"
                letrero = "VIDEO"
                break
            elif opcion ==3:
                seleccion = "3"
                letrero = "FOTOS Y VIDEO"
                break
            else: 
                print("no es la opcion deseada")
                time.sleep(2)
                os.system("cls")
                break
        
        time.sleep(2)
        os.system("cls")
        return seleccion, letrero

    def mvideos_multimedia():

        while True:
            letrero = """
//            _ _                       _ _   _                    _ _       
//           | ( )                     | | | (_)                  | (_)      
// _   _ _ __| |/ ___   _ __ ___  _   _| | |_ _ _ __ ___   ___  __| |_  __ _ 
//| | | | '__| | / __| | '_ ` _ \| | | | | __| | '_ ` _ \ / _ \/ _` | |/ _` |
//| |_| | |  | | \__ \ | | | | | | |_| | | |_| | | | | | |  __/ (_| | | (_| |
// \__,_|_|  |_| |___/ |_| |_| |_|\__,_|_|\__|_|_| |_| |_|\___|\__,_|_|\__,_|
//                                                                           """
            print(letrero)
        
            direc_de_assets = input("ingresa la  direccion de busqueda de los assets: ")
            list_de_archivos = os.listdir(direc_de_assets)
            valor = 1
            for i in list_de_archivos:
                print(f"opcion {valor}: ",i)
                valor = valor+1
            opcion2 = input("¿Desea hacer una nueva consulta? Si/No: ")
            if opcion2 == "Si":
                
                time.sleep(2)
                os.system("cls")
            elif opcion2 == "No":
                break
            else:
                print("nop es la opcion deseada")
                time.sleep(2)
                os.system("cls")
                time.sleep(2)

        opcion = int(input("ingresa la opcion para el assets (Loading): "))

        load = direc_de_assets + "/" + list_de_archivos[opcion-1]

        print(load)

        opcion = int(input("ingresa la opcion para el assets (Protector de pantalla): "))

        prot_de_pan = direc_de_assets + "/" + list_de_archivos[opcion-1]

        print(prot_de_pan)

        

        
        list_cont = []
        for x in range(6):
            opcion = int(input(f"ingresa la opcion para el assets (Conteo No. {x+1}): ")) 
            list_cont.append(direc_de_assets + "/" + list_de_archivos[opcion-1])
            print(list_cont[x])

        opcion = int(input("ingresa la opcion para el assets (Imprimiendo): "))

        imp = direc_de_assets + "/" + list_de_archivos[opcion-1]

        print(imp)

        opcion = int(input("ingresa la opcion para el assets (Plantilla redes): "))

        face = direc_de_assets + "/" + list_de_archivos[opcion-1]

        print(face)

        time.sleep(2)
        os.system("cls")

        return load, prot_de_pan, list_cont, imp, face


    def cant_loop():
        cant = int(input("cuantos lops deseas: "))
        return cant
        

    def resumen(rut_evento,num_camara,nom_de_plantillas,list_pdf,opc,let,load,protec,cont,impre,plan):
        letrero = f"""

        _           _                                         _        _     _           _     _           
  __ _ (_)_   _ ___| |_ ___  ___   _ __  _ __ ___    ___  ___| |_ __ _| |__ | | ___  ___(_) __| | ___  ___ 
 / _` || | | | / __| __/ _ \/ __| | '_ \| '__/ _ \  / _ \/ __| __/ _` | '_ \| |/ _ \/ __| |/ _` |/ _ \/ __|
| (_| || | |_| \__ \ ||  __/\__ \ | |_) | | |  __/ |  __/\__ \ || (_| | |_) | |  __/ (__| | (_| | (_) \__ \
 \__,_|/ |\__,_|___/\__\___||___/ | .__/|_|  \___|  \___||___/\__\__,_|_.__/|_|\___|\___|_|\__,_|\___/|___/
     |__/                         |_|                                                                      
     
        URL de la carpeta del evento creada: {rut_evento}

        Subindice de la camara seleccionada: {num_camara+1}

        No de plantillas que se desean usar: {nom_de_plantillas}
    """

        print(letrero)
        print("lista de urls de las plantillas: ")
        for x in range(len(list_pdf)):
            letrero = f"""
            Plantilla numero {x+1}: {lista_pdf[x]}
            """
            print(letrero)

        letrero = f"""
        Opcion de entrega de producto final: [{opc}], {let}

        URL de loading: {load}

        URL de protector: {protec}

    """
        print(letrero)

        print("lista de urls de las de conteo: ")
        for x in range(len(cont)):
            letrero = f"""
        Conteo numero {x+1}: {cont[x]}
        """
            print(letrero)

        print(f"        URL de impresion: {impre}")

        print(f"        URL de plantilla de face: {plan}")
        time.sleep(2)
        

        

        

    
class Procesos:
    def __init__(self, plan,direc,pla_face, list_pdf= []):
        self.can_plantillas = plan
        self.direcci = direc
        self.li_pdf = list_pdf
        self.pla_red = pla_face

    def detector_de_cara( video, dibujar= True):
        face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        gray_image = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray_image, 1.7, 5, minSize=(40, 40))
        if dibujar:
            for (x, y, w, h) in faces:
                cv2.rectangle(video, (x, y), (x + w, y + h), (0, 255, 0), 4)
        return faces

    def pdf(self, ev):
        print("inicio metodo pdf")
        
        while escuchador.is_alive():

            # numero_al = random.randint(0,5)
            numero_al = random.randint(0,self.can_plantillas-1)
           
            pdf = fpdf.FPDF()
            pdf.add_page()
            # Agregamos una imagen
    

            pdf.image(f"{self.direcci}/carpeta "+ str(ev) + "/imagen 0.jpg",13,11,89,67)

            pdf.image(f"{self.direcci}/carpeta "+ str(ev) + "/imagen 1.jpg",108,11,89,67)

            pdf.image(f"{self.direcci}/carpeta "+ str(ev) + "/imagen 2.jpg",13,84,89,67)

            pdf.image(f"{self.direcci}/carpeta "+ str(ev) + "/imagen 3.jpg",108,84,89,67)

            pdf.image(f"{self.direcci}/carpeta "+ str(ev) + "/imagen 4.jpg",13,157,89,67)

            pdf.image(f"{self.direcci}/carpeta "+ str(ev) + "/imagen 5.jpg",108,157,89,67)

            # pdf.image("plantillas/Plantilla cabina " + str(numero_al) + ".png", 0, 0)

            pdf.image(self.li_pdf[numero_al], 0, 0)

            

            # Guardamos el documento
            pdf.output(f"{self.direcci}/carpeta "+ str(ev) + "/documento.pdf")
            break

    def imprimir(self,ev):
        print("inicio metodo imprimir:")
        ruta_de_impresion =f"{self.direcci}/carpeta "+ str(ev) + "/documento.pdf"
        while escuchador.is_alive():
            
            
            win32api.ShellExecute(0,
                                   'print',
                                     ruta_de_impresion,
                                       win32print.GetDefaultPrinter(),
                                         '.',
                                           0)
            break

    def creacion_de_carpeta(self,ev):
        while escuchador.is_alive():
            ruta_de_carpeta = f"{self.direcci}/carpeta " + str(ev)
            if not os.path.exists(ruta_de_carpeta):
                print("carpeta creada: ", ruta_de_carpeta)
                os.makedirs(ruta_de_carpeta)
                break

    def plantilla_face(self,ev):
        
        print("inicio metodo plantilla face")
        
        
        while escuchador.is_alive():
            for k in range(6):
                img_foto = cv2.imread(f"{self.direcci}/carpeta {ev}/imagen " + str(k) + ".jpg")
                alto, ancho, _ = img_foto.shape
                img_face = cv2.imread(self.pla_red,cv2.IMREAD_UNCHANGED)
                img_face = cv2.resize(img_face,(ancho,alto))
                img_foto = cv2.cvtColor(img_foto,cv2.COLOR_BGR2BGRA)
                for i in range(img_face.shape[0]):
                    for j in range(img_face.shape[1]):
                        if (img_face[i,j][3]!=0):
                            img_foto[i,j] = img_face[i,j]

                img_foto = cv2.cvtColor(img_foto,cv2.COLOR_BGRA2BGR)
                cv2.imwrite(f"{self.direcci}/carpeta "+ str(ev)+ f"/imagen face no {k+1}.jpg",img_foto) 
                print(f"foto de face no. {k+1} terminada")           
                #cv2.imshow("vista de foto", img_foto)
                #cv2.waitKey(0)

            break

    def video_face (self, ev):
        img_array = []
        print("inicio metodo video face")
        while escuchador.is_alive():
            for k in range(6):
                img_foto = cv2.imread(f"{self.direcci}/carpeta {ev}/imagen " + str(k) + ".jpg")
                alto, ancho, _ = img_foto.shape
                img_face = cv2.imread(self.pla_red,cv2.IMREAD_UNCHANGED)
                img_face = cv2.resize(img_face,(ancho,alto))
                img_foto = cv2.cvtColor(img_foto,cv2.COLOR_BGR2BGRA)
                for i in range(img_face.shape[0]):
                    for j in range(img_face.shape[1]):
                        if (img_face[i,j][3]!=0):
                            img_foto[i,j] = img_face[i,j]

                img_foto = cv2.cvtColor(img_foto,cv2.COLOR_BGRA2BGR)
                img_array.append(img_foto)

                print(f"Imagen ya editada no. {k+1}")

        

            alto, ancho = img_foto.shape[:2]

            video = cv2.VideoWriter(self.direcci + f"/carpeta {ev}/video face.mp4",cv2.VideoWriter_fourcc(*'mp4v'),2,(ancho,alto))
               
            for i in range(6):
                video.write(img_array[i])

            print("video ya creado")
            video.release()

            break



class Animaciones:

    def __init__(self,n_cam, ur_video,ur_bucle,direc_ev,list_cont=[]):
        self.numero_cam = n_cam
        self.frem = ur_video
        self.prot = ur_bucle
        self.cont = list_cont
        self.derec_ev = direc_ev

    def bucle_striming_maxc(self,car_min,car_max):

        
        video_capture = cv2.VideoCapture(self.numero_cam,cv2.CAP_DSHOW)
        print("inicio metodo bucle: ",self.prot)
        while escuchador.is_alive():
            is_closed = False
            video_pro_pan = cv2.VideoCapture(self.prot)
            
            while escuchador.is_alive():
                ret_cap, video_frame = video_capture.read()
                ret_pan, frame = video_pro_pan.read()
                video_frame = cv2.flip(video_frame,1)
                info_caras = Procesos.detector_de_cara(video_frame)
                info_caras = len(info_caras)
                
                if ret_pan == True:
                    cv2.namedWindow("animacion", cv2.WND_PROP_FULLSCREEN)
                    cv2.setWindowProperty("animacion", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                    cv2.imshow("animacion",frame)
                    #cv2.imshow("detector de gestos", video_frame)
                    if (info_caras == car_min and info_caras <= car_max):
                        is_closed = True
                        break
                    cv2.waitKey(1)
                else: break
                
            if is_closed:
                break
        print("fin metodo")
        video_capture.release()
        cv2.destroyAllWindows

    def captura_fotos(self, ev):

        proceso = Procesos(plan=nume_de_plantillas,direc=ruta_evento,pla_face=pla_face,list_pdf=lista_pdf)
        proceso.creacion_de_carpeta(ev)
        captura = cv2.VideoCapture(self.numero_cam,cv2.CAP_DSHOW)
        print("inicio metodo captura foto")
        for i in range(6):
            conteo = cv2.VideoCapture(self.cont[i])
            
            tiempoA2 = dt.datetime.now()
            tiempoA3 = dt.datetime.now()

            
            
            while escuchador.is_alive():
                
                ret, imagen_conteo = conteo.read()
                ret_2, imagen_cap = captura.read()
                
                
                if ret == True:
                    
                    
                    tiempoB = dt.datetime.now()
                    tiempoTranscurrido2 = tiempoB - tiempoA2
                    tiempoTranscurrido3 = tiempoB - tiempoA3
                    alto, ancho, _ = imagen_conteo.shape
                    imagen_cap = cv2.resize(imagen_cap,(ancho,alto))
                    
                    imagen_cap = cv2.flip(imagen_cap,1)

                    
                    
                    suma = cv2.add(imagen_conteo,imagen_cap)
                    
                    
                    
                    cv2.namedWindow("video cap", cv2.WND_PROP_FULLSCREEN)
                    cv2.setWindowProperty("video cap", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                    cv2.imshow('video cap', suma)
                    if tiempoTranscurrido2.seconds >= 3:
                        tiempoTranscurrido2 = 0
                        arduino.write(b'1')
                        tiempoA2 = dt.datetime.now()
                        print("tiempo final 2:",tiempoA2)
                        
                        
                    if tiempoTranscurrido3.seconds >= 4 :
                        tiempoTranscurrido2 = 0
                        tiempoTranscurrido3 = 0
                        cadena = self.derec_ev + f"/carpeta {ev}/imagen {i}.jpg"
                        
                        cv2.imwrite(cadena,imagen_cap)
                        
                    #     # Se debe establecer un nuevo tiempoA
                        tiempoA2 = dt.datetime.now()
                        tiempoA3 = dt.datetime.now()
                    #     print("tiempo final 3:",tiempoA3)
                        print(f"foto no. {i+1} tomada")
                        
                        

                    if cv2.waitKey(1) == 27:
                        break
                        

                else:

                    break

        cv2.destroyAllWindows()    

        print("fin metodo captura fotos")
        captura.release()        

    def video(self, tiempo):
        video = cv2.VideoCapture(self.frem)
        print("reproduciendo: ", self.frem)
        while escuchador.is_alive():
            ret, frame = video.read()
            
            
            if ret == True:
                cv2.namedWindow("video", cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow("video", frame)
                

            cv2.waitKey(tiempo)
            if not ret:
                break
        
        print("fin de video")   
        
        cv2.destroyAllWindows()



def pulsa(tecla):
	pass

def suelta(tecla):
	if tecla == kb.KeyCode.from_char('q'):
            print("se puso tecla para cerrar metodos ")
            # if os.listdir("album de fotos/"):
            #     carpeta = 1 
            #     while True:
            #         isclosed = 0
            #         if not os.path.exists(direccion_de_seciones_guardadas + nombre_secion):
            #             os.makedirs(direccion_de_seciones_guardadas + nombre_secion)
            #             print("carpeta creada: ", direccion_de_seciones_guardadas + nombre_secion)
            
            #             while True:
            #                 if os.path.exists(direccion_de_seciones_en_album + str(carpeta)):
            #                     print("carpeta existente")
                                
            #                     if os.listdir(direccion_de_seciones_en_album + str(carpeta)):
            #                         sh.move(direccion_de_seciones_en_album + str(carpeta), direccion_de_seciones_guardadas + nombre_secion)
            #                         carpeta =carpeta+1

            #                     else:
            #                         print("carpeta vacia... borrar directorio")
            #                         os.rmdir(direccion_de_seciones_en_album + str(carpeta))
                         

            #                 else:
            #                     print("no existe la carpeta ")
            #                     isclosed = 1
            #                     break
        

            #         if isclosed:
            #             break
        
            exit()

if __name__ == "__main__":
    os.system("cls")
    arduino = serial.Serial(f"COM{Panel_control.init_arduino()}", 9600)
    #--------- panel de control--------------
    
    
    ruta_evento = Panel_control.creacion_de_evento()
    numero_camara =Panel_control.cal_camara()
    nume_de_plantillas, lista_pdf = Panel_control.pdf_start()
    Panel_control.nombre_impresora()
    opcion, let = Panel_control.entrega_digital()
    loading, protector, conteo, impresion,pla_face =Panel_control.mvideos_multimedia()
    cantidad = Panel_control.cant_loop()
    Panel_control.resumen(ruta_evento,
                          numero_camara,
                          nume_de_plantillas,
                          lista_pdf,
                          opcion,
                          let,
                          loading,
                          protector,
                          conteo,
                          impresion,
                          pla_face
                          )
    
    resultado = messagebox.askquestion("Salir", 
        "¿deseas guardar estos cambios?")

    if resultado == "no":
        
        while True:
            letrero = """

            MENU DE OPCIONES PARA CAMBIO DE VARIABLES 

            [1] Ruta de almacenamiento y nombre de carpeta 
            [2] Calibracion de camara 
            [3] Numero de plantillas y lista de URL
            [4] Entrega digital 
            [5] Videos multimedia
            [6] Salir de menu
            
            """  

            print(letrero)

            opcion = input("            inserte la opcion que desea modificar:")

            if opcion == "1":
                ruta_evento = Panel_control.creacion_de_evento()  
            if opcion == "2":
                numero_camara =Panel_control.cal_camara()
            if opcion == "3":
                nume_de_plantillas, lista_pdf = Panel_control.pdf_start()
            if opcion == "4":
                opcion, let = Panel_control.entrega_digital() 
            if opcion == "5":
                loading, protector, conteo, impresion,pla_face =Panel_control.mvideos_multimedia()

            if opcion == "6":
                break
            os.system("cls")

            Panel_control.resumen(ruta_evento,
                          numero_camara,
                          nume_de_plantillas,
                          lista_pdf,
                          opcion,
                          let,
                          loading,
                          protector,
                          conteo,
                          impresion,
                          pla_face
                          )

            resultado = messagebox.askquestion("Salir", 
            "¿deseas guardar estos cambios?")

            if resultado == "yes":
                break

            
    os.system("cls")
    
    
    animador= Animaciones(n_cam=numero_camara,  ur_video=loading, ur_bucle=protector,direc_ev=ruta_evento,list_cont=conteo)
    proceso = Procesos(plan=nume_de_plantillas,direc=ruta_evento,pla_face=pla_face,list_pdf=lista_pdf)
    
    escuchador = kb.Listener(pulsa, suelta)
    escuchador.start()

    

    animador.video(30)
    evento = 0
    
    while escuchador.is_alive():
        
        animador.bucle_striming_maxc(1,1)
        
        
        evento = evento +1
        animador.captura_fotos(evento)
        
        proceso.pdf(evento)
        proceso.imprimir(evento)

        if opcion == '1':
            proceso.plantilla_face(evento)

        elif opcion == '2':
            proceso.video_face(evento)

        elif opcion == '3':
            proceso.plantilla_face(evento)
            proceso.video_face(evento)
        
    #     
        animador.frem = impresion
        for i in range(cantidad):
            animador.video(30)

        os.system("cls")
    
        
    messagebox.showinfo(message="Pocesos y sistemas apagados", title="on/off")            
    print("programa cerrado")
   

