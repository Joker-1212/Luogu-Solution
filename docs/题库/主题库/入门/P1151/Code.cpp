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
