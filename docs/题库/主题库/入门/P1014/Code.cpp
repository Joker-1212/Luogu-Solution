#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    scanf("%d", &n);
    int num = 1, den = 1;
    bool down = false;
    while (--n)
    {
        if (down)
        {
            if (den == 1)
            {
                ++num;
                down = false;
            }
            else
            {
                ++num;
                --den;
            }
        }
        else
        {
            if (num == 1)
            {
                ++den;
                down = true;
            }
            else
            {
                ++den;
                --num;
            }
        }
    }
    printf("%d/%d", num, den);
    return 0;
}