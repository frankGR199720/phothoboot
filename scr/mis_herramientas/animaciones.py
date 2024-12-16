import cv2
from pynput import keyboard as kb
import serial



def pulsa(tecla):
	pass

def suelta(tecla):
    
    if tecla == kb.KeyCode.from_char('q'):
        print("se cierra el proghrama")
        exit()
    if tecla == kb.KeyCode.from_char('p'):
        print("se presiono p")
        # print(f"el estado anterior es {estado}")
        # estado = ~estado
        # print(f"el estado actual es {estado}")


escuchador = kb.Listener(pulsa, suelta)
escuchador.start()

def video(frame,tiempo):
    video = cv2.VideoCapture(frame)
    print("reproduciendo: ", frame)
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

        except Exception as cabra:
            print(cabra)
        


def bucle_striming_maxc(numero_cam,prot):

        
    
    linea = arduino.readline()
    respuesta = linea.decode()
    
    print("inicio metodo bucle: ",prot)
    while escuchador.is_alive():
        is_closed = False
        video_pro_pan = cv2.VideoCapture(prot)
        
            
        while escuchador.is_alive():
            
            ret_pan, frame = video_pro_pan.read()
            video_frame = cv2.flip(video_frame,1)
            
                
            if ret_pan == True:
                cv2.namedWindow("animacion", cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("animacion", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow("animacion",frame)
                
                print(respuesta)
                if respuesta == 1 or cv2.waitKey(1)==27:
                    is_closed= True
                    break
                else:pass
                
                cv2.waitKey(1)
            else: break
                
        if is_closed:
            break
    print("fin metodo")
    
    cv2.destroyAllWindows