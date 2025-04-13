#include <iostream>
#include <vector>
using namespace std;

int findMinimumLen(string input) {
    while (true) {
        int size = input.size();
        bool changed = false;
        vector<string> stack;
        for (int i = 0; i < size - 1; i++) {
            while (!stack.empty()) {
                changed = true;
                cout << input << endl;
                break;
            }
        }
        if (!changed) break;
    }
    return input.size();
}

int main() {
    int t;
    cin >> t;
    vector<int> res;
    for (int i = 0; i < t; i++) {
        string input;
        cin >> input;
        int output = findMinimumLen(input);
        res.push_back(output);
    }
    
    for (int x: res) {
        cout << x << endl;
    }
}