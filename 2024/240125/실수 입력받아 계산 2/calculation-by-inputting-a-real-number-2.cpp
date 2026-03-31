#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    cout << fixed;
    float a;
    cin >> a;
    
    cout.precision(2);
    cout << a + 1.5;
    
    return 0;
}