### 题目

已知 $F_1, F_2$ 是双曲线 $C: \frac{x^2}{4} - \frac{y^2}{6} = 1$ 的左右焦点，$A, B \in C$，且满足 $\vec{AF_2} = \lambda \vec{F_2 B} (\lambda > 0)$。若 $\cos \angle A F_1 B = \frac{3}{5}$，求 $\triangle ABF_1$ 的内切圆半径。

---

### 解析与答案

#### 1. 基础参数分析
双曲线方程为 $\frac{x^2}{4} - \frac{y^2}{6} = 1$，可得：
- $a^2 = 4 \implies a = 2$
- $b^2 = 6$
- $c^2 = a^2 + b^2 = 10 \implies c = \sqrt{10}$
- 焦距 $|F_1 F_2| = 2c = 2\sqrt{10}$

由 $\vec{AF_2} = \lambda \vec{F_2 B} (\lambda > 0)$ 可知，$A, F_2, B$ 三点共线，且 $F_2$ 位于线段 $AB$ 之间。即 $AB$ 是过右焦点 $F_2$ 的一条弦。

#### 2. 边长关系推导
设 $|AF_1| = m$，$|BF_1| = n$。
根据双曲线定义，对于右支上的点 $P$，有 $|PF_1| - |PF_2| = 2a = 4$。
假设 $A, B$ 均在双曲线右支（注：若分居左右支，几何结构不同，但通常此类定值问题结论一致，此处按常规右支弦处理）：
- $|AF_2| = |AF_1| - 2a = m - 4$
- $|BF_2| = |BF_1| - 2a = n - 4$
- $\triangle ABF_1$ 的边 $AB$ 长度为：$|AB| = |AF_2| + |BF_2| = (m - 4) + (n - 4) = m + n - 8$

#### 3. 利用余弦定理建立方程
在 $\triangle ABF_1$ 中，已知 $\cos \angle AF_1B = \frac{3}{5}$，则 $\sin \angle AF_1B = \sqrt{1 - (\frac{3}{5})^2} = \frac{4}{5}$。

由余弦定理：
$$ |AB|^2 = |AF_1|^2 + |BF_1|^2 - 2|AF_1||BF_1| \cos \angle AF_1B $$
代入边长表达式：
$$ (m + n - 8)^2 = m^2 + n^2 - 2mn \cdot \frac{3}{5} $$

展开左边：
$$ (m+n)^2 - 16(m+n) + 64 = m^2 + n^2 - \frac{6}{5}mn $$
$$ m^2 + 2mn + n^2 - 16(m+n) + 64 = m^2 + n^2 - \frac{6}{5}mn $$

消去 $m^2, n^2$ 并整理：
$$ 2mn + \frac{6}{5}mn = 16(m+n) - 64 $$
$$ \frac{16}{5}mn = 16(m+n) - 64 $$
两边同除以 16：
$$ \frac{1}{5}mn = (m+n) - 4 $$
$$ mn = 5(m+n) - 20 $$

#### 4. 计算内切圆半径
设 $\triangle ABF_1$ 的内切圆半径为 $r$，面积为 $S$，半周长为 $s$。

**计算半周长 $s$：**
$$ s = \frac{|AF_1| + |BF_1| + |AB|}{2} = \frac{m + n + (m + n - 8)}{2} = \frac{2(m+n) - 8}{2} = m + n - 4 $$

**计算面积 $S$：**
$$ S = \frac{1}{2} |AF_1| |BF_1| \sin \angle AF_1B = \frac{1}{2} mn \cdot \frac{4}{5} = \frac{2}{5} mn $$

**计算半径 $r$：**
$$ r = \frac{S}{s} = \frac{\frac{2}{5} mn}{m + n - 4} $$

将步骤 3 中得到的 $mn = 5(m+n) - 20 = 5(m+n-4)$ 代入上式：
$$ r = \frac{\frac{2}{5} \cdot 5(m+n-4)}{m+n-4} $$
$$ r = \frac{2(m+n-4)}{m+n-4} $$
$$ r = 2 $$

### 最终答案
$\triangle ABF_1$ 的内切圆半径为 **2**。
