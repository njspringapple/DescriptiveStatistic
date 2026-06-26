# Analysis 基础：偏导、分部积分、换元积分

练习题数：3

相关考试真题数：0

合计题目数：3

## 公式速查

### 常用数学：偏导、分部积分、换元积分

- **偏导**：$\frac{\partial}{\partial x}f(x,y)$ 是对 $x$ 求导、把 $y$ 当常数；$\frac{\partial}{\partial y}f(x,y)$ 同理。
- **乘积法则**：$(fg)'=f'g+fg'$。
- **商法则**：$\left(\frac fg\right)'=\frac{f'g-fg'}{g^2}$，分子是“上导下不导 - 上不导下导”。
- **链式法则**：$(f\circ g)'(x)=f'(g(x))g'(x)$，遇到 $e^{g(x)}$、$\log(g(x))$、三角复合函数时先找内层函数。
- **对数求导**：$\frac{d}{dx}\log x=\frac1x$，$\frac{d}{dx}\log(g(x))=\frac{g'(x)}{g(x)}$。
- **指数求导**：$\frac{d}{dx}e^{g(x)}=g'(x)e^{g(x)}$，$\frac{d}{dx}a^x=a^x\log a$。
- **三角函数求导**：$\frac{d}{dx}\sin x=\cos x$，$\frac{d}{dx}\cos x=-\sin x$。
- **幂函数积分**：$\int x^a\,dx=\frac{x^{a+1}}{a+1}+C,\ a\neq-1$；特殊情况 $\int\frac1x\,dx=\log|x|+C$。
- **分部积分**：$\int u\,dv=uv-\int v\,du$，选 $u$ 时优先选求导会变简单的因子。
- **换元积分**：$\int f(g(x))g'(x)\,dx=\int f(u)\,du$；定积分换元时上下限也要改成 $u=g(x)$ 的取值。
- **泰勒级数**：$e^x=\sum_{k=0}^{\infty}\frac{x^k}{k!}$，特别地 $e=\sum_{k=0}^{\infty}\frac1{k!}$。
- **等比数列**：$S_n=a_1\frac{1-q^n}{1-q}$；$|q|<1$ 时无穷和为 $\frac{a_1}{1-q}$。

---

## 习题与讲解

### Aufgabe 1 - 计算多元函数对各变量的偏导数。

#### 题目

Bilde jeweils die partielle Ableitung nach $x$ und nach $y$.

###### Aufgaben

$$
\begin{array}{ll}
\text{(a)}\quad g(x,y)=\dfrac{xy}{4+2y^2}
&
\text{(e)}\quad f(x,y)=\log(e^x)+e^{4y}
\\[0.8em]
\text{(b)}\quad f(x,y)=\log(xy)
&
\text{(f)}\quad m(x,y)=x^3\log(y)
\\[0.8em]
\text{(c)}\quad h(x,y)=a\sin(x)+\cos(y)
&
\text{(g)}\quad f(x,y)=e^{x^2-y}
\\[0.8em]
\text{(d)}\quad p(x,y)=x-\log(y^2+x)
&
\text{(h)}\quad h(x,y)=\log(y)+y\log(x)
\end{array}
$$

#### 解答

##### 中文解题思路

这道题先不要急着代公式，而是先识别每个小问属于偏导、分部积分还是换元积分。偏导题要把另一个变量当常数；分部积分题先选哪个因子求导会变简单、哪个因子容易积分；换元积分题要找出内层函数以及它的导数是否已经出现在被积式里。

偏导部分建议逐项写出原函数，再分别对 $x$ 和 $y$ 求导。遇到 $\log(xy)$ 可以先拆成 $\log x+\log y$，遇到商式用商法则，遇到 $e^{x^2-y}$ 用链式法则。

题目有多个小问时，建议每个小问都保留相同的解题格式：先列已知，再写公式，再代数化简。这样即使某一问算错，也不影响其它小问的结构分。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

###### (a)
g(x,y)=\frac{xy}{4+2y^2}
$$

$$
\frac{\partial g}{\partial x}
=\frac{y}{4+2y^2},
\qquad
\frac{\partial g}{\partial y}
=
\frac{x(4-2y^2)}{(4+2y^2)^2}.
$$

###### (b)
f(x,y)=\log(xy)
$$

$$
\frac{\partial f}{\partial x}=\frac1x,
\qquad
\frac{\partial f}{\partial y}=\frac1y.
$$

###### (c)
h(x,y)=a\sin(x)+\cos(y)
$$

$$
\frac{\partial h}{\partial x}=a\cos(x),
\qquad
\frac{\partial h}{\partial y}=-\sin(y).
$$

###### (d)
p(x,y)=x-\log(y^2+x)
$$

$$
\frac{\partial p}{\partial x}
=1-\frac1{y^2+x},
\qquad
\frac{\partial p}{\partial y}
=-\frac{2y}{y^2+x}.
$$

###### (e)
f(x,y)=\log(e^x)+e^{4y}=x+e^{4y}
$$

$$
\frac{\partial f}{\partial x}=1,
\qquad
\frac{\partial f}{\partial y}=4e^{4y}.
$$

###### (f)
m(x,y)=x^3\log(y)
$$

$$
\frac{\partial m}{\partial x}=3x^2\log(y),
\qquad
\frac{\partial m}{\partial y}=\frac{x^3}{y}.
$$

###### (g)
f(x,y)=e^{x^2-y}
$$

$$
\frac{\partial f}{\partial x}=2x e^{x^2-y},
\qquad
\frac{\partial f}{\partial y}=-e^{x^2-y}.
$$

###### (h)
h(x,y)=\log(y)+y\log(x)
$$

$$
\frac{\partial h}{\partial x}=\frac{y}{x},
\qquad
\frac{\partial h}{\partial y}=\frac1y+\log(x).
$$

---

---

### Aufgabe 2 - 用分部积分计算不定积分或定积分。

#### 题目

Bestimme die Stammfunktion oder das genaue Integral (falls Grenzen angegeben sind) der jeweiligen Funktion.

$$
\begin{array}{lll}
\text{(a)}\quad \displaystyle \int x\ln(x)\,dx
&
\text{(b)}\quad \displaystyle \int_0^{\pi/2} x\cos(x)\,dx
&
\text{(c)}\quad \displaystyle \int e^x\sin(x)\,dx
\end{array}
$$

Tipp für (c): Nutze zweimal partielle Integration. Nachdem du das zweite Mal partiell integriert hast, betrachte den Ausdruck vorsichtig.

#### 解答

##### 中文解题思路

这道题先不要急着代公式，而是先识别每个小问属于偏导、分部积分还是换元积分。偏导题要把另一个变量当常数；分部积分题先选哪个因子求导会变简单、哪个因子容易积分；换元积分题要找出内层函数以及它的导数是否已经出现在被积式里。

偏导部分建议逐项写出原函数，再分别对 $x$ 和 $y$ 求导。遇到 $\log(xy)$ 可以先拆成 $\log x+\log y$，遇到商式用商法则，遇到 $e^{x^2-y}$ 用链式法则。

积分部分要把每一步的换元或分部积分边界写清楚：定积分换元时上下限也要随 $u$ 改变，不定积分最后要换回原变量并加常数 $C$。

题目有多个小问时，建议每个小问都保留相同的解题格式：先列已知，再写公式，再代数化简。这样即使某一问算错，也不影响其它小问的结构分。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

###### (a)
\int x\ln(x)\,dx
=\frac{x^2}{2}\ln(x)-\frac{x^2}{4}+C.
$$

###### (b)
\int_0^{\pi/2}x\cos(x)\,dx
=
[x\sin(x)+\cos(x)]_0^{\pi/2}
=\frac{\pi}{2}-1.
$$

###### (c)
\int e^x\sin(x)\,dx
=
\frac{e^x}{2}\bigl(\sin(x)-\cos(x)\bigr)+C.
$$

---

---

### Aufgabe 3 - 用换元法计算不定积分或定积分。

#### 题目

Bestimme die Integrale.

$$
\begin{array}{lll}
\text{(a)}\quad \displaystyle \int_0^3 3x^2 e^{x^3}\,dx
&
\text{(b)}\quad \displaystyle \int x\sqrt{1+x^2}\,dx
&
\text{(c)}\quad \displaystyle \int \frac{\ln(x)}{x}\,dx
\end{array}
$$

Tipp für (b): Setze $u=1+x^2$.

#### 解答

##### 中文解题思路

这道题先不要急着代公式，而是先识别每个小问属于偏导、分部积分还是换元积分。偏导题要把另一个变量当常数；分部积分题先选哪个因子求导会变简单、哪个因子容易积分；换元积分题要找出内层函数以及它的导数是否已经出现在被积式里。

积分部分要把每一步的换元或分部积分边界写清楚：定积分换元时上下限也要随 $u$ 改变，不定积分最后要换回原变量并加常数 $C$。

题目有多个小问时，建议每个小问都保留相同的解题格式：先列已知，再写公式，再代数化简。这样即使某一问算错，也不影响其它小问的结构分。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

###### (a)
\int_0^3 3x^2e^{x^3}\,dx.
$$

Setze $u=x^3$, dann $du=3x^2\,dx$:

$$
\int_0^3 3x^2e^{x^3}\,dx
=
\int_0^{27}e^u\,du
=e^{27}-1.
$$

###### (b)
\int x\sqrt{1+x^2}\,dx.
$$

Setze $u=1+x^2$, dann $du=2x\,dx$:

$$
\int x\sqrt{1+x^2}\,dx
=
\frac12\int u^{1/2}\,du
=
\frac13(1+x^2)^{3/2}+C.
$$

###### (c)
\int\frac{\ln(x)}{x}\,dx.
$$

Setze $u=\ln(x)$, dann $du=\frac1x\,dx$:

$$
\int\frac{\ln(x)}{x}\,dx
=
\int u\,du
=
\frac12(\ln x)^2+C.
$$

---

---
