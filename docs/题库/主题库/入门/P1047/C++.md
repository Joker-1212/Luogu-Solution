# P1047 C++ 题解

## 题意理解

有一条长为 $l\ \mathrm{m}$ 的马路，每隔 $1 \ \mathrm{m}$ 种有一棵树。现在移除一些区域的树。每个区域都用 $[u, v]$ 表示，移除时包括两端的树。求还剩下多少棵树

**数据范围**

- $1 \leqslant m \leqslant 100$
- $1 \leqslant u \leqslant v \leqslant l$

## 题目分析

开一个 $l + 1$ 的 `bool` 数组，表示该点的树是否被移除。然后对于每一次操作，如果该点的树木没有被移除，$\mathcal{Ans} - 1$。最后输出 $\mathcal{Ans}$ 即可

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int l, m, b, e;
    bool road[10005]{0};
    scanf("%d%d", &l, &m);
    while(m--)
    {
        scanf("%d%d", &b, &e);
        for (int i = b; i <= e; ++i)
            if (!road[i])
                --l, road[i] = true;
    }
    printf("%d", l + 1 - ans);
    return 0;
}
```
