# 收敛、近似、LLN 与 CLT

练习题数：20

相关考试真题数：8

合计题目数：28

## 公式速查

### 独立性、收敛性、大数定律与中心极限定理

- **随机独立性**：$A\perp B\Longleftrightarrow P(A\cap B)=P(A)P(B)\Longleftrightarrow P(A|B)=P(A)$。
- **条件独立性**：$(A\perp B)|C\Longleftrightarrow P(A\cap B|C)=P(A|C)P(B|C)$。
- **概率收敛**：$X_n\xrightarrow{P}X$，若对任意 $\varepsilon>0$，$\lim_{n\to\infty}P(|X_n-X|>\varepsilon)=0$。
- **分布收敛**：$X_n\xrightarrow{D}X$，若 $F_{X_n}(x)\to F_X(x)$ 对所有 $F_X$ 的连续点成立。
- **均方收敛**：$E[(X_n-X)^2]\to0$；**几乎必然收敛**：$P(\lim_{n\to\infty}X_n=X)=1$。
- **收敛强度**：几乎必然收敛 $\Rightarrow$ 均方收敛 $\Rightarrow$ 概率收敛 $\Rightarrow$ 分布收敛。
- **连续映射定理**：若 $X_n\xrightarrow{P}X$ 且 $g$ 连续，则 $g(X_n)\xrightarrow{P}g(X)$；分布收敛版本同理。
- **Slutsky 定理**：若 $X_n\xrightarrow{D}X$，$Y_n\xrightarrow{P}c$，则 $X_n+Y_n\xrightarrow{D}X+c$，$X_nY_n\xrightarrow{D}cX$。
- **弱大数定律**：若 $E(X_i)=\mu$ 且方差有限，则 $\bar X_n\xrightarrow{P}\mu$。
- **强大数定律**：iid 且 $E|X_1|<\infty$ 时，$\bar X_n\xrightarrow{f.s.}E(X_1)$。
- **中心极限定理：和**：$Z_n=\frac{\sum_{i=1}^nX_i-n\mu}{\sqrt n\sigma}\xrightarrow{D}N(0,1)$。
- **中心极限定理：均值**：$\frac{\bar X_n-\mu}{\sigma/\sqrt n}\xrightarrow{D}N(0,1)$，等价于 $\sqrt n(\bar X_n-\mu)\xrightarrow{D}N(0,\sigma^2)$。
- **多元 CLT**：$\frac1{\sqrt n}(\sum_{i=1}^nX_i-n\mu)\xrightarrow{D}N_k(0,\Sigma)$。
- **二项正态近似**：$B(n,p)\approx N(np,np(1-p))$；**二项 Poisson 近似**：$B(n,p)\approx Po(np)$。

---

## 习题与讲解

### Aufgabe 1 - 练习收敛、极限定理和近似。

#### 题目

Es sei $\mathbb P$ ein Wahrscheinlichkeitsmaß, also ein normiertes Maß mit $\mathbb P(\Omega)=1$, auf dem Messraum $(\Omega,\mathcal F)$ und $A,B\in\mathcal F$.

###### (a)

Falls

$$
\mathbb P(A)=\frac{1}{3}
\qquad
\text{und}
\qquad
\mathbb P(\bar B)=\frac{1}{4},
$$

können $A$ und $B$ dann disjunkt sein? Beweisen oder widerlegen Sie.

###### (b)

Beweisen oder widerlegen Sie:

$$
\mathbb P(B)=0
\Rightarrow
\mathbb P(A\cap B)=0.
$$

###### (c)

Sei

$$
\Omega=\{x\mid x\in\mathbb N_0\}
$$

mit Elementarereignissen $\omega_x=x$. Außerdem gelte

$$
\mathbb P(\{\omega_x\})=\frac{c}{x!}.
$$

Wie groß ist $c$?

#### 解答

##### 中文解题思路

先把题目翻译成概率测度的基本性质：概率非负、全集概率为 $1$、单调性 $A\subseteq B\Rightarrow \mathbb P(A)\le \mathbb P(B)$，以及不交事件满足 $\mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B)$。这类题不要凭图像直觉判断，最好把每个条件都写成一个概率等式或不等式。

出现 $c/x!$ 这种点概率时，关键是用归一化条件：所有点概率加起来必须等于 $1$。所以先写 $\sum_x c/x!=1$，再把 $c$ 提出来；如果求和从 $0$ 到无穷，就会用到 $\sum_{x=0}^{\infty}1/x!=e$。

这是一道综合题，虽然放在本章中，但当前小问更像基础概率或建模题。解题时先按题目本身的关键词选择工具，不要因为章节标题就硬套 CLT 或大数定律。

题目有多个小问时，建议每个小问都保留相同的解题格式：先列已知，再写公式，再代数化简。这样即使某一问算错，也不影响其它小问的结构分。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

###### (a) Falls

Nein, $A$ und $B$ können nicht disjunkt sein.

Aus

$$
\mathbb P(\bar B)=\frac{1}{4}
$$

folgt

$$
\mathbb P(B)=1-\mathbb P(\bar B)=\frac{3}{4}.
$$

Wären $A$ und $B$ disjunkt, dann müsste gelten:

$$
\mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B).
$$

Also:

$$
\mathbb P(A\cup B)
=
\frac{1}{3}+\frac{3}{4}
=
\frac{13}{12}
>
1.
$$

Das ist unmöglich, da $\mathbb P(A\cup B)\leq 1$ gelten muss.

Damit können $A$ und $B$ nicht disjunkt sein.

###### (b) Beweisen oder widerlegen Sie:

Die Aussage ist wahr.

Es gilt:

$$
A\cap B\subseteq B.
$$

Wegen der Monotonie eines Wahrscheinlichkeitsmaßes folgt:

$$
\mathbb P(A\cap B)\leq \mathbb P(B).
$$

Da $\mathbb P(B)=0$ und Wahrscheinlichkeiten nicht negativ sind:

$$
0\leq \mathbb P(A\cap B)\leq 0.
$$

Also:

$$
\mathbb P(A\cap B)=0.
$$

###### (c) Sei

Da $\mathbb P$ ein Wahrscheinlichkeitsmaß ist, muss die Summe aller Punktwahrscheinlichkeiten $1$ ergeben:

$$
\sum_{x=0}^{\infty}\mathbb P(\{\omega_x\})=1.
$$

Einsetzen liefert:

$$
\sum_{x=0}^{\infty}\frac{c}{x!}=1.
$$

Also:

$$
c\sum_{x=0}^{\infty}\frac{1}{x!}=1.
$$

Bekannt ist:

$$
\sum_{x=0}^{\infty}\frac{1}{x!}=e.
$$

Daher:

$$
ce=1.
$$

Damit:

$$
c=\frac{1}{e}.
$$

---

---

### Aufgabe 2 - 练习收敛、极限定理和近似。

#### 题目

Gegeben sei ein Wahrscheinlichkeitsraum $(\Omega,\mathcal F,\mathbb P)$ und $B\subset\Omega$ mit $\mathbb P(B)>0$.

###### (a)

Beweisen oder widerlegen Sie:

$$
\mathbb P(A\mid B)\geq \mathbb P(A)
\Rightarrow
\mathbb P(B\mid A)\geq \mathbb P(B).
$$

###### (b)

Zeigen Sie:

$$
\mathbb P(A\mid B)
\geq
\frac{\mathbb P(A)+\mathbb P(B)-1}{\mathbb P(B)}.
$$

#### 解答

##### 中文解题思路

先把题目翻译成概率测度的基本性质：概率非负、全集概率为 $1$、单调性 $A\subseteq B\Rightarrow \mathbb P(A)\le \mathbb P(B)$，以及不交事件满足 $\mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B)$。这类题不要凭图像直觉判断，最好把每个条件都写成一个概率等式或不等式。

条件概率题先命名事件，再把题目给出的百分比写成条件概率。若题目问的是原因在结果已知后的概率，例如 $P(K\mid T+)$，就要用 Bayes，不能直接拿敏感度或检出率当答案。

这是一道综合题，虽然放在本章中，但当前小问更像基础概率或建模题。解题时先按题目本身的关键词选择工具，不要因为章节标题就硬套 CLT 或大数定律。

题目有多个小问时，建议每个小问都保留相同的解题格式：先列已知，再写公式，再代数化简。这样即使某一问算错，也不影响其它小问的结构分。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

###### (a) Beweisen oder widerlegen Sie:

Die Aussage ist wahr, sofern die bedingten Wahrscheinlichkeiten definiert sind, also insbesondere $\mathbb P(A)>0$ und $\mathbb P(B)>0$ gelten.

Aus

$$
\mathbb P(A\mid B)\geq \mathbb P(A)
$$

folgt:

$$
\frac{\mathbb P(A\cap B)}{\mathbb P(B)}\geq \mathbb P(A).
$$

Da $\mathbb P(B)>0$ gilt:

$$
\mathbb P(A\cap B)\geq \mathbb P(A)\mathbb P(B).
$$

Falls $\mathbb P(A)>0$, dürfen wir durch $\mathbb P(A)$ teilen:

$$
\frac{\mathbb P(A\cap B)}{\mathbb P(A)}
\geq
\mathbb P(B).
$$

Die linke Seite ist $\mathbb P(B\mid A)$. Also:

$$
\mathbb P(B\mid A)\geq \mathbb P(B).
$$

###### (b) Zeigen Sie:

Aus der Additionsformel folgt:

$$
\mathbb P(A\cup B)
=
\mathbb P(A)+\mathbb P(B)-\mathbb P(A\cap B).
$$

Da $\mathbb P(A\cup B)\leq 1$, gilt:

$$
\mathbb P(A)+\mathbb P(B)-\mathbb P(A\cap B)\leq 1.
$$

Umstellen liefert:

$$
\mathbb P(A\cap B)\geq \mathbb P(A)+\mathbb P(B)-1.
$$

Da $\mathbb P(B)>0$, folgt:

$$
\mathbb P(A\mid B)
=
\frac{\mathbb P(A\cap B)}{\mathbb P(B)}
\geq
\frac{\mathbb P(A)+\mathbb P(B)-1}{\mathbb P(B)}.
$$

Damit ist die Behauptung gezeigt.

---

---

### Aufgabe 3 - 练习收敛、极限定理和近似。

#### 题目

Es sei $\mathbb P$ ein Wahrscheinlichkeitsmaß auf dem Messraum $(\Omega,\mathcal F)$ und $A,B\in\mathcal F$.

###### (a)

Falls $\mathbb P(A)=\frac13$ und $\mathbb P(\bar B)=\frac14$, können $A$ und $B$ dann disjunkt sein?

###### (b)

Beweisen oder widerlegen Sie:

$$
\mathbb P(A)=\mathbb P(\bar B)\Rightarrow \bar A=B.
$$

###### (c)

Beweisen oder widerlegen Sie:

$$
\mathbb P(B)=0\Rightarrow \mathbb P(A\cap B)=0.
$$

###### (d)

Sei $\Omega=\{i\mid i\in\mathbb N_0\}$ mit Elementarereignissen $\omega_i=i$. Außerdem gelte:

$$
\mathbb P(\{\omega_i\})=\frac{c}{i!}.
$$

Wie groß ist $c$?

#### 解答

##### 中文解题思路

先把题目翻译成概率测度的基本性质：概率非负、全集概率为 $1$、单调性 $A\subseteq B\Rightarrow \mathbb P(A)\le \mathbb P(B)$，以及不交事件满足 $\mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B)$。这类题不要凭图像直觉判断，最好把每个条件都写成一个概率等式或不等式。

Laplace 模型的第一步是数清样本空间大小和有利结果个数。最后概率写成 $|A|/|\Omega|$；如果事件之间有重叠，要用容斥原理而不是直接相加。

这是一道综合题，虽然放在本章中，但当前小问更像基础概率或建模题。解题时先按题目本身的关键词选择工具，不要因为章节标题就硬套 CLT 或大数定律。

题目有多个小问时，建议每个小问都保留相同的解题格式：先列已知，再写公式，再代数化简。这样即使某一问算错，也不影响其它小问的结构分。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

###### (a)

Nein. Es gilt $\mathbb P(B)=\frac34$. Wären $A$ und $B$ disjunkt, dann:

$$
\mathbb P(A\cup B)=\frac13+\frac34=\frac{13}{12}>1.
$$

