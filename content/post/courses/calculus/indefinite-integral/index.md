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

> [!IMPORTANT]
> 可能用到的一些超出高中数学的公式:
>
> 1. $\cot x = \cfrac{1}{\tan x}$
> 2. $\sec x = \cfrac{1}{\cos x}$
> 3. $\csc x = \cfrac{1}{\sin x}$
> 4. $\sec^2 x - \tan^2 x = 1$
> 5. $\csc^2 x - \cot^2 x = 1$
> 6. $\frac{\mathrm{d}}{\mathrm{d}x} \tan x = \sec^2 x$
> 7. $\frac{\mathrm{d}}{\mathrm{d}x} \cot x = - \csc^2 x$
> 8. $\frac{\mathrm{d}}{\mathrm{d}x} \sec x = \sec x \tan x$
> 9. $\frac{\mathrm{d}}{\mathrm{d}x} \csc x = - \csc x \cot x$

## 凑微分法

### 例题

> 求不定积分: $$\int x \sin x^2 \mathrm{d}x $$

**【解】:** 把 $x$ 凑到 $\mathrm{d}$ 后面去

$$
\begin{aligned}
I &= \cfrac{1}{2} \int \sin x^2 \mathrm{d}(x^2) \\
  &= - \cfrac{1}{2} \cos x^2 + C
\end{aligned}
$$

### 练习

求解下列不定积分:

1. $ \displaystyle \int x e^{x^2} \mathrm{d}x $
2. $ \displaystyle \int \cfrac{\ln x}{x} \mathrm{d}x $
3. $ \displaystyle \int \sin^3 x \cos x \mathrm{d}x $
4. $ \displaystyle \int \cfrac{1}{\sqrt{1-x^2}} \cdot \cfrac{1}{\sqrt{1-(\arcsin x)^2}} \mathrm{d}x $
5. $ \displaystyle \int \cfrac{x}{(1+x^2)^2} \mathrm{d}x $
6. $ \displaystyle \int \cfrac{1}{x \ln x (\ln(\ln x))^2} \mathrm{d}x $
7. $ \displaystyle \int \cfrac{e^x (1 + \sin x)}{1 + \cos x} \mathrm{d}x $
8. $ \displaystyle \int \cfrac{1}{\sin^2 x \cos^2 x} \mathrm{d}x $
9. $ \displaystyle \int \cfrac{\sin x \cos x}{\sqrt{1 + \sin^4 x}} \mathrm{d}x $
10. $ \displaystyle \int \tan^4 x \mathrm{d}x $
11. $ \displaystyle \int \cfrac{x e^x}{(1+x)^2} \mathrm{d}x $
12. $ \displaystyle \int \cfrac{1 - \ln x}{(x - \ln x)^2} \mathrm{d}x $

## 代入换元法

### 例题

> 求不定积分: $$\int \sqrt{1 - x^2} \mathrm{d}x $$

**【解】:** 看到 $\sqrt{1 - x^2}$, 考虑三角换元 $x = \sin t$,
则 $\mathrm{d}x = \cos t \mathrm{d}t$, 故

$$
\begin{aligned}
I &= \int \sqrt{1 - \sin^2 t} \cos t \mathrm{d}t \\
  &= \int \cos^2 t \mathrm{d}t \\
  & = \cfrac{1}{2} \int (1 + \cos 2t) \mathrm{d}t \\
  &= \cfrac{1}{2} t + \cfrac{1}{4} \sin 2t + C
\end{aligned}
$$

### 练习

1. $ \displaystyle \int \sqrt{4 - x^2} dx $
2. $ \displaystyle \int \frac{1}{x^2 \sqrt{x^2 + 1}} dx $
3. $ \displaystyle \int \frac{1}{\sqrt{x} + \sqrt[3]{x}} dx $

## 综合练习

1. $ \displaystyle \int \frac{\mathrm{d}x}{1+e^{x}} $
2. $ \displaystyle \int \frac{\mathrm{d}x}{x\left(x^{6}+4\right)} $
3. $ \displaystyle \int \frac{\mathrm{d}x}{\sqrt{x(1-x)}} $
4. $ \displaystyle \int \frac{\mathrm{d}x}{x \sqrt{x^{2}-1}} $
5. $ \displaystyle \int \frac{\mathrm{d}x}{x \sqrt{4-x^{2}}} $
6. $ \displaystyle \int \sqrt{\frac{A+x}{A-x}} \mathrm{d}x $
7. $ \displaystyle \int \sqrt{\frac{x-A}{B-x}} \mathrm{d}x $
    - *注: $A<B$*
8. $ \displaystyle \int \frac{\mathrm{d}x}{1+x^{3}} $
