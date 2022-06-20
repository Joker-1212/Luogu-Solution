#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n = 0, mx = 0, // 直接设定初始值为0，就不用加flag判断了
        a, b;
    for (int i = 1; i <= 7; ++i)
    {
        scanf("%d %d", &a, &b);
        if (a + b - 8 > mx)
            n = i, mx = a + b - 8;
    }
    printf("%d", n);
    return 0;
}
