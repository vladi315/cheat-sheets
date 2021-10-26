# C++ cheatsheet

## Compile and Run
run cpp file on command line (with g++ compiler)	

```c
g++ -Wall -std=c++14 textfile.cpp
//	- Wall: turn all warnings on
//	std=c++14: set standart
//	textfile.cpp: set output file
```
Alternatives for multiple files

`g++ -Wall helloworld-helper.cpp helloworld.cpp -o compiled_file`

`g++ *.cpp -o compiled_file`

Afterwards run 
`./compiled_file`

## import header and helper functions

use following three files: 
1. hpp header file *numbers.hpp*
```c
// numbers.hpp
#pragma once  
// To make sure you don't declare the function more than once by including the header multiple times.
// alternatively use 
    // ifndef HEADERVAR   
    // #define HEADERVAR

#include <iostream>
#include <vector>

using namespace std;

void printNumbers(vector<int> numbers);
vector<int> addNumbers(vector<int> &numbers);
    // #endif
```

2. helper function *numbers-functions.cpp*
```c
// numbers-functions.cpp
#include "numbers-header.hpp"

void printNumbers(vector<int> numbers){
    if (numbers.size() == 0)
        cout << "[] - the list is empty" << endl;
    else {
        cout << "[ ";
        for (auto num: numbers)
            cout << num << " ";
        cout << "]" << endl;
    }
}
vector<int> addNumbers(vector<int> &numbers){
    int num_to_add {};
    cout << "Enter an integer to add to the list: ";
    cin >> num_to_add;
    numbers.push_back(num_to_add);
    cout << num_to_add << " added" << endl;
    return numbers;
```

3. include numbers.hpp in main file, but not numbers-functions.cpp! Compile and run main.cpp and numbers-functions.cpp, the linker will link the compiled binary files. 
```c
#include "numbers-header.h"

int main() {
    printNumbers(numbers);
    numbers = addNumbers(numbers);
}
```


## Coding 
safe way of variable initialisation	
`int catch_error{"abc"}`
initialize local static variable (retains the value over multiple function calls (like a global variable, but on a local scope)
`static int i{5000};`

dynamic memory allocation and deallocation 
```c
    size_t size{0};
    double *temp_ptr {nullptr};
    cout << "How much memory to allocate dynamically? ";
    cin >> size;
    
    temp_ptr = new double[size];    // allocate the storage on the heap
    cout << temp_ptr << endl;       // use it
    delete [] temp_ptr;             // release it
```

## input and output
import for std input/output 	
```c
#include <iostream>
using namespace std;
```

std output    			
`cout << "Enter your favorite number" << endl;`

std input    			
`std::cin >> favorite_number;`

string declaration in cpp
```c
#include <string> // add `using namespace std;` if necessary
string test = "Some text";
cout << test << endl;
```

## compound datatypes

create an 1d-**array** --> fixed size	
giving the length explicitly
`int numbers[4]{0, 1, 2, 3, 4}` 
giving the length implicitly
`int numbers[]{0, 1, 2, 3, 4}`  // 
initialize all elements to 3.14
`double arr[4] = {3.14};`

create a **vector** (non fixed sized)
```c
#include <vector>
using namespace std;
vector <int> examples(100, 98, 95, 93);
```
index the 5th vector element
`examples.at(4) = 80;`
adding value 80 at the end of vector
`examples.push_back(80);`
indexing last element of vector
`examples.at(examples.size()-1) = 1000;`
multidimensional vector 
```c
vector <vector<int>> movie_ratings 
{   
    {1, 2, 3, 4},
    {1, 2, 4, 4},
    {1, 3, 4, 5}
};
```
