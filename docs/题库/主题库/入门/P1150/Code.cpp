#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, k;
    scanf("%d%d", &n, &k);
    int ans = 0, butt = 0;
    while (n != 0)
    {
        ans += n;
        butt += n;
        n = butt / k;
        butt %= k;
    }
    printf("%d", ans);
    return 0;
}
