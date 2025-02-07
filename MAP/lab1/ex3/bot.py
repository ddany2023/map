import pyautogui
import time
import keyboard

def cautare_google():
    if pyautogui.locateOnScreen(r"C:\Users\Student1\Desktop\BucsaLucian\lab1\lab1\ex3\SEARCH.png",confidence=0.80) != None:
        #print("Bara de cautare a fost gasita")
        bara_cautare = pyautogui.locateOnScreen(r"C:\Users\Student1\Desktop\BucsaLucian\lab1\lab1\ex3\SEARCH.png",confidence=0.80)
        pyautogui.click(bara_cautare)
        time.sleep(5)
        pyautogui.write("https://www.youtube.com/@DanCadar")
        pyautogui.press('enter')

def click_videoclipuri ():
    time.sleep(3)
    pyautogui.click(1793,544)

def afisare_coordonate():
    while not keyboard.is_pressed('x'):
        print(pyautogui.position())
        time.sleep(0.2)

raspuns = pyautogui.confirm("Vrei sa incepi rularea programului?", "Confirmare")
if(raspuns=="OK"):
   cautare_google()
   click_videoclipuri()
else: afisare_coordonate()   