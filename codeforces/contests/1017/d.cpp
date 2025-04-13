#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<vector<int>> CountLRs(string input) {
    int i = 0;
    int inputSize = input.size();
    vector<vector<int>> res;
    while (i < inputSize) {
        if (input[i] == 'L') {
            int count = 0;
            while (input[i] == 'L') {
                count++;
                i++;
            }
            res.push_back(vector<int>{count, 0});
        } else {
            int count = 0;
            while (input[i] == 'R') {
                count++;
                i++;
            }
            res.push_back(vector<int>{count, 1});
        }
    }
    return res;
}

string CheckValid(string match, string check) {
    vector<vector<int>> countMatch = CountLRs(match);
    vector<vector<int>> countCheck = CountLRs(check);
    int matchSize = countMatch.size();
    int checkSize = countCheck.size();
    if (matchSize != checkSize) {
        return "NO";
    }

    for (int i = 0; i < matchSize; i++) {
        vector<int> match_i = countMatch[i];
        vector<int> check_i = countCheck[i];
        if (match_i[1] != check_i[1]) {
            return "NO";
        }
        int diff = check_i[0] - match_i[0];
        if (diff > 1 || diff < 0) {
            return "NO";
        }
    }
    return "YES";

}   

int main() {
    int t;
    cin >> t;
    vector<string> res;
    for (int i = 0; i < t; i++) {
        string input1;
        string input2;
        cin >> input1;
        cin >> input2;
        string test = CheckValid(input1, input2);
        res.push_back(test);
    }
    for (string x: res) {
        cout << x << endl;
    }
}