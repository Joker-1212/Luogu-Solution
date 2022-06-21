# P1150 C++ 题解

## 题意理解

有 $n$ 根烟，每 $k$ 个烟蒂可以卷成新烟。问 Peter 能吸到多少根烟。

**数据分析**

- $1 < n, k \leqslant 10^8$

## 题目分析

开无限循环模拟，直到无烟可吸，输出吸烟总个数。

## 编程实现

```cpp
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
```