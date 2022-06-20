# P1075 C++ 题解

## 题意理解

$n$ 是两个不同质数的乘积，求出较大质因数。

**数据范围**

- $n \leqslant 2 \times 10^9$

## 题目分析

由于 $n$ 是两个质数的积，$n$ 只能被分成这两个质数相乘（不考虑 $1 \times n$），因此只需要从 $2$ 开始遍历，一找到 $n$ 的因数 $k$，输出 $n \div k$ 即可

## 编程实现

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 2; i < n / 2; ++i)
        if (n % i == 0)
            return (printf("%d", n / i), 0);
}
```