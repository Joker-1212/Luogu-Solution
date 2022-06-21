#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, k;
    scanf("%d%d", &n, &k);
    int ans = 0,
        butt = 0; // 表示烟蒂个数
    while (n != 0)
    {
        // 为了节省时间，一次吸完所有的烟，一次全部卷成新烟。
        // 吸烟
        ans += n;
        butt += n;
        // 卷烟
        n = butt / k;
        butt %= k;
    }
    printf("%d", ans);
    return 0;
}
