#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, a[10000]{0}, ans = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
        scanf("%d", &a[i]);
    for (int i = 0; i < n; ++i)
        for (int j = i + 1; j < n; ++j)
            if (a[j] < a[i])
                ++ans;
    printf("%d", ans);
    return 0;
}
