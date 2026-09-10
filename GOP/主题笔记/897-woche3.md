
#### 1

随机变量 X ∈ {0,1,2} 和 Y ∈ {−1,0,2} 具有如下联合概率质量函数：

| pX,Y(x,y) | Y = −1 | Y = 0 | Y = 2 | pX(x) |
| --------- | ------ | ----- | ----- | ----- |
| X = 0     | 0.30   | 0.20  | 0     |       |
| X = 1     | 0.10   | 0.15  | 0.05  |       |
| X = 2     | 0      | 0.05  | 0.15  |       |
| pY(y)     |        |       |       |       |

1. 补全 X 和 Y 的边缘分布。


| pX,Y(x,y) | Y = −1 | Y = 0 | Y = 2 | pX(x) |
| --------- | ------ | ----- | ----- | ----- |
| X = 0     | 0.30   | 0.20  | 0     | 0.5   |
| X = 1     | 0.10   | 0.15  | 0.05  | 0.3   |
| X = 2     | 0      | 0.05  | 0.15  | 0.2   |
| pY(y)     | 0.4    | 0.4   | 0.2   | 1     |


2. 求给定 X = 0 条件下 Y 的条件分布，并用一句话解释 P(Y = 0 | X = 0) 的含义。

	- F(Y = y|X =0):
		- 0, y < -1
		- 0.6, [-1, 0)
		- 1, y >= 0
	- X = 0 且 Y = 0 时候的联合概率

3. X 和 Y 是否随机独立？请用表格中合适的单元格，尽可能简短地给出理由。

	- P(X=0,Y=0) = 0.3
	- P(X=0)=0.5
	- P(Y=0) = 0.4
	- P(X=0,Y=0) != P(X=0)P(Y=0)
	- 不独立

4. 计算 E(X)、E(Y)、Var(X)、Var(Y)、Cov(X,Y) 和 Corr(X,Y)

	- E(X) = 0 x 0.5 + 1 x 0.3 + 2 x 0.2 = 0.7
	- E(X^2) = 0 x 0.5 + 1 x 0.3 + 4 x 0.2 = 1.1
	- Var(X) = 1.1  - 0.7^2 = 0.61
	- E(Y) = -1 x 0.4 + 0 x 0.4 + 2 x 0.2 = 0
	- E(Y^2) = 1 x 0.4 + 0 x 0.4 + 4 x 0.2 = 1.2
	- Var(Y) = 1.2 - 0 = 1.2

	- **E(XY) = -1 x 0.1 + 2 x 0.05 + 4 x 0.15 = 0.6**   -- 这个的解法
	- Cov(XY) = E(XY) - E(X)E(Y) = 0.6 - 0.7 x 0 = 0.6
	- Corr(X,Y) = Cov(XY) / \sqrt(Var(X)Var(Y)) = 0.6 / sqrt{0.61 x 1.2} = 0.701

- **注意**：**题目给的是联合PMF，正好加起来= 1**，

5. 解释相关系数的符号和量级。为什么这个值不能完整描述联合分布？

	- [-1,1]
	- 存在明显的**正线性相关**关系。
	- 但相关系数既 **不包含各个概率**，**也不包含联合分布的非线性结构或其他结构**。
	- Es besteht ein deutlicher positiver linearer Zusammenhang. Die Korrelation enthält aber weder die einzelnen Wahrscheinlichkeiten noch nichtlineare oder sonstige Struktur der gemeinsamen Verteilung

#### 2

设 $c > 0$，联合密度函数为：
$$ f_{X,Y}(x,y) = c\,(1 + 2xy) \cdot \mathbb{I}_{[0,1]^2}(x,y) $$
其中 $\mathbb{I}_{[0,1]^2}(x,y)$ 表示在单位正方形 $[0,1]\times[0,1]$ 上取值为 1，否则为 0。
1. 确定常数 $c$，使得 $f_{X,Y}$ 成为合法的联合密度函数。

	- 积分 = 1，得到 c = 2/3

2. 计算边缘密度 $f_X$ 和 $f_Y$，并分别验证其积分为 1。

	- 单边积分得到两个边缘密度
	- 边缘密度在定义域积分得到 1

3. 求条件密度 $f_{X|Y}(x \mid y)$（$0 \le y \le 1$）。当 $y$ 增大时，条件密度如何变化？

	- f_X|Y(x|y) = f(x,y)/f(y) = ....
	- 整理得到一个线性函数，系数是  2y/1+y（斜率）化简得到 2（1 - 1/(1+y))
	- y增大，1/（1+y） 减少， 2（1 - 1/(1+y)) 增大，**密度函数更加 右陡 **

4. 证明 $X$ 和 $Y$ 不独立。

	- 边缘密度乘积看看是否等于联合密度
	- 直观看上去不等于（无法拆解一个只有x，一个只有y）

5. 计算 $E(X)$、$E(Y)$、$E(XY)$、$Cov(X,Y)$ 和 $Corr(X,Y)$。

	- 正常计算



**提示**：由于联合密度具有对称性，许多积分只需计算一次。


#### 3

设 $X \sim \text{Bernoulli}(1/2)$ 和 $Y \sim \text{Bernoulli}(1/2)$ 始终成立，但联合分布不同。考虑以下**三种模型**：

| 模型       | 正相关结构                   | 独立结构                       | 负相关结构                   |
| -------- | ----------------------- | -------------------------- | ----------------------- |
| **概率质量** | $P(0,0) = P(1,1) = 1/2$ | $P(x,y) = 1/4$ 对所有 $(x,y)$ | $P(0,1) = P(1,0) = 1/2$ |
| **其他组合** | 概率为 0                   | —                          | 概率为 0                   |

1. 对每个模型列出完整的 2×2 联合分布表，并验证所给出的边缘分布。

**正相关**

|       | Y = 0 | Y = 1 |     |
| ----- | ----- | ----- | --- |
| X = 0 | 1/2   | 0     | 1/2 |
| X = 1 | 0     | 1/2   | 1/2 |
|       | 1/2   | 1/2   | 1   |
**负相关**

|       | Y = 0 | Y = 1 |     |
| ----- | ----- | ----- | --- |
| X = 0 | 0     | 1/2   | 1/2 |
| X = 1 | 1/2   | 0     | 1/2 |
|       | 1/2   | 1/2   | 1   |
**独立**

|       | Y = 0 | Y = 1 |     |
| ----- | ----- | ----- | --- |
| X = 0 | 1/4   | 1/4   | 1/2 |
| X = 1 | 1/4   | 1/4   | 1/2 |
|       | 1/2   | 1/2   | 1   |
- **JedeZeilen-undSpaltensummeist1/2.**
- **每行和每列的和都是 1/21/2**

2. 分别求给定 $Y = 1$ 条件下 $X$ 的条件分布。

- 正相关
	- F_X = x|Y=1 =
		- 0, x < 1
		- 1, x >=1
- 负相关
	- F_X = x|Y=1 =
		- 0, x < 0
		- 1, x >=0
- 独立
	- F_X = x|Y=1 =
		- 0, x < 0
		- 1/2, [0,1)
		- 1, x >= 1

2. 计算每个模型中 $X$ 和 $Y$ 的协方差 $\text{Cov}(X,Y)$ 与相关系数 $\text{Corr}(X,Y)$

- 正相关
	- Cov(X,Y)：1/2 - 1/4 = 1/4
		- E(X):1/2
		- E(Y):1/2
		- E(XY):1/2
		- Var(X): 1/4
		- Var(Y)：1/4
	- Corr(X,Y)：Cov(X,Y)/\sqrt{Var(X)Var(Y)} = 1/4 / 1/4 = 1
- 负相关
	- Cov(X,Y)
	- Corr(X,Y)
- 独立
	- Cov(X,Y)
	- Corr(X,Y)

2. 哪个模型中 $X$ 和 $Y$ 相互独立？请通过因子分解或条件分布给出理由。

	- 独立模型
	- f_X = 0|Y = 0 = 1/2
	- f_X = 1|Y = 0 = 1/2
	- f_X(x =0) = 1/2
	- f_X(x =1) = 1/2
	- 所以，f_X|Y=0 = f_X
	- 所以独立

**以上是简略的写法，标准是 $f_{X|Y}(0|0) = 1/2$**

4. 求三个模型中 $P(X + Y = 1)$ 的值。这个结果说明边缘分布包含哪些信息？

	- 正相关
		- P(X+Y = 1) = 0
	- 负相关
		- P(X+Y = 1) = 1
	- 独立
		- P(X+Y = 1) = 1/2
	- **这三个模型中边缘分布都一样，但是完全决定不了（X+Y=1）的值  ！！！**
	- **相同的边缘分布并不能确定和的分布，因此也不能确定联合结构**
	- Die Wahrscheinlichkeiten sind der Reihe nach 0, 1/2 und 1. Identische Ränder legen die Verteilung einer Summe und damit die gemeinsame Struktur nicht fest.