Das ist unmöglich.

###### (b) Beweisen oder widerlegen Sie:

Falsch. Für $\Omega=\{1,2\}$ mit Laplace-Wahrscheinlichkeit und $A=B=\{1\}$ gilt:

$$
\mathbb P(A)=\frac12=\mathbb P(\bar B),
$$

aber $\bar A=\{2\}\neq B$.

###### (c) Beweisen oder widerlegen Sie:

Wahr, denn $A\cap B\subseteq B$. Also:

$$
0\leq\mathbb P(A\cap B)\leq\mathbb P(B)=0.
$$

###### (d)

Es muss gelten:

$$
\sum_{i=0}^{\infty}\frac{c}{i!}=1.
$$

Da $\sum_{i=0}^{\infty}\frac1{i!}=e$, folgt:

$$
c=\frac1e.
$$

---

---

### Aufgabe 4 - 用中心极限定理或近似分布计算概率。

#### 题目

Bestimmen Sie für die folgenden Situationen jeweils die passende Standardverteilung und berechnen Sie die gefragten Wahrscheinlichkeiten.

###### (a) Tombola

Es gibt $k$ Lose, durchnummeriert von $1$ bis $k$. Genau ein Los gewinnt. $X_1$ sei die Gewinnlosnummer.

###### (b) Lerngruppe

Es gibt fünf Aufgaben, vier wurden vorbereitet, zwei werden zufällig ausgewählt. $X_2$ sei die Anzahl der vorbereiteten ausgewählten Aufgaben.

###### (c) Kontrolle eines Betriebs

Jeden Tag wird unabhängig ein Anteil $a$ der Betriebe kontrolliert. $X_3$ sei die Anzahl der Tage bis zur ersten Kontrolle eines bestimmten Betriebs.

###### (d) Test mit 10 Fragen

Ein Schüler beantwortet jede von 10 Fragen unabhängig mit Wahrscheinlichkeit $0.9$ richtig. $X_4$ sei die Anzahl richtiger Antworten.

#### 解答

##### 中文解题思路

收敛题先区分收敛类型：几乎处处、概率收敛、分布收敛和矩收敛不能随便互换。证明概率收敛时，目标通常是让 $\mathbb P(|X_n-X|>\varepsilon)$ 趋于 $0$；证明分布收敛时，则看分布函数在连续点的极限。

CLT/近似题的路线是先确定单个变量的均值 $\mu$ 和方差 $\sigma^2$，再把和或均值标准化。最后用标准正态分布近似概率，必要时注意二项分布的连续性修正。

题目有多个小问时，建议每个小问都保留相同的解题格式：先列已知，再写公式，再代数化简。这样即使某一问算错，也不影响其它小问的结构分。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

###### (a) Tombola

$$
X_1\sim U(\{1,\dots,k\}),
\qquad
\mathbb P(X_1=i)=\frac1k.
$$

Für $k=100$ und $i=66$:

$$
\mathbb P(X_1<66)
=\frac{65}{100}
=0.65.
$$

###### (b) Lerngruppe

$$
X_2\sim\operatorname{Hyp}(N=5,K=4,n=2).
$$

Der Träger ist:

$$
\{1,2\}.
$$

Gesucht:

$$
\mathbb P(X_2=2)
=
\frac{\binom42\binom10}{\binom52}
=\frac35.
$$

###### (c) Kontrolle eines Betriebs

$$
X_3\sim\operatorname{Geom}(a).
$$

Gesucht:

$$
\mathbb P(X_3\leq 2)
=1-(1-a)^2
=2a-a^2.
$$

###### (d) Test mit 10 Fragen

$$
X_4\sim\operatorname{Bin}(10,0.9).
$$

Gesucht:

$$
\mathbb P(X_4\geq 9)
=
\binom{10}{9}0.9^9 0.1
+0.9^{10}
\approx 0.7361.
$$

---

---

### Aufgabe 5 - 判断并证明随机变量序列的收敛关系。

#### 题目

Gegeben seien zwei Folgen unabhängiger identisch verteilter Zufallsvariablen mit:

$$
X_i\sim U(\{1,2,3,4,5\}),
\qquad
Y_i\sim \operatorname{NB}\left(4,\frac12\right),
\qquad i\in\mathbb N.
$$

Außerdem seien:

$$
\bar X_n=\frac1n\sum_{i=1}^n X_i,
\qquad
\bar Y_n=\frac1n\sum_{i=1}^n Y_i.
$$

Bestimmen Sie $a,b\in\mathbb R$, sodass:

$$
\bar X_n+\bar Y_n \xrightarrow{P} a,
\qquad
\bar X_n\cdot \bar Y_n \xrightarrow{P} b.
$$

#### 解答

##### 中文解题思路

收敛题先认清目标符号：$\xrightarrow{P}$ 要证明偏离概率趋于 $0$，$\xrightarrow{D}$ 要看分布函数在连续点的极限。若表达式能拆成“一个分布收敛项 + 一个概率收敛到常数的项”，优先考虑 Slutsky。

大数定律题要把目标改写成样本均值，并检查 iid 与期望有限。满足条件后，样本均值依概率收敛到对应期望；若有函数 $g(X_i)$，就把 $g(X_i)$ 当作新的 iid 序列。

收敛题先区分收敛类型：几乎处处、概率收敛、分布收敛和矩收敛不能随便互换。证明概率收敛时，目标通常是让 $\mathbb P(|X_n-X|>\varepsilon)$ 趋于 $0$；证明分布收敛时，则看分布函数在连续点的极限。

大数定律题要把目标改写成样本均值形式，然后检查 iid 和期望有限这两个条件。满足后直接得到样本均值依概率收敛到期望。

含 Slutsky 或连续映射的题，不要展开复杂分布。先把表达式拆成一个已知分布收敛项和一个依概率收敛到常数的项，再套 Slutsky 或连续映射定理。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

Für $X_i\sim U(\{1,2,3,4,5\})$ gilt:

$$
\mathbb E(X_i)=3.
$$

Wir verwenden hier die übliche Parametrisierung der negativen Binomialverteilung als Anzahl der Misserfolge vor dem $r$-ten Erfolg. Dann gilt:

$$
\mathbb E(Y_i)=\frac{r(1-p)}p
=\frac{4\cdot(1/2)}{1/2}
=4.
$$

Nach dem schwachen Gesetz der großen Zahlen:

$$
\bar X_n\xrightarrow{P}3,
\qquad
\bar Y_n\xrightarrow{P}4.
$$

Mit dem Continuous-Mapping-Theorem:

$$
\bar X_n+\bar Y_n\xrightarrow{P}3+4=7,
$$

und:

$$
\bar X_n\bar Y_n\xrightarrow{P}3\cdot 4=12.
$$

Also:

$$
a=7,
\qquad
b=12.
$$

---

---

### Aufgabe 6 - 判断并证明随机变量序列的收敛关系。

#### 题目

Gegeben sei der Wahrscheinlichkeitsraum:

$$
([0,1],\mathcal B([0,1]),\lambda|_{[0,1]}).
$$

Betrachten Sie:

$$
X_n(\omega)=n\cdot\mathbf 1_{\left(0,\frac1n\right)}(\omega).
$$

Untersuchen Sie, ob $X_n$ gegen $0$ fast sicher, in Wahrscheinlichkeit, in Verteilung und im ersten Moment konvergiert.

#### 解答

##### 中文解题思路

收敛题先认清目标符号：$\xrightarrow{P}$ 要证明偏离概率趋于 $0$，$\xrightarrow{D}$ 要看分布函数在连续点的极限。若表达式能拆成“一个分布收敛项 + 一个概率收敛到常数的项”，优先考虑 Slutsky。

收敛题先区分收敛类型：几乎处处、概率收敛、分布收敛和矩收敛不能随便互换。证明概率收敛时，目标通常是让 $\mathbb P(|X_n-X|>\varepsilon)$ 趋于 $0$；证明分布收敛时，则看分布函数在连续点的极限。

含 Slutsky 或连续映射的题，不要展开复杂分布。先把表达式拆成一个已知分布收敛项和一个依概率收敛到常数的项，再套 Slutsky 或连续映射定理。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

Für jedes feste $\omega\in[0,1]$ gilt schließlich $X_n(\omega)=0$: Für $\omega>0$ ist irgendwann $\frac1n<\omega$, und für $\omega=0$ liegt $\omega$ nie im offenen Intervall. Also:

$$
X_n\to 0
\qquad
\text{fast sicher}.
$$

Für $\varepsilon>0$ und $n>\varepsilon$ gilt:

$$
\mathbb P(|X_n|>\varepsilon)
=
\lambda\left(\left(0,\frac1n\right)\right)
=\frac1n
\to 0.
$$

Also konvergiert $X_n$ in Wahrscheinlichkeit gegen $0$.

Konvergenz in Wahrscheinlichkeit impliziert Konvergenz in Verteilung, also:

$$
X_n\xrightarrow{d}0.
$$

Für das erste Moment:

$$
\mathbb E(|X_n-0|)
=\int_0^1 n\mathbf 1_{\left(0,\frac1n\right)}(\omega)\,d\omega
=n\cdot\frac1n
=1.
$$

Das geht nicht gegen $0$. Daher konvergiert $X_n$ nicht im ersten Moment gegen $0$.

---

---

### Aufgabe 7 - 用中心极限定理或近似分布计算概率。

#### 题目

Gegeben ist eine einzelne Zufallsvariable einer parametrischen Verteilungsfamilie. Nennen Sie Beispiele hinreichender Eigenschaften, unter denen $X$ selbst approximativ normalverteilt sein kann, ähnlich wie bei der Poisson-Approximation. Welche Prinzipien könnten zugrunde liegen?

#### 解答

##### 中文解题思路

中心极限定理题的固定路线是：先算单个变量的均值和方差，再把和或均值标准化成标准正态形式，最后用标准正态分布近似概率。二项分布近似时要注意是否需要连续性修正。

收敛题先区分收敛类型：几乎处处、概率收敛、分布收敛和矩收敛不能随便互换。证明概率收敛时，目标通常是让 $\mathbb P(|X_n-X|>\varepsilon)$ 趋于 $0$；证明分布收敛时，则看分布函数在连续点的极限。

CLT/近似题的路线是先确定单个变量的均值 $\mu$ 和方差 $\sigma^2$，再把和或均值标准化。最后用标准正态分布近似概率，必要时注意二项分布的连续性修正。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

Eine einzelne Zufallsvariable aus einer parametrischen Familie kann approximativ normalverteilt sein, wenn sie sich als Summe vieler kleiner, ungefähr unabhängiger Zufallsbeiträge verstehen lässt.

Typische hinreichende Prinzipien:

- Der relevante Parameter ist groß, zum Beispiel $n$ bei $\operatorname{Bin}(n,p)$ oder $\lambda$ bei $\operatorname{Poi}(\lambda)$.
- Kein einzelner Bestandteil dominiert die Summe.
- Die Varianz ist endlich und nicht degeneriert.
- Nach Zentrierung und Skalierung greift ein zentraler Grenzwertsatz.

Beispiele:

$$
\operatorname{Bin}(n,p)\approx N(np,np(1-p))
$$

für großes $n$ und nicht zu extreme $p$.

$$
\operatorname{Poi}(\lambda)\approx N(\lambda,\lambda)
$$

für großes $\lambda$.

Auch eine Gamma-Verteilung $\operatorname{Ga}(\alpha,\beta)$ ist für großes $\alpha$ näherungsweise normalverteilt, weil sie als Summe vieler unabhängiger Exponentialvariablen aufgefasst werden kann:

$$
\operatorname{Ga}(\alpha,\beta)
\approx
N\left(\frac{\alpha}{\beta},\frac{\alpha}{\beta^2}\right).
$$

---

---

### Aufgabe 8 - 用 Markov 或 Chebyshev 不等式给概率上界。

#### 题目

Wie oft muss mit einer idealen Münze mindestens geworfen werden, sodass die relative Häufigkeit von Wappen mit Wahrscheinlichkeit mindestens $0.95$ höchstens $0.01$ beziehungsweise $0.001$ von $\pi=0.5$ abweicht? Nutzen Sie eine geeignete Abschätzung durch eine Ungleichung.

#### 解答

##### 中文解题思路

