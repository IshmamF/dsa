#include <iostream>
#include <vector>
#include <string>
#include <set>
using namespace std;

vector<int> findPermutation(vector<vector<int>> grid, int size) {
    vector<int> res(2*size);
    set<int> hashSet;
    vector<int> hashVector;

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            int val = grid[i][j];
            if (hashSet.find(val) == hashSet.end()) {
                hashSet.insert(val);
                hashVector.push_back(val);
            } 
        }
    }
    
    vector<int> NotIncluded;
    for (int i = 1; i <= 2 * size; i++) {
        if (hashSet.find(i) == hashSet.end()) {
            NotIncluded.push_back(i);
        }
    }
    int j = 0;
    for (int i = 0; i < NotIncluded.size(); i++) {
        res[j++] = NotIncluded[i];
    }
    for (int i = 0; i < hashVector.size(); i++) {
        res[j++] = hashVector[i];
    }
    return res;
 } 

int main() {
    int t; 
    cin >> t;
    vector<vector<int>> res;
    for (int i = 0; i<t; i++) {
        int size;
        cin >> size;
        vector<vector<int>> grid(size, vector<int>(size));
        for (int j = 0; j < size; j++) {
            for (int k = 0; k < size; k++) {
                cin >> grid[j][k];
            }
        }
        vector<int> output = findPermutation(grid, size);
        res.push_back(output);
    }

    for (const vector<int>& x : res) {
        for (int val : x) {
            cout << val << " ";
        }
        cout << endl;
    }

}