#### 4

设随机向量 $X = (X_1, X_2)^\top$ 满足

$$ E(X) = \begin{pmatrix} 1 \\ -1 \end{pmatrix}, \qquad \Sigma = \text{Cov}(X) = \begin{pmatrix} 4 & 2 \\ 2 & 9 \end{pmatrix}. $$

定义

$$ Z = AX + b, \qquad A = \begin{pmatrix} 1 & 0 \\ 1 & -2 \end{pmatrix}, \qquad b = \begin{pmatrix} 0 \\ 3 \end{pmatrix}. $$

1. 利用矩阵公式 $\text{Cov}(AX+b) = A\Sigma A^\top$ 计算 $E(Z)$ 和 $\text{Cov}(Z)$。

	- E(Z) = E(AX + b) = AE(X) + b = A(1, -1)^T + b = (1,6)^T  
	- **$Cov(AX+b)=A\Sigma A^{T}$  -- 小抄公式**
	- Cov（Z） = Cov(AX + b) = A\SigmaA^T = ((4,0)^T,(0,32)^T)         **-- 协方差矩阵线性变换公式 + 熟练的2x2矩阵乘法**！！！

2. $Z_1$ 和 $Z_2$ 是否不相关？由此能否推出它们独立？请区分**一般情形**与 $X$ **服从联合正态分布**的情形。

	- 观察Cov(Z)，是对角矩阵，
		- Var(Z1) = 4
		- Var(Z2) = 32
		- Cov(Z1,Z2) = 0
		- 如果是一般情形，不一定独立，如果是联合正态分布，独立

	**注意：**
	- **随机向量 X1，X2 构造了 Sigma 协方差矩阵 Cov(X)**
	- **随机向量变换后得到Z，相当于 两个线性方程组，，其中，, A = ((a1,a2)^T, (b1,b2)^T)**
		- **Z1 = a1X1 + b1**    
		- **Z2 = a2X2 + b2**
		- **可以把这个方程组写为 AX + b = Z**
		-  **Z = （Z1,Z2)^T**
		- **X = （X1，X2）^T**
		- **A = （(a1,0)^T, (0,a2）^T) 对角阵！！！！**

3. 求 $\Sigma$ 对应的相**关系数矩阵**。

	- 根据协方差矩阵：
		- Var(X1) = 4
		- Var(X2) = 9
		- Cov(X1,X2) = 2
	- Corr(X1,X2) = Cov(X1,X2)/sqrt{Var(X1)Var(X2)} = 2 / sqrt{36} = 1/3
	- （（1, 1/3）^T，（1/3,1）^T）

4. 对哪些 $a \in \mathbb{R}$，矩阵

$$ \Sigma(a) = \begin{pmatrix} 4 & a \\ a & 9 \end{pmatrix} $$

可以作为协方差矩阵？请利用**行列式**或**协方差界限**来判断。

- 行列式 》0
- 36 - a^2 >= 0
- |a| <= 6
- -6 <= a <= 6

- 半正定矩阵  --  $x^T \Sigma x \geq 0$
- 设 $x = (x_1,x_2)^T$
- $x^T \Sigma x =$ 4x1^2 + 2ax1x2 + 9x2^2
- 把x2固定看成常数，二次型看为是 x1 de 函数，整理得到
- = 4x1^2 + (2ax2)x1 + 9x2^2
- 二次函数 a = 4，开口向上，如果要永远大于等于0，即 函数最多只有一个解，即 delta = b^2 - 4ac 
- = (2ax2)^2 - 4x4x9x2^2
- = 4a^2x2^2 - 144x2^2 <= 0
- 4a^2 <= 144
- a^2 <= 36
- -6 <= a <= 6

**注意：二次函数 delta = b^2 - 4ac 根的判别式**
**二阶行列式可以直接用行列式》0判定半正定，否则必须用 $x^T \Sigma x \geq 0$ 结合二次函数判定。**
#### 5

设

$$ \begin{pmatrix} X_1 \\ X_2 \end{pmatrix} \sim N_2 \left( \begin{pmatrix} 10 \\ 5 \end{pmatrix}, \begin{pmatrix} 4 & 2 \\ 2 & 9 \end{pmatrix} \right). $$

1. 给出 $X_1$ 和 $X_2$ 的边缘分布，并求相关系数 $\rho$。

	- X1 ~ N(10, 4)
	- X2 ~ N(5,9)
	- **Cov(X1,X2) = 2**
	- **Corr(X1,X2) = Cov(X1,X2) / sqrt{4x9} = 2/6 = 1/3**

2. 求给定 $X_2 = 8$ 条件下 $X_1$ 的条件分布，即其条件期望和条件方差。

- P(X1 <= x | X2 =8) = P(X1 <= x, X2 = 8) / P(X2 = 8)
- P(X2 = 8) = ？ **连续分布，单点概率没有，不行！！**
- **改用密度, 也有点复杂，缺少联合密度函数**
- 二元正态分布
- $X_1 \mid X_2 = x_2 \sim N \left( \mu_1 + \frac{\sigma_{12}}{\sigma_2^2} (x_2 - \mu_2),\; \sigma_1^2 - \frac{\sigma_{12}^2}{\sigma_2^2} \right).$
- 所以，X1|X2 = x2 ~ N(10 + 2(8 - 5)/9, 4 - 4/9)
- **~ N(32/3, 32/9)**
- E(X1|X2 = 8) = 32/3
- Var(X1|X2 = 8) = 32/9

1. 用标准正态分布的分布函数 $\Phi$ 表示 $P(X_1 \leq 12 \mid X_2 = 8)$。

	- **~ N(32/3, 32/9)**
	- $\Phi((12 - 32/3) / \sqrt{32}/3)$
	- 化简：$\Phi(1\sqrt{2})$

2. 如果将条件从 $X_2 = 8$ 改为 $X_2 = 5$，条件期望和条件方差如何变化？

	- 重新代入公式求分布
	- E(X1|X2 = 8) = 10
	- Var(X1|X2 = 8) = 32/9     --- **条件变化不影响方差！！**

3. 协方差矩阵的非对角元素取何值时，$X_1$ 和 $X_2$ 相互独立？为什么在此处联合正态性起关键作用？

	- 非对角元素是协方差，如果要独立，协方差 = 0，相关系数 = 0
	- Beim Nebendiagonaleintrag 0 ist ρ = 0 und damit sind die Komponenten unabhängig. Die Schlussrichtung von Unkorreliertheit zu Unabhängigkeit gilt hier wegen der gemeinsamen Nor malverteilung
	- **当非对角元素为 0 时，相关系数 ρ=0，因此各分量相互独立。此处之所以能从“不相关”推出“独立”，是因为（两个分量）服从联合正态分布。**

**提示**：对于二元正态分布，有

$$ X_1 \mid X_2 = x_2 \sim N \left( \mu_1 + \frac{\sigma_{12}}{\sigma_2^2} (x_2 - \mu_2),\; \sigma_1^2 - \frac{\sigma_{12}^2}{\sigma_2^2} \right). $$

#### 6 混合分布！！

设 $X \sim N(0,1)$，$B$ 独立于 $X$，且

$$ P(B = -1) = P(B = 1) = \frac{1}{2}. $$

定义

$$ U = X, \qquad V = BX. $$

1. 证明 $U$ 和 $V$ 都服从标准正态分布。

	- U = X ~ N(0,1)
	- V = BX
		- **P(V <= v) = P(B=1)P(X <= v|B=1) + P(P = -1)P(X <= v|B=-1)**   **-- 离散条件下的全概率公式，小抄**
		- 因为独立
		- = P(X <= v)/2 + P(X <= v)/2
		- = P(X <= v)

2. 计算 $E(U)$、$E(V)$、$\text{Var}(U)$、$\text{Var}(V)$ 以及 $\text{Cov}(U,V)$

	- E(U) = 0
	- Var(U) = 1
	- E(V) = 0
	- Var(V) = 1
	- Cov(U,V) = E(UV) - E(U)E(V) = E(UV) = E(XBX) = E(BX^2)
	- 因为B  和 X 独立
	- = E(B)E(X^2)
	- E(B) = -1/2 + 1/2 = 0
	- 所以 Cov(U,V)  = 0