Laplace 模型的第一步是数清样本空间大小和有利结果个数。最后概率写成 $|A|/|\Omega|$；如果事件之间有重叠，要用容斥原理而不是直接相加。

不等式题先判断可用条件：Markov 用非负性控制 $P(X\ge a)$，Chebyshev 用均值和方差控制 $P(|X-\mu|\ge\varepsilon)$。算出的上界如果超过 $1$，要说明概率上界只能取平凡界 $1$。

这是一道综合题，虽然放在本章中，但当前小问更像基础概率或建模题。解题时先按题目本身的关键词选择工具，不要因为章节标题就硬套 CLT 或大数定律。

大数定律题要把目标改写成样本均值形式，然后检查 iid 和期望有限这两个条件。满足后直接得到样本均值依概率收敛到期望。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

Sei:

$$
\bar X_n=\frac1n\sum_{i=1}^n X_i,
$$

wobei $X_i=1$ für Wappen und $X_i=0$ sonst. Dann:

$$
\mathbb E(\bar X_n)=\frac12,
\qquad
\operatorname{Var}(\bar X_n)=\frac{1/4}{n}=\frac1{4n}.
$$

Mit Chebyshev:

$$
\mathbb P\left(\left|\bar X_n-\frac12\right|>\varepsilon\right)
\leq
\frac{1}{4n\varepsilon^2}.
$$

Wir wollen, dass die Gegenwahrscheinlichkeit höchstens $0.05$ ist:

$$
\frac{1}{4n\varepsilon^2}\leq 0.05.
$$

Also:

$$
n\geq \frac{1}{0.2\varepsilon^2}
=\frac5{\varepsilon^2}.
$$

Für $\varepsilon=0.01$:

$$
n\geq \frac5{0.01^2}=50000.
$$

Für $\varepsilon=0.001$:

$$
n\geq \frac5{0.001^2}=5000000.
$$

---

---

### Aufgabe 9 - 用中心极限定理或近似分布计算概率。

#### 题目

Ein Beamter verlässt an den $225$ Arbeitstagen eines Jahres sein Büro immer erst kurz nach Dienstschluss. Die täglichen zusätzlichen Arbeitszeiten seien unabhängig exponentialverteilt mit Erwartungswert $1/\lambda=5$ Minuten.

###### (a)

Leiten Sie die approximative Verteilung der gesamten zusätzlichen Arbeitszeit eines Jahres her.

###### (b)

Berechnen Sie approximativ die Wahrscheinlichkeit, dass der Beamte in einem Jahr mehr als $16$ Stunden zusätzlich arbeitet.

#### 解答

##### 中文解题思路

中心极限定理题的固定路线是：先算单个变量的均值和方差，再把和或均值标准化成标准正态形式，最后用标准正态分布近似概率。二项分布近似时要注意是否需要连续性修正。

收敛题先区分收敛类型：几乎处处、概率收敛、分布收敛和矩收敛不能随便互换。证明概率收敛时，目标通常是让 $\mathbb P(|X_n-X|>\varepsilon)$ 趋于 $0$；证明分布收敛时，则看分布函数在连续点的极限。

CLT/近似题的路线是先确定单个变量的均值 $\mu$ 和方差 $\sigma^2$，再把和或均值标准化。最后用标准正态分布近似概率，必要时注意二项分布的连续性修正。

题目有多个小问时，建议每个小问都保留相同的解题格式：先列已知，再写公式，再代数化简。这样即使某一问算错，也不影响其它小问的结构分。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

###### (a)

Seien $X_1,\dots,X_{225}$ die täglichen zusätzlichen Arbeitszeiten in Minuten. Dann:

$$
X_i\sim\operatorname{Exp}(\lambda),
\qquad
\frac1\lambda=5,
\qquad
\lambda=\frac15.
$$

Für:

$$
S_{225}=\sum_{i=1}^{225}X_i
$$

gilt exakt:

$$
S_{225}\sim\operatorname{Ga}\left(225,\frac15\right)
$$

in Rate-Parametrisierung. Approximativ nach dem zentralen Grenzwertsatz:

$$
S_{225}\approx N(225\cdot 5,\ 225\cdot 5^2).
$$

Also:

$$
S_{225}\approx N(1125,\ 5625)
$$

in Minuten.

###### (b)

$16$ Stunden sind:

$$
16\cdot 60=960
$$

Minuten. Mit $\sigma=\sqrt{5625}=75$:

$$
\mathbb P(S_{225}>960)
\approx
\mathbb P\left(
Z>\frac{960-1125}{75}
\right)
=
\mathbb P(Z>-2.2).
$$

Also:

$$
\mathbb P(S_{225}>960)
=\Phi(2.2)
\approx 0.9861.
$$

---

### Aufgabe 10 - 用变量变换求新随机变量的密度或分布。

#### 题目

###### (a)

$X\sim\operatorname{Beta}(a,b)$. Berechnen Sie die Dichte von:

$$
Y=(X+2)^{-1}.
$$

###### (b)

Sei $X$ Weibull-verteilt mit:

$$
f_X(x)=abx^{b-1}e^{-ax^b}\mathbf 1_{\{x\geq 0\}},
\qquad a,b>0.
$$

Bestimmen Sie die Dichte von $Y=X^b$.

#### 解答

##### 中文解题思路

看到分布函数或密度，先检查对象类型：离散型看跳跃点概率，连续型看密度积分。分布函数要满足单调、右连续、极限从 $0$ 到 $1$；密度要非负且总积分为 $1$。

中心极限定理题的固定路线是：先算单个变量的均值和方差，再把和或均值标准化成标准正态形式，最后用标准正态分布近似概率。二项分布近似时要注意是否需要连续性修正。

变量变换题按三步走：写出变换和反变换，求导数或 Jacobian 绝对值，再把原密度代入并写出新支持集。支持集不能省，因为它决定密度在哪些地方为零。

收敛题先区分收敛类型：几乎处处、概率收敛、分布收敛和矩收敛不能随便互换。证明概率收敛时，目标通常是让 $\mathbb P(|X_n-X|>\varepsilon)$ 趋于 $0$；证明分布收敛时，则看分布函数在连续点的极限。

CLT/近似题的路线是先确定单个变量的均值 $\mu$ 和方差 $\sigma^2$，再把和或均值标准化。最后用标准正态分布近似概率，必要时注意二项分布的连续性修正。

题目有多个小问时，建议每个小问都保留相同的解题格式：先列已知，再写公式，再代数化简。这样即使某一问算错，也不影响其它小问的结构分。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

###### (a)

Die Transformation ist:

$$
y=\frac1{x+2},
\qquad
x=\frac1y-2.
$$

Da $x\in(0,1)$, gilt:

$$
y\in\left(\frac13,\frac12\right).
$$

Außerdem:

$$
\left|\frac{dx}{dy}\right|=\frac1{y^2}.
$$

Damit:

$$
f_Y(y)
=
\frac{1}{B(a,b)}
\left(\frac1y-2\right)^{a-1}
\left(3-\frac1y\right)^{b-1}
\frac1{y^2}
\mathbf 1_{\left(\frac13,\frac12\right)}(y).
$$

###### (b) Sei $X$ Weibull-verteilt mit:

Die Umkehrfunktion ist $x=y^{1/b}$, und:

$$
\left|\frac{dx}{dy}\right|
=\frac1b y^{1/b-1}.
$$

Also:

$$
f_Y(y)
=ab(y^{1/b})^{b-1}e^{-ay}\frac1b y^{1/b-1}
=ae^{-ay}\mathbf 1_{\{y\geq 0\}}.
$$

Damit:

$$
Y\sim\operatorname{Exp}(a).
$$

###### Bonus: Zentraler Grenzwertsatz

Sepp spielt $80$ unabhängige Runden. Die Wahrscheinlichkeit für ein gutes Blatt beträgt $\pi=0.14$. Sei:

$$
X\sim\operatorname{Bin}(80,0.14).
$$

Gesucht ist näherungsweise $\mathbb P(X>11)$. Es gilt:

$$
\mu=80\cdot 0.14=11.2,
\qquad
\sigma^2=80\cdot0.14\cdot0.86=9.632.
$$

Ohne Stetigkeitskorrektur:

$$
\mathbb P(X>11)
\approx
\mathbb P\left(Z>\frac{11-11.2}{\sqrt{9.632}}\right)
=\mathbb P(Z>-0.0644)
=\Phi(0.0644)
\approx 0.5257.
$$

---

---

### Aufgabe 11 - 练习收敛、极限定理和近似。

#### 题目

Es sei $\mathbb P$ ein Wahrscheinlichkeitsmaß mit $\mathbb P(\Omega)=1$ auf dem Messraum $(\Omega,\mathcal F)$ und $A,B\in\mathcal F$.

###### (a)

Falls

$$
\mathbb P(A)=\frac13
\qquad
\text{und}
\qquad
\mathbb P(\bar B)=\frac14,
$$

können $A$ und $B$ dann disjunkt sein?

###### (b)

Beweisen oder widerlegen Sie:

$$
\mathbb P(A)=\mathbb P(\bar B)
\Rightarrow
\bar A=B.
$$

###### (c)

Beweisen oder widerlegen Sie:

$$
\mathbb P(B)=0
\Rightarrow
\mathbb P(A\cap B)=0.
$$

###### (d)

Sei

$$
\Omega=\{i\mid i\in\mathbb N_0\}
$$

mit Elementarereignissen $\omega_i=i$. Außerdem gelte:

$$
\mathbb P(\{\omega_i\})=\frac{c}{i!}.
$$

Wie groß ist $c$?

#### 解答

##### 中文解题思路

先把题目翻译成概率测度的基本性质：概率非负、全集概率为 $1$、单调性 $A\subseteq B\Rightarrow \mathbb P(A)\le \mathbb P(B)$，以及不交事件满足 $\mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B)$。这类题不要凭图像直觉判断，最好把每个条件都写成一个概率等式或不等式。

Laplace 模型的第一步是数清样本空间大小和有利结果个数。最后概率写成 $|A|/|\Omega|$；如果事件之间有重叠，要用容斥原理而不是直接相加。

这是一道综合题，虽然放在本章中，但当前小问更像基础概率或建模题。解题时先按题目本身的关键词选择工具，不要因为章节标题就硬套 CLT 或大数定律。

题目有多个小问时，建议每个小问都保留相同的解题格式：先列已知，再写公式，再代数化简。这样即使某一问算错，也不影响其它小问的结构分。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

###### (a) Falls

Nein.

Aus $\mathbb P(\bar B)=\frac14$ folgt:

$$
\mathbb P(B)=\frac34.
$$

Falls $A$ und $B$ disjunkt wären, dann wäre:

$$
\mathbb P(A\cup B)
=
\mathbb P(A)+\mathbb P(B)
=
\frac13+\frac34
=
\frac{13}{12}>1.
$$

Das ist unmöglich. Also können $A$ und $B$ nicht disjunkt sein.

###### (b) Beweisen oder widerlegen Sie:

Die Aussage ist falsch.

Gegenbeispiel: Sei $\Omega=\{1,2\}$ mit Laplace-Wahrscheinlichkeit. Setze:

$$
A=\{1\},
\qquad
B=\{1\}.
$$

Dann:

$$
\mathbb P(A)=\frac12
\qquad
\text{und}
\qquad
\mathbb P(\bar B)=\mathbb P(\{2\})=\frac12.
$$

Also ist $\mathbb P(A)=\mathbb P(\bar B)$.

Aber:

$$
\bar A=\{2\}\neq \{1\}=B.
$$

###### (c) Beweisen oder widerlegen Sie:

Die Aussage ist wahr.

Da $A\cap B\subseteq B$, folgt aus Monotonie:

$$
0\leq \mathbb P(A\cap B)\leq \mathbb P(B)=0.
$$

Also:

$$
\mathbb P(A\cap B)=0.
$$

###### (d) Sei

Es muss gelten:

$$
\sum_{i=0}^{\infty}\mathbb P(\{\omega_i\})=1.
$$

Also:

$$
\sum_{i=0}^{\infty}\frac{c}{i!}=1.
$$

Da:

$$
\sum_{i=0}^{\infty}\frac1{i!}=e,
$$

folgt:

$$
ce=1.
$$

Damit:

$$
c=e^{-1}.
$$

---

---

### Aufgabe 12 - 练习收敛、极限定理和近似。

#### 题目

