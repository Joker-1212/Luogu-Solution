#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    scanf("%d", &n);
    int num = 1, den = 1; // 第一个数
    bool down = false;    // 是否为下降行
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