3. 尽管如此，证明 $U$ 和 $V$ 不独立。请利用 $|U|$ 与 $|V|$ 之间的关系。

	- Corr(|U|,|V|) = Cov(|U|,|V|) / \sqrt{Var(U)Var(V)}
	- =  Cov(|U|,|V|)
	- 独立随机变量有个重要性质：如果 U 和 V 独立，那么它们的**任何函数（比如绝对值）**也独立
	- ...

4. 随机向量 $(U,V)^\top$ 是否可能服从二元正态分布？请在不计算联合密度的情况下给出理由。

	- 如果是二维正态分布，那么 Cov(U,V) = 0(第二问解的) 应该可以推导出 U和V独立，但是第三问说明不独立，所以不是
	- Nein. Wäre (U,V)⊤ bivariat normalverteilt, würden aus Cov(U,V ) = 0 unabhängige Kompo nenten folgen, im Widerspruch zu Teilaufgabe 3.

#### 7

判断以下每个陈述为真或假。请用最多两句话说明理由，并将错误陈述改正。

1. 两个边缘分布唯一确定了 $X$ 和 $Y$ 的联合分布。

	- 否。X和Y独立唯一确定了X和Y的联合分布

2. 若 $X$ 和 $Y$ 独立，则对任意满足 $P(Y = y) > 0$ 的 $y$，都有 $P(X = x \mid Y = y) = P(X = x)$。

	- 对

3. 若联合密度在某点的取值大于 1，则它不可能是合法的密度函数。

	- 错，密度可以大于1，只要总积分=1，且密度》0，就是合法密度函数

4. 由 $\text{Cov}(X,Y) = 0$ 总能推出 $X \perp\!\!\!\perp Y$。

	- 只有X，Y是二维正态分布，才能 $X \perp\!\!\!\perp Y$

5. 若 $X$ 和 $Y$ 服从联合正态分布，则它们独立的充要条件是协方差为零。

	- 对

6. 协方差矩阵的对角线上是各分量的标准差。

	- 协方差矩阵的对角线上是各分量的方差

7. 给随机向量加上一个固定向量 $b$ 会改变其协方差矩阵。

	- Var(X1 + b) = Var(X1)
	- Cov(X1+b, X2 + b) = Cov(X1,X2)
	- 所以错误
	- 加上一个固定向量 $b$ **不会**改变其协方差矩阵

8. 若 $X$ 和 $Y$ 都服从标准正态分布，则随机向量 $(X,Y)^\top$ 自动服从二元正态分布。

	- **错误，边缘正态不能保证联合正态**
	- Randnormalverteilung garantiert nicht die gemeinsame Normalverteilung.

#### 8

在以下三个场景中，分布中的**某个参数本身不是固定的，而是一个随机变量**。

请按相同的步骤处理每个场景：  
- 命名随机变量，  
- 写出两个层次（条件分布和参数分布），  
- 然后利用公式  

$$ E(X) = E[E(X \mid \cdot)], \qquad \operatorname{Var}(X) = E[\operatorname{Var}(X \mid \cdot)] + \operatorname{Var}[E(X \mid \cdot)] $$

进行计算。整个过程中无需计算 $X$ 的边缘分布。

##### 1. 汽车保险

某保险公司对每位客户每年的事故报告次数 $X$ 进行建模。客户的驾驶风险不同：对于具有个体事故率 $\Lambda = \lambda$ 的客户，有  

$$ X \mid \Lambda = \lambda \sim \text{Poi}(\lambda). $$

在整个集体中，事故率本身是随机的，并且  

$$ \Lambda \sim \text{Ga}(a, b) $$

其中 $a$ 为形状参数，$b$ 为速率参数。

(a) 用 $a$ 和 $b$ 表示 $E(X)$。  

- E(X|A = lambda) = lambda
- E(X) = E(E(X|A)) = E(A) =  a /b

(b) 求 $\operatorname{Var}(X)$。  

- Var(X|A = lambda) = lambda
- E(A) = a/b
- E(X|A = lambda) = lambda
- Var(A) = a/b^2
- Var(X) = a/b + a/b^2


(c) 比较 $E(X)$ 与 $\operatorname{Var}(X)$。由此可得出什么关于普通泊松分布是否能描述该集体事故数量的结论？  

