#-----Imports-----#
import random, time
#-----------------#

#-----Constants-----#
Width = 70
PauseAmount = 0.05
#-------------------#

print("DeepCave Animation Starting...\nprogram will run for 3 seconds")
time.sleep(2)

#---Cave Widths---#
leftWidth = 20
gapWidth = 10
#-----------------#

#-----Variables-----#
start = time.time()
run = True
totalTime = 3 #Total Runtime
#-------------------#

#------Main Loop----------#
while run:
    #---Check program time---#
    if time.time() - start >= totalTime:
        run = False
        continue
    #-----------------------#

    rightWidth = Width - gapWidth - leftWidth
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))
    time.sleep(PauseAmount)

    #---Adjust left width---#
    diceRoll = random.randint(1,6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth -= 1 # Decreasing the left width
    elif diceRoll == 2 and leftWidth + gapWidth < Width - 1:
        leftWidth += 1
    else:
        pass
    #----------------------#

    #---Adjust gap width---#
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and gapWidth > 1:
        gapWidth -=1
    elif diceRoll == 2 and leftWidth + gapWidth < Width - 1:
        gapWidth += 1
    else:
        pass
    #------------------------#
