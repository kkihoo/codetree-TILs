#include <iostream>
using namespace std;
int main() {
    char c;
    float a, b;
    cin >> c >> a >> b;

    cout << fixed;
    cout.precision(2);
    cout << c << "\n";
    cout << a << "\n";
    cout << b << "\n";
    return 0;
}