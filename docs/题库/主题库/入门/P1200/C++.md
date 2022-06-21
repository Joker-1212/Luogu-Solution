# P1120 C++ 题解

## 题意理解

给定两个只有大写字母的字符串，将其转化为数字并 $\mod 47$。判断结果是否相同。

字符串转化为数字的方法：$A \rightarrow 1, B \rightarrow 2, \cdots, Y \rightarrow 25, Z \rightarrow 26$，将各位相乘得到数字

**数据范围**

- $1 \leqslant |s| \leqslant 6$

## 题目分析

将大写字母减去 `'A'` 再加 $1$ 即可。

## 编程实现

```cpp
#include <bits/stdc++.h>
#define mod 47
using namespace std;

inline int f(char c)
{
    return c - 'A' + 1;
}

int main()
{
    int x = 1, y = 1;
    char s[10];
    scanf("%s", s);
    for (int i = 0; s[i]; ++i)
    {
        x *= f(s[i]);
        x %= mod; // 一步一取模
    }
    scanf("%s", s);
    for (int i = 0; s[i]; ++i)
    {
        y *= f(s[i]);
        y %= mod;
    }
    puts(x == y ? "GO" : "STAY");
    return 0;
}
```