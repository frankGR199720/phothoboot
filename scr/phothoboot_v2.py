import cv2
import os
import time
import win32print
from tkinter import messagebox
import random
import fpdf
import win32api
from pynput import keyboard as kb
import serial
import datetime as dt

from mis_herramientas import panel_de_control as pan
from mis_herramientas import animaciones as anim
from mis_herramientas import procesos as pro



pan.ruta_de_secion
pan.numero_de_camara
pan.numero_de_plantillas
pan.lista_pdf_url
pan.opcion_d, pan.let
pan.loading, pan.protector, pan.conteo, pan.impresion, pan.pla_face
pan.cantidad
evento = 0

anim.init_arduino()

if __name__ == "__main__":
    
        pan.resumen(rut_evento = pan.ruta_de_secion,
                num_camara = pan.numero_de_camara,
                nom_de_plantillas = pan.numero_de_plantillas,
                list_pdf = pan.lista_pdf_url,
                opc = pan.opcion_d,
                let = pan.let,
                load = pan.loading,
                protec = pan.protector,
                cont = pan.conteo,
                impre = pan.impresion,
                plan = pan.pla_face)
        pan.menu_prin()
        anim.video(frame = pan.loading, 
            tiempo = 30)

        while anim.escuchador.is_alive():
            anim.bucle_striming_maxc(prot = pan.protector)

            evento = evento + 1
            
            print(f"**************SECION NO. {evento}*********************")
            anim.captura_fotos(ev = evento, 
                        direccion_envio = pan.ruta_de_secion, 
                        numero_de_camara = pan.numero_de_camara,
                        conteo_digital = pan.conteo)

            pro.pdf(ev = evento, 
            can_plantillas = pan.numero_de_plantillas,
            direccion_envio = pan.ruta_de_secion,
            lista_pdf = pan.lista_pdf_url)

            print(anim.modo_impresion)
        
            if anim.modo_impresion:
                pro.imprimir(ev = evento, direccion_de_envio = pan.ruta_de_secion)

            else:print("la impresora esta desactivada")

            pro.entrega_prod(opcion = pan.opcion_d, 
                        ev = evento)

            for i in range(pan.cantidad):
                anim.video(frame = pan.impresion,
                    tiempo= 30)

        pro.exit()
        

    