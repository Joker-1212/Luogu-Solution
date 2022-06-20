# P1035 C++ 题解

## 题意理解

定义：$S_n = \sum\limits_{i = 1}^n \frac{1}{i}$，试求出最小的 $n$ 的值，使得 $S_n > k$

**数据范围：**

- $1 \leqslant k \leqslant 15$

## 题目分析

使用循环逐个枚举即可

## 编程实现

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int k, n = 0;
    scanf("%d", &k);
    for (double s = 0.0; s <= k; s += 1.0 / ++n)
        ;
    printf("%d", n);
    return 0;
}
```
