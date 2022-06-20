# P1059 C++ 题解

## 题意理解

给你 $N$ 个整数 $a_i$，请去重并排序。输出个数和排序后的数组。

**数据范围**

- $N \leqslant 100$
- $1 \leqslant a_i \leqslant 1000$

## 题目分析

对于这道题，可以使用桶排序。开一个桶来存储每一个数是否出现过。

每当输入一个数据，判断其是否曾经出现过。如果没出现过，个数加 $1$，在桶中标记为出现过。

最后输出数组时，如果出现过，则输出。

## 编程实现

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    bool bucket[1001]{0};
    int n, x, ans = 0;
    scanf("%d", &n);
    while (n--)
    {
        scanf("%d", &x);
        // 没有出现过，标记一下
        if (!bucket[x])
            ++ans, bucket[x] = true;
    }
    printf("%d\n", ans);
    for (int i = 1; i <= 1000; ++i)
        if (bucket[i])
            printf("%d ", i);
        return 0;
}
```