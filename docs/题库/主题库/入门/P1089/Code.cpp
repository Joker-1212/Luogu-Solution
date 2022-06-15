#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n = 0, a = 0, x;
    for (int i = 1; i < 13; ++i)
    {
        n += 300;
        scanf("%d", &x);
        if (n < x)
            return (printf("-%d", i), 0);
        n -= x;
        a += n / 100;
        n %= 100;
    }
    printf("%d", n + a * 120);
    return 0;
}
