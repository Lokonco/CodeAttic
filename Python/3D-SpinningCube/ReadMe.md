# Terminal 3D Spinning Cube

## Overview
A Python program that renders a **rotating 3D cube** directly in the terminal using ASCII characters.  
The cube spins continuously around the **X, Y, and Z axes**, giving a simple wireframe 3D animation.

## How It Works

### Cube Definition
8 vertices (`cubeCorners`) and 12 edges (`edges`) define the cube.

### Rotation
Each point is rotated around **X, Y, and Z axes** using basic trigonometry.

### Projection
3D points are converted to **2D terminal coordinates** using scaling and translation.

### Line Drawing
Edges are drawn using the **Bresenham line algorithm**, which efficiently determines the points of a line.

### Animation Loop
Each frame:
1. Clears the screen  
2. Rotates the cube  
3. Draws edges  
4. Prints the frame  
5. Sleeps briefly for smooth motion

## Usage
```bash
python cube.py
