---
title: "利用正交系投影区分原子点与连续点" 
description: 通过归一正交系在 δ_t 上的投影，研究 Λ(t) 随正交系阶数 N 的渐近行为，从而区分原子点与连续点。 
author: 陈君逸
date: 2026-10-17
image: 
math: true 
license: All Right Reserved, 河源中学数学研究协会
draft: false 
categories:
    - Articles
tags:
    - 泛函分析
    - 正交系
---


Part 1

设 $r(t)$ 为点 $t$ 附近一个以 $\frac{r}{2}$ 为半径的邻域，$r \to 0$。

设 $\mu(r(t)) = r w(t)$。令 $\delta_t(x)$ 满足

$$ \int_D \delta_t(x) f(x), d\mu = f(t)  r w(t). $$

则

$$ |\delta_t|^2 = \int_D \delta_t^2(x) d\mu = r w(t), $$

从而

$$ \sum |\delta_t|^2 \to \mu(D), $$

其中 $\sum$ 类似于对 $t$ 的积分。

设 ${\varphi_i}$ 为归一正交系，则 $\delta_t$ 被 $\varphi_i$ 表示，于是

$$ |\delta_t|^2 = \sum_{i=1}^{n} \alpha_i^2, $$

其中 $\alpha_i$ 为 $\delta_t$ 在 $\varphi_i$ 上的投影：

$$ \alpha_i = \int_D \delta_t(x) \varphi_i(x), d\mu = r w(t) \varphi_i(t). $$

代入得

$$ \sum \left[ \left( \sum_{i=1}^{n} \varphi_i^2(t) \right) r^2 w^2(t) \right] \to \mu(D). $$

设

$$ \Lambda(t) = \frac{1}{\sum_{i=1}^{n} \varphi_i^2(t)}, $$

则

$$ \mu(D) \Lambda(t) \to \sum w^2(t) r^2 = \sum \mu^2(r(t)). $$

假定求和共有 $N$ 项，则由柯西不等式，

$$ \mu(D) \Lambda(t) \to \sum \mu^2(r(t)) \ge \frac{1}{N} \left( \sum \mu(r(t)) \right)^2 = \frac{\mu^2(D)}{N}. $$

因此

$$ N \cdot \Lambda(t) = O(1), $$

即

$$ \Lambda(t) = O\left( \frac{1}{N} \right). $$

Part 2

设 $\mu( \\{ t \\} ) > 0$，令 $\delta_t$ 满足

$$ \int_D \delta_t(x) f(x), d\mu = f(t) \mu( \\{ t \\} ). $$

则

$$ |\delta_t|^2 = \int_D \delta_t^2(x), d\mu = \mu( \\{ t \\ }
设 ${\varphi_i}$ 为一正交集，$\delta_t$ 被 $\varphi_i$ 表示，则

$$ |\delta_t|^2 = \sum_{i=1}^{n} \alpha_i^2, \qquad \alpha_i = \int_D \delta_t(x) \varphi_i(x), d\mu = \varphi_i(t) \mu( \\{ t \\} ). $$

于是

$$ \mu( \\{ t \\} ) = \mu^2( \\{ t \\} ) \sum_{i=1}^{n} \varphi_i^2(t). $$

设 $\Lambda(t) = \dfrac{1}{\sum_{i=1}^{n} \varphi_i^2(t)}$，则

$$ \Lambda(t) = \mu( \\{ t \\} ). $$

结论： 因此，只需观察 $\Lambda(t)$ 随 $N$ 变化的趋势，便能区分原子点与连续点。
