#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
using namespace std;

vector<int> findRange(int l, int r, int m) {
    
    while (l < r) {
        int val = abs(l) + abs(r);
        if (val > m) {
            r--;
        } else if (val < m) {
            l++;
        } else {
            return vector<int>({l, r});
        }
    }

    return {l, r};
}


int main() {
    int t;
    cin >> t;
    vector<vector<int> > res;
    for (int i = 0; i<t; i++) {
        vector<int> input(4);
        for (int &x: input) cin >> x;
        // vector<int> val = findRange(input[2], input[3], input[1]);
        for (int j = input[2]; j <= input[3]; j++) {
            if (abs(j) + abs(input[3]) == input[1]) {
                res.push_back({j, input[3]});
            }
        }
        //res.push_back(val);
    }
    for (vector<int> x: res) {
        cout << x[0] << ' ' << x[1] << endl;
    }
    return 0;
}