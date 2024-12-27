import cv2
from pynput import keyboard as kb
import serial
import datetime as dt
import os
import time
from pynput.keyboard import Listener
from mis_herramientas import procesos as pro
from mis_herramientas import panel_de_control as pan



def cambiar_modo_impresion():
    """Cambia el modo de impresión entre imprimir físicamente y guardar como PDF."""
    global modo_impresion  # Variable global para rastrear el modo actual
    modo_impresion = not modo_impresion  # Invierte el modo
    if modo_impresion:
        print("Modo impresión activado.")
    else:
        print("Modo impresion desactivado")



def pulsa(tecla):
	pass

def suelta(tecla):
    
    if tecla == kb.KeyCode.from_char('q'):
        print("se cierra el proghrama")
        exit()

    if tecla == kb.KeyCode.from_char('p'):
        cambiar_modo_impresion()
    
        
        


escuchador = kb.Listener(pulsa, suelta)
escuchador.start()



def video(frame,tiempo):
    video = cv2.VideoCapture(frame)
    print("REPRODUCIENDO VIDEO: ", frame)
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



def init_arduino ():
        global arduino
        try:
            com = input("pon el puerto com del arduino: ")
            arduino = serial.Serial(f"COM{com}", 9600)
            time.sleep(4)
            os.system("cls")

        except Exception as cabra:
            print(cabra)
        


def bucle_striming_maxc(prot):
    
    os.system("cls")
    print("LOOP DE VIDEO: ",prot)

    while escuchador.is_alive():
        is_closed = False
        video_pro_pan = cv2.VideoCapture(prot)

        while escuchador.is_alive():

            ret_pan, frame = video_pro_pan.read()    
                
            if ret_pan == True:
                cv2.namedWindow("animacion", cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("animacion", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow("animacion",frame)

                if cv2.waitKey(25) & 0xFF == ord('c'):
                    os.system("cls")
                    print("inicia trabajo")
                    is_closed = True
                    break

            else:break

        if is_closed == True:
            break
    
    video_pro_pan.release()
    cv2.destroyAllWindows

def creacion_de_carpeta(ev, direccion_envio):
    while escuchador.is_alive():    
        ruta_de_carpeta = f"{direccion_envio}/secion " + str(ev)
        if not os.path.exists(ruta_de_carpeta):
            print("carpeta creada: ", ruta_de_carpeta)
            os.makedirs(ruta_de_carpeta)

        break

def captura_fotos(ev, direccion_envio, numero_de_camara, conteo_digital):

        
        creacion_de_carpeta(ev = ev, direccion_envio = direccion_envio)
        
        captura = cv2.VideoCapture(numero_de_camara,cv2.CAP_DSHOW)
        print("\t\tINICIA METODO DE CAPTURA DE FOTOS")
        for i in range(6):
            conteo = cv2.VideoCapture(conteo_digital[i])
            
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
                        print("tiempo de flash:")
                        
                        
                    if tiempoTranscurrido3.seconds >= 4 :
                        tiempoTranscurrido2 = 0
                        tiempoTranscurrido3 = 0
                        cadena = direccion_envio+ f"/secion {ev}/imagen {i}.jpg"
                        print(f"LA DIRECCION DE LA FOTO NO. {i+1}: ",cadena)
                        cv2.imwrite(cadena,imagen_cap)
                        
                        # Se debe establecer un nuevo tiempoA
                        tiempoA2 = dt.datetime.now()
                        tiempoA3 = dt.datetime.now()
                    #     print("tiempo final 3:",tiempoA3)
                        
                        
                        

                    if cv2.waitKey(1) == 27:
                        break
                        

                else:

                    break

        cv2.destroyAllWindows()    

        print("fin metodo captura fotos")
        captura.release()  

modo_impresion = True