- 泊松分布期望方差相等，而这个事故分布是过度离散的，不能用普通泊松分布来描述
- Wegen Var(Λ) > 0 ist Var(X) > E(X). Eine Poisson-Verteilung erzwingt dagegen Var = E. Die Schadenszahlen im Kollektiv sind also überdispersioniert und können nicht durch eine einzige Poisson-Verteilung beschrieben werden– der Zusatzterm Var(Λ) misst genau die Heterogenität zwischen den Kunden. (Die Randverteilung ist hier negativ-binomial; für die Aufg

(d) 取 $a = 2$，$b = 4$ 计算上述两个量。

- Var(X) = 1/2 + 2/16 = 5/8

---

##### 2. 进货检验

一个供应商按批次交付零件。次品率随批次变化；对于随机选取的一批，次品率被建模为  

$$ P \sim \text{Beta}(a, b). $$

在次品率为 $\pi$ 的某批次内，被检验的零件是相互独立的，即  

$$ X \mid P = \pi \sim \text{Bin}(n, \pi), $$

其中 $X$ 表示在 $n$ 个被检验零件中的**次品数量**。

(a) 求 $E(X)$。  

- E(X|P = pi) = npi
- E(X) = E(E(X|P)) = E(nP) = na/(a+b)



(b) 证明  

$$ \operatorname{Var}(X) = n E(P)[1 - E(P)] + n(n-1)\operatorname{Var}(P). $$

- Var(X|P) = npi(1-pi)
- E(Var(X|P)) = E(nP(1-P)) = nE(P - P^2) = nE(P) - nE(P^2) = n(E(P) - E(P^2)) = n(E(P) - Var(P） -  E(P)^2)
- Var(E(X|P)) = Var(nP) = n^2Var(P)
- Var(X) = n(E(P) - Var(P） -  E(P)^2) +  n^2Var(P) = .... 


(c) 取 $n = 50$，$a = 2$，$b = 18$ 进行数值计算。并与在已知次品率 $\pi = E(P)$ 时的方差进行比较，同时给出两种情形下的标准差。  

- E(X) = 50 x 2 / (2 + 18) = 5
- E(P) = 2/20 = 1/10
- Var(P) = 2x18 / (20^2 x 21) = 3/700 = 0.**00429**
- 总方差：Var(X) = 50 x 1/10 x ( 1- 1/10 ) + 50 x 49 x 3/700 = 9/2 + 21/2 = 15
- 标准差1 = 3.873
- 已知 次品率 - pi = 1/10
- X|P = 1/10 ~ (50,1/10)
- Var(X|P = 1/10) = 50 x 1/10 x 9/10 = 9/2
- 标准差2 = 2.121
- **批次间的波动（次品率不恒定）使得方差增长近3倍，标准差几乎翻倍**
- Bei bekannter Quote π = 0,1 wäre Var(X) = nπ(1−π) = 4,5. Die Standardabweichungen  
sind √15 ≈ 3,87 gegenüber √4,5 ≈ 2,12: Die Chargenschwankung verdreifacht die Varianz  
und verdoppelt fast die Streuung.


(d) 求 $\operatorname{Var}(X/n)$，即检验出的次品比例的方差，并研究当 $n \to \infty$ 时该表达式的极限。这对大样本的效用有何意义？

- Var(X/n) = Var(X)/n^2 = 15/50^2 = 0.006
- X/n - 样品次品比率
- 即使样本量任意大，被检验的次品比例仍然会有波动，而且其波动幅度恰好等于各批次之间次品率的波动。原因在于：关于 PPP 的不确定性是所有 nnn 个被检验零件所共有的，因此无法通过平均来消除。**增加检验工作量可以更好地了解当前这一批次的情况，但无法消除批次之间的波动**
- Der geprüfte Ausschussanteil streut also auch bei beliebig großer Stichprobe weiter, und  
zwar genau so stark wie die Ausschussquote zwischen den Chargen. Der Grund: Die Un  
sicherheit über P ist allen n geprüften Teilen gemeinsam und mittelt sich deshalb nicht her  
aus. Mehr Prüfaufwand sagt viel über diese Charge, beseitigt aber nicht die Schwankung  
von Charge zu Charge. Für n = 50 ist Var(X/n) = 15/2500 = 0,006 und damit schon  
nahe am Grenzwert 0,00429.

##### 3. 展会摊位

某天到达展位的访客数 $N$ 服从  

$$ N \sim \text{Poi}(\lambda). $$

每位访客独立地以概率 $\pi$ 签订合同；给定 $N = k$ 时，有  

$$ X \mid N = k \sim \text{Bin}(k, \pi), $$

其中 $X$ 为签订合同的访客数。

(a) 求 $E(X)$。  

- E(X|N = k) = kpi
- E(X) = E(Npi) = piE(N) = lambda x pi

(b) 证明 $\operatorname{Var}(X) = E(X)$。  

- **总方差定理**：$\operatorname{Var}(X) = E\bigl(\operatorname{Var}(X \mid Z)\bigr) + \operatorname{Var}\bigl(E(X \mid Z)\bigr)$
- 
- Var(X|N) = kpi(1-pi)
- E(Var(X|Z)) = pi(1-pi)E(N) = pi(1-pi) x \lambda
- E(X|N) = kpi
- Var(E(X|N)) = pi^2Var(N) =pi^2 x \lambda
- Var(X) = pi(1-pi) x \lambda + pi^2 x \lambda = pi x \lambda  = E(X)

(c) 这个结果暗示 $X$ 可能服从什么分布？  

- 泊松分布（期望 = 方差）

(d) 取 $\lambda = 50$，$\pi = 0.2$ 进行数值计算。  

- 。。。

(e) 在题 1 和题 2 中，方差大于固定参数模型下的方差，而本题中方差恰好等于期望值。请利用方差分解的两个分量解释这一差异。

- 前两个 **随机参数** 影响了成功率（或者事故率）
- 第三个随机参数影响了试验次数，签约概率不会变

#### 9

给定 $X$ 的分布以及给定 $X$ 下 $Y$ 的条件分布如下表：

| $x$ | $p_X(x)$ | $P(Y=0 \mid X=x)$ | $P(Y=1 \mid X=x)$ | $P(Y=3 \mid X=x)$ |
|-----|----------|-------------------|-------------------|-------------------|
| $-1$ | $0.20$   | $0.60$            | $0.30$            | $0.10$            |
| $0$  | $0.50$   | $0.30$            | $0.20$            | $0.50$            |
| $2$  | $0.30$   | $0.20$            | $0.10$            | $0.70$            |

---

1. 利用全概率公式求 $Y$ 的边缘分布。

-  P(Y = 0) = P(Y = 0|X=-1)P(X=-1) + P(Y=0|X=0)P(X=0) + P(Y=0|X=2)P(X=2)
	- = 0.2 x 0.6 +0.5 x 0.3 + 0.3 x 0.2 = **0.33**
-  P(Y = 1) = P(Y = 1|X=-1)P(X=-1) + P(Y=1|X=0)P(X=0) + P(Y=1|X=2)P(X=2)
	- = 0.2 x 0.3 +0.5 x 0.2 + 0.3 x 0.1 = **0.19**
-  P(Y = 3) = P(Y = 3|X=-1)P(X=-1) + P(Y=3|X=0)P(X=0) + P(Y=3|X=2)P(X=2)
	- = 0.2 x 0.1 +0.5 x 0.5 + 0.3 x 0.7 = **0.48**

- 写成分布函数样式


2. 分别通过以下两种方式计算 $P(Y \geq 1)$：
   - 由边缘分布直接计算；

	- = 0.19 + 0.48 = 0.67

   - 通过三个条件 $X = -1, 0, 2$ 直接计算。

	- = 0.2 x 0.4 + 0.5 x 0.7 + 0.3 x 0.8 = 0.67  **-- 注意，是非等概率**

1. 首先对所有三个 $x$ 值求 $E(Y \mid X = x)$，然后利用迭代期望公式求 $E(Y)$。用边缘分布验证结果。

	- E(Y | X = -1) = 0 x 0.6+1 x 0.3 + 3 x 0.1 = 0.6
	- E(Y | X = 0) = 0 x 0.3+1 x 0.2 + 3 x 0.5 = 1.7
	- E(Y | X =2) = 0 x 0.2+1 x 0.1 + 3 x 0.7 = 2.2

	- E(Y) = 0.2 x 0.6 + 0.5 x 1.7 + 0.3 x 2.2 = 1.63

- **离散求重期望**

1. 分别通过以下两种方式计算 $\operatorname{Var}(Y)$：
   - 由边缘分布直接计算；

	- E(Y) = 0x0.33 + 1x0.19 + 3x0.48 = 1.63
	- E(Y^2) = 0x0.33 + 1x0.19 + 9x0.48 = 4.51
	- Var(Y) = 4.51 - 1.63^2 = 1.853

   - **利用全方差公式**（方差分解）。

	- xxx 太繁琐

#### 10

设 $X$ 和 $Y$ 的联合概率质量函数为

| $p_{X,Y}(x,y)$ | $Y=0$ | $Y=2$ |
|----------------|-------|-------|
| $X=-1$         | 0.10  | 0.15  |
| $X=0$          | 0.20  | 0.10  |
| $X=1$          | 0.25  | 0.20  |

定义

$$ G = (X - Y)^2, \qquad H = 2X + Y. $$

1. 利用公式 $E[g(X,Y)] = \sum_x \sum_y g(x,y) \, p_{X,Y}(x,y)$ 直接计算 $E(G)$，无需先求 $G$ 的分布。

- E(G) = 0.1 x 1 + 0.15 x 9 + 0.4 x 0 + 0.1 x 4 + 0.25 x 1 + 0.2 x 1
- = 2.3

1. 计算 $E(G^2)$，并由此求 $\operatorname{Var}(G)$。然后求 $G$ 的分布以作验证。

- E(G^2) = 0.1 x 1+ 0.15 x 81 + ...
- = 14.3
- Var(G) = 14.3 - 2.3^2 = 9.01
- G 的取值可能：1 9 0 4 ，然后把概率合并
	- P(G = 0) = 0.2
	- P(G = 9) = 0.15
	- P(G = 4) = 0.1
	- P(G = 1) = 0.55

1. 求 $E(X)$、$E(Y)$、$\operatorname{Var}(X)$、$\operatorname{Var}(Y)$ 以及 $\operatorname{Cov}(X,Y)$。

- E(X) = -1 x 0.25 + 0 x 0.3 + 1 x 0.45 = 0.2 
- ....

1. 利用线性函数的运算法则计算 $E(H)$ 和 $\operatorname{Var}(H)$。

- E(H) = 2E(X) + E(Y) = ....
- Var(H) = 4Var(X) + Var(Y) + 4Cov(X,Y) -- 不独立，有协方差 = 。。。

#### 11 顺序主子式，对角分块，行列式计算

判断以下每个矩阵是否可以是协方差矩阵。对每个判断给出理由：若矩阵有效，需充分说明其正半定性；若矩阵无效，只需指出一个明确的违例。

(a) $\begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$

**是**

(b) $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$
**不是，行列式 《 0**

(c) $\begin{pmatrix} 4 & -6 \\ -6 & 9 \end{pmatrix}$
**是**

(d) $\begin{pmatrix} 0 & 0 \\ 0 & 5 \end{pmatrix}$
**是**

(e) $\begin{pmatrix} 0 & 1 \\ 1 & 2 \end{pmatrix}$
**不是，行列式 《 0**

(f) $\begin{pmatrix} 1 & 0.4 \\ 0.5 & 1 \end{pmatrix}$

**不是，不对称**

(g) $\begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{pmatrix}$
是

(h) $\begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix}$
是，

(i) $\begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & -1 \\ 1 & -1 & 1 \end{pmatrix}$

二阶顺序主子式 >= 0
三阶顺序主子式，用余子式法行列式 = -4 < 0 不是
不是，

(j) $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 2 & 3 \\ 0 & 3 & 2 \end{pmatrix}$
不是，余子式法行列式 = -5 < 0 不是

(k) $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 1 \end{pmatrix}$
不是，不是方阵

(l) $\begin{pmatrix} 1 & 2 & 0 & 0 \\ 2 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$

- **观察矩阵，把矩阵转成2x2的分块矩阵**
- **分块矩阵式对角矩阵**
- **分块对角矩阵行列式 = 对角块行列式乘积**
- **det = （1-4） x （1-0 ） = -3**
- **所以，这个不是正定矩阵**

#### 12 -- Tag2

设 $X \sim \text{Exp}(2)$，即

$$ f_X(x) = 2e^{-2x} \cdot \mathbb{I}_{[0,\infty)}(x), $$

且

$$ Y = 3 - 2X. $$

---

1. 确定 $Y$ 的支撑集，并绘制哪些 $x$ 值映射到哪些 $y$ 值的示意图。

- x >=0, 2x >= 0, -2x <=0, 3-2x <= 3
-  支撑集 Y <= 3
- 画图，代入x = 0，y = 3，x = 1.5， y = 0
- 在 x >= 0 区域阴影

1. 分别对 $y < 3$ 和 $y \geq 3$ 两种情况求 $F_Y(y) = P(Y \leq y)$。为此，请将不等式 $3 - 2X \leq y$ 转化为关于 $X$ 的不等式。

	- 3-2X <= y => X >= (3-y)/2
	- P(Y <= y) = P(3-2X <= y) = P(X >= (3-y)/2)
	- 因为 X ~ exp(2)
	- 指数分布的分布函数：F(x) = 1 - exp(-lambda x), x >= 0
	- P(X >= (3-y)/2) = 1 - 1 + exp(-lambda (3-y)/2) = exp(-2 (3-y)/2) = exp(y-3)

	- **考试技巧：至少根据题目推导到这里，考场上最后要写分布函数，分布函数分段形式写出来再说，肯定式两端，有一段肯定式 exp(y-3), 最大一段肯定是1**

	- **F_Y(y) = P(Y <= y)  , 因为 前面一问， Y <= 3**
		- **exp(y-3), y < 3**
		- **1, y >= 3 ( Y <= 3, y >= 3情况下 ， Y <= y 一定存在)**


2. 通过求导得到密度函数 $f_Y$，并验证其归一性。

	- 反函数：X = （3-Y)/2 ==>  g(y) = (3-y)/2
	- |g(y)'| = 1/2
	- f_Y(y) = 2exp(-2 x (3-y)/2)x1/2 = **exp(y-3)**, y <= 3
	- 积分 = exp(y-3)|_负无穷^3 = 1 - 0 = 1


3. 利用仿射变换的运算法则计算 $E(Y)$ 和 $\operatorname{Var}(Y)$。

	- E(Y) = E(3-2X) = 3 - 2E(X)
	- **E(X) = 2\int_0^{无穷} x exp(-2x) dx**
	- **分部积分法**
		- **u = x， dv = exp(-2x)dx**
		- **du = 1, v = -exp(-2x)/2**
		- **= -xexp(-2x)/ - \int -exp(-2x)/2 dx**
		- **=1/2**
	- 或者直接用指数分布期望结果 = 1/lambda = 1/2
	- E(Y) = 3 - 1 = 2

	- Var(Y) = Var(3-2X) = 4Var(X) = 4 x 1/4 = 1
#### 13 -- 密度根号类型 -- 绝对值分区间！!!!

设 $X \sim \mathcal{U}(-2,1)$，且 $Y = X^2$。

1. 确定 $Y$ 的支撑集。将 $X$ 的支撑集分解为若干区间，使得在每个区间上 $g(x) = x^2$ 是双射。


- 1-4
- -2 - 0， 0 - 1


1. 对 $0 < y < 1$ 和 $1 < y < 4$ 两种情况，给出所有满足 $x \in [-2,1]$ 的原像 $x$。

- $Y = X^2 == > |X| = \sqrt{Y}$ -- **注意带绝对值**
	- $x = \sqrt{y}$
	- $x = -\sqrt{y}$
- 0 < y < 1
	- 看 x 两个取值空间，（-1，0），（0，1）都满足
	- $x \in (-\sqrt{y},\sqrt{y})$
- 1 < y < 4
	- 看 x 的取值空间，（-2，1）满足，**虽然 （0，1）也满足，但是不连续满足**
	- $x \in (-\sqrt{y},0)$

1. 利用一维密度变换通式推导 $f_Y$ 的密度函数。结果请分段给出。

	- $g(y)' = y^{-1/2}/2$
	- $f_X(x) = 1/（1-（-2）= 1/3$
	- **0 < y < 1  有两个原像**
		- $g_1(y) = \sqrt{y}$
		- $g_1(y)' = y^{-1/2}/2$ ==> $|g_1(y)'| = y^{-1/2}/2$
		- $g_1(y) = - \sqrt{y}$
		- $g_2(y)' = -y^{-1/2}/2$ ==>$|g_2(y)'| = y^{-1/2}/2$
		- **$f_Y(y) = 1/3 \cdot y^{-1/2}/2 + 1/3 \cdot y^{-1/2}/2 = 1/3 \cdot y^{-1/2}$**
	- **1 < y < 4**
		- $g(y) = \sqrt{y}$
		- $g(y)' = y^{-1/2}$ ==> $|g(y)'| = y^{-1/2}/2$
		- **$f_Y(y) = 1/3 \cdot y^{-1/2}/2 = y^{-1/2}/6$**

2. 通过积分验证 $f_Y$ 的归一化积分为 1。

	- 两个区间积分相加

3. 分别通过以下两种方式计算 $P(Y \leq 1)$：
   - 直接利用 $X$ 的分布；

	- **$P(Y <= 1) = P(X^2 <= 1) = P(-1 <= X <= 1)$**
	- X ~ U（-2，1）
	- 均匀分布函数：F(x) = (x-a)/(b-a) = (x+2)/3
	- F(1) = 1
	- F(-1) = 1/3
	- P(Y <= 1) = 1 - 1/3 = 2/3

   - 利用 $Y$ 的密度函数 $f_Y$。

	- 利用 1 < y < 4 区间密度函数积分
	- = 2/3

#### 14 雅可比, 支撑集的计算。。。

设 $X_1, X_2$ 独立且均服从 $(0,1)$ 上的均匀分布。定义

$$ U = X_1 + X_2, \qquad V = X_1 - X_2. $$

---

1. 将变换写成 $(U,V)^\top = A (X_1, X_2)^\top$ 的形式，并求逆变换 $(x_1, x_2) = g^{-1}(u, v)$。

- （（1，1)^T, (1,-1)^T)
- A^-1 = （（1，1）^T, (1,-1)^T) x 1/2
- 逆变换：X = A^-1(U,V)^T
	- X1 = (U+V)/2
	- X2 = (U-V)/2