Es sei $(\Omega,\mathcal F,\mathbb P)$ ein Wahrscheinlichkeitsraum und $A,B\in\mathcal F$.

###### (a)

Beweisen oder widerlegen Sie:

$$
A\text{ und }B\text{ disjunkt}
\Rightarrow
A\text{ und }\bar B\text{ stochastisch unabhängig.}
$$

###### (b)

Sei

$$
\mathbb P(A)=0.5
\qquad
\text{und}
\qquad
\mathbb P(A\cup B)=0.7.
$$

Bestimmen Sie $\mathbb P(B)$, wenn:

- $A$ und $B$ stochastisch unabhängig sind,
- $A$ und $B$ disjunkt sind.

###### (c)

Betrachten Sie beim einmaligen fairen Würfelwurf das Ereignis

$$
A=\text{„Die Augenzahl ist gerade“}.
$$

Geben Sie ein zu $A$ unabhängiges Ereignis $B\in\mathcal P(\Omega)$ mit $B\notin\{\emptyset,\Omega\}$ an.

#### 解答

##### 中文解题思路

先把题目翻译成概率测度的基本性质：概率非负、全集概率为 $1$、单调性 $A\subseteq B\Rightarrow \mathbb P(A)\le \mathbb P(B)$，以及不交事件满足 $\mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B)$。这类题不要凭图像直觉判断，最好把每个条件都写成一个概率等式或不等式。

Laplace 模型的第一步是数清样本空间大小和有利结果个数。最后概率写成 $|A|/|\Omega|$；如果事件之间有重叠，要用容斥原理而不是直接相加。

这是一道综合题，虽然放在本章中，但当前小问更像基础概率或建模题。解题时先按题目本身的关键词选择工具，不要因为章节标题就硬套 CLT 或大数定律。

题目有多个小问时，建议每个小问都保留相同的解题格式：先列已知，再写公式，再代数化简。这样即使某一问算错，也不影响其它小问的结构分。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

###### (a) Beweisen oder widerlegen Sie:

Die Aussage ist wahr.

Wenn $A$ und $B$ disjunkt sind, dann gilt:

$$
A\subseteq \bar B.
$$

Daher:

$$
A\cap\bar B=A.
$$

Somit:

$$
\mathbb P(A\cap\bar B)=\mathbb P(A).
$$

Außerdem ist wegen Disjunktheit:

$$
\mathbb P(A\cap B)=0.
$$

Allerdings folgt daraus nicht allgemein

$$
\mathbb P(A)=\mathbb P(A)\mathbb P(\bar B).
$$

Die ursprüngliche Aussage ist also im Allgemeinen falsch.

Gegenbeispiel: fairer Würfelwurf, $A=\{1\}$, $B=\{2\}$. Dann sind $A$ und $B$ disjunkt, aber:

$$
\mathbb P(A\cap\bar B)=\mathbb P(A)=\frac16,
$$

während:

$$
\mathbb P(A)\mathbb P(\bar B)
=
\frac16\cdot\frac56
=
\frac{5}{36}.
$$

Also sind $A$ und $\bar B$ nicht unabhängig.

###### (b) Sei

Setze $q=\mathbb P(B)$.

Falls $A$ und $B$ unabhängig sind:

$$
\mathbb P(A\cup B)
=
\mathbb P(A)+\mathbb P(B)-\mathbb P(A)\mathbb P(B).
$$

Also:

$$
0.7=0.5+q-0.5q=0.5+0.5q.
$$

Damit:

$$
q=0.4.
$$

Falls $A$ und $B$ disjunkt sind:

$$
\mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B).
$$

Also:

$$
0.7=0.5+q.
$$

Damit:

$$
q=0.2.
$$

###### (c)

Beim fairen Würfelwurf ist:

$$
\Omega=\{1,2,3,4,5,6\}
$$

und:

$$
A=\{2,4,6\}.
$$

Wähle zum Beispiel:

$$
B=\{1,2\}.
$$

Dann:

$$
\mathbb P(A)=\frac12,
\qquad
\mathbb P(B)=\frac13,
\qquad
A\cap B=\{2\}.
$$

Also:

$$
\mathbb P(A\cap B)=\frac16
=
\frac12\cdot\frac13
=
\mathbb P(A)\mathbb P(B).
$$

Damit sind $A$ und $B$ unabhängig.

---

---

### Aufgabe 13 - 处理测度、可测性、Dirac 测度或积分。

#### 题目

Sei $(x_n)_{n\in\mathbb N}$ eine Folge reeller Zahlen und seien

$$
X_n\sim\delta_{x_n},
\qquad
X\sim\delta_x
$$

Dirac-verteilte Zufallsvariablen. Zeigen Sie:

$$
x_n\to x
$$

genau dann, wenn

$$
X_n\to X
$$

in Wahrscheinlichkeit.

#### 解答

##### 中文解题思路

测度/可测性题要回到定义：可测性通常看原像是否属于 $\sigma$-Algebra；Lebesgue 测度算长度或面积；计数测度算元素个数；Dirac 测度只看集合是否包含支撑点。

这是一道综合题，虽然放在本章中，但当前小问更像基础概率或建模题。解题时先按题目本身的关键词选择工具，不要因为章节标题就硬套 CLT 或大数定律。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

Da $X_n$ Dirac-verteilt in $x_n$ ist, gilt fast sicher:

$$
X_n=x_n.
$$

Ebenso gilt fast sicher:

$$
X=x.
$$

Für $\varepsilon>0$ ist daher:

$$
\mathbb P(|X_n-X|>\varepsilon)
=
\begin{cases}
1, & |x_n-x|>\varepsilon,\\
0, & |x_n-x|\leq\varepsilon.
\end{cases}
$$

Falls $x_n\to x$, dann ist für jedes $\varepsilon>0$ irgendwann $|x_n-x|\leq\varepsilon$, also:

$$
\mathbb P(|X_n-X|>\varepsilon)\to0.
$$

Damit gilt $X_n\to X$ in Wahrscheinlichkeit.

Umgekehrt: Wenn $X_n\to X$ in Wahrscheinlichkeit, dann muss für jedes $\varepsilon>0$ gelten:

$$
\mathbb P(|X_n-X|>\varepsilon)\to0.
$$

Da diese Wahrscheinlichkeit nur die Werte $0$ oder $1$ annimmt, muss sie ab einem gewissen Index $0$ sein. Also gilt schließlich:

$$
|x_n-x|\leq\varepsilon.
$$

Damit folgt $x_n\to x$.

---

---

### Aufgabe 14 - 判断并证明随机变量序列的收敛关系。

#### 题目

Sei $(X_i)_{i\in\mathbb N}$ eine Folge iid Zufallsvariablen in $\mathbb R$ und $g:\mathbb R\to\mathbb R$ messbar. Nutzen Sie das schwache Gesetz der großen Zahlen, um zu zeigen:

$$
\frac1n\sum_{i=1}^n g(X_i)
\xrightarrow{P}
E[g(X_1)].
$$

#### 解答

##### 中文解题思路

收敛题先认清目标符号：$\xrightarrow{P}$ 要证明偏离概率趋于 $0$，$\xrightarrow{D}$ 要看分布函数在连续点的极限。若表达式能拆成“一个分布收敛项 + 一个概率收敛到常数的项”，优先考虑 Slutsky。

大数定律题要把目标改写成样本均值，并检查 iid 与期望有限。满足条件后，样本均值依概率收敛到对应期望；若有函数 $g(X_i)$，就把 $g(X_i)$ 当作新的 iid 序列。

测度/可测性题要回到定义：可测性通常看原像是否属于 $\sigma$-Algebra；Lebesgue 测度算长度或面积；计数测度算元素个数；Dirac 测度只看集合是否包含支撑点。

收敛题先区分收敛类型：几乎处处、概率收敛、分布收敛和矩收敛不能随便互换。证明概率收敛时，目标通常是让 $\mathbb P(|X_n-X|>\varepsilon)$ 趋于 $0$；证明分布收敛时，则看分布函数在连续点的极限。

大数定律题要把目标改写成样本均值形式，然后检查 iid 和期望有限这两个条件。满足后直接得到样本均值依概率收敛到期望。

含 Slutsky 或连续映射的题，不要展开复杂分布。先把表达式拆成一个已知分布收敛项和一个依概率收敛到常数的项，再套 Slutsky 或连续映射定理。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

Setze:

$$
Y_i=g(X_i).
$$

Da die $X_i$ iid sind und $g$ messbar ist, sind auch die $Y_i$ iid.

Falls $E[|g(X_1)|]<\infty$ gilt, kann das schwache Gesetz der großen Zahlen angewendet werden:

$$
\frac1n\sum_{i=1}^nY_i
\xrightarrow{P}
E[Y_1].
$$

Einsetzen von $Y_i=g(X_i)$ liefert:

$$
\frac1n\sum_{i=1}^n g(X_i)
\xrightarrow{P}
E[g(X_1)].
$$

---

---

### Aufgabe 15 - 判断并证明随机变量序列的收敛关系。

#### 题目

Sei $f:\mathbb R\to\mathbb R$ stetig und

$$
X_n\xrightarrow{P}X.
$$

Zeigen Sie:

$$
f(X_n)\xrightarrow{P}f(X).
$$

#### 解答

##### 中文解题思路

收敛题先认清目标符号：$\xrightarrow{P}$ 要证明偏离概率趋于 $0$，$\xrightarrow{D}$ 要看分布函数在连续点的极限。若表达式能拆成“一个分布收敛项 + 一个概率收敛到常数的项”，优先考虑 Slutsky。

收敛题先区分收敛类型：几乎处处、概率收敛、分布收敛和矩收敛不能随便互换。证明概率收敛时，目标通常是让 $\mathbb P(|X_n-X|>\varepsilon)$ 趋于 $0$；证明分布收敛时，则看分布函数在连续点的极限。

含 Slutsky 或连续映射的题，不要展开复杂分布。先把表达式拆成一个已知分布收敛项和一个依概率收敛到常数的项，再套 Slutsky 或连续映射定理。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

Dies ist die stetige Abbildungseigenschaft der Konvergenz in Wahrscheinlichkeit.

Sei $\varepsilon>0$. Wegen der Stetigkeit von $f$ ist $f$ lokal um Werte von $X$ kontrollierbar. Formal kann man über Teilfolgen argumentieren:

Aus jeder Teilfolge von $X_n$ besitzt man wegen $X_n\to X$ in Wahrscheinlichkeit eine weitere Teilfolge, die fast sicher gegen $X$ konvergiert.

Auf dieser weiteren Teilfolge folgt wegen Stetigkeit:

$$
f(X_{n_k})\to f(X)
$$

fast sicher und damit in Wahrscheinlichkeit.

Daraus folgt für die ursprüngliche Folge:

$$
f(X_n)\xrightarrow{P}f(X).
$$

---

---

### Aufgabe 16 - 判断并证明随机变量序列的收敛关系。

#### 题目

Sei $(X_n)_{n\in\mathbb N}$ eine Folge diskreter Zufallsvariablen mit

$$
\mathbb P(X_n=n)=\frac1n
$$

und

$$
\mathbb P(X_n=0)=1-\frac1n.
$$

###### (1)

Zeigen Sie:

$$
X_n\xrightarrow{P}0.
$$

#### 解答

##### 中文解题思路

收敛题先认清目标符号：$\xrightarrow{P}$ 要证明偏离概率趋于 $0$，$\xrightarrow{D}$ 要看分布函数在连续点的极限。若表达式能拆成“一个分布收敛项 + 一个概率收敛到常数的项”，优先考虑 Slutsky。

收敛题先区分收敛类型：几乎处处、概率收敛、分布收敛和矩收敛不能随便互换。证明概率收敛时，目标通常是让 $\mathbb P(|X_n-X|>\varepsilon)$ 趋于 $0$；证明分布收敛时，则看分布函数在连续点的极限。

含 Slutsky 或连续映射的题，不要展开复杂分布。先把表达式拆成一个已知分布收敛项和一个依概率收敛到常数的项，再套 Slutsky 或连续映射定理。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

Für jedes $\varepsilon>0$ gilt für alle hinreichend großen $n$ mit $n>\varepsilon$:

$$
\{|X_n-0|>\varepsilon\}=\{X_n=n\}.
$$

Also:

$$
\mathbb P(|X_n|>\varepsilon)
=
\mathbb P(X_n=n)
=
\frac1n
\to0.
$$

