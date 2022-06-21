#include <bits/stdc++.h>
using namespace std;

int cnt(int x)
{
    int ans = 0;
    while (x != 0)
    {
        if (x % 10 == 2)
            ++ans;
        x /= 10;
    }
    return ans;
}

int main()
{
    int l, r, ans = 0;
    scanf("%d%d", &l, &r);
    for (int i = l; i <= r; ++i)
        ans += cnt(i);
    printf("%d", ans);
    return 0;
}
