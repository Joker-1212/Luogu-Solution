# P1001 Python3 题解

## 题意理解

给定两个数 $a,b$，输出它们的和。

**数据范围：**

- $|a|,|b| \leqslant 10^9$

## 题目分析

用 `input` 读取一行，`split` 分割，`map` 转化格式，`sum` 求和

## 编程实现

```python
print(sum(map(int, input().split())))
```