Damit:

$$
X_n\xrightarrow{P}0.
$$

###### (2)

Zeigen Sie:

$$
E[X_n]=1.
$$

###### Lösung

Es gilt:

$$
E[X_n]
=
n\cdot\frac1n
+0\cdot\left(1-\frac1n\right)
=
1.
$$

###### (3)

Folgern Sie:

$$
E[X_n]\not\to E[X].
$$

###### Lösung

Aus Teil (1) ist der Grenzwert in Wahrscheinlichkeit:

$$
X=0.
$$

Daher:

$$
E[X]=0.
$$

Aber:

$$
E[X_n]=1
$$

für alle $n$. Also:

$$
E[X_n]\to1\neq0=E[X].
$$

Konvergenz in Wahrscheinlichkeit allein impliziert also keine Konvergenz der Erwartungswerte.

---

### Aufgabe 17 - 判断并证明随机变量序列的收敛关系。

#### 题目

Sei $f:\mathbb R\to\mathbb R$ eine stetige Dichtefunktion. Seien $X_i\sim f$ iid. Für den Bandbreitenparameter $h>0$ definiere den Dichteschätzer mit uniformem Kern:

$$
\hat f_n(x)
=
\frac1n\sum_{i=1}^n
\frac1{2h}I_{\{|X_i-x|\leq h\}}.
$$

Sei $x\in\mathbb R$ fix.

###### (1)

Nutzen Sie das schwache Gesetz der großen Zahlen, um zu zeigen:

$$
\hat f_n(x)\xrightarrow{P}E[\hat f_n(x)].
$$

#### 解答

##### 中文解题思路

看到分布函数或密度，先检查对象类型：离散型看跳跃点概率，连续型看密度积分。分布函数要满足单调、右连续、极限从 $0$ 到 $1$；密度要非负且总积分为 $1$。

收敛题先认清目标符号：$\xrightarrow{P}$ 要证明偏离概率趋于 $0$，$\xrightarrow{D}$ 要看分布函数在连续点的极限。若表达式能拆成“一个分布收敛项 + 一个概率收敛到常数的项”，优先考虑 Slutsky。

大数定律题要把目标改写成样本均值，并检查 iid 与期望有限。满足条件后，样本均值依概率收敛到对应期望；若有函数 $g(X_i)$，就把 $g(X_i)$ 当作新的 iid 序列。

中心极限定理题的固定路线是：先算单个变量的均值和方差，再把和或均值标准化成标准正态形式，最后用标准正态分布近似概率。二项分布近似时要注意是否需要连续性修正。

收敛题先区分收敛类型：几乎处处、概率收敛、分布收敛和矩收敛不能随便互换。证明概率收敛时，目标通常是让 $\mathbb P(|X_n-X|>\varepsilon)$ 趋于 $0$；证明分布收敛时，则看分布函数在连续点的极限。

大数定律题要把目标改写成样本均值形式，然后检查 iid 和期望有限这两个条件。满足后直接得到样本均值依概率收敛到期望。

CLT/近似题的路线是先确定单个变量的均值 $\mu$ 和方差 $\sigma^2$，再把和或均值标准化。最后用标准正态分布近似概率，必要时注意二项分布的连续性修正。

含 Slutsky 或连续映射的题，不要展开复杂分布。先把表达式拆成一个已知分布收敛项和一个依概率收敛到常数的项，再套 Slutsky 或连续映射定理。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

Setze:

$$
Y_i=\frac1{2h}I_{\{|X_i-x|\leq h\}}.
$$

Dann sind die $Y_i$ iid und:

$$
\hat f_n(x)=\frac1n\sum_{i=1}^nY_i.
$$

Nach dem schwachen Gesetz der großen Zahlen:

$$
\frac1n\sum_{i=1}^nY_i
\xrightarrow{P}
E[Y_1].
$$

Da $E[\hat f_n(x)]=E[Y_1]$, folgt:

$$
\hat f_n(x)\xrightarrow{P}E[\hat f_n(x)].
$$

###### (2)

Nutzen Sie den zentralen Grenzwertsatz, um zu zeigen:

$$
\sqrt n(\hat f_n(x)-E[\hat f_n(x)])
\xrightarrow{D}
N(0,\operatorname{Var}(Y_1)).
$$

###### Lösung

Mit $Y_i$ wie oben gilt:

$$
\hat f_n(x)=\frac1n\sum_{i=1}^nY_i.
$$

Der zentrale Grenzwertsatz liefert:

$$
\sqrt n
\left(
\frac1n\sum_{i=1}^nY_i-E[Y_1]
\right)
\xrightarrow{D}
N(0,\operatorname{Var}(Y_1)).
$$

Also:

$$
\sqrt n(\hat f_n(x)-E[\hat f_n(x)])
\xrightarrow{D}
N(0,\operatorname{Var}(Y_1)).
$$

###### (3)

Berechnen Sie $E[\hat f_n(x)]$.

###### Lösung

Es gilt:

$$
E[\hat f_n(x)]
=
E[Y_1]
=
\frac1{2h}\mathbb P(|X_1-x|\leq h).
$$

Also:

$$
E[\hat f_n(x)]
=
\frac{F(x+h)-F(x-h)}{2h}.
$$

###### (4)

Berechnen Sie $\operatorname{Var}(\hat f_n(x))$.

###### Lösung

Setze:

$$
p_h=\mathbb P(|X_1-x|\leq h).
$$

Dann:

$$
Y_1=\frac1{2h}I_{\{|X_1-x|\leq h\}}.
$$

Also:

$$
\operatorname{Var}(Y_1)
=
\frac1{4h^2}p_h(1-p_h).
$$

Da $\hat f_n(x)$ Mittelwert von $n$ iid Variablen $Y_i$ ist:

$$
\operatorname{Var}(\hat f_n(x))
=
\frac1n\operatorname{Var}(Y_1)
=
\frac{p_h(1-p_h)}{4nh^2}.
$$

Mit $p_h=2hE[\hat f_n(x)]$:

$$
\operatorname{Var}(\hat f_n(x))
=
\frac{E[\hat f_n(x)](1-2hE[\hat f_n(x)])}{2nh}.
$$

###### (5)

###### Lösung

Der Bias ist:

$$
E[\hat f_n(x)]-f(x).
$$

Für kleines $h$ ist

$$
E[\hat f_n(x)]
=
\frac1{2h}\int_{x-h}^{x+h}f(u)\,du
$$

der lokale Mittelwert von $f$ um $x$. Für $h\to0$ konvergiert dieser wegen Stetigkeit gegen $f(x)$.

Kleines $h$ reduziert also den Bias.

Die Varianz enthält ungefähr den Faktor:

$$
\frac1{nh}.
$$

Kleines $h$ erhöht also die Varianz. Es gibt den typischen Bias-Varianz-Tradeoff.

---

---

### Aufgabe 18 - 判断并证明随机变量序列的收敛关系。

#### 题目

Sei $\Omega=\{0,1\}$ mit Potenzmenge als $\sigma$-Algebra und

$$
\mathbb P(\{0\})=\mathbb P(\{1\})=\frac12.
$$

Definiere $X_n,X:\Omega\to\mathbb R$ durch:

$$
X(1)=0,\quad X(0)=1,
$$

und:

$$
X_n(0)=0,\quad X_n(1)=1.
$$

###### (1)

Zeigen Sie:

$$
\mathbb P(X_n\leq t)=\mathbb P(X\leq t).
$$

#### 解答

##### 中文解题思路

看到分布函数或密度，先检查对象类型：离散型看跳跃点概率，连续型看密度积分。分布函数要满足单调、右连续、极限从 $0$ 到 $1$；密度要非负且总积分为 $1$。

收敛题先认清目标符号：$\xrightarrow{P}$ 要证明偏离概率趋于 $0$，$\xrightarrow{D}$ 要看分布函数在连续点的极限。若表达式能拆成“一个分布收敛项 + 一个概率收敛到常数的项”，优先考虑 Slutsky。

收敛题先区分收敛类型：几乎处处、概率收敛、分布收敛和矩收敛不能随便互换。证明概率收敛时，目标通常是让 $\mathbb P(|X_n-X|>\varepsilon)$ 趋于 $0$；证明分布收敛时，则看分布函数在连续点的极限。

含 Slutsky 或连续映射的题，不要展开复杂分布。先把表达式拆成一个已知分布收敛项和一个依概率收敛到常数的项，再套 Slutsky 或连续映射定理。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

Sowohl $X_n$ als auch $X$ nehmen die Werte $0$ und $1$ jeweils mit Wahrscheinlichkeit $\frac12$ an.

Damit haben beide dieselbe Verteilungsfunktion:

$$
F(t)=
\begin{cases}
0, & t<0,\\
\frac12, & 0\leq t<1,\\
1, & t\geq1.
\end{cases}
$$

Also:

$$
\mathbb P(X_n\leq t)=\mathbb P(X\leq t).
$$

###### (2)

Zeigen Sie:

$$
\mathbb P(|X_n-X|>\frac12)=1
$$

für alle $n$.

###### Lösung

Für $\omega=0$ gilt:

$$
X_n(0)=0,\quad X(0)=1.
$$

Für $\omega=1$ gilt:

$$
X_n(1)=1,\quad X(1)=0.
$$

Also:

$$
|X_n-X|=1
$$

für alle $\omega\in\Omega$. Daher:

$$
\mathbb P(|X_n-X|>\frac12)=1.
$$

###### (3)

Folgern Sie:

$$
X_n\xrightarrow{D}X,
\qquad
\text{aber}
\qquad
X_n\not\xrightarrow{P}X.
$$

###### Lösung

Da $X_n$ und $X$ für alle $n$ dieselbe Verteilung haben, gilt sofort:

$$
X_n\xrightarrow{D}X.
$$

Aber aus Teil (2):

$$
\mathbb P(|X_n-X|>\frac12)=1
$$

für alle $n$. Diese Wahrscheinlichkeit konvergiert nicht gegen $0$.

Also:

$$
X_n\not\xrightarrow{P}X.
$$

---

---

### Aufgabe 19 - 判断并证明随机变量序列的收敛关系。

#### 题目

Sei $(X_n)$ eine Folge von Zufallsvariablen mit

$$
X_n\xrightarrow{D}c,
$$

wobei $c\in\mathbb R$ konstant ist. Zeigen Sie:

$$
X_n\xrightarrow{P}c.
$$

#### 解答

##### 中文解题思路

收敛题先认清目标符号：$\xrightarrow{P}$ 要证明偏离概率趋于 $0$，$\xrightarrow{D}$ 要看分布函数在连续点的极限。若表达式能拆成“一个分布收敛项 + 一个概率收敛到常数的项”，优先考虑 Slutsky。

收敛题先区分收敛类型：几乎处处、概率收敛、分布收敛和矩收敛不能随便互换。证明概率收敛时，目标通常是让 $\mathbb P(|X_n-X|>\varepsilon)$ 趋于 $0$；证明分布收敛时，则看分布函数在连续点的极限。

含 Slutsky 或连续映射的题，不要展开复杂分布。先把表达式拆成一个已知分布收敛项和一个依概率收敛到常数的项，再套 Slutsky 或连续映射定理。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

Sei $\varepsilon>0$. Dann:

$$
\mathbb P(|X_n-c|>\varepsilon)
=
\mathbb P(X_n<c-\varepsilon)
+\mathbb P(X_n>c+\varepsilon).
$$

Da $X_n\xrightarrow{D}c$ und die Grenzverteilung die konstante Zufallsvariable $c$ ist, gilt an den Stetigkeitsstellen $c-\varepsilon$ und $c+\varepsilon$:

$$
\mathbb P(X_n\leq c-\varepsilon)\to0
$$

und:

$$
\mathbb P(X_n\leq c+\varepsilon)\to1.
$$

Also:

$$
\mathbb P(X_n>c+\varepsilon)\to0.
$$

Damit:

$$
\mathbb P(|X_n-c|>\varepsilon)\to0.
$$

Also:

$$
X_n\xrightarrow{P}c.
$$

---

---

### Aufgabe 20 - 判断并证明随机变量序列的收敛关系。

#### 题目

Sei $(X_n)$ eine Folge von Zufallsvariablen mit

$$
\sqrt n(X_n-E[X_n])\xrightarrow{D}X.
$$

Zeigen Sie:

