#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

// function to get pc move
char PcMove() {
    int move;
    // generate rand nums
    srand(time(NULL));
    move = rand() % 3;

    // return move based on rand num
    if (move == 0) {
        return 'p';
    }
    else if (move == 1) {
        return 's';
    }
    return 'r';
}
// func to return result of game
int getResult(char playerMove, char PcMove) {
    // condition for draw
    if (playerMove == PcMove) {
        return 0;
    }
    // conditions for win/lose
    if (playerMove == 's' && PcMove == 'p') {
        return 1;
    }
    if (playerMove == 's' && PcMove == 'r') {
        return -1;
    }
    if (playerMove == 'p' && PcMove == 'r') {
        return 1;
    }
    if (playerMove == 'p' && PcMove == 's') {
        return -1;
    }
    if (playerMove == 'r' && PcMove == 'p') {
        return 1;
    }
    if (playerMove == 'r' && PcMove == 's') {
        return -1;
    }
    return 0;
}
// driver code
int main() {
    char playerMove;
    cout << "X------------Welcome------------X" << endl;
    cout << "Welcome to Rock, Paper, Scissors" << endl;
    cout << "X-------------------------------X" << endl;

    cout << "r = Rock, p = Paper, s = Scissor" << endl;
    // input from user
    while(1) {
        cin >> playerMove;
        if (playerMove == 'p' || playerMove == 'r' || playerMove == 's' || playerMove == '1') {
            break;
        }
        else {
            cout << "Invalid Player Move, try again\n";
        }
    }

    // pc move
    char pcMove = PcMove();
    int result = getResult(playerMove,pcMove);
    // print result
    if (result == 0) {
        cout << "Game Draw" << endl;
    }
    else if (result == 1) {
        cout << "Congrats you beat the stupid computer!!\n";
    }
    else {
        cout << "Computer won the game, you suck!\n";
    }
    //showing both moves
    cout << "Your Move: " << playerMove << endl;
    cout << "Computer Move: " << pcMove << endl;
    return 0;
}
