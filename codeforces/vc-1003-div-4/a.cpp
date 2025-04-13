#include <iostream>
#include <vector>
#include <string>
using namespace std;

string convertToPlural(string input) {
    int size = input.size();
    string output = input.substr(0, size - 2);
    return output + 'i';
}

int main() {
    int t;
    cin >> t;
    vector<string> res; 
    for (int i = 0; i < t; i++) {
        string input;
        cin >> input;
        string convertedString =  convertToPlural(input);
        res.push_back(convertedString);
    }
    for (string str: res) {
        cout << str << endl;
    }
}