$$
X_n-E[X_n]\xrightarrow{P}0.
$$

#### 解答

##### 中文解题思路

收敛题先认清目标符号：$\xrightarrow{P}$ 要证明偏离概率趋于 $0$，$\xrightarrow{D}$ 要看分布函数在连续点的极限。若表达式能拆成“一个分布收敛项 + 一个概率收敛到常数的项”，优先考虑 Slutsky。

收敛题先区分收敛类型：几乎处处、概率收敛、分布收敛和矩收敛不能随便互换。证明概率收敛时，目标通常是让 $\mathbb P(|X_n-X|>\varepsilon)$ 趋于 $0$；证明分布收敛时，则看分布函数在连续点的极限。

含 Slutsky 或连续映射的题，不要展开复杂分布。先把表达式拆成一个已知分布收敛项和一个依概率收敛到常数的项，再套 Slutsky 或连续映射定理。

写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。

Es gilt:

$$
X_n-E[X_n]
=
\frac1{\sqrt n}\cdot \sqrt n(X_n-E[X_n]).
$$

Nach Voraussetzung:

$$
\sqrt n(X_n-E[X_n])\xrightarrow{D}X.
$$

Außerdem:

$$
\frac1{\sqrt n}\to0.
$$

Mit Slutsky folgt:

$$
\frac1{\sqrt n}\cdot \sqrt n(X_n-E[X_n])
\xrightarrow{D}
0.
$$

Da der Grenzwert konstant ist, folgt aus Aufgabe 3:

$$
X_n-E[X_n]\xrightarrow{P}0.
$$

---

## 相关考试真题

### 真题 1（2012） - Aufgabe 4

#### 题目

Ein fairer Würfel werde $6000$-mal unabhängig geworfen. Bestimmen Sie für die Wahrscheinlichkeit, dass zwischen $900$-mal und $1100$-mal eine Sechs geworfen wird,

##### (a)

mit dem zentralen Grenzwertsatz eine Approximation.  
$(6\text{ Pkt.})$

##### (b)

mit der Tschebyscheff-Ungleichung eine untere Schranke.  
$(4\text{ Pkt.})$

**Hinweis zu (a):**  
Sie dürfen verwenden, dass für die Verteilungsfunktion $\Phi(x)$ der Standardnormalverteilung die Identität

$$
\Phi(-x)=1-\Phi(x)
\qquad \forall x\in \mathbb{R}
$$

sowie

$$
\Phi(3.46)\approx 0.9997
$$

gilt.

---

#### 解答

##### (a)

###### 中文解题思路

这是中心极限定理/极限分布题。先确认 $X_i$ 独立同分布且方差有限，再写出和变量的均值与方差；标准化以后直接用 CLT 得到收敛到 $N(0,1)$。

Zentraler Grenzwertsatz:

$$
\frac{\sum_{i=1}^n X_i-nE(X_i)}
{\sqrt{n}\cdot \sqrt{\operatorname{Var}(X_i)}}
\overset{a}{\sim}
\mathcal{N}(0,1)
$$

Hier:

$$
X_i\sim \mathcal{B}\left(\pi=\frac{1}{6}\right)
$$

mit

$$
E(X_i)=\pi=\frac{1}{6},
$$

$$
\operatorname{Var}(X_i)
=
\pi(1-\pi)
=
\frac{1}{6}\cdot \frac{5}{6}
=
\frac{5}{36}.
$$

Mit $n=6000$ folgt für den ZGWS:

$$
\frac{\sum_{i=1}^{6000}X_i-1000}
{\sqrt{6000}\cdot \sqrt{5/36}}
\overset{a}{\sim}
\mathcal{N}(0,1).
$$

Gesucht:

$$
P\left(
900<\sum_{i=1}^{6000}X_i<1100
\right).
$$

$$
\begin{aligned}
P\left(
900<\sum_{i=1}^{6000}X_i<1100
\right)
&=
P\left(
\sum_{i=1}^{6000}X_i<1100
\right)
-
P\left(
\sum_{i=1}^{6000}X_i\le 900
\right)
\\
&=
P\left(
\frac{\sum_{i=1}^{6000}X_i-1000}
{\sqrt{6000}\cdot \sqrt{5/36}}
<
\frac{1100-1000}
{\sqrt{6000}\cdot \sqrt{5/36}}
\right)
\\
&\quad -
P\left(
\frac{\sum_{i=1}^{6000}X_i-1000}
{\sqrt{6000}\cdot \sqrt{5/36}}
\le
\frac{900-1000}
{\sqrt{6000}\cdot \sqrt{5/36}}
\right)
\\
&=
\Phi(3.46)-\Phi(-3.46)
\\
&=
\Phi(3.46)-\left(1-\Phi(3.46)\right)
\\
&=
2\Phi(3.46)-1
\\
&=
2\cdot 0.9997-1
\\
&=
0.9994.
\end{aligned}
$$

##### (b)

###### 中文解题思路

把题目给出的均值、方差、协方差先列成公式，再用线性组合的期望方差规则；正态题最后标准化到 $N(0,1)$。

$$
Y=\sum_{i=1}^{6000}X_i
\sim
\mathcal{B}\left(n=6000,\pi=\frac{1}{6}\right)
$$

mit

$$
E(Y)=n\pi=1000,
$$

$$
\operatorname{Var}(Y)
=
n\pi(1-\pi)
=
\frac{2500}{3}.
$$

Tschebyscheff-Ungleichung:

$$
P(|Y-E(Y)|\ge c)
\le
\frac{\operatorname{Var}(Y)}{c^2}
$$

$$
\Longleftrightarrow
1-P(|Y-E(Y)|<c)
\le
\frac{\operatorname{Var}(Y)}{c^2}
$$

$$
\Longleftrightarrow
P(|Y-E(Y)|<c)
\ge
1-\frac{\operatorname{Var}(Y)}{c^2}
$$

Also:

$$
P(|Y-1000|<100)
=
P(900<Y<1100)
\ge
1-\frac{\frac{2500}{3}}{100^2}
=
0.9167.
$$

---

---

### 真题 2（2015） - Aufgabe 5: Rechenzeiten

#### 题目

Rechenzeit in Sekunden von $n=100$ Programmen auf einem Großrechner seien durch $100$ Zufallsvariablen

$$
X_1,\dots,X_{100}
$$

beschrieben, die stochastisch unabhängig und identisch verteilt sind mit

$$
E(X_i)=\mu
$$

und

$$
\operatorname{Var}(X_i)=100.
$$

a) Es wurde eine Gesamtrechenzeit der $100$ Programme von $1900$ Sekunden beobachtet.  
Basierend auf der Normalapproximation überprüfen Sie die Hypothese

$$
H_0:\mu=20
$$

gegen

$$
H_1:\mu \ne 20
$$

zum Niveau

$$
\alpha=0{,}1.
$$

b) Es sei nun $\mu=20$. Geben Sie für die Wahrscheinlichkeit, dass die Gesamtrechenzeit der $100$ Programme zwischen $1800$ und $2200$ Sekunden liegt, einen Näherungswert durch Anwendung des zentralen Grenzwertsatzes an.  
Verwenden Sie die Verteilungsfunktion der Standardnormalverteilung im Anhang.

---

#### 解答

##### 中文解题思路

先把题目给出的对象、要求证明或计算的量逐一标出来；然后选择对应的定义、定理或计算公式，最后把结果和题目要求逐项对应。

Für die Summe $S=\sum_{i=1}^{100}X_i$ gilt unter $H_0:\mu=20$:

$$
E(S)=100\cdot20=2000,\qquad
\operatorname{Var}(S)=100\cdot100=10000.
$$

Also:

$$
\frac{S-2000}{100}\approx N(0,1).
$$

Beobachtet wurde $S=1900$, also:

$$
z=\frac{1900-2000}{100}=-1.
$$

Für einen zweiseitigen Test zum Niveau $\alpha=0.1$ ist der kritische Bereich ungefähr

$$
|z|>1.645.
$$

Da $|-1|<1.645$, wird $H_0$ nicht verworfen.

Für $\mu=20$ und Durchschnitt $\bar X$ gilt:

$$
E(\bar X)=20,\qquad \operatorname{Var}(\bar X)=\frac{100}{100}=1.
$$

Also ist $\bar X$ näherungsweise normalverteilt mit

$$
\bar X\approx N(20,1).
$$

---

### 真题 3（Altklausur2LV） - Aufgabe 4 — 13 Punkte

#### 题目

Ein fairer Würfel werde $6000$-mal unabhängig geworfen.

Hinweis:

$$
\Phi(3.46)\approx0.9997
$$

##### (a)

Bestimmen Sie mit Hilfe des zentralen Grenzwertsatzes eine Approximation für die Wahrscheinlichkeit, dass zwischen $900$-mal und $1100$-mal eine Sechs geworfen wird.

##### (b)

Bestimmen Sie mit der Tschebyscheff-Ungleichung eine untere Schranke für die Wahrscheinlichkeit, dass zwischen $900$-mal und $1100$-mal eine Sechs geworfen wird.

#### 解答

###### (a) Bestimmen Sie mit Hilfe des zentralen Grenzwertsatzes eine Approximation für die Wahrscheinlichkeit, dass zwischen $900$-mal und $1100$-mal eine Sechs geworfen wird.

###### 中文解题思路

这是中心极限定理/极限分布题。先确认 $X_i$ 独立同分布且方差有限，再写出和变量的均值与方差；标准化以后直接用 CLT 得到收敛到 $N(0,1)$。

Zentraler Grenzwertsatz:

$$
\frac{\sum_{i=1}^{n}X_i-nE(X_i)}{\sqrt n\sqrt{\operatorname{Var}(X_i)}}\overset{a}{\sim}\mathcal N(0,1)
$$

Hier gilt:

$$
X_i\sim \mathcal B\left(\pi=\frac16\right)
$$

also

$$
E(X_i)=\pi=\frac16
$$

und

$$
\operatorname{Var}(X_i)=\pi(1-\pi)=\frac16\cdot\frac56=\frac5{36}.
$$

Mit $n=6000$ folgt:

$$
\frac{\sum_{i=1}^{6000}X_i-1000}{\sqrt{6000}\sqrt{5/36}}\overset{a}{\sim}\mathcal N(0,1).
$$

Gesucht ist:

$$
P\left(900<\sum_{i=1}^{6000}X_i<1100\right).
$$

Nun:

$$
\begin{aligned}
P\left(900<\sum_{i=1}^{6000}X_i<1100\right)
&=P\left(\sum_{i=1}^{6000}X_i<1100\right)-P\left(\sum_{i=1}^{6000}X_i\le900\right)\\
&=P\left(\frac{\sum_{i=1}^{6000}X_i-1000}{\sqrt{6000}\sqrt{5/36}}<\frac{1100-1000}{\sqrt{6000}\sqrt{5/36}}\right)\\
&\quad-P\left(\frac{\sum_{i=1}^{6000}X_i-1000}{\sqrt{6000}\sqrt{5/36}}\le\frac{900-1000}{\sqrt{6000}\sqrt{5/36}}\right)\\
&=\Phi(3.46)-\Phi(-3.46)\\
&=\Phi(3.46)-\left(1-\Phi(3.46)\right)\\
&=2\Phi(3.46)-1\\
&=2\cdot0.9997-1\\
&=0.9994.
\end{aligned}
$$

---

###### (b) Bestimmen Sie mit der Tschebyscheff-Ungleichung eine untere Schranke für die Wahrscheinlichkeit, dass zwischen $900$-mal und $1100$-mal eine Sechs geworfen wird.

###### 中文解题思路

这一步先识别极限定理的适用条件：是否独立同分布、是否有有限期望/方差、样本量是否足够大。若是样本和或样本均值，先算均值和方差，再标准化到近似标准正态。

Sei

$$
Y=\sum_{i=1}^{6000}X_i.
$$

Dann gilt:

$$
Y\sim \mathcal B\left(n=6000,\pi=\frac16\right)
$$

mit

$$
E(Y)=n\pi=1000
$$

und

$$
\operatorname{Var}(Y)=n\pi(1-\pi)=\frac{2500}{3}.
$$

Tschebyscheff-Ungleichung:

$$
P(|Y-E(Y)|\ge c)\le\frac{\operatorname{Var}(Y)}{c^2}
$$

Daraus folgt:

