#include <bits/stdc++.h>
using namespace std;

bool open[2000005]{0};

int main()
{
    int n, t;
    double a;
    scanf("%d", &n);
    while (n--)
    {
        scanf("%lf%d", &a, &t);
        for (int i = 1; i <= t; ++i)
            open[int(a * i)] ^= 1;
    }
    for (int i = 1;; ++i)
        if (open[i])
            return (printf("%d", i), 0);
}