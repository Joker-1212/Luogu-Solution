#include <bits/stdc++.h>
using namespace std;
int main()
{
    bool a[1005]{0};
    int n, x, y, cnt;
    scanf("%d%d", &n, &x);
    cnt = n;
    while (--cnt)
    {
        y = x, scanf("%d", &x);
        if (abs(y - x) > n - 1 || a[abs(y - x)])
            return (puts("Not jolly"), 0);
        a[abs(y - x)] = true;
    }
    puts("Jolly");
    return 0;
}
