---
title: "不定积分专项练习答案"
description:
date: 2026-04-11T17:44:25+08:00
image: 
math: true
license: 
draft: false
categories:
    - Courses
tags:
    - 不定积分
    - 答案
---

<!--markdownlint-disable MD029-->
<!--markdownlint-disable MD032-->

## 凑微分法

1. **【解】:** 把 $x$ 凑到 $\mathrm{d}$ 后面去
$$
\begin{aligned}
I &= \frac{1}{2} \int e^{x^2} \mathrm{d}(x^2) \\
  &= \frac{1}{2} e^{x^2} + C
\end{aligned}
$$

2. **【解】:** 把 $\frac{1}{x}$ 凑到 $\mathrm{d}$ 后面去
$$
\begin{aligned}
I &= \int \ln x \, \mathrm{d}(\ln x) \\
  &= \frac{1}{2} (\ln x)^2 + C
\end{aligned}
$$

3. **【解】:** 把 $\cos x$ 凑到 $\mathrm{d}$ 后面去
$$
\begin{aligned}
I &= \int \sin^3 x \, \mathrm{d}(\sin x) \\
  &= \frac{1}{4} \sin^4 x + C
\end{aligned}
$$

4. **【解】:** 把 $\frac{1}{\sqrt{1-x^2}}$ 凑到 $\mathrm{d}$ 后面
$$
\begin{aligned}
I &= \int \frac{1}{\sqrt{1-(\arcsin x)^2}} \mathrm{d}(\arcsin x) \\
  &= \arcsin(\arcsin x) + C
\end{aligned}
$$

5. **【解】:** 把 $x$ 凑到 $\mathrm{d}$ 后面去
$$
\begin{aligned}
I &= \frac{1}{2} \int (1+x^2)^{-2} \mathrm{d}(1+x^2) \\
  &= -\frac{1}{2(1+x^2)} + C
\end{aligned}
$$

6. **【解】:** 逐层凑微分
$$
\begin{aligned}
I &= \int \frac{1}{(\ln(\ln x))^2} \mathrm{d}(\ln(\ln x)) \\
  &= -\frac{1}{\ln(\ln x)} + C
\end{aligned}
$$

