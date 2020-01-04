#include <iostream>
#define ll long long
using namespace std;


ll fact(int n) {

    ll ans = 1;
    for (int i = 1; i <= n; i++) {
        ans *= i;
    }
    return ans;
}

int main() {
    
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        cout << fact(n);
    } 
    
    
	return 0;
}
