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
`g++ -Wall helloworld-helper.cpp helloworld.cpp -o myprogram `
`g++ -c *.cpp -o myprogram`
Afterwards run 
`./myprogram`

							
## Coding 
safe way of variable initialisation	
`int catch_error{"abc"}`
initialize local static variable (retains the value over multiple function calls (like a global variable, but on a local scope)
`static int i{5000};`

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
