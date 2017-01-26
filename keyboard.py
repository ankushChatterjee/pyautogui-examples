import pyautogui as ptg 

#minimize the command prompt window with anytext editor opened in background
ptg.hotkey('win','down')
#write down a sentence
ptg.typewrite('we love python!',interval=0.25)
#write another one
ptg.typewrite(['enter',':',')'],interval=0.25)

