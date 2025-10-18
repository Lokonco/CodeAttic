#If you want to use this you will need a csv file containing information about the perodic table from wikipedia
# -----Imports-----#
import csv, sys, re
# -----------------#

# -----Read data from file-----#
periodicTable = open("periodictable.csv", encoding="utf-8")
fileReader = csv.reader(periodicTable)
fileContents = list(fileReader)

# -----------------------------#


# -----Columns-----#
columns = ["Atomic-Number", "Symbol", "Element", "Origin of name",
           "Group", "Period", "Atomic-Weight", "Density", "Melting-Point",
          "Boiling-Point", "Specific heat capacity", "Electronegativity",
           "Abundance in earth\'s crust"]
# -----------------#


# ---Find longest col---#
longest_Column = 0
for key in columns:
    if len(key) > longest_Column:
        longest_Column = len(key)
# ----------------------#


# ----------Store elements in dict-----------#
elements = {}
for line in fileContents:
    element = {
        "Atomic-Number": line[0],
        "Symbol": line[1],
        "Element": line[2],
        "Origin of name": line[3],
        "Group": line[4],
        "Period": line[5],
        "Atomic-Weight": line[6] + ' u',
        "Density": line[7] + ' g/cm^3',
        "Melting-Point": line[8] + ' K',
        "Boiling-Point": line[9] + ' K',
        "Specific heat capacity": line[10] + ' J/(g*k)',
        "Electronegativity": line[11],
        "Abundance in earth\'s crust": line[12] + ' mg/kg'
    }
# --------------------------------------------#


# ---------Remove unwanted chars-------------#
    for key, value in element.items():
        element[key] = re.sub(r'\[(I|V|X)\]', '', value)

    elements[line[0]] = element  # Map atomic num
    elements[line[1]] = element  # map symbol
# ----------------------#


# ------Main-Loop-----#
print("Perodic Table of Elements")
print()
while True:
    print('''            Periodic Table of Elements
        1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
        1 H                                                  He
        2 Li Be                               B  C  N  O  F  Ne
        3 Na Mg                               Al Si P  S  Cl Ar
        4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
        5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
        6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
        7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

                Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
                Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr''')
    print('Enter a symbol or atomic number to examine, or QUIT to quit.')
    response = input('> ').title()

    if response == "Quit":
        sys.exit()

    if response in elements:
        for key in columns:
            keyJustified = key.rjust(longest_Column)
            print(keyJustified + ": " + elements[response][key])
        input("Enter to continue")
# --------------------#
