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
