# DeepCave ASCII Animation

## Overview
A Python program that simulates **traveling down a cave** using ASCII characters.  
The program prints a continuously changing tunnel to the terminal, creating the illusion of motion.

## How It Works

### Cave Layout
- The cave is represented as a line of `#` characters for walls and spaces for the gap (the "path").  
- **Left wall width (`leftWidth`)** and **gap width (`gapWidth`)** control the cave shape.  
- **Right wall width** is automatically calculated to fill the line.

### Animation
- Each frame prints a new cave line to the terminal.  
- `time.sleep(PauseAmount)` controls the animation speed.  
- The program runs for a fixed duration (`totalTime`).

### Random Variation
- `leftWidth` and `gapWidth` are randomly adjusted each frame to simulate a **winding cave**.  
- Random rolls ensure the cave occasionally narrows or widens.

## Usage
```bash
python deepcave.py
