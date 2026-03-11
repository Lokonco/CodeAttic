# Mini-Game Arcade

## Overview
A **Python terminal-based mini-game collection** featuring four games:  
1. **Guess The Roll** – Guess the sum of two dice.  
2. **High Card Wins** – Player and computer draw cards; highest card wins.  
3. **Trivia Game** – Answer questions from Python, Pop-Culture, or Logic categories.  
4. **Math Game** – Solve arithmetic and logic problems with increasing difficulty.

Each game has its own rules and scoring system. The program includes menus, score tracking, and ASCII graphics for dice and cards.

---

## How It Works

### Menu System
- The main menu allows the player to select a game or exit.  
- Each game has a **sub-menu** with options to see rules, play, or return.

### Dice Game – Guess The Roll
- Generates **two random dice rolls**.  
- Player guesses the sum (2–12).  
- Correct guesses earn points; incorrect guesses award points to the computer.  
- Uses ASCII art to display dice faces.

### Card Game – High Card Wins
- Player and computer draw **random cards**.  
- Highest card wins the round.  
- First to 5 points wins.  
- Cards are displayed with **ASCII templates**.

### Trivia Game
- Questions are categorized into **Python, Pop-Culture, or Logic**.  
- Correct answers give **+10 points**, wrong answers **-5 points**.  
- Score is displayed after each question, with a final evaluation.

### Math Game
- Questions are categorized into **Easy, Medium, Hard**.  
- Points vary with difficulty: correct answers give 5–15 points, wrong answers subtract 2–7 points.  
- Player must reach 50 points or complete 10 questions to finish.

---

## Usage
```bash
python mini_game_arcade.py
