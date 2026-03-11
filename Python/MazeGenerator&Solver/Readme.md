# Maze Generator & Solver

## Overview
A Python program that **generates and solves a maze** visually using **Tkinter**.  
- Generates the maze with **depth-first traversal**  
- Solves it automatically using **recursive backtracking**  
- Animates the maze creation and solution in a GUI window

---

## How It Works

### Maze Generation
- The maze is composed of a grid of `Cell` objects.  
- Each cell has **top, bottom, left, and right walls**.  
- Uses **depth-first traversal** to break walls and create a solvable maze.  
- Entrance (top-left) and exit (bottom-right) are automatically opened.

### Maze Solving
- Recursively explores neighboring cells (**right, down, left, up**)  
- Marks visited cells to avoid loops  
- Draws the solution path in **red** and undo steps in **gray**  

### GUI & Animation
- `Window` class manages the Tkinter canvas  
- Cells and solution paths are drawn with `Line` and `Point` objects  
- Each step updates the window for smooth animation  

---

## Usage
```bash
python maze.py

