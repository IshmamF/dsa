#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	cout << "hello world" << endl;
	cout << abs(-4.7) << endl;
	vector<int> numbers = {1, 3, 5, 7, 2, 9};
	sort(numbers.begin(), numbers.end());
	for (int number : numbers) {
		cout << number << " ";
	}
	return 0;
}