#include <bits/stdc++.h>
using namespace std;
int main()
{
    int a[10], ans = 0, n;
    for (int i = 0; i < 10; ++i)
        scanf("%d", &a[i]);
    scanf("%d", &n);
    n += 30;
    for (int i = 0; i < 10; ++i)
        if (a[i] <= n)
            ++ans;
    printf("%d", ans);
    return 0;
}