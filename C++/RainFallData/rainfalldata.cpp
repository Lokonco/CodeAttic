/*The purpose of this program is recieve user input for monthly rainfall
 *for the entire year and allow them to view the data in mutiple ways.*/
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

// Function for Total Rainfall
double getTotal(double rain[], const int months) {
 // Variable for total from adding all array elements together.
 double total = 0;
 // For loop to traverse thru all array elements.
 for (int i = 0; i < months; ++i) {
  // Adds the array elements.
  total += rain[i];
 }
 // Returning the total of all elements added together
 return total;
}

// Function for average/mean
double getAverage(double rain[], const int months) {
// Total variable so we can call getTotal and so we can divide it by the amount of elements.
 double total = getTotal(rain, months);
// Average variable so we can divide total by the amount of months and store that answer.
 double average = total / months;
// Return the mean for rainfall.
 return average;
}

//Function for getting largest element in array
double getLargest(double rain[], const int months, int &largestMonth) {
// Variable to assign largest number with the first element in array.
 double largest = rain[0];
 largestMonth = 0;
 //For loop to traverse thru loop and update Variable each time a larger is met.
 for(int i = 1; i < months; ++i) {
  if (rain[i] > largest) {
   largest = rain[i];
   largestMonth = i;
  }
 }
 return largest;
}

//Function for getting smallest element.
//Same as getLargest but we change the if statement,
//to smaller than instead of bigger than.
double getSmallest(double rain[], const int months, int &smallestMonth) {
 // Variable to assign largest number with the first element in array.
 double smallest = rain[0];
 smallestMonth = 0;
 //For loop to traverse thru loop and update Variable each time a larger is met.
 for(int i = 1; i < months; ++i) {
  if (rain[i] < smallest) {
   smallest = rain[i];
   smallestMonth = i;
  }
 }
 return smallest;
}

//Function to sort array in ascending order:
void selectionSort(double rain[], const int months) {
 sort(rain, rain + months);
}


int main() {
 //Variables
 const int months = 12; // Total numbers of months in year.
 double rain[months]; // Array to store user input for rainfall for each motnth.

 //  For loop to prompt user for input for the 12 months.
 for (int i=0; i < months; ++i) {
  // Variable for user input so we can check if its valid.
  double input = 0;
  // Asking user for input and updating i each time until 12 since a year has 12 months.
  cout << "Enter the rainfall (in inches) for month #"<< (i+1) << ": ";
  // Storing user input into input variable so we can check for validity using if statement.
  cin >> input;
  // while loop to check for validity and reask for input.
  while (input < 0) {
   // Telling user input is inValid
   cout << "Rainfall must be 0 or more." << endl;
   // Asking user to re-enter rainfall
   cout << "Please re-enter: ";
   // Storing valid user input into input variable so we can store it in array next.
   cin >> input;
   // Storing valid input into array
  }
  rain[i] = input;
 }
 cout << endl;
 int largestMonth, smallestMonth;

 // Output Section
 // Setprecision used since everything is in inches.
 cout << fixed << setprecision(2);
 cout << "The total rainfall for the year is " << getTotal(rain, months) << " inches." << endl;
 cout << "The average rainfall for the year is " << getAverage(rain, months) <<" inches." << endl;

 double largestRain = getLargest(rain, months,largestMonth);
 double smallestRain = getSmallest(rain,months,smallestMonth);

 cout << "The largest amount of rainfall was " << largestRain << " inches in month "
 << (largestMonth + 1) << "." <<endl;

 cout << "The smallest amount of rainfall was " << smallestRain << " inches in month "
 << (smallestMonth + 1) << "." <<endl;

 cout << endl;
 cout << "Here are the rainfall amounts, sorted in ascending order:" << endl;;
 cout << "----------------------------------------" << endl;
// Calling function to sort array in ascending order.
 selectionSort(rain, months);
 // For loop so we can display the amounts
 for (int i = 0; i < months; ++i) {
  cout << rain[i] << endl;
 }

 return 0;
}

/*Psuedocode
 * Variables
 *
 * User input for total Rainfall for each of the 12 months # Done
 *
 * If statements incase input is negative  #Done
 *
 * Store Input into array of doubles #Done
 *
 * Calculate Total, Mean for months and months with lowest and highest Rainfall
 * for the year using given function names #Done
 *
 * Output calculations and list of months in lowest to highest #Done
 *
 */
