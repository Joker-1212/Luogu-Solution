#include <bits/stdc++.h>
#define mod 47
using namespace std;

inline int f(char c)
{
    return c - 'A' + 1;
}

int main()
{
    int x = 1, y = 1;
    char s[10];
    scanf("%s", s);
    for (int i = 0; s[i]; ++i)
    {
        x *= f(s[i]);
        x %= mod;
    }
    scanf("%s", s);
    for (int i = 0; s[i]; ++i)
    {
        y *= f(s[i]);
        y %= mod;
    }
    puts(x == y ? "GO" : "STAY");
    return 0;
}
