---
title: "2025年河源中学高一年级数学竞赛答案"
description: 2025年河源中学高一年级数学竞赛答案
date: 2025-12-19
image: 
math: true
license: All Right Reserved, 河源中学数学研究协会
hidden: false
comments: true
draft: false
categories:
    - Contests
tags:
    - 高一竞赛
    - 答案
---

## 填空题

| 题号 |                        答案                         |
|:--:|:-------------------------------------------------:|
| 1  |                      $M = N$                      |
| 2  | $\frac{1 + \sqrt{3} \cdot 2023}{\sqrt{3} - 2023}$ |
| 3  |                      $2540$                       |
| 4  |                   $\mathbb{R}$                    |
| 5  |                       $27$                        |
| 6  |                        $4$                        |
| 7  |                   $\frac{1}{2}$                   |
| 8  |                        $5$                        |

由于第 4 题没有说明 $a, b, c > 0$, 故答案为 $\mathbb{R}$, 更改后为 $[\frac{3}{2}, +\infty)$.

## 解答题

### 9. (16分, 10+6)

本题为射影几何(极点极线)背景下的几何题,
可以考虑使用建系并当作圆锥曲线大题完成.

#### 小题答案速览

1. 证明略
2. $BG$ 是定值, 定值为 $\frac{r^2}{a}-r$

#### 详细解析

答案暂不提供

<!--
##### 第 (1) 问

##### 第 (2) 问
-->

### 10. (20分, 4+8+8)

本题改编自 2024 年高三 T8 联考 14 题.

#### 小题答案速览

1. $2 + 2\sqrt{2}$
2. $x$ 的取值范围是 $[-4, 4]$, $y$ 的取值范围是 $[-\sqrt{2}, \sqrt{2}]$, 当 $|x|$ 最大时 $|x+y|=5$
3. $f(x)$ 单调递增, 证明略

#### 详细解析

##### 第 (1) 问

$$ 8 = x^2 - 4xy + 8y^2 \ge 4\sqrt{2} - 4xy $$

$$\therefore xy \le 2 + 2\sqrt{2}$$

当且仅当 $x = 2\sqrt{2}y$, 即

$$
\begin{cases}
    x = \sqrt{8+4\sqrt{2}} \\
    y = \sqrt{1+\frac{\sqrt{2}}{2}}
\end{cases}
\quad \text{或} \quad
\begin{cases}
    x = -\sqrt{8+4\sqrt{2}} \\
    y = -\sqrt{1+\frac{\sqrt{2}}{2}}
\end{cases}
$$

时取等.

##### 第 (2) 问

配方得

$(x - 2y)^2 + 4y^2 = 8$

$\therefore 8 = (x - 2y)^2 + 4y^2 \ge \frac{1}{2}x^2 \Rightarrow x^2 \le 16$

$\therefore x$ 的范围是

$$
[-4, 4]
$$

又 $x^2-4xy+8y^2-8=0$,

把它看作关于 $x$ 的一元二次方程, 则该方程有解,

$\therefore \Delta = (4y)^2 - 4 \cdot 1 \cdot (8y^2 - 8)  = 16(2-y^2) \ge 0$

$\therefore y$ 的范围是

$$
[-\sqrt{2}, \sqrt{2}]
$$

当 $|x|$ 取最大值 4 时, 令 $x = 4 \Rightarrow y = 1, x = -4 \Rightarrow y = -1$,

$$
\therefore |x+y| = 5
$$

##### 第 (3) 问

$\forall -4 \le x_1 < x_2 < 0$ 且 $y_1 = f(x_1) > 0, y_2 = f(x_2) > 0$,

则

$$
\begin{align*}
x_1^2 - 4x_1y_1 + 8y_1^2 = 8 \\
x_2^2 - 4x_2y_2 + 8y_2^2 = 8
\end{align*}
$$

两式相减得

$(x_1^2 - x_2^2) - 4(x_1y_1 - x_2y_2) + 8(y_1 - y_2)(y_1 + y_2) = 0$

$\because x_1 < x_2 < 0 \Rightarrow (x_1 - x_2)(x_1 + x_2) > 0$,

$\therefore 2(y_1 - y_2)(y_1 + y_2) < x_1y_1 - x_2y_2 < x_2(y_1 - y_2)$

$\therefore (y_1 - y_2)(2y_1 + 2y_2 - x_2) < 0$

$\because y_1 > 0, y_2 > 0, x_2 < 0 \Rightarrow 2y_1 + 2y_2 - x_2 > 0$

$\therefore y_1 < y_2, f(x_1) < f(x_2)$

$\therefore f(x)$ 单调递增.

### 11. (16分, 4+7+9)

本题有误, 由于 $L$ 函数的条件写错为“实数 $s, t$”导致本题无解, 条件应改为“正数 $s, t$”

改正后答案如下.

#### 小题答案速览

1. 是
2. $a \in [1, +\infty)$
3. 证明略

#### 详细解析

##### 第 (1) 问

$\forall s, t > 0$, 显然 $h(s) = s^3 + s >0, h(t) = t^3 + t >0$

且 $h(s) + h(t) - h(s + t) = -3st(s+t) < 0 \Rightarrow h(s) + h(t) < h(s + t)$

$\therefore h(x)$ 是“L 函数”.

##### 第 (2) 问

$\because \forall x > 0, g(x) = a(e^x - 1) + (e^{-x}-1) = (e^x -1)(a - e^{-x}) > 0$

$\therefore a > e^{-x} \forall x > 0$ 恒成立, 即 $a \ge 1$

又 $\forall s, t > 0, g(s)+g(t) < g(s+t) \Rightarrow (e^s - 1)(e^t - 1)(a + \frac{1}{e^{s+t}})>0$

$\therefore a \ge 0$

综上, $a \in [1, +\infty)$

##### 第 (3) 问

当 $x \in \mathbb{N^*}$ 时, 

- $f(2) > f(1) + f(1) = 2 \cdot 2 > 2(2 - 1)$
- $\forall n \in \mathbb{N^*}$, 若 $f(n) > 2n > 2(n-1)$, 则 $f(n+1) > f(n) + f(1) = f(n) + 2 > 2(n + 1) > 2n$

$\therefore \forall x \in \mathbb{N^*}, f(x) > 2x > 2(x-1)$

当 $x > 1$ 且 $x \notin \mathbb{N^*}$ 时, 令 $n = \lfloor x \rfloor$, 则 $x-1 < n < x < n+1$,

$\therefore f(x) > f(n) > 2n > 2(x-1)$

综上, $\forall x \in (1, +\infty), f(x) > 2(x-1)$

## 选择题

| 题号 | 答案 |
|:--:|:--:|
| 12 | A  |
| 13 | 24 |
| 14 | C  |
| 15 | B  |
| 16 | D  |
