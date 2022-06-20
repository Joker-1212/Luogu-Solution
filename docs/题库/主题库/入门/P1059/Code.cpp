#include <bits/stdc++.h>
using namespace std;
int main()
{
    bool bucket[1001]{0};
    int n, x, ans = 0;
    scanf("%d", &n);
    while (n--)
    {
        scanf("%d", &x);
        // 没有出现过，标记一下
        if (!bucket[x])
            ++ans, bucket[x] = true;
    }
    printf("%d\n", ans);
    for (int i = 1; i <= 1000; ++i)
        if (bucket[i])
            printf("%d ", i);
    return 0;
}