7. **【解】:** 拆分为 $e^x[f(x)+f'(x)]$ 形式, 取 $f(x)=\frac{\sin x}{1+\cos x}$, 则 $f'(x)=\frac{1}{1+\cos x}$
$$
\begin{aligned}
I &= \int e^x \left[ \frac{\sin x}{1+\cos x} + \left(\frac{\sin x}{1+\cos x}\right)' \right] \mathrm{d}x \\
  &= e^x \frac{\sin x}{1+\cos x} + C \\
  &= e^x \tan\frac{x}{2} + C
\end{aligned}
$$

8. **【解】:** 利用 $1=\sin^2 x+\cos^2 x$ 拆分分子
$$
\begin{aligned}
I &= \int \frac{\sin^2 x + \cos^2 x}{\sin^2 x \cos^2 x} \mathrm{d}x \\
  &= \int \left( \frac{1}{\cos^2 x} + \frac{1}{\sin^2 x} \right) \mathrm{d}x \\
  &= \tan x - \cot x + C
\end{aligned}
$$

9. **【解】:** 把 $\sin x \cos x$ 凑到 $\mathrm{d}$ 后面去, $\sin x \cos x \mathrm{d}x = \frac{1}{2}\mathrm{d}(\sin^2 x)$
$$
\begin{aligned}
I &= \frac{1}{2} \int \frac{\mathrm{d}(\sin^2 x)}{\sqrt{1+(\sin^2 x)^2}} \\
  &= \frac{1}{2} \ln\left( \sin^2 x + \sqrt{1+\sin^4 x} \right) + C
\end{aligned}
$$

10. **【解】:** 利用 $\tan^2 x = \sec^2 x - 1$ 降幂
$$
\begin{aligned}
I &= \int \tan^2 x (\sec^2 x - 1) \mathrm{d}x \\
  &= \int \tan^2 x \mathrm{d}(\tan x) - \int (\sec^2 x - 1) \mathrm{d}x \\
  &= \frac{1}{3} \tan^3 x - \tan x + x + C
\end{aligned}
$$

11. **【解】:** 观察为 $e^x[f(x)+f'(x)]$ 形式, 取 $f(x)=\frac{1}{1+x}$, 则 $f'(x)=-\frac{1}{(1+x)^2}$
$$
\begin{aligned}
I &= \int e^x \left[ \frac{1}{1+x} - \frac{1}{(1+x)^2} \right] \mathrm{d}x \\
  &= \frac{e^x}{1+x} + C
\end{aligned}
$$

12. **【解】:** 观察被积函数恰为 $\left(\frac{x}{x-\ln x}\right)'$
$$
\begin{aligned}
I &= \frac{x}{x - \ln x} + C
\end{aligned}
$$

## 代入换元法

1. **【解】:** 令 $x = 2\sin t$, 则 $\mathrm{d}x = 2\cos t \mathrm{d}t$, $\sqrt{4-x^2}=2\cos t$
$$
\begin{aligned}
I &= \int 4\cos^2 t \mathrm{d}t = 2\int (1+\cos 2t)\mathrm{d}t \\
  &= 2t + \sin 2t + C = 2t + 2\sin t\cos t + C \\
  &= 2\arcsin\frac{x}{2} + \frac{x}{2}\sqrt{4-x^2} + C
\end{aligned}
$$

2. **【解】:** 令 $x = \tan t$, 则 $\mathrm{d}x = \sec^2 t \mathrm{d}t$, $\sqrt{x^2+1}=\sec t$
$$
\begin{aligned}
I &= \int \frac{\sec^2 t}{\tan^2 t \sec t} \mathrm{d}t = \int \frac{\cos t}{\sin^2 t} \mathrm{d}t \\
  &= \int (\sin t)^{-2} \mathrm{d}(\sin t) = -\frac{1}{\sin t} + C \\
  &= -\frac{\sqrt{x^2+1}}{x} + C
\end{aligned}
$$

3. **【解】:** 令 $x = t^6$ 去根号, 则 $\mathrm{d}x = 6t^5 \mathrm{d}t$
$$
\begin{aligned}
I &= \int \frac{6t^5}{t^3+t^2} \mathrm{d}t = 6\int \frac{t^3}{t+1} \mathrm{d}t = 6\int \left(t^2-t+1-\frac{1}{t+1}\right)\mathrm{d}t \\
  &= 6\left(\frac{t^3}{3}-\frac{t^2}{2}+t-\ln|t+1|\right)+C \\
  &= 2\sqrt{x} - 3\sqrt[3]{x} + 6\sqrt[6]{x} - 6\ln|\sqrt[6]{x}+1| + C
\end{aligned}
$$

## 综合练习

1. **【解】:** 分子凑 $1+e^x-e^x$ 拆分
$$
\begin{aligned}
I &= \int \left(1 - \frac{e^x}{1+e^x}\right)\mathrm{d}x \\
  &= x - \ln(1+e^x) + C
\end{aligned}
$$

2. **【解】:** 分子分母同乘 $x^5$, 令 $u=x^6$, $\mathrm{d}u=6x^5\mathrm{d}x$
$$
\begin{aligned}
I &= \frac{1}{6}\int \frac{\mathrm{d}u}{u(u+4)} = \frac{1}{24}\int \left(\frac{1}{u}-\frac{1}{u+4}\right)\mathrm{d}u \\
  &= \frac{1}{24}\ln\left|\frac{x^6}{x^6+4}\right| + C
\end{aligned}
$$

3. **【解】:** 配方 $x(1-x) = \frac{1}{4} - \left(x-\frac{1}{2}\right)^2$
$$
\begin{aligned}
I &= \int \frac{\mathrm{d}(x-\frac{1}{2})}{\sqrt{(\frac{1}{2})^2-(x-\frac{1}{2})^2}} \\
  &= \arcsin(2x-1) + C
\end{aligned}
$$

4. **【解】:** 令 $x = \sec t$, $\mathrm{d}x = \sec t \tan t \mathrm{d}t$
$$
\begin{aligned}
I &= \int \frac{\sec t \tan t}{\sec t \tan t} \mathrm{d}t = t + C \\
  &= \arccos\frac{1}{x} + C
\end{aligned}
$$

5. **【解】:** 令 $x = 2\sin t$, $\mathrm{d}x = 2\cos t \mathrm{d}t$
$$
\begin{aligned}
I &= \frac{1}{2}\int \csc t \mathrm{d}t = \frac{1}{2}\ln|\csc t - \cot t| + C \\
  &= \frac{1}{2}\ln\left|\frac{2-\sqrt{4-x^2}}{x}\right| + C
\end{aligned}
$$

6. **【解】:** 分子有理化 $\frac{A+x}{\sqrt{A^2-x^2}} = \frac{A}{\sqrt{A^2-x^2}} + \frac{x}{\sqrt{A^2-x^2}}$
$$
\begin{aligned}
I &= A\int \frac{\mathrm{d}x}{\sqrt{A^2-x^2}} + \int \frac{x}{\sqrt{A^2-x^2}} \mathrm{d}x \\
  &= A\arcsin\frac{x}{A} - \sqrt{A^2-x^2} + C
\end{aligned}
$$

7. **【解】:** 令 $t = \sqrt{\frac{x-A}{B-x}}$, 则 $x = \frac{A+Bt^2}{1+t^2}$, $\mathrm{d}x = \frac{2(B-A)t}{(1+t^2)^2}\mathrm{d}t$
$$
\begin{aligned}
I &= 2(B-A)\int \frac{t^2}{(1+t^2)^2}\mathrm{d}t \\
  &= (B-A)\left(\arctan t - \frac{t}{1+t^2}\right) + C \\
  &= (B-A)\arctan\sqrt{\frac{x-A}{B-x}} - \sqrt{(x-A)(B-x)} + C
\end{aligned}
$$

8. **【解】:** 部分分式分解 $\frac{1}{1+x^3} = \frac{1}{3(1+x)} + \frac{2-x}{3(1-x+x^2)}$
$$
\begin{aligned}
I &= \frac{1}{3}\int \frac{\mathrm{d}x}{1+x} + \frac{1}{3}\int \frac{2-x}{x^2-x+1}\mathrm{d}x \\
  &= \frac{1}{3}\ln|1+x| - \frac{1}{6}\ln(x^2-x+1) + \frac{1}{\sqrt{3}}\arctan\frac{2x-1}{\sqrt{3}} + C
\end{aligned}
$$
