# P1151 C++ 题解

## 题意理解

定义：对于一个 $5$ 位数 $\overline{a_1a_2a_3a_4a_5}$，有：

$$
\begin{align*}
sub_1 &= \overline{a_1a_2a_3}\\
sub_2 &= \overline{a_2a_3a_4}\\
sub_3 &= \overline{a_3a_4a_5}\\
\end{align*}
$$

现在给定整数 $K$，求使得 $K|sub_1 \cap K|sub_2 \cap K|sub_3$ 成立的五位数 $\overline{a_1a_2a_3a_4a_5}$ 并分别输出它们。如果没有，输出 `NO`。

## 题目分析

这个题的关键点即难点都在求 $sub_1, sub_2, sub_3$ 上。下面分别加以讨论（设原五位数为 $a$）

### $sub_1$

$sub_1$ 是 $a$ 去掉后两位得到的。则 $sub_1 = \left\lfloor{\frac{a}{100}}\right\rfloor$

### $sub_2$

$sub_2$ 是 $a$ 去掉首尾得到的。则可以先除以 $10$ 去掉末位，在对 $1000$ 取模去掉首位，即：$sub_2 = \lfloor\frac{a}{10}\rfloor \bmod 1000$

## $sub_3$

$sub_3$ 是 $a$ 去掉前两位得到的，即：$sub_3 = a \bmod 1000$

## 编程实现

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int k, find = 0;
    scanf("%d", &k);
    for (int i = 10000; i <= 30000; ++i)
    {
        int sub1 = i / 100, sub2 = i / 10 % 1000, sub3 = i % 1000;
        if (sub1 % k == 0 && sub2 % k == 0 && sub3 % k == 0)
            printf("%d\n", i), find = 1;
    }
    if (find == 0)
        puts("No");
    return 0;
}
```