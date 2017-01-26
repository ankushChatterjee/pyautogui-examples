import pyautogui as ptg 

#setting fail safes
ptg.FAIL_SAFE=True
ptg.PAUSE=1

#moving the pointer to screen center
screenWidth, screenHeight = ptg.size()
ptg.moveTo(screenWidth / 2, screenHeight / 2)
ptg.click() #click!!

#moving mouse like in staircase pattern
distance=20
for i in range(0,20):
	if i%2==0:
		ptg.moveRel(0,-distance,0.5)
	else:
		ptg.moveRel(distance,0,0.5)