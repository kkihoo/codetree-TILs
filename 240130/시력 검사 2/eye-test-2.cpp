#include <iostream>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    float a;
    cin >> a;

    if (a >= 1.0){
        cout << "High" << endl;
    }
    else if (a >= 0.5){
        cout << "Middle" << endl;
    }
    else {
        cout << "Low" << endl;
    }
    return 0;
}