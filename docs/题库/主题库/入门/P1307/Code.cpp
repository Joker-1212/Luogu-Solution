#include <bits/stdc++.h>
using namespace std;
int main()
{
    int flag = 1, x, ans = 0;
    scanf("%d", &x);
    if (x < 0)
        flag = -1, x = -x;
    while (x != 0)
    {
        ans *= 10;
        ans += x % 10;
        x /= 10;
    }
    printf("%d", ans * flag);
    return 0;
}
