# P1304 C++ 题解

## 题意理解

在$[4, N]$的范围内验证哥德巴赫猜想

**数据范围**

- $N \leqslant 10^4$

## 题目分析

先筛出所有素数，再逐个枚举即可。

## 编程实现

```cpp
#include <bits/stdc++.h>
using namespace std;

bool is[10005];
int primer[5010], cnt = 0;

// 线性筛
void mark()
{
    memset(is, 0, sizeof(is));
    is[0] = is[1] = true;
    for (int i = 2; i <= 10000; ++i)
    {
        if (!is[i])
            primer[cnt++] = i;
        for (int j = 0; i * primer[j] <= 10000; ++j)
        {
            is[i * primer[j]] = true;
            if (i % primer[j] == 0)
                break;
        }
    }
}

int main()
{
    mark();
    int n;
    scanf("%d", &n);
    for (int i = 4; i <= n; i += 2)
    {
        for (int j = 0; j < cnt; ++j)
        {
            if (!is[i - primer[j]])
            {
                printf("%d=%d+%d\n", i, primer[j], i - primer[j]);
                break;
            }
        }
    }
    return 0;
}
```