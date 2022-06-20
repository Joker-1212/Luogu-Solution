#include <bits/stdc++.h>
using namespace std;
int main()
{
    int l, m, b, e, ans = 0;
    bool road[10005]{0};
    scanf("%d%d", &l, &m);
    while(m--)
    {
        scanf("%d%d", &b, &e);
        for (int i = b; i <= e; ++i)
            if (!road[i])
                ++ans, road[i] = true;
    }
    printf("%d", l + 1 - ans);
    return 0;
}
