#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int findY(int k, int l1, int r1, int l2, int r2) {
    int count = 0;
    long long kn=1;
    for (int n = 0; r2/kn>=l1; n++) {
        int min_x = max(l1, (int)((l2 + kn - 1) / kn));
        int max_x = min(r1, (int)(r2 / kn));
        if (max_x >= min_x) count += max_x - min_x + 1;
        kn *= k;
    }
    return count;
}

int main() {
    int t;
    cin >> t;
    vector<int> res;
    for(int i = 0; i < t; i++) {
        vector<int> input(5);
        for (int &x: input) cin>>x;
        int k = input[0];
        int l1 = input[1];
        int r1 = input[2];
        int l2 = input[3];
        int r2 = input[4];
        int output = findY(k, l1, r1, l2, r2);
        res.push_back(output);
    }
    for (int val: res) {
        cout << val << endl;
    }
}