1. 计算雅可比行列式 $\det J_{g^{-1}}(u, v)$。

- **|det(J)| = 1/2  -- 注意，题目要求的J的右下角是 g^-1 (u,v)，也就是给U,V 得到 X1，X2的映射，不能反过来求解**
- $det J_g = 1 / det J_{g^{-1}}$

1. 将条件 $0 < x_1 < 1$ 和 $0 < x_2 < 1$ 转化为关于 $u$ 和 $v$ 的不等式，并在 $u$-$v$ 平面中画出变换后的支撑集。

	- 1) 0 < (U+V)/2 < 1  =>   0 < U+V < 2
	- 2) 0 < (U-V)/2 < 1  => 0 < U-V < 2 
	- 3) 1 + 2 : 0 < 2U < 4 => **0 < U < 2**
	- 4) 因为 0 < U+V < 2， 0 < U < 2, 所以，**0-U < V < 2 - U**
	- 5) U-V > 0 => **V < U**
	- 6) U-V < 2 => **V > U - 2**
	- 7) 结合下：**max(-U, U-2) < V < max(2-U, U)，0 < U < 2**

	- **画图，横轴为 U ， 纵轴为 V，画 函数 V = -U  V = U - 2  V = U   V = 2 - U 的直线，围成的面积**

2. 求 $U$ 和 $V$ 的联合密度 $f_{U,V}(u, v)$。

	- $f_{U,V}(u,v) = f_{X,Y}(x,y) \cdot |\det J_{g^{-1}}(u, v)|$
	- $= 1/2 \cdot f_{X,Y}(x,y)$
	- $= 1/2 \cdot f_{X,Y}((u+v)/2,(u-v)/2)$
	- **因为独立，且在 0 - 1 区间均匀分布，x1，x2 密度在定义域为 1**
	- $=1/2 \cdot f_X((u+v)/2) \cdot f_Y((u-v)/2)$
	- 所以，
		- $f_{U,V}(u,v) = 1/2 , 0 < u+v < 2, 0 < u-v < 2$ 

3. 对 $v$ 进行边际化，分段求出 $f_U(u)$。说明为什么通过卷积也应该得到相同的结果。

	- 。。。 太复杂

#### 15

设独立随机变量 $X$ 和 $Y$ 的概率质量函数分别为：

| $x$ | 0 | 1 | 2 |
|-----|---|---|---|
| $p_X(x)$ | $1/4$ | $1/2$ | $1/4$ |

| $y$ | 0 | 1 |
|-----|---|---|
| $p_Y(y)$ | $2/3$ | $1/3$ |

令 $Z = X + Y$。

---

1. 确定 $Z$ 的支撑集。

	- T_Z : {0，1，2，3}

2. **对支撑集中的所有 $z$，计算**

