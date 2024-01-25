#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    float a, b;
    cout << fixed;
    cin >> a >> b;
    
    cout.precision(2);
    cout << a + b;
    return 0;
}