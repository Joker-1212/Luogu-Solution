# P1116 C++ 题解

## 题意理解

有 $N$ 节火车厢，每次可以交换相邻的两个车厢。要将车厢按编号从小到大的顺序排序，最少需要几步？

**数据范围**

- $N \leqslant 10^4$

## 题目分析

这个题的排序方法类似于冒泡排序，但是可以不用排序，算出逆序对的个数即可。

> 略证：
> 因为每一次交换，都使得一对逆序对被更改，所以逆序对的个数就是最少交换次数

## 编程实现

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, a[10000]{0}, ans = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i)
        scanf("%d", &a[i]);
    for (int i = 0; i < n; ++i)
        for (int j = i + 1; j < n; ++j)
            if (a[j] < a[i])
                ++ans;
    printf("%d", ans);
    return 0;
}
```