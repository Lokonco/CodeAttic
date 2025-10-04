# MUST BE RUN IN A TERMINAL

#-------Imports-------#
import math,time,sys,os
#---------------------#

#------Constants-------#
width,height = 80, 24
cubeSize = 10
scaleX = cubeSize
scaleY = cubeSize
translateX = width / 2
translateY = height / 2
#-----------------------#

#-----Rotation speeds-----#
xSpeed = 0.03
ySpeed = 0.08
zSpeed = 0.13
#-------------------------#

#----------Cube----------#
cubeCorners = [
    [-1, -1, -1], [1, -1, -1],
    [-1, -1, 1],  [1, -1, 1],
    [-1, 1, -1],  [1, 1, -1],
    [-1, 1, 1],   [1, 1, 1]
]

edges = [
    (0,1),(1,3),(3,2),(2,0),  # Bottom
    (4,5),(5,7),(7,6),(6,4),  # Top
    (0,4),(1,5),(2,6),(3,7)   # Sides
]
#------------------------#

# Cube points
X,Y,Z = 0, 1, 2

#-----Rotation-Function-----#
#Purpose of this function is to rotate a 3d point around either the x, y or z axis using the angles ax,ay,az
def rotate(x, y, z, ax, ay, az):
    # y and z are rotated by using a 2d formula for a plane
    #-----X-Axis-----#
    x1 = x # Stays the same since we are rotating around this axis
    y1 = y * math.cos(ax) - z* math.sin(ax)
    z1 = y * math.sin(ax) + z* math.cos(ax)
    #-----------------#

    #-----Y-Axis------#
    x2 = z1 * math.sin(ay) + x1 * math.cos(ay)
    y2 = y1 # Stays the same since we are rotating around this axis
    z2 = z1 * math.cos(ay) - x1 * math.sin(ay)
    #------------------#

    #-----Z-Axis------#
    x3 = x2 * math.cos(az) - y2 * math.sin(az)
    y3 = x2 * math.sin(az) + y2 * math.cos(az)
    z3 = z2 # Stays the same since we are rotating around this axis
    #-----------------#

    return x3, y3, z3
#--------------------------#

#----------Adjust-Function------------#
# Purpose is to convert the 3d points into 2d cords
def adjust(point):
    return int(point[X] * scaleX + translateX), int(point[Y] * scaleY + translateY)
    #Mutiple by scale factor to fit in terminal then add translate to center and force int for whole num
#-------------------------------------#

#-----Line-Function-----#
# Implements the Bresenham line algorithm
def line_algorithm(x1, x2, y1, y2):
        points = [] #Stores the pixel cords to create line
        dx, dy = abs(x1 - x2), abs(y1 - y2) #Horizontal and vertical distances
        x, y = x1, y1
        #Checks which direction we are moving sx: 1=right, -1=left / sy: 1=up, -1=down
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1

        # ------------Case 1---------------#
        # If the line has a gentle slope / more horizontal
        if dx > dy:
            err = dx // 2 #Lets us know when to move vertically
            while x != x2: #Continue until we meet the end xcord
                points.append((x,y))
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx #always move left or right
        #------------Case 2---------------#
        else: #The opposite of our first case // replace x with y
            err = dy // 2
            while y != y2:
                points.append((x,y))
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy
        #----------------------------------#

        points.append((x,y))
        return points
#-----------------------#

#----------MAIN-LOOP----------#
rotX = rotY = rotZ = 0.0 #Start at 0 sine no rotation has happened

try:
    while True:
        #------Clear Screen-----#
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')
        #------------------------#

        #-----Speeds-----#
        rotX += xSpeed
        rotY += ySpeed
        rotZ += zSpeed
        #----------------#

        # Rotate cube corners
        rotated = [rotate(*p, rotX, rotY, rotZ) for p in cubeCorners]

        #-----Draw Edges-----#
        buffer = [[' ' for _ in range (width)] for _ in range (height)]
        for a,b in edges:
            x1, y1 = adjust(rotated[a])
            x2, y2 = adjust(rotated[b])
            for px, py in line_algorithm(x1, x2, y1, y2): #Get points to create line
                if 0 <= px < width and 0 <= py < height:
                    buffer[py][px] = '#'
        #--------------------#

        for row in buffer:
            print(''.join(row))
        time.sleep(0.05) #Controls animation speed
        # Lower num = Fast, Larger num = slower

#----------Exit Logic--------#
except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit(0)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
#----------------------------#
