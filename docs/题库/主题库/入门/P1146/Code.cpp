#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, a[100]{0};
    scanf("%d", &n);
    printf("%d\n", n);
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            if (j != i)
                a[j] = a[j] == 0 ? 1 : 0;
            printf("%d", a[j]);
        }
        putchar(10);
    }
    return 0;
}
