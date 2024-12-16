import os
import time
import cv2
import win32print
from tkinter import messagebox




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
    print("Lista de urls de las plantillas: ")
    for x in range(len(list_pdf)):
        letrero = f"""
        Plantilla numero {x+1}: {list_pdf[x]}
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

    print(f"        URL de impresion: {impre}\n")

    print(f"        URL de plantilla de face: {plan}")
    time.sleep(2)


def menu_prin():
    resultado = messagebox.askquestion("Salir", 
        "¿deseas guardar estos cambios?")

    if resultado == 'no':
        global ruta_evento, numero_camara,nume_de_plantillas, lista_pdf, opcion, let, loading, protector, conteo, impresion,pla_face
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

            opcion1 = input("            inserte la opcion que desea modificar:")

            if opcion1 == "1":
                ruta_evento = creacion_de_evento()  
            if opcion1 == "2":
                numero_camara =cal_camara()
            if opcion1 == "3":
                nume_de_plantillas, lista_pdf = pdf_start()
            if opcion1 == "4":
                opcion, let = entrega_digital() 
            if opcion1 == "5":
                loading, protector, conteo, impresion,pla_face = mvideos_multimedia()

            if opcion1 == "6":
                print("Saliendo.....")
                break
            time.sleep(3)
        
            os.system("cls")

            resumen(rut_evento = ruta_de_secion,
                num_camara = numero_de_camara,
                nom_de_plantillas = numero_de_plantillas,
                list_pdf = lista_pdf_url,
                opc = opcion_d,
                let = let,
                load = loading,
                protec = protector,
                cont = conteo,
                impre = impresion,
                plan = pla_face)

            resultado = messagebox.askquestion("Salir", "¿deseas guardar estos cambios?")

            if resultado == "yes":
                break


ruta_de_secion = creacion_de_evento()
numero_de_camara = cal_camara()
numero_de_plantillas, lista_pdf_url = pdf_start()
opcion_d, let = entrega_digital()
loading, protector, conteo, impresion,pla_face =mvideos_multimedia()
    
