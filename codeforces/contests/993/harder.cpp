#include <iostream>
#include <set>
#include <vector>
using namespace std;

set<int> CreateFullSet(int size) {
    set<int> fullSet;
    for (int i = 1; i <= size; i++) {
        fullSet.insert(i);
    }
    return fullSet;
}

vector<int> CreateNewArrB(vector<int> arr, int size) {
    set<int> visit;
    set<int> fullSet = CreateFullSet(size);
    vector<int> newArr(size, 0);
    for (int i = 0; i < size; i++) {
        if (!visit.contains(arr[i])) {
            visit.insert(arr[i]);
            fullSet.erase(arr[i]);
            newArr[i] = arr[i];
        }
    }

    for (int i = 0; i < size; i++) {
        if (newArr[i] == 0) {
            int setVal = *fullSet.begin();
            fullSet.erase(setVal);
            newArr[i] = setVal;
        }
    }
 
    return newArr;
}

int main() {
    int t;
    cin >> t;
    vector<vector<int>> newArrBs;
    for (int i = 0; i < t; i++) {
        int size;
        cin >> size;
        vector<int> arr(size);
	    for(int &i: arr)cin>>i;
        vector<int> newArr = CreateNewArrB(arr, size);
        newArrBs.push_back(newArr);
    }
    
    for (vector<int>& x : newArrBs) {
        bool first = true;
        for (int val : x) {
            if (!first) cout << " ";
            cout << val;
            first = false;
        }
        cout << endl;
    }
    return 0;
}