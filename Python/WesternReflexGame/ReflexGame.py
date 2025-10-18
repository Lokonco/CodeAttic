#-----Imports-----#
import random, sys, time
#-----------------#

#------Print Rules-----#
print("Welcome to the wild wild west!\nLets test those reflexes.")
print("When 'DRAW' is displayed, you have 0.3 seconds to press ENTER.")
print('You Lose if you press ENTER before "DRAW" is displayed or if you are too slow.\n')
input("Press ENTER to begin")
#-----------------------#

#-----Main Loop-----#
while True:
    print()
    print("It is high noon...")
    time.sleep(random.randint(20, 50) / 10.0)
    print("DRAW!")
    drawTime = time.time()
    input()
    timeElapsed = time.time() - drawTime  #Used to get the time it took for enter to be pressed after draw is displayed..

    #-----Logic------#
    if timeElapsed < 0.01:
        print("You drew to early ")
    elif timeElapsed > 0.3:
        timeElapsed = round(timeElapsed, 4)
        print('You took', timeElapsed, 'seconds to draw. Too slow!')
    else:
        timeElapsed = round(timeElapsed, 4)
        print('You took', timeElapsed, 'seconds to draw. You Win!')
    #-----------------#

    #-----Exit Logic-----#
    print('Press "Quit" to leave or "Enter" to play again')
    response = input('> ').upper()
    if response == "QUIT":
        print("Thanks for playing")
        sys.exit()
    #--------------------#
