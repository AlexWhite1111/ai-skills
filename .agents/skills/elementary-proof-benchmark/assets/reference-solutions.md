# Public Development Reference Solutions

These solutions are public. The corresponding items are pipeline and rubric examples, not official hidden evaluation items.

<a id="EPB-DEV-001"></a>
## EPB-DEV-001：七个实数的矩与极差

设所有正数为

\[
p_1,\ldots,p_r>0,
\]

所有负数写成

\[
-q_1,\ldots,-q_s,\qquad q_j>0.
\]

零不参与下面的和。由 \(\sum x_i=0\)，正数之和与负数绝对值之和相等，记为

\[
A=\sum_{i=1}^r p_i=\sum_{j=1}^s q_j.
\]

由 \(\sum x_i^3=0\)，三次方之和也相等，记为

\[
B=\sum_{i=1}^r p_i^3=\sum_{j=1}^s q_j^3.
\]

再记

\[
U=\sum_{i=1}^r p_i^2,\qquad V=\sum_{j=1}^s q_j^2.
\]

若所有数均为零，结论显然。以下设 \(A,B>0\)。

七个数中正数和负数的总个数至多为七，因此至少一侧至多有三个数。不妨设 \(r\le3\)。

由柯西不等式，

\[
A^2\le rU
\]

以及

\[
U^2=\left(\sum p_i^2\right)^2
\le\left(\sum p_i\right)\left(\sum p_i^3\right)
=AB.
\]

所以

\[
A^4\le r^2U^2\le r^2AB,
\]

即

\[
A^3\le r^2B\le9B. \tag{1}
\]

对正负两侧分别再次使用柯西不等式，

\[
U\le\sqrt{AB},\qquad V\le\sqrt{AB}.
\]

于是

\[
U+V\le2\sqrt{AB}.
\]

由 (1)，

\[
\sqrt{AB}\le\frac{3B}{A},
\]

故

\[
U+V\le\frac{6B}{A}. \tag{2}
\]

设

\[
P=\max_i p_i,\qquad Q=\max_j q_j.
\]

原七个数的极差为

\[
R=P+Q.
\]

因为 \(p_i\le P\)，

\[
p_i^3\le P^2p_i.
\]

求和得

\[
B\le P^2A,
\qquad
P\ge\sqrt{\frac BA}.
\]

同理

\[
Q\ge\sqrt{\frac BA}.
\]

因此

\[
R=P+Q\ge2\sqrt{\frac BA},
\]

从而

\[
\frac32R^2\ge\frac{6B}{A}. \tag{3}
\]

结合 (2)、(3)：

\[
\sum_{i=1}^7x_i^2=U+V
\le\frac{6B}{A}
\le\frac32R^2.
\]

所以 \(C\le3/2\)。

取七个数为

\[
-t,-t,-t,0,t,t,t,
\]

则两项矩约束都成立，\(R=2t\)，平方和为 \(6t^2=\frac32R^2\)。因此

\[
C_{\min}=\frac32.
\]

### 等号

若 \(t>0\) 时等号成立，上述每一步都必须取等。

在 \(A^3\le r^2B\le9B\) 中取等迫使 \(r=3\)，并且正侧柯西取等，所以三个正数相等。负侧 \(V^2\le AB\) 取等迫使所有负数绝对值相等。又 \(B\le P^2A\) 与其负侧版本都取等。

设三个正数均为 \(p\)，负数共有 \(s\) 个且绝对值均为 \(q\)。由一阶和三阶矩平衡，

\[
3p=sq,\qquad3p^3=sq^3.
\]

相除得 \(p=q\)，继而 \(s=3\)。总共六个非零数，所以剩余一个数为零。

故等号当且仅当七个数是

\[
\{-t,-t,-t,0,t,t,t\}
\]

的一个排列，其中 \(t\ge0\)。

### 已知攻击点

一个常见但不完整的路线是用 KKT 声称极值分布只有三个取值。KKT 至多直接限制内部临界值的种类，不能跳过所有四值分布。以下四值例子确实满足两项矩约束：

\[
-1,\ u,\ u,\ v,\ v,\ 1,\ 1,
\]

其中

\[
u=-\frac{1+\sqrt5}{4},\qquad v=\frac{\sqrt5-1}{4}.
\]

它不是反例，但能击穿“所有可行极值候选自动三值化”的无证明断言。

---

<a id="EPB-CAL-001"></a>
## EPB-CAL-001：成对步长蚱蜢

令

\[
d_k=x_k-x_{k-1},\qquad x_0=x_{2m}=0.
\]

对每一步都有恒等式

\[
d_k^2+(x_k+x_{k-1})^2
=2x_k^2+2x_{k-1}^2.
\]

从 \(k=1\) 到 \(2m\) 求和，并利用首尾为零，得

\[
4\sum_{k=1}^{2m-1}x_k^2
=
\sum_{k=1}^{2m}d_k^2+
\sum_{k=1}^{2m}(x_k+x_{k-1})^2. \tag{4}
\]

位移集合为 \(\{\pm1,\ldots,\pm m\}\)，所以

