#include <bits/stdc++.h>
using namespace std;
int main()
{
    int k, n = 0;
    scanf("%d", &k);
    for (double s = 0.0; s <= k; s += 1.0 / ++n)
        ;
    printf("%d", n);
    return 0;
}