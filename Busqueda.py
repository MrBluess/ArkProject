import pyautogui
import cv2

# Cargar la imagen que queremos buscar
template = cv2.imread('IMG/Cemento.png')

# Obtener las dimensiones de la imagen del template
w, h = template.shape[:-1]

# Buscar la imagen en pantalla
pos = pyautogui.locateOnScreen('IMG/Cemento.png')

# Si la imagen se encontró, imprimir "cemento encontrado"
if pos is not None:
    print("En proceso")
else: print("No se encontro el recurso")