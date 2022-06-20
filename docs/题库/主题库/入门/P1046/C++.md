# P1046 C++ 题解

## 题意理解

有 $10$ 个苹果，每个苹果有一定的高度 $a_i$，陶陶身高为 $k$，并且有 $30\, \mathrm{cm}$ 高的凳子。问陶陶能摘到几个苹果？（手一碰到苹果就能摘到）

**数据范围：**

- $100 \leqslant a_i \leqslant 200（单位：\mathrm{cm}）$
- $100 \leqslant k \leqslant 120（单位：\mathrm{cm}）$

## 题目分析

先用一个数组把苹果高度 $a_i$ 存起来，再将 $k + 30$ 与 $a_i$ 一一比较即可

## 编程实现

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int a[10], ans = 0, n;
    for (int i = 0; i < 10; ++i)
        scanf("%d", &a[i]);
    scanf("%d", &n);
    n += 30;
    for (int i = 0; i < 10; ++i)
        if (a[i] <= n)
            ++ans;
    printf("%d", ans);
    return 0;
}
```