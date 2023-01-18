#include <iostream>
#include <string>
using namespace std;
//hello
int main(int argc, char const **argv) {

    string line;
    int i, maxseen, subsum;
    subsum = maxseen =  0;

    while (getline(cin,line)) {
        if (line.size() == 0) {
            maxseen = max(maxseen, subsum);
            subsum = 0;
        }
        else {
            i = stoi(line);
            subsum += i;
        }
    }
    if (subsum != 0) {
        maxseen = max(maxseen, subsum);
    }
    cout << maxseen << endl;

    return 0;
}
