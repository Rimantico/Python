#Hecho por: Juan Gómez Ruiz

import pyautogui
import time


# Código Principal

pyautogui.press("win")
time.sleep(0.3)
pyautogui.write("chrome")
time.sleep(0.3)
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("https://seneca.juntadeandalucia.es/seneca/jsp/portal/")
time.sleep(2)
pyautogui.press("enter")
time.sleep(0.3)

usuario = input("Introduzca el usuario: ")
contraseña = input("Introduzca la contraseña: ")

pyautogui.hotkey("alt", "tab")
time.sleep(0.5)


pyautogui.write(usuario)
time.sleep(0.3)
pyautogui.press("tab")
pyautogui.write(contraseña)
time.sleep(0.4)
pyautogui.press("tab")
pyautogui.press("enter")