$$ P_Z(z) = \sum_x P_X(x) \, P_Y(z - x). $$
	- P_Z(0) = P_X(0)P_Y(0) = 2/12 = **1/6**
	- P_Z(1) = P_X(0)P_Y(1) + P_X(1)P_Y(0) = 1/12 + 2/6 = **5/12**
	- P_Z(2) = P_X(0)P_Y(2) + P_X(1)P_Y(1) + P_X(2)P_Y(0) = 1/6 + 2/12 = **1/3**
	- P_Z(3) = P_X(2)P_Y(1) = **1/12**

3. 验证所得概率之和为 1。

	- P_Z(0) + ... + P_Z(3) = 12/12 = 1

4. 利用新得到的 $Z$ 的分布计算 $E(Z)$ 和 $\operatorname{Var}(Z)$。

	- E(Z) = 0 x 1/6 + ... + 3 x 1/12 = 4/3
	- E(Z^2) = 5/2
	- Var(Z) = 13/18


5. 用以下公式验证第 4 小题的结果：

$$ E(X + Y) = E(X) + E(Y), $$

$$ \operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y). $$

在第二个等式中，独立性的必要性体现在哪里？

- E(Z) = E(X+Y) = E(X) + E(Y) 
	- E(X) =1
	- E(Y) = 1/3
	- E(Z) = E(X+Y) = 4/3 .。。
- Var(X+Y) = Var(X) + Var(Y)
	- Var(X) = ....

#### 16 二项式定理

本题不涉及具体数值，而是用参数进行卷积运算。两个部分遵循相同的模式：写出卷积和，确定支撑交集，将参数从求和中提取出来，然后用已知的求和公式完成计算。

###### 1. 泊松分布

设 $X \sim \text{Poi}(\lambda_1)$ 和 $Y \sim \text{Poi}(\lambda_2)$ 独立，且 $Z = X + Y$。

(a) 给出 $Z$ 的支撑集，并对固定的 $z$ 确定卷积求和时的支撑交集。

- x >= 0
- y >= 0
- Z = X+ Y,  Z >= 0
- **Y = Z - X, 固定Z，所以，$Y \in [0,Z]$**

(b) 写出

$$ P_Z(z) = \sum_x P_X(x) \, P_Y(z - x) $$

的具体形式，并将所有与 $x$ 无关的因子提到求和号外。

- 直接根据PMF来化简
- $P_Z(z) = exp(-(\lambda_1+\lambda_2)) \cdot \Sigma_x (\lambda_1^x \cdot \lambda_2^{z-x}) / (x! \cdot (z-x)!)$

(c) 乘以 $z!$ 进行凑配，识别剩余的求和为二项式定理，从而证明

$$ Z \sim \text{Poi}(\lambda_1 + \lambda_2). $$

- **二项式定理 ：$\displaystyle \binom{n}{k} = \frac{n!}{(n-k)!\,k!}$**
- **二项式定理：$(a+b)^n = \Sigma_{k=0}^n a^k b^{(n-k)}$**
- 所以，$z! / (x! \cdot (z-x)!) = C(z,x)$
- $z! \cdot P_Z(z) = exp(-(\lambda_1 + \lambda_2)) \cdot \Sigma_x (\lambda_1^x \cdot \lambda_2^{z-x}) \cdot C(z,x)$
- $= exp(-(\lambda_1 + \lambda_2)) \cdot (\lambda_1 + \lambda_2)^x$
- 所以，$P_Z(z) = exp(-(\lambda_1 + \lambda_2)) \cdot (\lambda_1 + \lambda_2)^x / z!$
- 即 Z ~ Poi(\lambda_1, \lambda_2)

**解题技巧：推导到后面公式不记得，再反向把要证明的东西展开，直接等于！！！**

(d) 某呼叫中心每小时从两个独立区域接到电话，参数分别为 $\lambda_1 = 3$ 和 $\lambda_2 = 5$。每小时的总呼叫数服从什么分布？求 $E(Z)$ 和 $\operatorname{Var}(Z)$，并用求和法则验证结果。

- 总呼叫次数 Z ~ Poi(3+5)
- E(Z) = 8
- Var(Z) = 8

###### 2. 二项分布

设 $X \sim \text{Bin}(n, \pi)$ 和 $Y \sim \text{Bin}(m, \pi)$ 独立，且**具有相同的成功概率** $\pi$，令 $Z = X + Y$。

(a) 确定卷积时的支撑交集。注意这里求**和区间是双边受限的**：

$$ x \in \{ \max(0, z - m), \ldots, \min(n, z) \}. $$

- T_X : 0,1,2,...n，     0 <= x <= n
- T_Y: 0,1,2,...,m  ,     0 <= y <= m  -- **二项分布支撑集合别忘了写上限**
- z = x + y
- 0 <= z - x <= m  ==> 0 >= x - z >= -m ==>  z >= x >= z-m
- 结合 0 <= x <= n
- **max(0,z-m) <= x <= min(n, z)**


(b) 写出 $P_Z(z)$ 的表达式，并证明 $\pi^z (1 - \pi)^{n+m-z}$ 可以完全从求和号中提取出来。

- **P_Z(z) = P(X+Y = z)**
- = $\Sigma_x P(X=x)P(Y=z-x)$
- **代入上面支撑集**
- $=\Sigma_{max(0,z-m)}^{min(n, z)} C(n,x)p^x(1-p)^{(n-x)}C(m,z-x)p^{(z-x)}(1-p)^{(m-(z-x))}$
- $=p^z(1-p)^{(n+m-z)} \cdot \Sigma_{max(0,z-m)}^{min(n, z)} C(n,x)C(m,z-x)$


(c) 利用范德蒙德恒等式

$$ \sum_x \binom{n}{x} \binom{m}{z-x} = \binom{n+m}{z} $$

证明 $Z \sim \text{Bin}(n+m, \pi)$。

- $=p^z(1-p)^{(n+m-z)} \cdot C(n+m,z)$
- 所以，$Z \sim \text{Bin}(n+m, \pi)$

(d) 不经过计算，用两句话解释为什么这个结果必然成立——将二项变量写成伯努利变量之和。

- X 是 n 个独立 Bernoulli(π) 变量之和，Y 是另外 m 个这样的变量之和，并且这两组变量彼此独立。那么 Z = X + Y 就是 n + m 个独立 Bernoulli(π) 变量之和，因此服从 Bin(n + m, π) 分布。
- XistdieSummevonnunabhängigenBernoulli(π)-Variablen,Y dieSummevonmweit eren,undbeideGruppensindunabhängigvoneinander.DannistZ=X+YdieSumme vonn+munabhängigenBernoulli(π)-Variablen,alsoBin(n+m,π)-verteilt

**解题技巧：解释现象就把现象说一下**


(e) 如果 $X \sim \text{Bin}(n, \pi_1)$ 和 $Y \sim \text{Bin}(m, \pi_2)$ 且 $\pi_1 \neq \pi_2$，为什么上述论证会失败？请指出在推导过程中哪一步需要参数相等。

- 如果 p 不相等，底数不同没有办法计算，这样就没有办法把 $\pi^z (1 - \pi)^{n+m-z}$ 作为公共的项提取
- - Wenn die p nicht gleich sind, kann man wegen der verschiedenen Basen nicht rechnen; auf diese Weise gibt es keine Möglichkeit, πz(1−π)n+m−zπz(1−π)n+m−z als gemeinsamen Faktor auszuklammern.
- “底数” → **die Basis**（复数：**die Basen**）
“提取” → **herausziehen / ausklammern**（把公因子提出来常用 **ausklammern**）



**提示**：二项式定理：

$$ (a+b)^n = \sum_{k=0}^n \binom{n}{k} a^k b^{n-k}. $$

#### 17 归纳法，连续随机变量众数

设 $X_1, X_2, \ldots$ 独立且均服从 $\text{Exp}(\lambda)$，即

$$ f_{X_i}(x) = \lambda e^{-\lambda x} \mathbb{I}_{[0,\infty)}(x). $$

##### 1. 两个变量的卷积

对 $S_2 = X_1 + X_2$，确定卷积的支撑交集 $A(s) = T_{X_1} \cap (s - T_{X_2})$，并通过卷积计算 $f_{S_2}$。证明

$$ f_{S_2}(s) = \lambda^2 s e^{-\lambda s}, \quad s \geq 0, $$

并指出这是形状-速率参数化下的 $\text{Ga}(2, \lambda)$ 分布。

