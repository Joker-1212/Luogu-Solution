# P1179 C++ AC

## 题意理解

求出 $[L, R]$ 中的所有整数中数字 $2$ 出现的次数。

**数据范围**

- $1 \leqslant L \leqslant R \leqslant 10^5$

## 题目分析

重点在于如何取得每一位数字。

首先对 $10$ 取模可以得到个位，除以 $10$ 可以舍弃个位。所以可以不断 $\bmod 10$ 再 $\div 10$，直到数字为 $0$，就可以求得各位数字。

## 编程实现

```cpp
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
```