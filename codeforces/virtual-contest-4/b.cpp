#include <iostream>
#include <vector>
using namespace std;


int getOperations(string input) {
    int size = input.size();

    for (int i = 0; i < size - 1; i++) {
        if (input[i] == input[i + 1]) {
            return 1;
        }
    }
    return size;
}

int main() {
    int t;
    cin >> t;
    vector<int> res;
    for (int i = 0; i < t; i++) {
        string input;
        cin >> input;
        int output = getOperations(input);
        res.push_back(output);
    }

    for (int x: res) {
        cout << x << endl;
    }
}