- x1 >= 0
- x2 >= 0
- s2 = x1 + x2
- x1 = s2 - x2 >= 0 ==> x2 <= s2
- 所以，0 <= x2 <= s2
- 因为独立，$f_{s2} = \int f_{x1}(x) f_{x2}(s - x) = \lambda \cdot e^{-\lambda x} \cdot \lambda \cdot e^{-\lambda(s-x)} dx$
- $=\int \lambda^2 \cdot e^{-\lambda s} dx$
- $=\lambda^2 \cdot e^{-\lambda s} x|_0^s$
- $=\lambda^2 \cdot e^{-\lambda s} \cdot s$

对比Gamma 分布 PDF

- b =$\lambda$
- a = 2
- 对比gamma分布pdf前面的常数，就是 $\lambda^2$

###### 2. 归纳证明一般情形

对 $S_n = X_1 + \cdots + X_n$，用归纳法证明

$$ f_{S_n}(s) = \frac{\lambda^n s^{n-1}}{(n-1)!} e^{-\lambda s}, \quad s \geq 0, $$

即 $S_n \sim \text{Ga}(n, \lambda)$。归纳步骤中只需使用积分 $\int_0^s x^{n-2} \, dx$。


- $f_{s_2} = \lambda^2 \cdot e^{-\lambda s} \cdot s$ ，和要证明的结果代入 n = 2 一致
- 假设 $S_{n-1} = X_1 + ... + X_{n-1}$，则 $f_{s_{n-1}}(s) = ...$
- 则 $S_n = S_n-1 + X_n$
- $f_{S_n} = \int ... \cdot \lambda \cdot e^{-\lambda \cdot (s-n)}$

**技巧：数学归纳法步骤，先1，后 n-1，然后列 n 的计算表达式，可以跳过步骤，得到结果。。。。**

###### 3. 矩的计算

不用积分，求 $E(S_n)$ 和 $\operatorname{Var}(S_n)$。

- $E(S_n) = \Sigma E(X_i)$
- $E(X_i) = 1/\lambda$
- $E(S_n) = n/\lambda$

- $Var(S_n)$ = $\Sigma Var(X_i)$
- $=n/\lambda^2$

###### 4. 密度函数草图

在同一个坐标系中，对固定的 $\lambda$ 画出 $f_{S_n}$ 在 $n = 1, 2, 3$ 时的图像。各情形的**众数**位于何处？为什么随着 $n$ 增大，众数会逐渐远离 0？


- 根据上面，S_n ~ Ga(n,\lambda)
- 密度函数：$s^{(n−1)} exp(−\lambda s)$
- **众数就是密度函数最大值**
- 对密度函数求导：$f' = (n-1)/\lambda$



- 画图：
	- 代入n=1，2，3
	- 根据上面密度公式 f_sn
		- $f_s1(s) = e^{-s}$
		- $f_s2(s) = se^{-s}$
		- $f_s3(s) = s^2e^{(-s)}/2$
	- 众数分别是
		- n = 1，密度函数单调递减，又 s >= 0，所以众数位置 s = 0
		- n = 2，$f_{s2}' = 0$, s = 1
		- n = 3, $f_{s3}'$ = 0, s = 2
	

**技巧：众数就是密度函数求导 = 0，解出x等于多少**


###### 5. 不同速率的卷积

设 $X \sim \text{Exp}(\lambda_1)$ 和 $Y \sim \text{Exp}(\lambda_2)$ 独立，且 $\lambda_1 \neq \lambda_2$。通过卷积计算 $f_{X+Y}$，并证明

$$ f_{X+Y}(s) = \frac{\lambda_1 \lambda_2}{\lambda_2 - \lambda_1} \left( e^{-\lambda_1 s} - e^{-\lambda_2 s} \right), \quad s \geq 0. $$

这个结果还是 Gamma 分布吗？用 $\lambda_1 = 1$，$\lambda_2 = 2$ 验证结果是否与讲义示例一致。

- **卷积积分计算**
- 。。。
###### 6. 应用：服务器处理时间

某服务器逐个处理任务，处理时间相互独立且服从 $\text{Exp}(\lambda)$，其中 $\lambda = 2$（每分钟）。第三个任务完成的时刻服从什么分布？其平均完成时间是多少？

- S3 = X1 + X2 + X3
- 根据前面结论，S3 ~ Ga(3,2)
- E(S3) = 3/2 = 1.5

**技巧：利用前面结论公式直接解答**


**注**：泊松分布、二项分布（仅在 $\pi$ 相同时）和 Gamma 分布（仅在速率相同时）在卷积下封闭。在考试中若遇到这些变量的和，应能直接指出结果分布，只有在明确要求推导时才需要实际计算卷积。

#### 18

设 $X, Y \overset{\text{iid}}{\sim} \text{Exp}(1)$，且 $D = X - Y$。

1. 说明为什么联合密度可以分解因式，并给出 $f_{X,Y}$ 及其支撑集。

- f_XY = f_X f_Y= exp(-x)exp(-y), x >= 0, y>=0

1. 由于差不是和，先将 $Y$ 变换为 $W = -Y$，并给出 $W$ 的密度和支撑集。

- f_W(w) = exp(w)   w <= 0

1. 计算 $f_D = f_X * f_W$。为此，先确定卷积的支撑交集，并对 $d < 0$ 和 $d \geq 0$ 两种情形进行分类讨论。

- x >= 0
- w <= 0
- D = X - Y = X + W
- X = D - W
- $f_D = \int f_X(x) \cdot f_W(d-x) dx$
- 交集：x >= 0, d-x <= 0 ==> x >= d
- x >= max(0,d) 
- d < 0
	- x >= 0
	- $f_D = \int_0^{\infty} e^{-x} e^{x-d} dx$
	- **$= e^d / 2$**
- d>= 0
	- x >= d
	- .,,
	- **$=e^{-d}/2$**

1. 将结果合并为只含 $|d|$ 的单一公式。这个分布称为拉普拉斯分布。

	- 观察上面，两个区间都是要指数部分小于零
	- $=e^{-|d|}/2$

2. 在同一坐标系中画出 $f_D$ 以及第 6 题中和 $S = X + Y$ 的密度 $f_S$。比较二者的支撑集、对称性和众数。

	- d = 0, 正负无穷，按正负坐标轴画图
	- 

3. 无需额外积分，求 $E(D)$ 和 $\operatorname{Var}(D)$。并利用所得密度计算 $P(|D| \leq 1)$。

	- E(D) = E(X-Y) = E(X) - E(Y) = 0\
	- Var(D) = Var(X-Y) = Var(X) + Var(Y) = 2  -- **注意符号在方差场景**
	 -  -1= < d <= 1 区间积分
		 - 看图像，是对称的
		 - 在 0-1区间积分
		 - = 2 \int_0^1 exp(-d)/2 dd
		 - = 1 - 1/e

**注意**：**卷积的最终结果通常形式简洁**。**考试的关键步骤在于：独立性假设、$f_Y(z - x)$ 的代入、支撑交集的确定以及清晰的分类讨论。**

#### 19 串联与并联系统的寿命分布

某设备由三个独立部件组成，其寿命分别为 $T_1, T_2, T_3$，且 $T_i \sim \text{Exp}(\lambda_i)$。考虑两种设计方案：

- **串联系统**：设备在第一个部件失效时即失效。寿命为 $S = \min(T_1, T_2, T_3)$。
- **并联系统**：设备在所有部件都失效后才失效。寿命为 $M = \max(T_1, T_2, T_3)$。

###### 1. 串联系统

利用互补事件求 $P(S > t)$，进而得到 $F_S$。证明

$$ S \sim \text{Exp}(\lambda_1 + \lambda_2 + \lambda_3), $$

并给出 $E(S)$。解释：若在串联系统中再增加一个部件，期望寿命会发生什么变化？


- P(S > t) = P(min(T1,T2,T3) > t)
- = P(T1 > t)P(T2 > t)P(T3 > t)
- = (1 - F_1(t))(1- F_2(t))(1 - F_3(t))
- 指数分布函数：$F(x) = 1 - exp(-\lambda x), x \geq 0$
- 所以 $= exp(-\lambda_1 t)exp(-\lambda_2 t)exp(-\lambda_3 t)$
- $= exp(-(\lambda_1 + \lambda_2 + \lambda_3)t)$
- 所以，P(S <= t) = 1 - $exp(-(\lambda_1 + \lambda_2 + \lambda_3)t)$
- 所以，$S \sim \text{Exp}(\lambda_1 + \lambda_2 + \lambda_3)$

- E(S1) = 1/(lambda_1 + lambda_2 + lambda_3)
- E(S2) = 1/(lambda_1 + lambda_2 + lambda_3 + lambda_4)
- 可见，E(S2) < E(S1)


###### 2. 并联系统（同分布情形）

