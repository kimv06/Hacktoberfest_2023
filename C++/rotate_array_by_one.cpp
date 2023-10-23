#include <iostream>
using namespace std;

void rotateByOne(int arr[], int n) {
  int t = arr[0];
  arr[0] = arr[n - 1];

  for (int i = 1; i < n; i++) {
    int temp = arr[i];
    arr[i] = t;
    t = temp;
  }
}

int main() {
  int arr[6] = {10, 20, 30, 40, 50, 60};

  for (int i = 0; i < 6; i++) {
    cout << arr[i] << "  ";
  }
  cout << endl;

  rotateByOne(arr, 6);

  for (int i = 0; i < 6; i++) {
    cout << arr[i] << "  ";
  }
  cout << endl;

  return 0;
}
