#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(int argc, char const **argv) {
    string line;
    int i, maxseen, subsum;
    subsum = maxseen =  0;
    int top3[3] = {0,0,0};
    while (getline(cin,line)) {
        if (line.size() == 0) {
            sort(top3, top3 + 3);
            for (size_t i = 0; i < 3; i++) {
                if (top3[i] < subsum) {
                    top3[i] = subsum;
                    break;
                }
             }
            subsum = 0;
        }
        else {
            i = stoi(line);
            subsum += i;
        }
    }
    if (subsum != 0) {
        for (size_t i = 0; i < 3; i++) {
            if(top3[i] < subsum) {
                top3[i] = subsum;
                break;
            }
        }
    }
    int final = 0;
    for (int j: top3) {
        final += j;
    }
    cout << final << endl;
    return 0;
}