$$
P(|Y-E(Y)|<c)\ge1-\frac{\operatorname{Var}(Y)}{c^2}.
$$

Mit $c=100$:

$$
P(|Y-1000|<100)=P(900<Y<1100)
$$

$$
\ge1-\frac{2500/3}{100^2}
=1-\frac{2500}{30000}
=1-\frac1{12}
=\frac{11}{12}
\approx0.9167.
$$

---

---

### 真题 4（GOP-Klausur-1） - Aufgabe 7 -- 12 Punkte

#### 题目

Prof. S. nimmt täglich, also $n=225$-mal, den Bus zur Universität und ist immer pünktlich an der Bushaltestelle. Der Bus verspätet sich jedoch jeden Tag. Bezeichne $X_i$ die zufällige Zeitdauer der Verspätung in Minuten am Tag $i$. Nehmen Sie an, dass $X_i$, $i=1,\dots,n$, unabhängig und identisch exponentialverteilt sind mit $E(X_i)=1$.

Betrachten Sie die Zufallsgröße:

$$
X=\sum_{i=1}^n X_i
$$

also die aufsummierte Verspätung in einem Jahr.

##### (a)

Zeigen Sie, dass $X$ approximativ normalverteilt ist. Wie lauten approximativer Erwartungswert und approximative Varianz?

##### (b)

Bestimmen Sie approximativ die Wahrscheinlichkeit dafür, dass Prof. S. über das Jahr gesehen mehr als $4$ Stunden auf den Bus wartet.

Hinweis:

$$
\Phi(0.5)\approx 0.6915,\quad
\Phi(1)\approx 0.8413,\quad
\Phi(2)\approx 0.9772
$$

#### 解答

###### (a) Zeigen Sie, dass $X$ approximativ normalverteilt ist. Wie lauten approximativer Erwartungswert und approximative Varianz?

###### 中文解题思路

这是中心极限定理/极限分布题。先确认 $X_i$ 独立同分布且方差有限，再写出和变量的均值与方差；标准化以后直接用 CLT 得到收敛到 $N(0,1)$。

Da:

$$
E(X_i)=\mu=1=\frac{1}{\lambda}
$$

gilt:

$$
\lambda=1
$$

und damit:

$$
\operatorname{Var}(X_i)=\frac{1}{\lambda^2}=1=\sigma^2
$$

Da die $X_i$ unabhängig und identisch verteilt sind, folgt mit dem zentralen Grenzwertsatz:

$$
\frac{X-n\mu}{\sigma\sqrt n}\xrightarrow{a}N(0,1)
$$

Also approximativ:

$$
X\approx N(n\mu,n\sigma^2)
$$

Mit $n=225$, $\mu=1$ und $\sigma^2=1$ folgt:

$$
X\approx N(225,225)
$$

Der approximative Erwartungswert ist:

$$
\mu_X=n\mu=225
$$

Die approximative Varianz ist:

$$
\sigma_X^2=n\sigma^2=225
$$

###### (b) Bestimmen Sie approximativ die Wahrscheinlichkeit dafür, dass Prof. S. über das Jahr gesehen mehr als $4$ Stunden auf den Bus wartet.

###### 中文解题思路

这一步先识别极限定理的适用条件：是否独立同分布、是否有有限期望/方差、样本量是否足够大。若是样本和或样本均值，先算均值和方差，再标准化到近似标准正态。

Von Interesse ist:

$$
P(X>4\cdot 60)=P(X>240)
$$

Mit $\sigma_X=\sqrt{225}=15$:

$$
P(X>240)
=
1-P(X\leq 240)
$$

$$
=
1-P\left(
\frac{X-\mu_X}{\sigma_X}
\leq
\frac{240-225}{15}
\right)
$$

$$
=
1-\Phi(1)
$$

Also:

$$
P(X>240)\approx 1-0.8413=0.1587
$$

Gerundet:

$$
P(X>240)\approx 0.16
$$

---

---

### 真题 5（GOP-Klausur-2） - Aufgabe 4 — 13 Punkte

#### 题目

Ein fairer Würfel werde $6000$-mal unabhängig geworfen.

Hinweis:

$$
\Phi(3.46)\approx 0.9997
$$

---

##### (a)

Bestimmen Sie mit Hilfe des zentralen Grenzwertsatzes eine Approximation für die Wahrscheinlichkeit, dass zwischen $900$-mal und $1100$-mal eine Sechs geworfen wird.

##### (b)

Bestimmen Sie mit der Tschebyscheff-Ungleichung eine untere Schranke für die Wahrscheinlichkeit, dass zwischen $900$-mal und $1100$-mal eine Sechs geworfen wird.

#### 解答

###### (a) Bestimmen Sie mit Hilfe des zentralen Grenzwertsatzes eine Approximation für die Wahrscheinlichkeit, dass zwischen $900$-mal und $1100$-mal eine Sechs geworfen wird.

###### 中文解题思路

这是中心极限定理/极限分布题。先确认 $X_i$ 独立同分布且方差有限，再写出和变量的均值与方差；标准化以后直接用 CLT 得到收敛到 $N(0,1)$。

Sei $X$ die Anzahl der geworfenen Sechsen.

Dann gilt:

$$
X\sim \operatorname{Bin}(n,p)
$$

mit

$$
n=6000
$$

und

$$
p=\frac{1}{6}
$$

Damit:

$$
E(X)=np=6000\cdot \frac{1}{6}=1000
$$

Die Varianz ist:

$$
\operatorname{Var}(X)=np(1-p)
$$

Also:

$$
\operatorname{Var}(X)=6000\cdot \frac{1}{6}\cdot \frac{5}{6}
$$

$$
\operatorname{Var}(X)=1000\cdot \frac{5}{6}=\frac{5000}{6}\approx 833.33
$$

Die Standardabweichung ist:

$$
\sigma=\sqrt{833.33}\approx 28.87
$$

Mit dem zentralen Grenzwertsatz:

$$
X\approx N(1000,833.33)
$$

Gesucht ist:

$$
P(900\leq X\leq 1100)
$$

Standardisieren:

$$
P(900\leq X\leq 1100)
=
P\left(
\frac{900-1000}{28.87}
\leq Z \leq
\frac{1100-1000}{28.87}
\right)
$$

Also:

$$
P(900\leq X\leq 1100)
=
P(-3.46\leq Z\leq 3.46)
$$

Daher:

$$
P(-3.46\leq Z\leq 3.46)
=
\Phi(3.46)-\Phi(-3.46)
$$

Wegen Symmetrie:

$$
\Phi(-3.46)=1-\Phi(3.46)
$$

Also:

$$
P(-3.46\leq Z\leq 3.46)
=
2\Phi(3.46)-1
$$

Mit

$$
\Phi(3.46)\approx 0.9997
$$

folgt:

$$
P(900\leq X\leq 1100)
\approx 2\cdot 0.9997-1
=
0.9994
$$

---

###### (b) Bestimmen Sie mit der Tschebyscheff-Ungleichung eine untere Schranke für die Wahrscheinlichkeit, dass zwischen $900$-mal und $1100$-mal eine Sechs geworfen wird.

###### 中文解题思路

这一步先识别极限定理的适用条件：是否独立同分布、是否有有限期望/方差、样本量是否足够大。若是样本和或样本均值，先算均值和方差，再标准化到近似标准正态。

Wir haben:

$$
E(X)=1000
$$

und

$$
\operatorname{Var}(X)=\frac{5000}{6}\approx 833.33
$$

Gesucht ist:

$$
P(900\leq X\leq 1100)
$$

Das ist:

$$
P(|X-1000|\leq 100)
$$

Nach Tschebyscheff gilt:

$$
P(|X-\mu|\geq a)\leq \frac{\operatorname{Var}(X)}{a^2}
$$

Also:

$$
P(|X-\mu|<a)\geq 1-\frac{\operatorname{Var}(X)}{a^2}
$$

Mit $a=100$:

$$
P(|X-1000|\leq 100)
\geq
1-\frac{833.33}{100^2}
$$

Also:

$$
P(|X-1000|\leq 100)
\geq
1-\frac{833.33}{10000}
$$

$$
=
1-0.08333
=
0.91667
$$

Damit:

$$
P(900\leq X\leq 1100)\geq 0.917
$$

---

---

### 真题 6（GOP-Klausur-3） - Aufgabe 4 - 13 Punkte

#### 题目

Ein fairer Würfel werde $6000$-mal unabhängig geworfen.

Hinweis:

$$
\Phi(3.46)\approx 0.9997
$$

---

##### (a)

Bestimmen Sie mit Hilfe des zentralen Grenzwertsatzes eine Approximation für die Wahrscheinlichkeit, dass zwischen $900$-mal und $1100$-mal eine Sechs geworfen wird.

##### (b)

Bestimmen Sie mit der Tschebyscheff-Ungleichung eine untere Schranke für die Wahrscheinlichkeit, dass zwischen $900$-mal und $1100$-mal eine Sechs geworfen wird.

#### 解答

###### (a) Bestimmen Sie mit Hilfe des zentralen Grenzwertsatzes eine Approximation für die Wahrscheinlichkeit, dass zwischen $900$-mal und $1100$-mal eine Sechs geworfen wird.

###### 中文解题思路

这是中心极限定理/极限分布题。先确认 $X_i$ 独立同分布且方差有限，再写出和变量的均值与方差；标准化以后直接用 CLT 得到收敛到 $N(0,1)$。

Sei $X$ die Anzahl der geworfenen Sechsen.

Dann gilt:

$$
X\sim \operatorname{Bin}(n,p)
$$

mit

$$
n=6000
$$

und

$$
p=\frac{1}{6}
$$

Damit:

$$
E(X)=np=6000\cdot \frac{1}{6}=1000
$$

Die Varianz ist:

$$
\operatorname{Var}(X)=np(1-p)
$$

Also:

$$
\operatorname{Var}(X)=6000\cdot \frac{1}{6}\cdot \frac{5}{6}
$$

$$
\operatorname{Var}(X)=1000\cdot \frac{5}{6}=\frac{5000}{6}\approx 833.33
$$

Die Standardabweichung ist:

$$
\sigma=\sqrt{833.33}\approx 28.87
$$

Mit dem zentralen Grenzwertsatz:

$$
X\approx N(1000,833.33)
$$

Gesucht ist:

$$
P(900\leq X\leq 1100)
$$

Standardisieren:

$$
P(900\leq X\leq 1100)
=
P\left(
\frac{900-1000}{28.87}
\leq Z \leq
\frac{1100-1000}{28.87}
\right)
$$

Also:

$$
P(900\leq X\leq 1100)
=
P(-3.46\leq Z\leq 3.46)
$$

Daher:

$$
P(-3.46\leq Z\leq 3.46)
=
\Phi(3.46)-\Phi(-3.46)
$$

Wegen Symmetrie:

$$
\Phi(-3.46)=1-\Phi(3.46)
$$

Also:

$$
P(-3.46\leq Z\leq 3.46)
=
2\Phi(3.46)-1
$$

Mit

$$
\Phi(3.46)\approx 0.9997
$$

folgt:

$$
P(900\leq X\leq 1100)
\approx 2\cdot 0.9997-1
=
0.9994
$$

---

###### (b) Bestimmen Sie mit der Tschebyscheff-Ungleichung eine untere Schranke für die Wahrscheinlichkeit, dass zwischen $900$-mal und $1100$-mal eine Sechs geworfen wird.

###### 中文解题思路

这一步先识别极限定理的适用条件：是否独立同分布、是否有有限期望/方差、样本量是否足够大。若是样本和或样本均值，先算均值和方差，再标准化到近似标准正态。

Wir haben:

$$
E(X)=1000
$$

und

$$
\operatorname{Var}(X)=\frac{5000}{6}\approx 833.33
$$

Gesucht ist:

$$
P(900\leq X\leq 1100)
$$

Das ist:

$$
P(|X-1000|\leq 100)
$$

Nach Tschebyscheff gilt:

$$
P(|X-\mu|\geq a)\leq \frac{\operatorname{Var}(X)}{a^2}
$$

Also:

$$
P(|X-\mu|<a)\geq 1-\frac{\operatorname{Var}(X)}{a^2}
$$

Mit $a=100$:

$$
P(|X-1000|\leq 100)
\geq
1-\frac{833.33}{100^2}
$$

Also:

