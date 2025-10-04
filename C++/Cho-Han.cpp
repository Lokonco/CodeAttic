#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;


void startGame(int& bankRoll);
string toLower(string s);

int main() {
    string input;
    int bankRoll = 10000;
    srand(time(0));

    cout << "\t\t\t------Welcome to Cho-Han------\n"
         "Rules are simple, The dealer will shake 2 dice in a cup\n"
         "He will then ask if the total of the 2 dice is even(Cho) or odd(Han)\n"
         "You will then be prompted to press C for Cho or H for Han\n"
         "\t\t-------------------------------------------\n";

    // Make sure input is valid
    while(true) {
        cout << " Ready to play? Press Q to quit or S to start\n > ";
        cin >> input;
        input = toLower(input);
        if(input == "s") {
            startGame(bankRoll);
        } else if(input == "q") {
            cout << "Thanks for playing" << endl;
            break;
        } else { cout << "Invalid input" << endl;}
    }
    return 0;
}


//Function to roll two 6 sided dice
int rollDice() {
    int dice1 = rand() % 6 + 1;
    int dice2 = rand() % 6 + 1;
    return dice1 + dice2;
}

// Function to make input lowercase
string toLower(string s) {
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    return s;
}

//Main game function
void startGame(int& bankRoll) {
    int bet = 0;
    string input;

    while (true) {
        int diceResult = rollDice();
        cout << "--------------------------------------------" << endl;
        cout << "Your total bankroll right now is ¥" << bankRoll << endl;
        cout << "Dealer is rolling the dice... you hear the dice rolling in the cup\n"
                "He ask for you to enter your bet\n> ";
        //cin >> bet;
        cout << "------------------------------------------" << endl;

        // Check if bet is valid
        while(!(cin >> bet) || bet <= 0 || bet > bankRoll) {
            cin.clear(); // Clear error flag
            cin.ignore(numeric_limits<streamsize>::max(), '\n'); // Discard invalid input
            cout << "Enter a valid bet 1 - " << bankRoll << endl << "> ";
        }


        cout << "He slams the cup on the table and looks up...\n"
                "He ask sternly Even(Cho) or Odd(Han)?\n"
                "-------------------------------------\n"
                "> ";

        while(true) {
            cin >> input;
            input = toLower(input);
            if(input == "c" || input == "h") {
                break;
            } else {
                cout << "Invalid choice. Please enter C for Cho (even) or H for Han (odd)\n> ";
                cout << "------------------------------------------------------------------" << endl;
            }
        }

        cout << "The result is " << diceResult << endl;

        // Check if player guess is correct
        if ((input == "c" && diceResult % 2 == 0) || input == "h" && diceResult % 2 != 0) { //Check if even or odd
            bankRoll += bet * 2;
            cout << "Congrats on the win... You got lucky this time"<< endl;
            cout << "Your bank roll is now ¥" << bankRoll << endl;
        } else {
            bankRoll -= bet;
            cout << "Sorry but you lost" << endl;
            cout << "Your bank roll is now ¥" << bankRoll << endl;}
        cout << "--------------------------" << endl;

        // Handle if user has run out of money
        if(bankRoll == 0) {
            cout << "Thanks for playing, but your out of money" << endl;
            cout << "Press R to restart or press Q to quit\n> ";
            while (true) {
                cin >> input;
                input = toLower(input);
                if (input == "r") {
                    bankRoll = 10000;
                    startGame(bankRoll);
                } else if (input == "q") {
                    break;
                } else {cout << "Invalid input. Please try again.\n";}
            }
        }

    }
}
