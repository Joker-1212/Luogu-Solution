#include <bits/stdc++.h>
using namespace std;
int main()
{
    int flag = 1, x, ans = 0;
    scanf("%d", &x);
    if (x < 0)
        flag = -1, x = -x; // flag = -1 表示负数
    while (x != 0)
    {
        ans *= 10;     // ans挪出一位
        ans += x % 10; // 拼上x的最后一位
        x /= 10;
    }
    printf("%d", ans * flag);
    return 0;
}
