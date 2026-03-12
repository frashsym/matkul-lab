#include <iostream>
using namespace std;

int main()
{
    int total = 0;
    int jumlah = 0;

    cout << "Deret Bilangan 0 - 50 (Kelipatan 5):" << endl;

    for (int i = 0; i <= 50; i += 5)
    {
        cout << i << " ";
        total += i;
        jumlah++;
    }

    cout << "\nJumlah Data  : " << jumlah << endl;
    cout << "Total Nilai  : " << total << endl;
    
    return 0;
}