从现在起假设三个部件相同，即 $\lambda_1 = \lambda_2 = \lambda_3 = \lambda$。求 $F_M$，并通过求导得到 $f_M$。

- F_M(m) = P(M <= m) = P(max(T1,T2,T3) <= m) = P(T1 <= m)P(T2 <= m)P(T3 <= m)
- = F_M(m)^3
- 因为 $F(x) = 1 - exp(-\lambda x), x \geq 0$   --- **指数分布函数**
- 所以 $= (1 - exp(-\lambda x))^3$
- f_M(m) = F(M)' = ....


###### 3. 并联系统的期望寿命

利用表示式 $E(M) = \int_0^\infty [1 - F_M(t)] \, dt$ 计算 $E(M)$，并证明

$$ E(M) = \frac{1}{\lambda} \left( 1 + \frac{1}{2} + \frac{1}{3} \right) = \frac{11}{6\lambda}. $$

- 设 v = exp(-lambda) x
- 1 - F_M(t) = 1 - (1 - v)^3 = 3v - 3v^2 + v^3  -- 换元法
- 。。。 = 11/6\lambda


###### 4. 数值计算

取 $\lambda = 1/1000$（每小时），给出 $E(T_i)$、$E(S)$ 和 $E(M)$（以小时为单位）。三倍冗余将平均寿命延长了多少倍？请评价三倍材料投入是否值得。

- E(T_i) = 1000
- E(S) = 1000/3
- E(M) = 11x1000/6 = ..  代入上面公式


###### 5. 生存概率

计算 $P(S > 2000)$ 和 $P(M > 2000)$。

- S ~ Exp(3/1000)
- $F_S(x) = 1 - exp(-\lambda x), x \geq 0$  
- P(S > 2000) = 1 - F(2000) = exp(-3/1000 x 2000) = e^-6

-  $F_M= (1 - exp(-\lambda x))^3$
- 代入，lambda = 1/1000
- = （1 - exp(-2))^3 = ...


###### 6. 方法限制

为什么此处不能用卷积来求 $f_M$ 和 $f_S$？请用一句话说明原因。

...

#### 20 离散情形的最小值与最大值

$n$ 名玩家同时独立地掷骰子，每人一直掷到首次掷出 6 点为止。设 $X_i$ 为玩家 $i$ 所需的掷骰次数，即 $X_i \sim \text{Geom}(p)$，其中 $p = 1/6$，采用“**首次成功所需试验次数**”的约定，支撑集为 $\{1, 2, 3, \ldots\}$。定义

$$ L = \min(X_1, \ldots, X_n), $$

$$ M = \max(X_1, \ldots, X_n), $$

分别表示第一个玩家完成和最后一个玩家完成时的掷骰次数。



1. 不用求和公式，直接通过对应的事件说明：

$$ P(X_i > k) = (1 - p)^k, \quad k = 0, 1, 2, \ldots $$

- **几何分布函数：$F(x) = 1 - (1-p)^{\lfloor x \rfloor}, x \geq 1$**
- $P(Xi > k) = 1 - P(Xi <= k) = 1 - F_X(k) = 1 - 1 + (1-p)^{k} = (1-p)^k$


2. 证明 $P(L > k) = (1 - p)^{nk}$，并由此推出

$$ L \sim \text{Geom}\left(1 - (1 - p)^n\right), \quad F_L(k) = 1 - (1 - p)^{nk}. $$

最小值仍属于同一分布族——这与题目 8 中指数分布寿命的最小值情形完全类似。

- $P(L > k) = P(min(X_1,...,X_n) > k) = P(X_1>k)...P(X_n >k)$
- $= (1-p)^k ... (1-p)^k = (1-p)^{nk}$

- $F_L(k) = P(L <= k) = 1 - (1-p)^{nk}$
- Geom(1-(1-p)^n) 的分布函数：$1 - （1-1+(1-p)^n)^x = 1 - (1-p)^{nk}$
- 所以 L ~ Geom(...)

3. 求 $E(L)$。取 $p = 1/6$ 和 $n = 4$ 进行数值计算，并与 $E(X_i)$ 进行比较。

	- E(L) = 1/(1 - (1-p)^n) = 1 / (1 - (5/6)^4) = .... = 1.93
	- E(Xi) = 6


4. 求 $F_M(k)$，并由此导出概率质量函数 $P_M(k)$。注意在离散情形中，从分布函数恢复概率质量函数是通过差分而非求导。对 $p = 1/6$ 和 $n = 4$，计算 $P(M \leq 10)$。

- $F_M(k) = P(M <= k) = P(max(X_1,...,X_n) <= k) = P(X_1 <= k)...P(X_n <= k)$
- $=F_{X}(k)...F_X(k)$
- X ~ Geom(p)
- $=(1-(1-p)^k)...(1 - (1-p)^k)$
- $=(1-(1-p)^k)^n$

- $P_M(k) = F(k) - F(k-1)$
- $=(1 - (1-p)^k)^n - (1 - (1-p)^{k-1})^n$


- 代入参数。。。


3. 至少需要多少名玩家，才能以至少 $95\%$ 的概率保证在第一轮掷骰中有人掷出 6？给出思路和计算过程。

- L = 1
- P(L = 1)
- $L \sim \text{Geom}\left(1 - (1 - p)^n\right), \quad F_L(k) = 1 - (1 - p)^{nk}$
- $P(L = 1) = F_L(1) = 1 - (1-p)^n >= 0.95$
- (1-p)^n <= 0.05
- $(5/6)^n <= 0.05$
- nln 5/6 <= ln 0.05
- **ln 5/6 < = 0  !!!!**
- n > ln 0.05 / ln 5/6
- n > -2.99 / -0.182 = 16.4
- n = 17


3. $M$ 是否也服从几何分布？请根据 $F_M$ 的形式说明理由，并用 $p = 1/6, n = 4$ 的具体数值来反驳这个猜测。

- $P_M(k) = F(k) - F(k-1)$
- $=(1 - (1-p)^k)^n - (1 - (1-p)^{k-1})^n$
- .... 太复杂

**提示**：对于支撑集为 $\{1, 2, \ldots\}$ 的 $X \sim \text{Geom}(p)$，有 $P(X = k) = (1 - p)^{k-1} p$ 且 $E(X) = 1/p$。对不等式取对数时，**由于 $\ln(1 - p) < 0$，不等号方向会反转。**

#### 21 理解检验——判断正误

判断以下每个陈述为真或假。用最多两句话说明理由，并将错误陈述改正。
1. 若 $g$ 严格单调递减，且 $Y = g(X)$，则恒有 $F_Y(y) = F_X(g^{-1}(y))$。

**错误。** 密度变换使用上面公式需要变换函数单调递增

2. 对于非双射变换，必须将所有有效原像的密度贡献相加。

**确。**

当变换不是一一对应时，同一个像点可能由多个原像映射而来，

3. 若某变换在局部将面积扩大为原来的四倍，则变换后的密度在相应的像点处也要乘以四。

**面积扩大4倍，密度变成1/4**


4. **卷积公式 $f_{X+Y}(z) = \int f_X(x) f_Y(z - x) \, dx$ 可在无需额外条件的下对任意 $X$ 和 $Y$ 使用。**

**错误。**

**该公式需要 X 与 Y 独立**


5. $X + Y$ 的支撑集等于其支撑集的闵可夫斯基和 $T_X + T_Y = \{x + y : x \in T_X, y \in T_Y\}$。

正确

6. 卷积具有交换性：$f_X * f_Y = f_Y * f_X$。

**正确。**

卷积是可交换的：

7. 两个独立的 $(0,1)$ 均匀分布变量之和在 $(0,2)$ 上服从均匀分布。

**错误。**

两个独立均匀分布之和的密度是三角形分布：


8. 对于任意具有有限方差的随机变量，都有 $\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)$。

错误，需要协方差=0 **不相关**


9. 两个独立的泊松分布变量之和仍服从泊松分布，即使两个参数不同也是如此。

泊松可加性，正确

X+Y ~ Poi(lambda1 + lamdab_2)

10. 两个独立的二项分布变量之和仍服从二项分布，即使两个成功概率不同也是如此。

**错误。**

**只有概率相同 X+Y ~ Bin(m+n,p)**

1. 对于独立的 $X_1, \ldots, X_n$，有 $F_{\max}(z) = \prod_{i=1}^n F_{X_i}(z)$。

正确：Fmax(z) = P(max(...) <= z) = P(X1 <= z)P(X2 <= z ) ... = F_x1(z)F_x2(z)...


12. 多个独立随机变量最小值的密度函数，可以通过在每个点处取各单个密度中的最小值得到。