$$
P(|X-1000|\leq 100)
\geq
1-\frac{833.33}{10000}
$$

$$
=
1-0.08333
=
0.91667
$$

Damit:

$$
P(900\leq X\leq 1100)\geq 0.917
$$

---

---

### 真题 7（Konvergenz） - Aufgabe 1 — 21 Punkte

#### 题目

Betrachten Sie eine Münze, die beim Münzwurf mit unbekannter Wahrscheinlichkeit $p\in(0,1)$ Zahl anzeigt und dementsprechend mit Wahrscheinlichkeit $1-p$ Kopf.

Es bezeichne $X$ die Anzahl an Würfen, die nötig ist, bis das erste Mal Zahl erscheint. Das Experiment werde $n=200$ mal wiederholt, d.h. $X_i$ bezeichnet die Anzahl der benötigten Würfe, bis das erste Mal Zahl erscheint, bei der $i$-ten Wiederholung des Experiments.

Mit

$$
\overline X
=
\frac{1}{200}\sum_{i=1}^{200}X_i
$$

wird die durchschnittlich benötigte Anzahl an Versuchen bezeichnet.

---

##### (a)

Bestimmen Sie eine approximative Verteilung für $\overline X$.

##### (b)

Wie muss $p$ gewählt werden, damit mit einer Wahrscheinlichkeit von mindestens $0.9$ folgendes gilt:

$$
\overline X
$$

weicht betragsmäßig vom unbekannten Erwartungswert $E(X_i)$ um höchstens $0.1645$ ab?

Hinweis: Das $0.95$-Quantil der Standardnormalverteilung ist $1.645$, d.h. für $Z\sim \mathcal N(0,1)$ gilt

$$
P(Z\le 1.645)=0.95.
$$

##### (c)

Bestimmen Sie eine approximative Verteilung für $\overline X^2$.

#### 解答

###### (a) Bestimmen Sie eine approximative Verteilung für $\overline X$.

###### 中文解题思路

这是中心极限定理/极限分布题。先确认 $X_i$ 独立同分布且方差有限，再写出和变量的均值与方差；标准化以后直接用 CLT 得到收敛到 $N(0,1)$。

Da $X_i$ die Anzahl der Würfe bis zum ersten Auftreten von Zahl beschreibt, gilt

$$
X_i\sim \operatorname{Geom}(p).
$$

In der hier verwendeten Parametrisierung gilt:

$$
E(X_i)=\mu=\frac{1}{p}
$$

und

$$
\operatorname{Var}(X_i)=\sigma^2=\frac{1-p}{p^2}.
$$

Da die Experimente unabhängig wiederholt werden und

$$
\operatorname{Var}(X_i)<\infty
$$

gilt, kann der zentrale Grenzwertsatz angewendet werden.

Für

$$
n=200
$$

gilt approximativ:

$$
\overline X
\approx
\mathcal N\left(
\mu,\frac{\sigma^2}{n}
\right).
$$

Also:

$$
\overline X
\approx
\mathcal N\left(
\frac{1}{p},
\frac{1-p}{200p^2}
\right).
$$

Äquivalent:

$$
\sqrt{200}\left(\overline X-\frac{1}{p}\right)
\approx
\mathcal N\left(
0,
\frac{1-p}{p^2}
\right).
$$

---

###### (b) Wie muss $p$ gewählt werden, damit mit einer Wahrscheinlichkeit von mindestens $0.9$ folgendes gilt:

###### 中文解题思路

这是用中心极限定理反推参数范围。先把 $|\overline X-\mu|\le x$ 标准化成标准正态区间，再利用双侧 $90\%$ 对应 $0.95$ 分位数 $1.645$，最后把不等式化成关于 $p$ 的二次不等式。

Gesucht ist, dass

$$
P\left(
\left|\overline X-\mu\right|\le 0.1645
\right)
\ge 0.9,
$$

wobei

$$
\mu=E(X_i)=\frac{1}{p}.
$$

Setze

$$
x=0.1645.
$$

Nach Teil (a) gilt näherungsweise:

$$
\frac{\overline X-\mu}{\sigma/\sqrt n}
\approx
\mathcal N(0,1),
$$

mit

$$
\sigma^2=\frac{1-p}{p^2}.
$$

Damit:

$$
P\left(
\left|\overline X-\mu\right|\le x
\right)
=
P\left(
-x\le \overline X-\mu\le x
\right).
$$

Standardisieren:

$$
P\left(
-\frac{x\sqrt n}{\sigma}
\le
\frac{\sqrt n(\overline X-\mu)}{\sigma}
\le
\frac{x\sqrt n}{\sigma}
\right).
$$

Approximativ ist dies

$$
\Phi\left(\frac{x\sqrt n}{\sigma}\right)
-
\Phi\left(-\frac{x\sqrt n}{\sigma}\right).
$$

Wegen Symmetrie der Standardnormalverteilung:

$$
\Phi\left(\frac{x\sqrt n}{\sigma}\right)
-
\Phi\left(-\frac{x\sqrt n}{\sigma}\right)
=
2\Phi\left(\frac{x\sqrt n}{\sigma}\right)-1.
$$

Gefordert ist also:

$$
2\Phi\left(\frac{x\sqrt n}{\sigma}\right)-1
\ge 0.9.
$$

Daraus folgt:

$$
\Phi\left(\frac{x\sqrt n}{\sigma}\right)
\ge 0.95.
$$

Mit dem Hinweis:

$$
\frac{x\sqrt n}{\sigma}
\ge
1.645.
$$

Quadrieren liefert:

$$
\frac{x^2 n}{\sigma^2}
\ge
1.645^2.
$$

Äquivalent:

$$
\frac{x^2 n}{1.645^2}
\ge
\sigma^2.
$$

Da

$$
\sigma^2=\frac{1-p}{p^2},
$$

folgt:

$$
\frac{x^2 n}{1.645^2}
\ge
\frac{1-p}{p^2}.
$$

Nun ist

$$
x=0.1645,
\qquad
n=200.
$$

Also:

$$
\frac{x^2n}{1.645^2}
=
\frac{0.1645^2\cdot 200}{1.645^2}.
$$

Da

$$
0.1645=\frac{1.645}{10},
$$

gilt

$$
0.1645^2=\frac{1.645^2}{100}.
$$

Somit:

$$
\frac{0.1645^2\cdot 200}{1.645^2}
=
\frac{200}{100}
=
2.
$$

Also muss gelten:

$$
2\ge \frac{1-p}{p^2}.
$$

Dies ist äquivalent zu

$$
2p^2\ge 1-p.
$$

Also:

$$
2p^2+p-1\ge 0.
$$

Faktorisieren:

$$
2p^2+p-1
=
(2p-1)(p+1).
$$

Damit:

$$
(2p-1)(p+1)\ge 0.
$$

Da

$$
p\in(0,1)
$$

gilt stets

$$
p+1>0.
$$

Also muss gelten:

$$
2p-1\ge 0.
$$

Damit:

$$
p\ge \frac{1}{2}.
$$

Also muss die Erfolgswahrscheinlichkeit mindestens

$$
\boxed{p\ge \frac{1}{2}}
$$

sein.

---

###### (c) Bestimmen Sie eine approximative Verteilung für $\overline X^2$.

###### 中文解题思路

这是中心极限定理/极限分布题。先确认 $X_i$ 独立同分布且方差有限，再写出和变量的均值与方差；标准化以后直接用 CLT 得到收敛到 $N(0,1)$。

Nach Teil (a) gilt approximativ:

$$
\overline X
\approx
\mathcal N\left(
\frac{1}{p},
\frac{1-p}{np^2}
\right).
$$

Äquivalent gilt nach dem zentralen Grenzwertsatz:

$$
\sqrt n\left(\overline X-\frac{1}{p}\right)
\approx
\mathcal N\left(
0,
\frac{1-p}{p^2}
\right).
$$

Gesucht ist eine approximative Verteilung von

$$
\overline X^2.
$$

Dafür verwenden wir die Delta-Methode mit

$$
f(x)=x^2.
$$

Dann ist

$$
f'(x)=2x.
$$

Für

$$
\mu=\frac{1}{p}
$$

gilt also:

$$
f'(\mu)
=
2\mu
=
\frac{2}{p}.
$$

Nach der Delta-Methode:

$$
\sqrt n
\left(
f(\overline X)-f(\mu)
\right)
\approx
\mathcal N\left(
0,
\left[f'(\mu)\right]^2\sigma^2
\right),
$$

wobei

$$
\sigma^2=\frac{1-p}{p^2}.
$$

Also:

$$
\sqrt n
\left(
\overline X^2-\frac{1}{p^2}
\right)
\approx
\mathcal N\left(
0,
\left(\frac{2}{p}\right)^2
\frac{1-p}{p^2}
\right).
$$

Damit:

$$
\sqrt n
\left(
\overline X^2-\frac{1}{p^2}
\right)
\approx
\mathcal N\left(
0,
\frac{4(1-p)}{p^4}
\right).
$$

Folglich:

$$
\overline X^2
\approx
\mathcal N\left(
\frac{1}{p^2},
\frac{4(1-p)}{np^4}
\right).
$$

Für

$$
n=200
$$

ergibt sich:

$$
\overline X^2
\approx
\mathcal N\left(
\frac{1}{p^2},
\frac{4(1-p)}{200p^4}
\right).
$$

Also:

$$
\boxed{
\overline X^2
\approx
\mathcal N\left(
\frac{1}{p^2},
\frac{1-p}{50p^4}
\right)
}
$$

---

### 真题 8（ss2022） - Aufgabe 7 -- Zentraler Grenzwertsatz

#### 题目

Gegeben:

$$
X_i\sim \operatorname{Exp}(\lambda)
$$

mit:

$$
E(X_i)=1
$$

Für die Exponentialverteilung gilt:

$$
E(X_i)=\frac{1}{\lambda}
$$

Also:

$$
\lambda=1
$$

und:

$$
\operatorname{Var}(X_i)=\frac{1}{\lambda^2}=1
$$

Es gilt:

$$
X=\sum_{i=1}^{225}X_i
$$

###### (a)

Approximation durch Normalverteilung.

###### (b)

Wahrscheinlichkeit für mehr als $4$ Stunden Wartezeit.

#### 解答

Gegeben:

$$
X_i\sim \operatorname{Exp}(\lambda)
$$

mit:

$$
E(X_i)=1
$$

Für die Exponentialverteilung gilt:

$$
E(X_i)=\frac{1}{\lambda}
$$

Also:

$$
\lambda=1
$$

und:

$$
\operatorname{Var}(X_i)=\frac{1}{\lambda^2}=1
$$

Es gilt:

$$
X=\sum_{i=1}^{225}X_i
$$

##### (a) Approximation durch Normalverteilung

###### 中文解题思路

这是中心极限定理/极限分布题。先确认 $X_i$ 独立同分布且方差有限，再写出和变量的均值与方差；标准化以后直接用 CLT 得到收敛到 $N(0,1)$。

Da die $X_i$ unabhängig und identisch verteilt sind und endliche Varianz haben, gilt nach dem zentralen Grenzwertsatz:

$$
X\approx N(n\mu,n\sigma^2)
$$

mit:

$$
n=225,
\qquad
\mu=1,
\qquad
\sigma^2=1
$$

Also:

$$
X\approx N(225,225)
$$

Approximativer Erwartungswert:

$$
E(X)\approx 225
$$

Approximative Varianz:

$$
\operatorname{Var}(X)\approx 225
$$

##### (b) Wahrscheinlichkeit für mehr als $4$ Stunden Wartezeit

###### 中文解题思路

这一步先识别极限定理的适用条件：是否独立同分布、是否有有限期望/方差、样本量是否足够大。若是样本和或样本均值，先算均值和方差，再标准化到近似标准正态。

$4$ Stunden sind:

$$
4\cdot 60=240
$$

Gesucht:

$$
P(X>240)
$$

Standardabweichung:

$$
\sigma_X=\sqrt{225}=15
$$

Standardisieren:

$$
P(X>240)
=
1-P(X\leq 240)
$$

$$
=
1-P\left(
\frac{X-225}{15}
\leq
\frac{240-225}{15}
\right)
$$

$$
=
1-P(Z\leq 1)
$$

Mit:

$$
\Phi(1)\approx 0.84
$$

folgt:

$$
P(X>240)\approx 1-0.84=0.16
$$

---

---
