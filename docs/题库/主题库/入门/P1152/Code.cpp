#include <bits/stdc++.h>
using namespace std;
int main()
{
    bool a[1005]{0}; // 记录差值是否出现过的数组
    int n,
        x, y, // 表示相邻的两个元素
        cnt;  // 由于需要使用n进行比较，用cnt作为循环控制变量
    scanf("%d%d", &n, &x);
    cnt = n;
    while (--cnt)
    {
        y = x, scanf("%d", &x);
        if (abs(y - x) > n - 1 ||          // 爆range
            a[abs(y - x)])                 // 差值重复
            return (puts("Not jolly"), 0); // 直接输出+退出
        a[abs(y - x)] = true;
    }
    puts("Jolly");
    return 0;
}