import pyautogui as ptg 
import os

#setting fail safes
ptg.FAIL_SAFE = True
ptg.PAUSE = 1

#open paint
os.system('START "" mspaint')

#moving the pointer to screen center
screenWidth, screenHeight = ptg.size()
ptg.moveTo(screenWidth / 2, screenHeight / 2)

#dagging mouse like in staircase pattern
distance=20
for i in range(0,20):
	if i%2==0:
		ptg.dragRel(0,-distance,0.5)
	else:
		ptg.dragRel(distance,0,0.5)