import cv2
import numpy as np
import pyautogui
import time


# Cargar la imagen de la plantilla y convertirla a escala de grises
template = cv2.imread('IMG/Cemento.png', cv2.IMREAD_GRAYSCALE)

# Establecer la región de interés (ROI) para el área donde se buscará la imagen
x1, y1, x2, y2 = 500, 300, 900, 700

# Iniciar el bucle principal para buscar la imagen
while True:
    # Tomar una captura de pantalla y convertirla a escala de grises
    screenshot = pyautogui.screenshot(region=(x1, y1, x2, y2))
    frame = np.array(screenshot)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Buscar la imagen de la plantilla en la captura de pantalla
    res = cv2.matchTemplate(frame_gray, template, cv2.TM_CCOEFF_NORMED)

    # Obtener las coordenadas del centro de la imagen encontrada
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    h, w = template.shape

    # Si se encuentra la imagen, mover el cursor del mouse al centro de la imagen y presionar la tecla 'A'
    if max_val > 0.8:
        center_x, center_y = top_left[0] + w // 2 + x1, top_left[1] + h // 2 + y1
        pyautogui.moveTo(center_x, center_y)
        pyautogui.press('a')
    
    # Agregar una pequeña pausa para reducir la carga en la CPU
    #time.sleep(0.1)
