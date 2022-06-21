#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, a[100]{0};
    scanf("%d", &n);
    printf("%d\n", n);
    // i 表示当前不翻的硬币
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            if (j != i)
                a[j] ^= 1;      // 因为 a[i] 只有01两种状态，所以与1异或相当于去翻
            putchar(a[j] ^ 48); // 即a[j] + '0'
        }
        putchar(10); // putchar('\n')
    }
    return 0;
}