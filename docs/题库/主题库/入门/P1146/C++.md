# P1146 C++ 题解

## 题意理解

有 $N$ 枚正面朝上的硬币，每次翻 $N - 1$ 枚硬币，最少翻几次能使得所有硬币反面朝上？并输出字典序最小翻转序列（$0$ 表示正面朝上，$1$ 表示反面朝上）。

**数据范围**

- $N \in \{2x | x \leqslant 50, x \in \mathbb N\}$

## 题目分析

因为每次翻 $N - 1$ 枚硬币，相当于每次只不翻转一枚硬币，所以最小次数即为硬币个数 $N$。而字典序最小，则是从第 $1$ 枚硬币开始，不翻当前硬币，翻转其他所有硬币。

## 编程实现

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, a[100]{0};
    scanf("%d", &n);
    printf("%d\n", n);
    // i 表示当前不翻的硬币
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            if (j != i)
                a[j] ^= 1; // 因为 a[i] 只有01两种状态，所以与1异或相当于去翻
            putchar(a[j] ^ 48); // 即a[j] + '0'
        }
        putchar(10); // putchar('\n')
    }
    return 0;
}
```
