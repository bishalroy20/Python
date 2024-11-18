import pyautogui

a = int(input())

for i in range(1,a+1):
    pyautogui.typewrite('*' * i)
    pyautogui.typewrite('\n')




