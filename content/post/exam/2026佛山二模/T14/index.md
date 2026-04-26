---
title: "2026佛山二模第14题详解"
description:
author:
- xieyuen
date: 2026-04-18T14:22:29+08:00
image:
math: true
license:
draft: false
build:
    list: always    # Change to "never" to hide the page from the list
categories:
- Examinations
tags:
- 佛山二模
---

## 原题

已知 $F_1, F_2$ 是双曲线 $C: \frac{x^2}{4} - \frac{y^2}{6} = 1$ 的左右焦点, $A, B \in C$, 且满足 $\overrightarrow{AF_2} = \lambda \overrightarrow{F_2 B} (\lambda > 0)$. 若 $\cos \angle A F_1 B = \frac{3}{5}$, 求 $\triangle ABF_1$ 的内切圆半径.

## 答案

内切圆半径为 2.

## 解析

双曲线方程为 $\frac{x^2}{4} - \frac{y^2}{6} = 1$, 可得:

- $a^2 = 4 \implies a = 2$
- $b^2 = 6$
- $c^2 = a^2 + b^2 = 10 \implies c = \sqrt{10}$
- 焦距 $|F_1 F_2| = 2c = 2\sqrt{10}$

由 $\overrightarrow{AF_2} = \lambda \overrightarrow{F_2 B} (\lambda > 0)$ 可知, $A, F_2, B$ 三点共线, 且 $F_2$ 位于线段 $AB$ 之间. 即 $AB$ 是过右焦点 $F_2$ 的一条弦, 并且 $A$, $B$都在双曲线的右支.

设 $|AF_1| = m$, $|BF_1| = n$.
根据双曲线定义, 对于右支上的点 $P$, 有 $|PF_1| - |PF_2| = 2a = 4$. 那么有:

- $|AF_2| = |AF_1| - 2a = m - 4$
- $|BF_2| = |BF_1| - 2a = n - 4$
- $\triangle ABF_1$ 的边 $AB$ 长度为: $|AB| = |AF_2| + |BF_2| = (m - 4) + (n - 4) = m + n - 8$

在 $\triangle ABF_1$ 中, 已知 $\cos \angle AF_1B = \frac{3}{5}$, 则 $\sin \angle AF_1B = \sqrt{1 - (\frac{3}{5})^2} = \frac{4}{5}$.

由余弦定理:

$$
|AB|^2 = |AF_1|^2 + |BF_1|^2 - 2|AF_1||BF_1| \cos \angle AF_1B
$$

代入边长表达式:

$$
(m + n - 8)^2 = m^2 + n^2 - 2mn \cdot \frac{3}{5}
$$

展开左边:

$$
(m+n)^2 - 16(m+n) + 64 = m^2 + n^2 - \frac{6}{5}mn
$$

$$
m^2 + 2mn + n^2 - 16(m+n) + 64 = m^2 + n^2 - \frac{6}{5}mn
$$

消去 $m^2, n^2$ 并整理:

$$
2mn + \frac{6}{5}mn = 16(m+n) - 64
$$

即

$$
\frac{16}{5}mn = 16(m+n) - 64
$$

两边同除以 16:

$$
\frac{1}{5}mn = (m+n) - 4
$$
$$
mn = 5(m+n) - 20
$$

设 $\triangle ABF_1$ 的内切圆半径为 $r$, 面积为 $S$, 半周长为 $s$. 则:

$$
\begin{aligned}
    s &= \frac{|AF_1| + |BF_1| + |AB|}{2} \\
    &= \frac{m + n + (m + n - 8)}{2} \\
    &= \frac{2(m+n) - 8}{2} \\
    &= m + n - 4
\end{aligned}
$$

$$
S = \frac{1}{2} |AF_1| |BF_1| \sin \angle AF_1B = \frac{1}{2} mn \cdot \frac{4}{5} = \frac{2}{5} mn
$$

故

$$
r = \frac{S}{s} = \frac{\frac{2}{5} mn}{m + n - 4}
$$

将步骤 3 中得到的 $mn = 5(m+n) - 20 = 5(m+n-4)$ 代入上式:

$$
r = \frac{\frac{2}{5} \cdot 5(m+n-4)}{m+n-4} = 2
$$
