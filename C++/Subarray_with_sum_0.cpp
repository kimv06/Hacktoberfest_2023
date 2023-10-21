#include <iostream>
#include <unordered_set>
using namespace std;

bool subarrayWithSumZero(int arr[], int n) {
    unordered_set<int> s;
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
        if (sum == 0 || s.find(sum) != s.end()) {
            return true;
        }
        s.insert(sum);
    }
    return false;
}

int main() {
    int arr[] = {4, 2, -3, 1, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    if (subarrayWithSumZero(arr, n)) {
        cout << "Found a subarray with sum 0\n";
    } else {
        cout << "No subarray with sum 0\n";
    }
    return 0;
}
