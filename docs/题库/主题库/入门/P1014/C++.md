# P1014 C++ 题解

## 题意理解

Catnor 表以 `z` 字形排列编号。求编号为 $N$ 的数字

**数据范围：**

- $1 \leqslant N \leqslant 10^7$

## 题目分析

通过观察，可以发现：分两种情况（下文中的行指一个从左下斜到右上的一个斜线）

### $\text{Case 1:}$ 下降行

对于下降行（从右上斜至左下），可以发现：每下降一个数，分子加 $1$，分母减 $1$。当分母为 $1$ 时，该行结束，分子加 $1$ 转入下一上升行。

### $\text{Case 2:}$ 上升行

对于上升行（从左下斜至右上），可以发现：每上升一个数，分母加 $1$，分子减 $1$。当分子为 $1$ 时，该行结束，分母加 $1$ 转入下一下降行。

再次分析可得：奇数行为上升行，偶数行为下降行。因此这道题的实现方法为：模拟直到第 $N$ 个数

## 编程实现

可以用 `bool` 型变量来记录当前行为下降行还是上升行，循环模拟即可

```cpp
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    scanf("%d", &n);
    int num = 1, den = 1; // 第一个数
    bool down = false; // 是否为下降行
    // 因为从 1 开始，要少循环一次
    while (--n) // 小技巧：while (--n) 只会循环 n - 1 次
    {
        // 模拟下降行
        if (down)
        {
            if (den == 1) // 到达 EOL
                ++num, down = false;
            else
                ++num, --den;
        }

        // 模拟上升行
        else
        {
            if (num == 1) // 到达 EOL
                ++den, down = true;
            else
                ++den, --num;
        }
    }
    printf("%d/%d", num, den);
    return 0;
}
```