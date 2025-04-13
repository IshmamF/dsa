#include <iostream>
#include <vector>
#include <string>
using namespace std;

string GetFirstChar(string input) {
    int inputSize = input.size();
    string output;
    for (int i = 0; i < inputSize; i++) {
        char c = input[i];
        if (c == ' ' && i + 1 < inputSize) {
            output += input[i + 1];
        }
    }
    return output;
}

int main() {
    int t;
    cin >> t;
    vector<string> res;
    for (int i = 0; i<t; i++) {
        string input;
        cin >> input;
        string val = GetFirstChar(input);
        res.push_back(val);
    }
    for (string x: res) {
        cout << x << endl;
    }
    return 0;
}