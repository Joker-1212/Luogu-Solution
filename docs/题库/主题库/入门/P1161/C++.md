# P1161 C++ 题解

## 题意理解

有无限盏路灯，编号从 $1$ 开始。现定义一次操作：给定两个数 $a$ 和 $t$，将编号为 $\lfloor a \rfloor, \lfloor 2a \rfloor, \lfloor 3a \rfloor, \cdots , \lfloor a \cdot t \rfloor$

小明进行了 $n$ 操作，发现只有一盏灯亮起。请求出灯的编号。

**数据范围**

记 $T = \sum\limits_{i = 1}^{n} t_i$

则：

- $n \leqslant 5000$
- $1 \leqslant a_i < 1000$
- $T \leqslant 2 \times 10^6$
- $1 \leqslant t_i \leqslant T$
- $t_i \times a_i \leqslant 2 \times 10^6$

## 题目分析

只需按题目所说模拟即可。

## 编程实现

```cpp
#include <bits/stdc++.h>
using namespace std;

int open[2000005]{0};

int main()
{
    int n, t;
    double a;
    scanf("%d", &n);
    while (n--)
    {
        scanf("%lf%d", &a, &t);
        for (int i = 1; i <= t; ++i)
            open[int(a * i)] ^= 1;
    }
    for (int i = 1;; ++i)
        if (open[i])
            return (printf("%d", i), 0);
}
```