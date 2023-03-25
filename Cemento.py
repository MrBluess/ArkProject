import cv2
import numpy as np
import pyautogui

# Cargamos la imagen de la muestra
template = cv2.imread('IMG/Cemento.png', 0)
w, h = template.shape[::-1]

# Configuramos los parámetros de OpenCV
threshold = 0.8

# Iniciamos la captura de pantalla
while True:
    # Capturamos la pantalla y la convertimos a escala de grises
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Buscamos la muestra en la pantalla
    res = cv2.matchTemplate(frame_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    # Si encontramos la muestra, salimos del ciclo
    if len(loc[0]) > 0:
        break

# Mostramos la posición de la muestra en la pantalla
for pt in zip(*loc[::-1]):
    cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imshow('image', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
