---
title: "不定积分专项练习"
description: 凑微分法和代入换元法
date: 2026-04-11T12:18:58+08:00
image: 
math: true
license: 
comments: true
draft: false
build:
    list: always    # Change to "never" to hide the page from the list
categories:
    - Courses
tags:
    - 不定积分
---

## 凑微分法

### 例题

> $\int x \sin x^2 \mathrm{d}x $

**【解】:** 把 $x$ 凑到 $\mathrm{d}$ 后面去

$$
\begin{aligned}
I &= \cfrac{1}{2} \int \sin x^2 \mathrm{d}(x^2) \\
  &= - \cfrac{1}{2} \cos x^2 + C
\end{aligned}
$$

### 练习

1. $ \int x e^{x^2} \mathrm{d}x $
2. $ \int \cfrac{\ln x}{x} \mathrm{d}x $
3. $ \int \sin^3 x \cos x \mathrm{d}x $
4. $ \int \cfrac{1}{\sqrt{1-x^2}} \cdot \cfrac{1}{\sqrt{1-(\arcsin x)^2}} \mathrm{d}x $
5. $ \int \cfrac{x}{(1+x^2)^2} \mathrm{d}x $
6. $ \int \cfrac{1}{x \ln x (\ln(\ln x))^2} \mathrm{d}x $
7. $ \int \cfrac{e^x (1 + \sin x)}{1 + \cos x} \mathrm{d}x $
8. $ \int \cfrac{1}{\sin^2 x \cos^2 x} \mathrm{d}x $
9. $ \int \cfrac{\sin x \cos x}{\sqrt{1 + \sin^4 x}} \mathrm{d}x $
10. $ \int \tan^4 x \mathrm{d}x $
    - *提示: 利用 $\tan^2 x = \sec^2 x - 1$ 降幂拆分*
11. $ \int \cfrac{x e^x}{(1+x)^2} \mathrm{d}x $
12. $ \int \cfrac{1 - \ln x}{(x - \ln x)^2} \mathrm{d}x $