\[
\sum d_k^2
=2\sum_{j=1}^m j^2
=\frac{m(m+1)(2m+1)}3. \tag{5}
\]

所有位置都是整数，且

\[
x_k+x_{k-1}=2x_{k-1}+d_k\equiv d_k\pmod2.
\]

当 \(d_k\) 为奇数时，\(x_k+x_{k-1}\) 是非零奇数，其平方至少为 \(1\)；当 \(d_k\) 为偶数时，其平方至少为 \(0\)。

奇位移的总数是

\[
2\left\lceil\frac m2\right\rceil
=
\begin{cases}
m,&m\text{ 为偶数},\\
m+1,&m\text{ 为奇数}.
\end{cases}
\]

由 (4)、(5) 得到下界

\[
\sum_{k=1}^{2m-1}x_k^2
\ge
\frac14\left[
\frac{m(m+1)(2m+1)}3+
\begin{cases}
m,&m\text{ 偶},\\
m+1,&m\text{ 奇}.
\end{cases}
\right]. \tag{6}
\]

构造位移序列：

\[
d_j=(-1)^{j-1}j\quad(1\le j\le m),
\]

并令

\[
d_{2m+1-j}=-d_j\quad(1\le j\le m).
\]

它恰好使用每个 \(\pm j\) 一次。前半段的位置满足

\[
x_{2r-1}=r,\qquad x_{2r}=-r
\]

（在指标有效时），因此偶位移对应 \(x_k+x_{k-1}=0\)，奇位移对应其绝对值为 \(1\)。由定义可直接得到，对 \(1\le j\le m\)，

\[
x_{2m-j}=x_j,\qquad x_{2m+1-j}=x_{j-1}.
\]

因此后半段与其配对的前半段具有相同的相邻位置和，只差位移符号；偶位移仍使相邻位置和为 \(0\)，奇位移仍使其绝对值为 \(1\)。所以 (6) 取等。

最小值即为 (6) 右端，也可写成

\[
\left\lceil
\frac{m(m+1)(2m+1)+3m}{12}
\right\rceil.
\]

---

<a id="EPB-CAL-002"></a>
## EPB-CAL-002：嵌套下标排列

令排列 \(\sigma\) 定义为

\[
\sigma(i)=a_i,
\]

再令翻转排列

\[
\tau(i)=n+1-i.
\]

原条件正是

\[
\sigma^2=\tau. \tag{7}
\]

### (1) 存在的 \(n\)

\(\tau\) 含有 \(\lfloor n/2\rfloor\) 个互不相交的二循环；当 \(n\) 为奇数时另有一个不动点。

若 \(\sigma\) 中一个循环长度为奇数，其平方仍是同长度循环；若长度为 \(2\ell\)，其平方分裂为两个长度为 \(\ell\) 的循环。由于 \(\tau=\sigma^2\) 只含二循环和至多一个不动点，\(\sigma\) 的循环长度只能是 \(1,2,4\)。二循环平方会产生两个不动点，而 \(\tau\) 至多只有一个不动点，所以二循环不可能出现。于是所有非平凡循环都必须是四循环；当 \(n\) 为奇数时，中间点必须是 \(\sigma\) 的唯一不动点。因此 \(\tau\) 的二循环数必须为偶数：

\[
\left\lfloor\frac n2\right\rfloor\equiv0\pmod2.
\]

这等价于

\[
n\equiv0\text{ 或 }1\pmod4.
\]

反过来，若二循环数为偶数，就把它们两两配对。对任意两对

\[
(a\,b),\qquad(c\,d),
\]

四循环

\[
(a\,c\,b\,d)
\]

的平方为 \((a\,b)(c\,d)\)。若有中间不动点，则保持它不动。故上述条件也充分。

### (2) 逆序对数

任取数值对 \(u<v\)，令

\[
i=\sigma^{-1}(u),\qquad j=\sigma^{-1}(v).
\]

由 (7)，

\[
\sigma(u)=\sigma^2(i)=n+1-i,
\]

\[
\sigma(v)=\sigma^2(j)=n+1-j.
\]

若 \(i<j\)，则 \(\sigma(u)>\sigma(v)\)，所以 \((u,v)\) 是 \(\sigma\) 的逆序，而不是 \(\sigma^{-1}\) 的逆序。若 \(i>j\)，情况正好相反。

因此每个 \(u<v\) 恰在 \(\sigma\) 与 \(\sigma^{-1}\) 中贡献一个逆序：

\[
\operatorname{inv}(\sigma)+\operatorname{inv}(\sigma^{-1})
=\binom n2.
\]

任意排列与其逆排列的逆序数相等，故

\[
\operatorname{inv}(\sigma)
=\frac12\binom n2
=\frac{n(n-1)}4.
\]

### (3) 排列总数

写 \(n=4k\) 或 \(n=4k+1\)。此时 \(\tau\) 有 \(2k\) 个二循环。

把这些二循环两两配对的方法数为

\[
\frac{(2k)!}{2^k k!}.
\]

每一对二循环有两个四循环平方根，所以再乘 \(2^k\)。若 \(n=4k+1\)，中间不动点的处理唯一。

故总数为

\[
\frac{(2k)!}{k!}.
\]
