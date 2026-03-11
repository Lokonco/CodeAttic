# Periodic Table Lookup

## Overview
A **Python terminal program** that allows users to explore information about chemical elements.  
The program reads element data from a CSV file (from Wikipedia) and lets the user query by **atomic number** or **symbol**.

---

## How It Works

### Data Import
- Reads a CSV file `periodictable.csv` containing details of all chemical elements.  
- Stores elements in a dictionary for **fast lookup** using either **atomic number** or **symbol**.  
- Removes reference notation like `[I]`, `[V]`, `[X]` from the CSV data.

### Element Information
Each element has the following fields:

- Atomic Number  
- Symbol  
- Element Name  
- Origin of Name  
- Group  
- Period  
- Atomic Weight (u)  
- Density (g/cm³)  
- Melting Point (K)  
- Boiling Point (K)  
- Specific Heat Capacity (J/(g·K))  
- Electronegativity  
- Abundance in Earth's Crust (mg/kg)

### Terminal Interface
- Displays a **schematic periodic table**.  
- Prompts the user to **enter a symbol or atomic number**.  
- Prints the detailed information for the selected element.  
- User can type `QUIT` to exit the program.

---

## Usage
```bash
python periodic_table_lookup.py
