# Wild West Reflex Game

## Overview
A **Python terminal game** that tests your reflexes.  
When `DRAW!` appears, you must press **ENTER within 0.3 seconds**.  
Pressing too early or being too slow results in a loss.

---

## How It Works

### Game Logic
1. The program waits a random delay (`2.0 – 5.0` seconds) before displaying `DRAW!`.  
2. The player must press **ENTER** as quickly as possible.  
3. The reaction time is measured:
   - **< 0.01 sec** → Drew too early  
   - **> 0.3 sec** → Too slow  
   - **≤ 0.3 sec** → You Win!  
4. After each round, the player can **quit** or **play again**.

### Terminal Interaction
- Instructions are displayed at the start.  
- Prompts for reaction input and displays the reaction time.  
- Accepts `QUIT` to exit the game.

---

## Usage
```bash
python wild_west_reflex.py
