from asyncore import read
from logging import root
import pyautogui
import time
# f = open('t.txt','r')
x=0
f = open('t2.txt','r')
def run():
    time.sleep(5)
    for i in range(0,100):
        pyautogui.typewrite(str(i))
        pyautogui.press('enter')
        time.sleep(1)

def lyric():
    time.sleep(7)
    for i in range(1,5):
        pyautogui.typewrite("*")
        pyautogui.press('enter')
    pyautogui.typewrite("                                                                       Letsssssssssssss Begggggggggggggggginnnnnnnnnn                                       ")
    pyautogui.press('enter')
    for i in range(1,4):
        pyautogui.typewrite(str(i))
        pyautogui.press('enter')
        time.sleep(1)
    for word in f :
        print(x)
        try:
            pyautogui.typewrite(word)
            pyautogui.press('enter')
            time.sleep(2)
            x=x+1
        except:
            pass
    pyautogui.typewrite("DOne......")
    pyautogui.press('enter')

def lyric_mov():
    z = open('merchant_of_venice.txt','r')
    time.sleep(7)
    pyautogui.typewrite("                                      THe MeRcHaNt of VENICE                               ")
    for i in range(1,5):
        pyautogui.typewrite("*")
        pyautogui.press('enter')
    pyautogui.typewrite("                                                                       Letsssssssssssss Begggggggggggggggginnnnnnnnnn                                       ")
    pyautogui.press('enter')
    for i in range(1,4):
        
        pyautogui.typewrite(str(i))
        pyautogui.press('enter')
        time.sleep(1)
    for word in z :
        # print(x)
        try:
            pyautogui.typewrite(word)
            pyautogui.press('enter')
            # time.sleep(10)
        except:
            pass
    pyautogui.typewrite("DOne......")
    pyautogui.press('enter')
    
if __name__ == "__main__":  
    pass