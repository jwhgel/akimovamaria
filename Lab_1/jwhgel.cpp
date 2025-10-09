#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    float x, y;

    cin >> x;
    cin >> y;

    float S = tan(x / y);

    float R = (pow(x, 1/3) * sin(x)) / (exp(3 * x) + exp(3 * y));

    cout << "R = " << R << endl;
    cout << "S = " << S << endl;

    float C = max(R, S);

    cout << "C = " << C << endl;

    return 0;
}