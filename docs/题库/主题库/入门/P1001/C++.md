# P1001 C++ 题解

## 题意理解

输入两个数 $a,b$，输出它们的和 $a + b$

**数据范围：**

- $|a|, |b| \leqslant 10^9$

## 题目分析

用 `scanf` 输入两个数，输出 $a + b$ 即可

## 编程实现

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int a, b;
    scanf("%d%d", &a, &b);
    printf("%d", a + b);
    return 0;
}
```