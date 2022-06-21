# P1152 C++ 题解

## 题意理解

一个 $n$ 个元素的数组，两个连续元素之间差的绝对值包括了 $[1,n−1]$ 之间的所有整数，则符合欢乐的跳。给定一个数组，判断是否符合欢乐的跳。

**数据范围**

- $1 \leqslant n \leqslant 100$

## 题目分析

由于长度为 $n$ 的数组只有 $n - 1$ 个相邻元素差，只要差值出现重复或超出 $[1, n - 1]$ 这个范围，就一定不是欢乐的跳。

## 编程实现

```cpp
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
```