#include <iostream> // used for basic input and output
#include <cstdlib> // used for general purpose functions
#include <windows.h>
using namespace std; // for ease of not writing std


int main(){
    short min, seconds;  // short data type since we dont need large nums
    int time;          // this will store the total time to be displayed

    // Input from user
    cout << "Enter minutes: \n";
    cin >> min;
    while (min < 0) {
        cout << "Re-enter minutes: \n";
        cin >> min;
    }

    cout << "Enter seconds:\n";
    cin >> seconds;
    while (seconds < 0) {
        cout << "Re-enter seconds: \n";
        cin >> seconds;
    }

        time = min * 60 + seconds;

    // Output for countdown
    for(int i = time; i>0; i--) { // initialize for loop for count down

        cout << "\rTime left: " << min << ":" << seconds << flush << endl;
        Sleep(1000);
        min = i % 60 == 0 ? --min :min;
        seconds = seconds == 0? 59: --seconds;

    }
    cout << "Timer ended" << endl;
}
