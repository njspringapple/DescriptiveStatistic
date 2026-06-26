# Analysis 基础：偏导、分部积分、换元积分

练习题数：3

相关考试真题数：0

合计题目数：3

## 公式速查

### 考试可用版

- **偏导**：$\partial_x f(x,y)$ 对 $x$ 求导，把 $y$ 当常数；$\partial_y f(x,y)$ 反过来。
- **乘积法则**：$(fg)'=f'g+fg'$
- **商法则**：$\left(\frac fg\right)'=\frac{f'g-fg'}{g^2}$
- **链式法则**：$(f\circ g)'(x)=f'(g(x))g'(x)$
- **对数**：$(\log x)'=\frac1x$，$(\log g(x))'=\frac{g'(x)}{g(x)}$
- **指数**：$(e^{g(x)})'=g'(x)e^{g(x)}$，$(a^x)'=a^x\log a$
- **三角**：$(\sin x)'=\cos x$，$(\cos x)'=-\sin x$
- **幂函数积分**：$\int x^a dx=\frac{x^{a+1}}{a+1}+C,\ a\ne-1$
- **倒数积分**：$\int\frac1x dx=\log|x|+C$
- **分部积分**：$\int u\,dv=uv-\int v\,du$
- **换元积分**：令 $u=g(x)$，$du=g'(x)dx$

### 不会时怎么下手

- **题目问偏导**：先圈出“对谁求导”。对 $x$ 求导时，所有 $y$、$a$、常数都当常数。
- **看到乘积**：先判断是不是两个因子相乘。对 $x$ 求 $x^3\log y$ 时，$\log y$ 是常数。
- **看到分式**：分母与求导变量无关就当常数；有关就用商法则。
- **看到 $\log(\cdot)$**：先找括号里的内层函数，再写 $\frac{\text{内层导数}}{\text{内层}}$。
- **看到 $e^{(\cdot)}$**：原样保留 $e^{(\cdot)}$，再乘内层导数。
- **题目问分部积分**：优先选求导会变简单的因子当 $u$，例如 $\log x$ 或 $x$。
- **题目问换元积分**：先找内层函数 $u$，再检查 $du$ 是否已经出现；定积分要换上下限。

---

## 习题与讲解

### Aufgabe 1 - 计算多元函数对各变量的偏导数。

#### 题目

Bilde jeweils die partielle Ableitung nach $x$ und nach $y$.

译：分别求关于 $x$ 和关于 $y$ 的偏导数。

###### Aufgaben

译：题目

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

$$
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

$$
f(x,y)=\log(xy)
$$

$$
\frac{\partial f}{\partial x}=\frac1x,
\qquad
\frac{\partial f}{\partial y}=\frac1y.
$$

###### (c)

$$
h(x,y)=a\sin(x)+\cos(y)
$$

$$
\frac{\partial h}{\partial x}=a\cos(x),
\qquad
\frac{\partial h}{\partial y}=-\sin(y).
$$

###### (d)

$$
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

$$
f(x,y)=\log(e^x)+e^{4y}=x+e^{4y}
$$

$$
\frac{\partial f}{\partial x}=1,
\qquad
\frac{\partial f}{\partial y}=4e^{4y}.
$$

###### (f)

$$
m(x,y)=x^3\log(y)
$$

$$
\frac{\partial m}{\partial x}=3x^2\log(y),
\qquad
\frac{\partial m}{\partial y}=\frac{x^3}{y}.
$$

###### (g)

$$
f(x,y)=e^{x^2-y}
$$

$$
\frac{\partial f}{\partial x}=2x e^{x^2-y},
\qquad
\frac{\partial f}{\partial y}=-e^{x^2-y}.
$$

###### (h)

$$
h(x,y)=\log(y)+y\log(x)
$$

$$
\frac{\partial h}{\partial x}=\frac{y}{x},
\qquad
\frac{\partial h}{\partial y}=\frac1y+\log(x).
$$

---

### Aufgabe 2 - 用分部积分计算不定积分或定积分。

#### 题目

Bestimme die Stammfunktion oder das genaue Integral (falls Grenzen angegeben sind) der jeweiligen Funktion.

译：求对应函数的原函数；如果给出了积分上下限，则求定积分的精确值。

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

译：提示 (c)：使用两次分部积分。第二次分部积分后，要仔细整理得到的表达式。

#### 解答

##### 中文解题思路

这道题先不要急着代公式，而是先识别每个小问属于偏导、分部积分还是换元积分。偏导题要把另一个变量当常数；分部积分题先选哪个因子求导会变简单、哪个因子容易积分；换元积分题要找出内层函数以及它的导数是否已经出现在被积式里。

偏导部分建议逐项写出原函数，再分别对 $x$ 和 $y$ 求导。遇到 $\log(xy)$ 可以先拆成 $\log x+\log y$，遇到商式用商法则，遇到 $e^{x^2-y}$ 用链式法则。

积分部分要把每一步的换元或分部积分边界写清楚：定积分换元时上下限也要随 $u$ 改变，不定积分最后要换回原变量并加常数 $C$。

题目有多个小问时，建议每个小问都保留相同的解题格式：先列已知，再写公式，再代数化简。这样即使某一问算错，也不影响其它小问的结构分。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

###### (a)

$$
\int x\ln(x)\,dx
=\frac{x^2}{2}\ln(x)-\frac{x^2}{4}+C.
$$

###### (b)

$$
\int_0^{\pi/2}x\cos(x)\,dx
=
[x\sin(x)+\cos(x)]_0^{\pi/2}
=\frac{\pi}{2}-1.
$$

###### (c)

$$
\int e^x\sin(x)\,dx
=
\frac{e^x}{2}\bigl(\sin(x)-\cos(x)\bigr)+C.
$$

---

### Aufgabe 3 - 用换元法计算不定积分或定积分。

#### 题目

Bestimme die Integrale.

译：求下列积分。

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

译：提示 (b)：令 $u=1+x^2$。

#### 解答

##### 中文解题思路

这道题先不要急着代公式，而是先识别每个小问属于偏导、分部积分还是换元积分。偏导题要把另一个变量当常数；分部积分题先选哪个因子求导会变简单、哪个因子容易积分；换元积分题要找出内层函数以及它的导数是否已经出现在被积式里。

积分部分要把每一步的换元或分部积分边界写清楚：定积分换元时上下限也要随 $u$ 改变，不定积分最后要换回原变量并加常数 $C$。

题目有多个小问时，建议每个小问都保留相同的解题格式：先列已知，再写公式，再代数化简。这样即使某一问算错，也不影响其它小问的结构分。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

###### (a)

$$
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

$$
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

$$
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

## 常见错误提醒

- **偏导时把另一个变量也求导了**：对 $x$ 求偏导时，$y$ 是常数。
  例：$\partial_x(y\log x)=y/x$，不是 $1/x$。
- **商法则分子顺序写反**：分子是 $f'g-fg'$。
  例：$\left(\frac{x}{1+y^2}\right)_y=\frac{0\cdot(1+y^2)-x\cdot2y}{(1+y^2)^2}$。
- **链式法则漏乘内层导数**：外层求完必须乘内层导数。
  例：$\frac d{dx}e^{x^2}=2xe^{x^2}$。
- **分部积分选错 $u$**：$u$ 应该越求导越简单。
  例：$\int x\log x\,dx$ 选 $u=\log x$，$dv=x\,dx$。
- **定积分换元忘改上下限**：换元后上下限也必须变。
  例：$u=x^3$ 时，$x=0\to u=0$，$x=3\to u=27$。

## 本章必会题型清单

- 会对多元函数分别求 $\partial_x$ 和 $\partial_y$。
- 会使用乘积法则、商法则、链式法则。
- 会处理 $\log(\cdot)$、$e^{(\cdot)}$、$\sin$、$\cos$ 的求导。
- 会用分部积分计算含 $x\log x$、$x\cos x$、$e^x\sin x$ 的积分。
- 会用换元法计算定积分和不定积分，并正确处理上下限。

---
