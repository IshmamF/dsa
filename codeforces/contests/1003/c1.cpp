#include <iostream>
#include <vector>
using namespace std;

bool isSorted(vector<int> a, int size) {
    int prev = a[0];
    for (int i = 1; i < size; i++) {
        if (a[i] < prev) {
            return false;
        }
        prev = a[i];
    }
    return true;
}

string checkIfCanSort(vector<int> a, int b) {
    int size = a.size();
    if (isSorted(a, size)) {return "YES";}
    for (int i = 0; i < size; i++) {
        int temp = a[i];
        a[i] = b - a[i];
        bool check = isSorted(a, size);
        
    }
}

int main() {
    int t;
    cin >> t;
    vector<string> res;
    for (int i = 0; i < t; i++) {
        int n; int m; 
        cin >> n >> m;
        vector<int> arr(n);
        for (int &x: arr) cin >> x;
        int b; 
        cin >> b;
        string output = checkIfCanSort(arr, b);
        res.push_back(output);
    }
    
    for (string x: res) {
        cout << x << endl;
    }
}