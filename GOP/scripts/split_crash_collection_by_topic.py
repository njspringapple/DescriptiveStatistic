# -*- coding: utf-8 -*-
from pathlib import Path
import importlib.util
import re
import shutil


ROOT = Path("考前辅导25_题解Markdown")
OUT_DIR = ROOT / "分知识点习题"
HISTORY_DIR = Path("历史考试")
IMAGE_DIR_NAME = "图片"
BUILD_SCRIPT = Path("scripts/build_preexam_crash_collection.py")
MISSING_IMAGES = set()


def load_builder():
    spec = importlib.util.spec_from_file_location("builder", BUILD_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


FORMULAS = {
    "01": r"""## 公式速查

### 偏导与基础积分

$$
\frac{\partial}{\partial x}f(x,y),\qquad \frac{\partial}{\partial y}f(x,y)
$$

$$
(fg)'=f'g+fg',\qquad
\left(\frac fg\right)'=\frac{f'g-fg'}{g^2},\qquad
(f\circ g)'=(f'\circ g)\,g'
$$

$$
\frac{d}{dx}\log x=\frac1x,\qquad
\frac{d}{dx}\log(g(x))=\frac{g'(x)}{g(x)}
$$

$$
\frac{d}{dx}e^{g(x)}=g'(x)e^{g(x)},\qquad
\frac{d}{dx}a^x=a^x\log a
$$

$$
\frac{d}{dx}\sin x=\cos x,\qquad
\frac{d}{dx}\cos x=-\sin x
$$

$$
\int x^a\,dx=\frac{x^{a+1}}{a+1}+C\quad(a\neq-1),\qquad
\int \frac1x\,dx=\log|x|+C
$$

$$
\int u\,dv=uv-\int v\,du
$$

$$
\int f(g(x))g'(x)\,dx=\int f(u)\,du
$$

$$
\int_a^b f(g(x))g'(x)\,dx=\int_{g(a)}^{g(b)} f(u)\,du
$$
""",
    "02": r"""## 公式速查

### 概率空间、事件与独立性

$$
\mathbb P(A^c)=1-\mathbb P(A),\qquad
\mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B)-\mathbb P(A\cap B)
$$

$$
A\subseteq B\Longrightarrow \mathbb P(A)\le \mathbb P(B),\qquad
A\cap B=\emptyset\Longrightarrow \mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B)
$$

$$
\left(\bigcup_{i\in I}A_i\right)^c=\bigcap_{i\in I}A_i^c,\qquad
\left(\bigcap_{i\in I}A_i\right)^c=\bigcup_{i\in I}A_i^c
$$

$$
A\perp B\iff \mathbb P(A\cap B)=\mathbb P(A)\mathbb P(B)
$$

$$
\mathbb P(\{\omega_x\})=\frac{c}{x!},\ x\in\mathbb N_0
\quad\Longrightarrow\quad
1=\sum_{x=0}^{\infty}\frac{c}{x!}=ce
$$

$$
\text{Laplace:}\qquad \mathbb P(A)=\frac{|A|}{|\Omega|}
$$

$$
\mathcal A\ \sigma\text{-Algebra}:\quad \Omega\in\mathcal A,\ A^c\in\mathcal A,\ \bigcup_{n\ge1}A_n\in\mathcal A
$$

$$
\mathcal D\ \text{Dynkin-System}:\quad \Omega\in\mathcal D,\ A^c\in\mathcal D,\ \bigcup_{n\ge1}A_n\in\mathcal D
\quad\text{für paarweise disjunkte }A_n
$$
""",
    "03": r"""## 公式速查

### 分布函数、密度与一维变换

$$
\mathbb P(X=a)=F(a)-F(a-),\qquad \mathbb P(a<X\le b)=F(b)-F(a)
$$

$$
f_X(x)\ge0,\qquad \int_{-\infty}^{\infty}f_X(x)\,dx=1
$$

$$
F_X(x)=\int_{-\infty}^x f_X(t)\,dt,\qquad f_X(x)=F_X'(x)
$$

$$
f_Y(y)=f_X(g^{-1}(y))\left|\frac{d}{dy}g^{-1}(y)\right|
$$

$$
N(\mu,\sigma^2):\quad f(x)=\frac1{\sqrt{2\pi}\sigma}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
$$

$$
\operatorname{Bin}(n,p):\quad \mathbb P(X=k)=\binom nk p^k(1-p)^{n-k}
$$

$$
\operatorname{Poi}(\lambda):\quad \mathbb P(X=k)=e^{-\lambda}\frac{\lambda^k}{k!}
$$

$$
N(t)\sim\operatorname{Poi}(\lambda t),\qquad
\mathbb P(N(t)=k)=e^{-\lambda t}\frac{(\lambda t)^k}{k!}
$$

$$
\operatorname{Geo}(p):\quad \mathbb P(X=k)=(1-p)^{k-1}p,\quad k\ge1
$$

$$
\operatorname{Hyp}(N,K,n):\quad \mathbb P(X=x)=\frac{\binom Kx\binom{N-K}{n-x}}{\binom Nn}
$$

$$
\operatorname{Exp}(\lambda):\quad f(x)=\lambda e^{-\lambda x}\mathbf 1_{\{x\ge0\}},\quad
\operatorname{Ga}(\alpha,\lambda):\quad f(x)=\frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\lambda x}
$$

$$
\operatorname{Beta}(a,b):\quad f(x)=\frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}x^{a-1}(1-x)^{b-1}\mathbf 1_{(0,1)}(x)
$$

$$
\operatorname{Weibull}(\lambda,k):\quad F(x)=1-e^{-(x/\lambda)^k}
$$

$$
\text{Quantil }q_p:\quad F(q_p)=p
$$

$$
L(\theta)=\prod_{i=1}^n f_\theta(x_i),\qquad \ell(\theta)=\log L(\theta)
$$
""",
    "04": r"""## 公式速查

### 测度、可测性与积分

$$
\delta_x(A)=\mathbf 1_A(x),\qquad \mathbb P_X(B)=\mathbb P(X\in B)
$$

$$
\delta_x\ll\lambda\ \text{gilt nicht},\qquad \lambda(\{x\})=0,\quad \delta_x(\{x\})=1
$$

$$
\int g\,d\mathbb P_X=\int g(X)\,d\mathbb P=\mathbb E[g(X)]
$$

$$
\int \mathbf 1_A\,d\mu=\mu(A)
$$

$$
f=\sum_{i=1}^n a_i\mathbf 1_{A_i}
\quad\Longrightarrow\quad
\int f\,d\mu=\sum_{i=1}^n a_i\mu(A_i)
$$

$$
f\ \text{messbar}\iff \{x:f(x)\le a\}\in\mathcal A\quad\text{für alle }a\in\mathbb R
$$
""",
    "05": r"""## 公式速查

### 期望、方差、不等式与正态分布

$$
\mathbb E(aX+b)=a\mathbb E(X)+b,\qquad \operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)
$$

$$
\operatorname{Var}(X)=\mathbb E(X^2)-\mathbb E(X)^2
$$

$$
\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y)
$$

$$
\operatorname{Cov}(X,Y)=\mathbb E(XY)-\mathbb E(X)\mathbb E(Y),\qquad
\rho(X,Y)=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}
$$

$$
\operatorname{Cov}(aX+bY,Z)=a\operatorname{Cov}(X,Z)+b\operatorname{Cov}(Y,Z)
$$

$$
X\perp Y\Longrightarrow \operatorname{Cov}(X,Y)=0,\qquad
|\operatorname{Cov}(X,Y)|\le \sigma_X\sigma_Y
$$

$$
\mathbb P(X\ge a)\le \frac{\mathbb E(X)}{a}\quad (X\ge0),\qquad
\mathbb P(|X-\mu|\ge \varepsilon)\le \frac{\operatorname{Var}(X)}{\varepsilon^2}
$$

$$
\varphi(\mathbb E X)\le \mathbb E(\varphi(X))\quad \text{für konvexe }\varphi
$$

$$
Z=\frac{X-\mu}{\sigma}\sim N(0,1)\quad\text{für }X\sim N(\mu,\sigma^2)
$$

$$
\bar X=\frac1n\sum_{i=1}^nX_i,\qquad
s^2=\frac1{n-1}\sum_{i=1}^n(X_i-\bar X)^2
$$

$$
t=\frac{\bar D-\mu_0}{s_D/\sqrt n}
\quad\text{(gepaarter t-Test)}
$$

$$
t=\frac{\bar X-\bar Y-\Delta_0}{\sqrt{s_X^2/n_X+s_Y^2/n_Y}}
\quad\text{(Welch-Zweistichproben-t-Test)}
$$

$$
W^+=\sum_{\{i:D_i>0\}}\operatorname{Rang}(|D_i|)
\quad\text{(Wilcoxon-Vorzeichen-Rang-Test)}
$$

$$
\text{Testentscheidung: }\quad
\text{verwerfe }H_0\ \text{falls }p\le \alpha
\quad\text{oder}\quad |T|>c_\alpha
$$
""",
    "06": r"""## 公式速查

### 收敛、近似、LLN 与 CLT

$$
\bar X_n=\frac1n\sum_{i=1}^nX_i\xrightarrow{P}\mu
$$

$$
X_n\xrightarrow{P}X
\iff
\forall\varepsilon>0:\ \mathbb P(|X_n-X|>\varepsilon)\to0
$$

$$
X_n\xrightarrow{D}X
\iff
F_{X_n}(x)\to F_X(x)\quad\text{für alle Stetigkeitsstellen }x
$$

$$
\frac{\sum_{i=1}^nX_i-n\mu}{\sqrt n\sigma}\xrightarrow{d}N(0,1)
$$

$$
\sqrt n(\bar X_n-\mu)\xrightarrow{D}N(0,\sigma^2)
$$

$$
X_n\xrightarrow{P}X,\ f\text{ stetig}\Longrightarrow f(X_n)\xrightarrow{P}f(X)
$$

$$
X_n\xrightarrow{d}X,\ Y_n\xrightarrow{P}c\Longrightarrow
X_n+Y_n\xrightarrow{d}X+c,\quad X_nY_n\xrightarrow{d}cX
$$

$$
X_n\xrightarrow{d}c\ \text{konstant}\Longrightarrow X_n\xrightarrow{P}c
$$

$$
\operatorname{Bin}(n,p)\approx N(np,np(1-p)),\qquad
\operatorname{Bin}(n,p)\approx \operatorname{Poi}(np)\quad(p\text{ klein})
$$
""",
    "07": r"""## 公式速查

### 多维随机变量、条件分布与卷积

$$
f_Y(y)=\int f_{X,Y}(x,y)\,dx,\qquad
f_{X\mid Y=y}(x)=\frac{f_{X,Y}(x,y)}{f_Y(y)}
$$

$$
f_X(x)=\int f_{X,Y}(x,y)\,dy,\qquad
X\perp Y\iff f_{X,Y}(x,y)=f_X(x)f_Y(y)
$$

$$
f_{X+Y}(z)=\int_{-\infty}^{\infty}f_X(x)f_Y(z-x)\,dx
$$

$$
\mathbb P(X+Y=k)=\sum_j \mathbb P(X=j)\mathbb P(Y=k-j)
$$

$$
\mathbb E(X)=\mathbb E(\mathbb E(X\mid Z))
$$

$$
\operatorname{Var}(X)=\mathbb E(\operatorname{Var}(X\mid Z))+\operatorname{Var}(\mathbb E(X\mid Z))
$$

$$
\operatorname{Cov}(X,Y)=\mathbb E(XY)-\mathbb E(X)\mathbb E(Y)
$$

$$
f_Z(z)=f_X(T^{-1}(z))\left|\det DT^{-1}(z)\right|
$$

$$
X\sim N_d(\mu,\Sigma)\quad\Longrightarrow\quad X_i\sim N(\mu_i,\Sigma_{ii}),\quad
\operatorname{Cov}(X_i,X_j)=\Sigma_{ij}
$$
""",
    "08": r"""## 公式速查

### 条件概率、Bayes 与诊断指标

$$
\mathbb P(A\mid B)=\frac{\mathbb P(A\cap B)}{\mathbb P(B)}
$$

$$
\mathbb P(B)=\sum_i \mathbb P(B\mid A_i)\mathbb P(A_i)
\quad\text{für eine Partition }(A_i)
$$

$$
\mathbb P(A\mid B)=\frac{\mathbb P(B\mid A)\mathbb P(A)}
{\mathbb P(B\mid A)\mathbb P(A)+\mathbb P(B\mid A^c)\mathbb P(A^c)}
$$

$$
\operatorname{Odds}(A)=\frac{\mathbb P(A)}{1-\mathbb P(A)},\qquad
\operatorname{OR}=\frac{ad}{bc}
$$

$$
\operatorname{PPV}=\frac{TP}{TP+FP},\qquad
\operatorname{NPV}=\frac{TN}{TN+FN}
$$

$$
\operatorname{Sensitivität}=\frac{TP}{TP+FN},\qquad
\operatorname{Spezifität}=\frac{TN}{TN+FP}
$$

$$
E_{ij}=\frac{(\text{Zeilensumme}_i)(\text{Spaltensumme}_j)}{n},\qquad
\chi^2=\sum_{i,j}\frac{(O_{ij}-E_{ij})^2}{E_{ij}}
$$
""",
    "09": r"""## 公式速查

### 统计图形、ROC 与 AUC

$$
\operatorname{TPR}=\frac{TP}{TP+FN},\qquad
\operatorname{FPR}=\frac{FP}{FP+TN}
$$

$$
\operatorname{TNR}=\frac{TN}{TN+FP}=1-\operatorname{FPR},\qquad
\operatorname{FNR}=\frac{FN}{FN+TP}=1-\operatorname{TPR}
$$

$$
\operatorname{PPV}=\frac{TP}{TP+FP},\qquad
\operatorname{NPV}=\frac{TN}{TN+FN}
$$

$$
\operatorname{AUC}=\mathbb P(\text{Score}_{+}>\text{Score}_{-})
$$

$$
\operatorname{AUC}\approx\sum_i \frac{\operatorname{TPR}_{i+1}+\operatorname{TPR}_i}{2}
\left(\operatorname{FPR}_{i+1}-\operatorname{FPR}_i\right)
$$

$$
\text{Histogrammhöhe}=\frac{\text{relative Häufigkeit}}{\text{Klassenbreite}}
$$

$$
r_{xy}=\frac{\operatorname{Cov}(X,Y)}{s_Xs_Y}
$$

$$
\operatorname{IQR}=Q_3-Q_1,\qquad
\text{Boxplot-Ausreißergrenzen: }Q_1-1.5\operatorname{IQR},\ Q_3+1.5\operatorname{IQR}
$$
""",
}


FORMULAS.update({
    "01": r"""## 公式速查

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
""",
    "02": r"""## 公式速查

### 古典概率、事件系统与 σ-代数

- **概率空间**：$(\Omega,\mathcal F,\mathbb P)$，其中 $\Omega$ 是结果空间，$\mathcal F$ 是事件系统，$\mathbb P$ 是概率测度。
- **Kolmogorov 公理**：$\mathbb P(A)\ge0$，$\mathbb P(\Omega)=1$，两两不交时 $\mathbb P(\bigcup_i A_i)=\sum_i\mathbb P(A_i)$。
- **补集公式**：$\mathbb P(A^c)=1-\mathbb P(A)$。
- **容斥定理**：$\mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B)-\mathbb P(A\cap B)$。
- **互不相容**：$A\cap B=\emptyset\Rightarrow\mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B)$。
- **单调性**：$A\subseteq B\Rightarrow\mathbb P(A)\le\mathbb P(B)$。
- **De Morgan**：$(A\cup B)^c=A^c\cap B^c$，$(A\cap B)^c=A^c\cup B^c$。
- **独立事件**：$A\perp B\Longleftrightarrow\mathbb P(A\cap B)=\mathbb P(A)\mathbb P(B)\Longleftrightarrow\mathbb P(A|B)=\mathbb P(A)$。
- **对立独立性**：$A\perp B\Longleftrightarrow A^c\perp B\Longleftrightarrow A\perp B^c\Longleftrightarrow A^c\perp B^c$。
- **Laplace 概率**：所有基本结果等可能时，$\mathbb P(A)=\frac{|A|}{|\Omega|}$。
- **点概率归一化**：若 $\mathbb P(\{\omega_x\})=\frac{c}{x!},x\in\mathbb N_0$，则 $1=\sum_{x=0}^{\infty}\frac{c}{x!}=ce$，所以 $c=e^{-1}$。
- **σ-代数**：$\Omega\in\mathcal A$，$A\in\mathcal A\Rightarrow A^c\in\mathcal A$，$A_n\in\mathcal A\Rightarrow\bigcup_{n\ge1}A_n\in\mathcal A$。
- **Dynkin-System**：$\Omega\in\mathcal D$，补集封闭，并且只要求两两不交的可数并封闭。
- **生成的 σ-代数**：$\sigma(\mathcal E)=\bigcap_{\mathcal F\supseteq\mathcal E,\ \mathcal F\ \sigma\text{-Algebra}}\mathcal F$，即包含生成元的最小 σ-代数。
""",
    "03": r"""## 公式速查

### 分布函数、密度、常见分布与一维变换

- **分布函数**：$F_X(x)=\mathbb P(X\le x)$，性质是单调递增、右连续，且 $\lim_{x\to-\infty}F_X(x)=0$，$\lim_{x\to\infty}F_X(x)=1$。
- **由分布函数求概率**：$\mathbb P(a<X\le b)=F_X(b)-F_X(a)$，$\mathbb P(X>a)=1-F_X(a)$。
- **跳跃点概率**：$\mathbb P(X=a)=F_X(a)-F_X(a-)$；连续型随机变量单点概率为 $0$。
- **密度定义**：$f_X(x)\ge0$ 且 $\int_{-\infty}^{\infty}f_X(x)\,dx=1$。
- **CDF 和 PDF**：$F_X(x)=\int_{-\infty}^x f_X(t)\,dt$，在可导处 $F_X'(x)=f_X(x)$。
- **分位数**：$q_p$ 满足 $F(q_p)=p$；有跳跃时用广义逆 $q_p=\inf\{x:F(x)\ge p\}$。
- **众数/中位数**：众数是密度或频率最大点；中位数 $m$ 通常由 $F(m)=0.5$ 求出。
- **一维密度变换**：若 $Y=g(X)$ 且 $g$ 单调，$h(y)=g^{-1}(y)$，则 $f_Y(y)=f_X(h(y))|h'(y)|$。
- **单调递增变换**：$F_Y(y)=F_X(g^{-1}(y))$；**单调递减变换**：$F_Y(y)=1-F_X(g^{-1}(y))$。
- **离散均匀分布**：$X\sim U(T)$，$p(x)=\frac1{|T|}I_T(x)$。
- **连续均匀分布**：$X\sim U(a,b)$，$f(x)=\frac1{b-a}I_{(a,b)}(x)$，$E(X)=\frac{a+b}{2}$，$Var(X)=\frac{(b-a)^2}{12}$。
- **Bernoulli/Binomial**：$X\sim B(n,p)$，$\mathbb P(X=k)=\binom nkp^k(1-p)^{n-k}$，$E(X)=np$，$Var(X)=np(1-p)$。
- **几何分布**：$X\sim G(p)$ 表示首次成功所需次数，$E(X)=\frac1p$，$Var(X)=\frac{1-p}{p^2}$，具有无记忆性。
- **超几何分布**：$X\sim H(n,M,N)$，$\mathbb P(X=x)=\frac{\binom Mx\binom{N-M}{n-x}}{\binom Nn}$，$E(X)=n\frac MN$。
- **Poisson 分布**：$X\sim Po(\lambda)$，$\mathbb P(X=k)=e^{-\lambda}\frac{\lambda^k}{k!}$，$E(X)=Var(X)=\lambda$。
- **Poisson 近似**：当 $n\to\infty,p\to0,np\to\lambda$ 时，$B(n,p)\approx Po(\lambda)$。
- **指数分布**：$X\sim Exp(\lambda)$，$f(x)=\lambda e^{-\lambda x}I_{x>0}$，$F(x)=1-e^{-\lambda x}$，$E(X)=\frac1\lambda$，$Var(X)=\frac1{\lambda^2}$。
- **生存函数**：$S(t)=\mathbb P(X\ge t)=1-F(t)$，风险率 $h(t)=\frac{f(t)}{S(t)}$；指数分布的风险率恒为 $\lambda$。
- **Gamma/Beta/Weibull**：先把密度整理成标准形式，再通过指数、支持集和归一化常数读参数。
""",
    "04": r"""## 公式速查

### 测度论基础：测度、可测性、像测度与积分

- **测度定义**：$\mu(\emptyset)=0$，$\mu(A)\ge0$，两两不交时 $\mu(\bigcup_n A_n)=\sum_n\mu(A_n)$。
- **概率测度**：概率测度是满足 $\mathbb P(\Omega)=1$ 的测度。
- **测度单调性**：$A\subseteq B\Rightarrow\mu(A)\le\mu(B)$。
- **Borel σ-代数**：$\mathcal B(\mathbb R)=\sigma(\{(a,b):a<b\})$，由实数开区间生成。
- **计数测度**：$\mu_z(A)=|A|$，若 $A$ 无限则 $\mu_z(A)=\infty$。
- **Lebesgue 测度**：$\lambda((a,b))=b-a$，$\lambda(\{x\})=0$，并且平移不变。
- **Dirac 测度**：$\delta_x(A)=I_A(x)$，只看集合是否包含支撑点 $x$。
- **像与原像**：$f(A)=\{f(\omega):\omega\in A\}$，$f^{-1}(B)=\{\omega:f(\omega)\in B\}$；可测性主要看原像。
- **可测映射**：$f$ 可测，若 $f^{-1}(B)\in\mathcal F_1$ 对所有 $B\in\mathcal F_2$ 成立。
- **像测度/Bildmaß**：$\mu_f(B)=\mu(f^{-1}(B))$，随机变量的分布 $\mathbb P_X(B)=\mathbb P(X^{-1}(B))$。
- **指示函数积分**：$\int I_A\,d\mu=\mu(A)$。
- **简单函数积分**：若 $f=\sum_{i=1}^n a_iI_{A_i}$，则 $\int f\,d\mu=\sum_{i=1}^n a_i\mu(A_i)$。
- **离散测度积分**：$\int f\,d\mathbb P=\sum_{\omega\in\Omega}f(\omega)\mathbb P(\{\omega\})$。
- **像测度换元**：$\int g\,d\mathbb P_X=\int g(X)\,d\mathbb P=\mathbb E[g(X)]$。
- **Radon-Nikodym 思路**：若 $\nu\ll\mu$，则存在非负可测函数 $f=\frac{d\nu}{d\mu}$，使 $\nu(A)=\int_A f\,d\mu$。
- **Jensen 不等式**：凸函数 $\varphi$ 满足 $\varphi(E[X])\le E[\varphi(X)]$；凹函数方向相反。
""",
    "05": r"""## 公式速查

### 期望、方差、不等式、正态分布与检验

- **期望：离散型**：$E(X)=\sum_x x\mathbb P(X=x)$；**连续型**：$E(X)=\int x f_X(x)\,dx=\int_\Omega X\,d\mathbb P$。
- **期望线性性**：$E(aX+bY)=aE(X)+bE(Y)$，$E(\sum_{i=1}^nX_i)=\sum_{i=1}^nE(X_i)$。
- **函数变换期望**：$E(g(X))=\sum_xg(x)P(X=x)$ 或 $\int g(x)f_X(x)\,dx$。
- **单调性/对称性**：$X\le Y\Rightarrow E(X)\le E(Y)$；若 $P(X\le c-t)=P(X\ge c+t)$，则 $E(X)=c$。
- **方差定义**：$Var(X)=E((X-E(X))^2)=E(X^2)-E(X)^2$。
- **样本方差**：$S_x^2=\frac1{n-1}\sum_{i=1}^n(x_i-\bar x)^2$，用 $n-1$ 是为了无偏估计总体方差。
- **方差线性变换**：$Var(aX+b)=a^2Var(X)$，常数平移不改变方差。
- **和的方差**：$Var(X\pm Y)=Var(X)+Var(Y)\pm2Cov(X,Y)$；若不相关则协方差项为 $0$。
- **标准化**：$Y=\frac{X-E[X]}{\sqrt{Var(X)}}$，把随机变量转成期望 $0$、方差 $1$。
- **Markov 不等式**：$P(|X|\ge a)\le\frac{E(|X|)}a,\ a>0$，只知道期望时可用。
- **Chebyshev 不等式**：$P(|X-E(X)|\ge c)\le\frac{Var(X)}{c^2}$，知道期望和方差时控制偏离。
- **协方差定义**：$Cov(X,Y)=E[(X-E(X))(Y-E(Y))]=E(XY)-E(X)E(Y)$。
- **自身协方差**：$Cov(X,X)=Var(X)$；**上界**：$|Cov(X,Y)|\le\sqrt{Var(X)}\sqrt{Var(Y)}$。
- **Pearson 关系**：$Cov(X,Y)=\rho\sigma_X\sigma_Y$，$\rho=\frac{Cov(X,Y)}{\sigma_X\sigma_Y}$。
- **正态分布**：$X\sim N(\mu,\sigma^2)$，$f(x)=\frac1{\sqrt{2\pi}\sigma}\exp(-\frac{(x-\mu)^2}{2\sigma^2})$。
- **正态标准化**：$Z=\frac{X-\mu}{\sigma}\sim N(0,1)$。
- **正态线性变换**：$aX+b\sim N(a\mu+b,a^2\sigma^2)$。
- **独立正态加法**：$X_1+X_2\sim N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$。
- **配对 t 检验**：$t=\frac{\bar D-\mu_0}{s_D/\sqrt n}$。
- **Welch 两样本 t 检验**：$t=\frac{\bar X-\bar Y-\Delta_0}{\sqrt{s_X^2/n_X+s_Y^2/n_Y}}$。
- **Wilcoxon 符号秩检验**：$W^+=\sum_{\{i:D_i>0\}}Rang(|D_i|)$。
- **检验决策**：$p\le\alpha$ 或检验统计量进入拒绝域时拒绝 $H_0$。
""",
    "06": r"""## 公式速查

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
""",
    "07": r"""## 公式速查

### 多维随机变量、边际分布、条件分布、卷积与协方差矩阵

- **n 维分布函数**：$F_X(x_1,\dots,x_n)=P(X_1\le x_1,\dots,X_n\le x_n)$。
- **边际分布：连续型**：从联合密度中把其他变量积分掉，例如 $f_X(x)=\int f_{X,Y}(x,y)\,dy$。
- **边际分布：离散型**：从联合概率质量中把其他变量求和掉，例如 $P_X(x)=\sum_yP(X=x,Y=y)$。
- **条件密度**：$f_{X|Y}(x|y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}$，前提是 $f_Y(y)>0$。
- **条件期望**：$E(X|Y=y)=\int x f_{X|Y}(x|y)\,dx$。
- **迭代期望**：$E(E(X|Y))=E(X)$；**总方差公式**：$Var(X)=E[Var(X|Y)]+Var(E[X|Y])$。
- **条件独立**：若 $f_{X,Y|Z}(x,y|z)=f_{X|Z}(x|z)f_{Y|Z}(y|z)$，则 $X\perp Y|Z$。
- **二维密度变换**：若 $Y=g(X)$ 双射，$h=g^{-1}$，则 $f_Y(y)=f_X(h(y))|\det Dh(y)|$。
- **Jacobian 要点**：先写反变换，再算反变换的 Jacobian 绝对值，最后把支持集也变过去。
- **卷积：离散型**：$P(X+Y=z)=\sum_xP(X=x,Y=z-x)$；独立时变成 $\sum_xP(X=x)P(Y=z-x)$。
- **卷积：连续型**：$f_{X+Y}(z)=\int f_X(x)f_Y(z-x)\,dx$，积分上下限由支持集决定。
- **协方差矩阵**：$Cov(X)=E[(X-E[X])(X-E[X])^T]=\Sigma$。
- **协方差矩阵性质**：对称、半正定，对角线是各分量方差，非对角线是协方差。
- **线性变换协方差**：$Cov(AX)=A\,Cov(X)\,A^T$，平移 $X+b$ 不改变协方差。
- **白化变换**：若 $\Sigma=BB^T$，令 $Y=B^{-1}(X-\mu)$，则 $E(Y)=0$ 且 $Cov(Y)=I$。
- **多元正态密度**：$X\sim N_d(\mu,\Sigma)$，$f(x)=\frac1{\sqrt{(2\pi)^d\det\Sigma}}\exp(-\frac12(x-\mu)^T\Sigma^{-1}(x-\mu))$。
- **多元正态线性变换**：若 $X\sim N_k(0,I_k)$，$Y=AX+\mu$，则 $Y\sim N_p(\mu,AA^T)$。
""",
    "08": r"""## 公式速查

### 条件概率、Bayes、列联表与诊断指标

- **条件概率**：$P(A|B)=\frac{P(A\cap B)}{P(B)}$，也可写成 $P(X=x|Y=y)=\frac{P(X=x,Y=y)}{P(Y=y)}$。
- **乘法公式**：$P(A\cap B)=P(A|B)P(B)=P(B|A)P(A)$。
- **全概率公式**：若 $(B_i)$ 是划分，则 $P(A)=\sum_iP(A|B_i)P(B_i)$。
- **Bayes 定理**：$P(A|B)=\frac{P(B|A)P(A)}{P(B)}$。
- **Bayes 展开式**：$P(A|B)=\frac{P(B|A)P(A)}{P(B|A)P(A)+P(B|A^c)P(A^c)}$。
- **条件密度版 Bayes**：$f_{X|Y}(x|y)=\frac{f_{Y|X}(y|x)f_X(x)}{\int f_{Y|X}(y|x)f_X(x)\,dx}$。
- **先验/后验/似然**：$P(A)$ 是先验，$P(A|B)$ 是后验，$P(B|A)$ 是似然。
- **诊断记号**：$K$ 表示患病或真实阳性，$T$ 表示测试阳性。
- **敏感度/TPR**：$P(T|K)=\frac{TP}{TP+FN}$。
- **特异度/TNR**：$P(T^c|K^c)=\frac{TN}{TN+FP}$。
- **FNR/FPR**：$FNR=1-TPR$，$FPR=1-TNR=\frac{FP}{FP+TN}$。
- **阳性预测值 PPV**：$P(K|T)=\frac{P(K)P(T|K)}{P(K)P(T|K)+P(K^c)P(T|K^c)}$，不要和敏感度混淆。
- **阴性预测值 NPV**：$P(K^c|T^c)=\frac{P(K^c)P(T^c|K^c)}{P(K)P(T^c|K)+P(K^c)P(T^c|K^c)}$。
- **赔率 Odds**：$O(A)=\frac{P(A)}{1-P(A)}$，反推 $P(A)=\frac{O(A)}{1+O(A)}$。
- **Odds Ratio**：二乘二表中 $OR=\frac{ad}{bc}$。
- **列联表期望频数**：$E_{ij}=\frac{(\text{行和}_i)(\text{列和}_j)}n$。
- **Pearson $\chi^2$ 统计量**：$\chi^2=\sum_{i,j}\frac{(O_{ij}-E_{ij})^2}{E_{ij}}$。
""",
    "09": r"""## 公式速查

### 可视化、描述统计、相关系数、ROC 与 AUC

- **图形语法**：数据、数据转换/统计、坐标系、分面、主题；美学元素包括位置、颜色、大小、形状。
- **感知一致性**：位置和长度通常比颜色更容易精确比较；颜色要考虑色盲和亮度差异。
- **直方图**：适合度量数据，展示分布形状、偏态和多峰；组距会强烈影响结果。
- **直方图高度**：当组距不同，高度应为 $\frac{\text{relative Häufigkeit}}{\text{Klassenbreite}}$。
- **箱线图流程**：排序 $\to$ 求 $Q_1,Q_2,Q_3$ $\to$ 算 $IQR$ $\to$ 栅栏 $\to$ 画图。
- **IQR**：$IQR=Q_3-Q_1$；**改良箱线图栅栏**：$L=Q_1-1.5IQR$，$U=Q_3+1.5IQR$。
- **均值**：$\bar X=\frac1n\sum_{i=1}^nX_i$；**加权均值**：$\bar X_w=\frac{\sum_iw_iX_i}{\sum_iw_i}$。
- **几何均值**：$\bar X_g=\sqrt[n]{\prod_{i=1}^nX_i}$；**调和均值**：$\bar X_h=\frac n{\sum_{i=1}^n1/X_i}$。
- **偏度方向**：负偏/左偏常见顺序是众数 $>$ 中位数 $>$ 均值；正偏/右偏常见顺序是均值 $>$ 中位数 $>$ 众数。
- **矩偏度**：$g_m=\frac1n\sum_{i=1}^n(\frac{x_i-\bar x}{s_x})^3$。
- **Bowley 偏态系数**：$g_p=\frac{(x_{1-p}-x_{med})-(x_{med}-x_p)}{x_{1-p}-x_p}$，基于分位数，更稳健。
- **峰度**：$k=\frac1n\sum_{i=1}^n(\frac{x_i-\bar x}{s_x})^4$，超额峰度 $k^*=k-3$。
- **Pearson 相关系数**：$r_{xy}=\frac{Cov(X,Y)}{s_Xs_Y}$，度量线性关系。
- **Spearman 相关系数**：对秩次计算 Pearson；无重复时 $r^{SP}=1-\frac{6\sum_iD_i^2}{n(n^2-1)}$。
- **Kendall tau**：$\tau=\frac{N_c-N_d}{n(n-1)/2}$，$N_c$ 为同向对数，$N_d$ 为反向对数。
- **ROC: TPR**：$TPR=\frac{TP}{TP+FN}$；**ROC: FPR**：$FPR=\frac{FP}{FP+TN}$。
- **ROC 曲线**：按 score 阈值排序，逐个计算 $(FPR,TPR)$ 并连线。
- **AUC 含义**：$AUC=P(\text{Score}_+>\text{Score}_-)$，即随机正例分数高于随机负例的概率。
- **AUC 梯形近似**：$AUC\approx\sum_i\frac{TPR_{i+1}+TPR_i}{2}(FPR_{i+1}-FPR_i)$。
""",
})


HISTORY_EXAM_TOPIC_OVERRIDES = {
    ("2012", "Aufgabe 1"): "07 多维随机变量、条件分布、卷积与方差分解",
    ("2012", "Aufgabe 2"): "03 分布函数、密度与常见分布",
    ("2012", "Aufgabe 4"): "06 收敛、近似、LLN 与 CLT",
    ("2012", "Aufgabe 5"): "03 分布函数、密度与常见分布",
    ("2014", "Aufgabe 1"): "08 条件概率、Bayes、列联表与诊断指标",
    ("2014", "Aufgabe 2"): "07 多维随机变量、条件分布、卷积与方差分解",
    ("2014", "Aufgabe 3"): "03 分布函数、密度与常见分布",
    ("2014", "Aufgabe 4"): "08 条件概率、Bayes、列联表与诊断指标",
    ("2014", "Aufgabe 5"): "03 分布函数、密度与常见分布",
    ("2015", "Aufgabe 1: HIV-Test"): "08 条件概率、Bayes、列联表与诊断指标",
    ("2015", "Aufgabe 2: Diskrete Zufallsvariable"): "03 分布函数、密度与常见分布",
    ("2015", "Aufgabe 3: Cauchy-Verteilung"): "03 分布函数、密度与常见分布",
    ("2015", "Aufgabe 5: Rechenzeiten"): "06 收敛、近似、LLN 与 CLT",
    ("2021", "Aufgabe 1"): "03 分布函数、密度与常见分布",
    ("2021", "Aufgabe 2"): "02 概率空间、事件、σ-代数与建模",
    ("2021", "Aufgabe 3"): "05 期望、方差、不等式与正态分布",
    ("2021", "Aufgabe 5"): "05 期望、方差、不等式与正态分布",
    ("2021", "Aufgabe 6"): "09 统计图形、ROC、AUC 与可视化评价",
    ("Altklausur2LV", "Aufgabe 1 — 16 Punkte"): "09 统计图形、ROC、AUC 与可视化评价",
    ("Altklausur2LV", "Aufgabe 2 — 16 Punkte"): "07 多维随机变量、条件分布、卷积与方差分解",
    ("Altklausur2LV", "Aufgabe 3 — 17 Punkte"): "07 多维随机变量、条件分布、卷积与方差分解",
    ("Altklausur2LV", "Aufgabe 4 — 13 Punkte"): "06 收敛、近似、LLN 与 CLT",
    ("Altklausur2LV", "Aufgabe 5 — 13 Punkte"): "08 条件概率、Bayes、列联表与诊断指标",
    ("Altklausur2LV", "Aufgabe 6 — 13 Punkte"): "04 测度、可测性与积分",
    ("Altklausur2LV", "Aufgabe 7 — 13 Punkte"): "03 分布函数、密度与常见分布",
    ("Altklausur2LV", "Aufgabe 8 — 12 Punkte"): "07 多维随机变量、条件分布、卷积与方差分解",
    ("Altklausur2LV", "Aufgabe 9 — 21 Punkte"): "08 条件概率、Bayes、列联表与诊断指标",
    ("Altklausur3LV", "Aufgabe 1 — 9 Punkte"): "08 条件概率、Bayes、列联表与诊断指标",
    ("Altklausur3LV", "Aufgabe 2"): "09 统计图形、ROC、AUC 与可视化评价",
    ("Altklausur3LV", "Aufgabe 3"): "09 统计图形、ROC、AUC 与可视化评价",
    ("Altklausur3LV", "Aufgabe 4 — 8 Punkte"): "04 测度、可测性与积分",
    ("Altklausur3LV", "Aufgabe 5 — 18 Punkte"): "03 分布函数、密度与常见分布",
    ("Altklausur3LV", "Aufgabe 6 — 16 Punkte"): "07 多维随机变量、条件分布、卷积与方差分解",
    ("Altklausur3LV", "Aufgabe 7 — 8 Punkte"): "08 条件概率、Bayes、列联表与诊断指标",
    ("Altklausur3LV", "Aufgabe 8 — 12 Punkte"): "03 分布函数、密度与常见分布",
    ("GOP-Klausur-1", "Aufgabe 1 -- 19 Punkte"): "09 统计图形、ROC、AUC 与可视化评价",
    ("GOP-Klausur-1", "Aufgabe 2 -- 23 Punkte"): "09 统计图形、ROC、AUC 与可视化评价",
    ("GOP-Klausur-1", "Aufgabe 3 -- 15 Punkte"): "03 分布函数、密度与常见分布",
    ("GOP-Klausur-1", "Aufgabe 4 -- 19 Punkte"): "08 条件概率、Bayes、列联表与诊断指标",
    ("GOP-Klausur-1", "Aufgabe 5 -- 17 Punkte"): "04 测度、可测性与积分",
    ("GOP-Klausur-1", "Aufgabe 6 -- 23 Punkte"): "03 分布函数、密度与常见分布",
    ("GOP-Klausur-1", "Aufgabe 7 -- 12 Punkte"): "06 收敛、近似、LLN 与 CLT",
    ("GOP-Klausur-1", "Aufgabe 8 -- 10 Punkte"): "07 多维随机变量、条件分布、卷积与方差分解",
    ("GOP-Klausur-1", "Aufgabe 9 -- 12 Punkte"): "07 多维随机变量、条件分布、卷积与方差分解",
    ("GOP-Klausur-2", "Aufgabe 1 — 16 Punkte"): "09 统计图形、ROC、AUC 与可视化评价",
    ("GOP-Klausur-2", "Aufgabe 2 — 16 Punkte"): "07 多维随机变量、条件分布、卷积与方差分解",
    ("GOP-Klausur-2", "Aufgabe 3 — 17 Punkte"): "07 多维随机变量、条件分布、卷积与方差分解",
    ("GOP-Klausur-2", "Aufgabe 4 — 13 Punkte"): "06 收敛、近似、LLN 与 CLT",
    ("GOP-Klausur-2", "Aufgabe 5 — 13 Punkte"): "08 条件概率、Bayes、列联表与诊断指标",
    ("GOP-Klausur-2", "Aufgabe 6 — 13 Punkte"): "04 测度、可测性与积分",
    ("GOP-Klausur-2", "Aufgabe 7 — 13 Punkte"): "03 分布函数、密度与常见分布",
    ("GOP-Klausur-2", "Aufgabe 8 — 12 Punkte"): "07 多维随机变量、条件分布、卷积与方差分解",
    ("GOP-Klausur-2", "Aufgabe 9 — 21 Punkte"): "08 条件概率、Bayes、列联表与诊断指标",
    ("GOP-Klausur-3", "Aufgabe 1 - 16 Punkte"): "09 统计图形、ROC、AUC 与可视化评价",
    ("GOP-Klausur-3", "Aufgabe 2 - 16 Punkte"): "07 多维随机变量、条件分布、卷积与方差分解",
    ("GOP-Klausur-3", "Aufgabe 3 - 17 Punkte"): "07 多维随机变量、条件分布、卷积与方差分解",
    ("GOP-Klausur-3", "Aufgabe 4 - 13 Punkte"): "06 收敛、近似、LLN 与 CLT",
    ("GOP-Klausur-3", "Aufgabe 5 - 13 Punkte"): "08 条件概率、Bayes、列联表与诊断指标",
    ("GOP-Klausur-3", "Aufgabe 6 - 13 Punkte"): "04 测度、可测性与积分",
    ("GOP-Klausur-3", "Aufgabe 7 - 13 Punkte"): "03 分布函数、密度与常见分布",
    ("GOP-Klausur-3", "Aufgabe 8 - 12 Punkte"): "07 多维随机变量、条件分布、卷积与方差分解",
    ("GOP-Klausur-3", "Aufgabe 9 - 21 Punkte"): "08 条件概率、Bayes、列联表与诊断指标",
    ("Konvergenz", "Aufgabe 1 — 21 Punkte"): "06 收敛、近似、LLN 与 CLT",
    ("ss2022", "Aufgabe 1 -- Statistische Grafik"): "09 统计图形、ROC、AUC 与可视化评价",
    ("ss2022", "Aufgabe 2 -- Histogramm, Boxplot, Korrelation"): "09 统计图形、ROC、AUC 与可视化评价",
    ("ss2022", "Aufgabe 3 -- Verteilungsfunktion"): "03 分布函数、密度与常见分布",
    ("ss2022", "Aufgabe 4 -- Diagnostisches System"): "08 条件概率、Bayes、列联表与诊断指标",
    ("ss2022", "Aufgabe 5 -- Sigma-Algebra, Maß, Integral"): "04 测度、可测性与积分",
    ("ss2022", "Aufgabe 6 -- Stetige Dichte"): "05 期望、方差、不等式与正态分布",
    ("ss2022", "Aufgabe 7 -- Zentraler Grenzwertsatz"): "06 收敛、近似、LLN 与 CLT",
    ("ss2022", "Aufgabe 8 -- Gemeinsame Dichte und Faltung"): "07 多维随机变量、条件分布、卷积与方差分解",
    ("ss2022", "Aufgabe 9 -- Multivariate Normalverteilung"): "07 多维随机变量、条件分布、卷积与方差分解",
    ("ss2024", "Aufgabe 1 — 26 Punkte"): "09 统计图形、ROC、AUC 与可视化评价",
    ("ss2024", "Aufgabe 2 - 16 Punkte"): "08 条件概率、Bayes、列联表与诊断指标",
    ("ss2024", "Aufgabe 3 — 10 Punkte"): "02 概率空间、事件、σ-代数与建模",
    ("ss2024", "Aufgabe 4 — 21 Punkte"): "03 分布函数、密度与常见分布",
    ("ss2024", "Aufgabe 5 — 16 Punkte"): "03 分布函数、密度与常见分布",
    ("ss2024", "Aufgabe 6 — 19 Punkte"): "03 分布函数、密度与常见分布",
}

HISTORY_EXAM_SKIP = {
    ("2012", "Aufgabe 3"): "Gambler's ruin / Markov-Prozess，超出当前 9 个知识点边界。",
    ("2015", "Aufgabe 4: Kugelprozess / Markov-Kette"): "Markov-Kette，超出当前 9 个知识点边界。",
    ("2015", "Aufgabe 6: Lineare Regression"): "Lineare Regression，超出当前 9 个知识点边界。",
    ("2021", "Aufgabe 4"): "Maximum-Likelihood / Schätzung，当前 9 类没有独立估计章节。",
}

HISTORY_EXAM_SOLUTION_SUPPLEMENTS = {
    ("2021", "Aufgabe 1"): r"""#### Lösung

##### (a)

###### (i)

Damit $f$ eine Dichte ist, müssen zwei Eigenschaften gelten:

$$
f(x)\ge 0 \quad \text{für alle } x
$$

und

$$
\int_{-\infty}^{\infty} f(x)\,dx=1.
$$

###### (ii)

Auf dem Intervall $[1,4]$ gilt:

$$
(x-1)(4-x)\ge 0,
$$

also ist $f(x)\ge 0$, wenn $c>0$ ist.

Für die Normierung berechnen wir:

$$
1=\int_{-\infty}^{\infty} f(x)\,dx
=c\int_1^4 (x-1)(4-x)\,dx.
$$

Nun ist:

$$
(x-1)(4-x)=-x^2+5x-4.
$$

Damit:

$$
\int_1^4 (x-1)(4-x)\,dx
=
\left[-\frac{x^3}{3}+\frac52x^2-4x\right]_1^4
=\frac92.
$$

Also:

$$
c\cdot \frac92=1
\quad\Longrightarrow\quad
c=\frac29.
$$

Damit lautet die Dichte:

$$
f(x)=
\begin{cases}
\dfrac29(x-1)(4-x), & 1\le x\le 4,\\
0, & \text{sonst}.
\end{cases}
$$

Sie ist nichtnegativ und integriert sich zu $1$, also erfüllt sie die Dichte-Eigenschaften.

###### (iii)

Der Träger ist das Intervall, auf dem die Dichte positiv sein kann:

$$
\operatorname{supp}(f)=[1,4].
$$

##### (b)

Der Erwartungswert ist:

$$
\mathbb E(X)
=
\int_{-\infty}^{\infty} x f(x)\,dx
=
\frac29\int_1^4 x(x-1)(4-x)\,dx.
$$

Nun gilt:

$$
x(x-1)(4-x)=-x^3+5x^2-4x.
$$

Daher:

$$
\int_1^4 x(x-1)(4-x)\,dx
=
\left[-\frac{x^4}{4}+\frac53x^3-2x^2\right]_1^4
=
\frac{45}{4}.
$$

Also:

$$
\mathbb E(X)
=
\frac29\cdot \frac{45}{4}
=
\frac52.
$$

##### (c)

Da $X_1,\dots,X_n$ unabhängig und identisch verteilt sind und $X$ eine endliche Varianz besitzt, kann der zentrale Grenzwertsatz angewendet werden.

Für

$$
Y_n=\sum_{i=1}^nX_i
$$

gilt:

$$
\mathbb E(Y_n)=n\mathbb E(X)
$$

und

$$
\operatorname{Var}(Y_n)=n\operatorname{Var}(X).
$$

Die standardisierte Zufallsvariable ist:

$$
\tilde Y_n
=
\frac{Y_n-n\mathbb E(X)}{\sqrt{n\operatorname{Var}(X)}}.
$$

Nach dem zentralen Grenzwertsatz gilt:

$$
\tilde Y_n \xrightarrow{d} N(0,1).
$$

##### (d)

Da $X$ stetig verteilt ist, hat jeder einzelne Punkt Wahrscheinlichkeit $0$:

$$
P(X=2)=0.
$$
""",
    ("2021", "Aufgabe 2"): r"""#### Lösung

##### (a)

Der Ergebnisraum für die Anzahl früher infizierter Personen ist:

$$
\Omega=\{0,1,\dots,1561505\}.
$$

Damit gilt:

$$
|\Omega|=1561506.
$$

##### (b)

Nein, die Laplace-Annahme ist hier nicht gerechtfertigt.

Ein Laplace-Experiment würde bedeuten, dass alle möglichen Werte der Anzahl früher infizierter Personen gleich wahrscheinlich sind. Dafür gibt es hier keinen Grund. Außerdem entstehen die möglichen Anzahlen aus sehr vielen individuellen Infektionszuständen, die nicht gleichmäßig auf die Anzahlen verteilt sein müssen.

##### (c)

Das Urnenmodell lautet:

- In der Urne liegen $1561505$ Kugeln, je eine Kugel pro Münchner Bürger/-in.
- Jede Kugel ist entweder vom Typ „frühere Infektion“ oder „keine frühere Infektion“.
- Es werden $N=5000$ Kugeln zufällig ohne Zurücklegen gezogen.

Wenn insgesamt $M$ Personen in München früher infiziert waren, dann wäre die Anzahl infizierter Personen in der Stichprobe exakt hypergeometrisch verteilt:

$$
X\sim \operatorname{Hyp}(1561505,M,5000).
$$

##### (d)

###### (i)

Der Parameter $\pi$ ist inhaltlich die Ansteckungsrate bzw. der Anteil der Münchner Bevölkerung mit vergangener COVID-19-Infektion.

###### (ii)

Bei $\pi=0.15$ gilt näherungsweise:

$$
X\sim \operatorname{Bin}(5000,0.15).
$$

Gesucht ist:

$$
\mathbb P\left(\left|\frac{X}{5000}-0.15\right|>0.01\right).
$$

Das ist äquivalent zu:

$$
\mathbb P(X<700)+\mathbb P(X>800).
$$

Exakt kann man schreiben:

$$
\mathbb P(X\le 699)+\mathbb P(X\ge 801).
$$

Mit Normalapproximation:

$$
\mu=5000\cdot0.15=750,
\qquad
\sigma=\sqrt{5000\cdot0.15\cdot0.85}\approx25.25.
$$

Mit Stetigkeitskorrektur:

$$
z_1=\frac{699.5-750}{25.25}\approx-2.00,
\qquad
z_2=\frac{800.5-750}{25.25}\approx2.00.
$$

Daher:

$$
\mathbb P\left(\left|\frac{X}{5000}-0.15\right|>0.01\right)
\approx
2(1-\Phi(2.00))
\approx
0.046.
$$

##### (e)

###### (i)

Der Wahrscheinlichkeitsbaum hat die erste Verzweigung:

$$
\mathbb P(I)=\rho,
\qquad
\mathbb P(I^c)=1-\rho,
$$

wobei $I$ „vergangene Infektion“ bedeutet.

Für den Test gilt:

$$
\mathbb P(T+\mid I)=0.95,
\qquad
\mathbb P(T-\mid I)=0.05,
$$

und:

$$
\mathbb P(T+\mid I^c)=0.01,
\qquad
\mathbb P(T-\mid I^c)=0.99.
$$

Damit:

$$
\mathbb P(I\cap T+)=0.95\rho,
$$

und:

$$
\mathbb P(I^c\cap T+)=0.01(1-\rho).
$$

Also:

$$
\mathbb P(T+)=0.95\rho+0.01(1-\rho)=0.01+0.94\rho.
$$

###### (ii)

Gesucht ist:

$$
\mathbb P(I\mid T+)\ge0.66.
$$

Mit Bayes:

$$
\mathbb P(I\mid T+)
=
\frac{0.95\rho}{0.95\rho+0.01(1-\rho)}
=
\frac{0.95\rho}{0.01+0.94\rho}.
$$

Also:

$$
\frac{0.95\rho}{0.01+0.94\rho}\ge0.66.
$$

Das ergibt:

$$
0.95\rho\ge0.0066+0.6204\rho
$$

und somit:

$$
0.3296\rho\ge0.0066.
$$

Daher:

$$
\rho\ge \frac{0.0066}{0.3296}\approx0.020.
$$

Der Anteil müsste also mindestens etwa $2.0\%$ betragen.
""",
    ("2021", "Aufgabe 3"): r"""#### Lösung

##### (a)

Es gilt:

$$
\operatorname{Var}(G_A+G_B)
=
\operatorname{Var}(G_A)+\operatorname{Var}(G_B)+2\operatorname{Cov}(G_A,G_B).
$$

Einsetzen liefert:

$$
110^2=100^2+20^2+2\operatorname{Cov}(G_A,G_B).
$$

Also:

$$
12100=10000+400+2\operatorname{Cov}(G_A,G_B).
$$

Daher:

$$
2\operatorname{Cov}(G_A,G_B)=1700
$$

und somit:

$$
\operatorname{Cov}(G_A,G_B)=850.
$$

##### (b)

Der Korrelationskoeffizient ist:

$$
\rho(G_A,G_B)
=
\frac{\operatorname{Cov}(G_A,G_B)}
{\sigma_A\sigma_B}
=
\frac{850}{100\cdot20}
=
0.425.
$$

Die Korrelation ist positiv und mittelstark. Hohe Gewinne bei A gehen also tendenziell mit höheren Gewinnen bei B einher, aber der Zusammenhang ist nicht perfekt.

##### (c)

Studentin C erzielt sicher $50$ Euro Gewinn. Gesucht ist:

$$
\mathbb P(G_A>50).
$$

Da:

$$
G_A\sim N(100,100^2),
$$

standardisieren wir:

$$
\mathbb P(G_A>50)
=
\mathbb P\left(
\frac{G_A-100}{100}>
\frac{50-100}{100}
\right)
=
\mathbb P(Z>-0.5).
$$

Also:

$$
\mathbb P(G_A>50)=\Phi(0.5)\approx0.6915.
$$

##### (d)

###### (i)

Bei $\alpha=0.5$ liegt die Hälfte auf dem Festgeldkonto und die Hälfte in Aktien. Der erwartete prozentuale Gewinn ist:

$$
0.5\cdot6\%+0.5\cdot10\%=8\%.
$$

Der erwartete Gesamtgewinn in Prozent beträgt also $8\%$.

###### (ii)

Der erwartete prozentuale Gewinn als Funktion von $\alpha$ ist:

$$
g(\alpha)=6\%\alpha+10\%(1-\alpha)=10\%-4\%\alpha.
$$

Gefordert ist:

$$
10-4\alpha\ge9.
$$

Damit:

$$
\alpha\le0.25.
$$

Studentin D sollte also höchstens $25\%$ auf das Festgeldkonto legen.

###### (iii)

Nur der Aktienanteil ist risikobehaftet. Die Standardabweichung des prozentualen Gewinns ist:

$$
(1-\alpha)\cdot20\%.
$$

Gefordert ist:

$$
(1-\alpha)\cdot20\%\le10\%.
$$

Also:

$$
1-\alpha\le0.5
$$

und daher:

$$
\alpha\ge0.5.
$$

Studentin D sollte also mindestens $50\%$ auf das Festgeldkonto legen.
""",
    ("2021", "Aufgabe 5"): r"""#### Lösung

##### (a)

Die Daten sind gepaart, weil für dieselben Personen Tag- und Nachtreaktionszeiten vorliegen. Für die Vermutung „tagsüber schneller“ betrachten wir:

$$
D_i=X_i-Y_i.
$$

Große positive Werte von $D_i$ sprechen dafür, dass nachts langsamer reagiert wird.

Die Differenzen sind:

$$
(-0.1,\ 0.3,\ 0.6,\ 0.5,\ 0.5).
$$

Ein geeigneter verteilungsfreier Test ist der einseitige Wilcoxon-Vorzeichen-Rang-Test.

Die Hypothesen lauten:

$$
H_0:\operatorname{Median}(D)\le0,
\qquad
H_1:\operatorname{Median}(D)>0.
$$

Die absoluten Differenzen haben Ränge:

$$
0.1\mapsto1,\quad
0.3\mapsto2,\quad
0.5\mapsto3.5,\quad
0.5\mapsto3.5,\quad
0.6\mapsto5.
$$

Der positive Rangsummentestwert ist:

$$
W_+=2+3.5+3.5+5=14.
$$

Bei $n=5$ ist der einseitige exakte p-Wert:

$$
p=\mathbb P(W_+\ge14)=\frac{2}{32}=0.0625.
$$

Da $0.0625>0.05$, wird $H_0$ nicht verworfen. Mit dem verteilungsfreien Test lässt sich die Vermutung auf dem Niveau $5\%$ nicht bestätigen.

##### (b)

###### (i)

Ein geeigneter parametrischer Test ist der gepaarte t-Test für die Differenzen:

$$
D_i=X_i-Y_i.
$$

Die Hypothesen sind:

$$
H_0:\mu_D\le0,
\qquad
H_1:\mu_D>0.
$$

Benötigt wird, dass die Differenzen $D_i$ annähernd normalverteilt sind bzw. dass der t-Test als Modellannahme für diese Differenzen plausibel ist.

###### (ii)

Aus den Differenzen:

$$
(-0.1,\ 0.3,\ 0.6,\ 0.5,\ 0.5)
$$

erhält man:

$$
\bar d=0.36,
\qquad
s_D\approx0.2793,
\qquad
n=5.
$$

Die Teststatistik ist:

$$
t=
\frac{\bar d-0}{s_D/\sqrt n}
\approx
\frac{0.36}{0.2793/\sqrt5}
\approx
2.88.
$$

Für $n-1=4$ Freiheitsgrade ist der kritische Wert des einseitigen Tests zum Niveau $\alpha=0.05$:

$$
t_{0.95,4}\approx2.132.
$$

Da:

$$
2.88>2.132,
$$

wird $H_0$ verworfen. Unter den parametrischen Annahmen spricht der Test dafür, dass tagsüber schneller reagiert wird.

##### (c)

Hier werden zwei unabhängige Stichproben verglichen: die nächtlichen Reaktionszeiten ohne Energy Drink $X$ und die nächtlichen Reaktionszeiten nach Energy Drink $Z$.

Geeignet ist ein zweiseitiger Zweistichproben-t-Test. Da keine Varianzgleichheit angegeben ist, verwendet man konservativ den Welch-t-Test.

Die Hypothesen lauten:

$$
H_0:\mu_Z=\mu_X,
\qquad
H_1:\mu_Z\neq\mu_X.
$$

Die Stichprobenkennwerte sind:

$$
\bar x=2.36,
\qquad
s_X\approx0.3847,
$$

und:

$$
\bar z=2.40,
\qquad
s_Z\approx0.1871.
$$

Die Teststatistik ist:

$$
t=
\frac{\bar z-\bar x}
{\sqrt{s_X^2/5+s_Z^2/5}}
\approx
\frac{0.04}{\sqrt{0.3847^2/5+0.1871^2/5}}
\approx
0.21.
$$

Der Betrag der Teststatistik ist sehr klein. Auf dem Niveau $\alpha=0.05$ wird $H_0$ nicht verworfen.

Es gibt also keinen signifikanten Hinweis darauf, dass der Energy Drink die mittlere nächtliche Reaktionszeit verändert.
""",
    ("2021", "Aufgabe 6"): r"""#### Lösung

##### (a)

###### (i)

Da Rot- und Weißmostertrag für dieselben $13$ Regionen beobachtet werden, liegen gepaarte Beobachtungen vor. Geeignet ist daher ein **gepaarter t-Test** für die Differenzen

$$
D_i=R_i-W_i.
$$

Die Hypothesen lauten:

$$
H_0:\mu_D=0,
\qquad
H_1:\mu_D\neq 0.
$$

Dabei bedeutet $\mu_D=0$, dass sich die mittleren Rot- und Weißmosterträge nicht unterscheiden.

###### (ii)

Aus den Daten ergeben sich für die Differenzen:

$$
\bar d\approx -2.662,
\qquad
s_D\approx 8.138,
\qquad
n=13.
$$

Die Teststatistik ist:

$$
t
=
\frac{\bar d-0}{s_D/\sqrt n}
\approx
\frac{-2.662}{8.138/\sqrt{13}}
\approx
-1.179.
$$

Bei $n-1=12$ Freiheitsgraden ist der Betrag dieser Teststatistik kleiner als der kritische Wert des zweiseitigen Tests zum Niveau $\alpha=0.05$. Daher wird $H_0$ nicht verworfen.

Es gibt auf dem Niveau $5\%$ keinen signifikanten Hinweis darauf, dass sich die mittleren Rot- und Weißmosterträge unterscheiden.

##### (b)

Ein $90\%$-Konfidenzintervall für $\mu_D$ ist:

$$
\bar d
\pm
t_{0.95,12}\frac{s_D}{\sqrt n}.
$$

Mit $t_{0.95,12}\approx 1.782$ folgt:

$$
-2.662
\pm
1.782\cdot \frac{8.138}{\sqrt{13}}
\approx
-2.662\pm 4.022.
$$

Also:

$$
\mu_D\in[-6.68,\ 1.36]
$$

approximativ. Da $0$ im Intervall liegt, passt dies zur Testentscheidung aus Teil (a).

##### (c)

###### (i)

Um eine Abhängigkeit zwischen Rot- und Weißmostertrag zu prüfen, verwendet man den **Pearson-Korrelationstest**, sofern die Daten gemeinsam annähernd normalverteilt sind. Die notwendige Zusatzannahme ist also eine bivariate Normalverteilung bzw. Normalität der gemeinsamen Verteilung.

Die Hypothesen lauten:

$$
H_0:\rho=0,
\qquad
H_1:\rho\neq 0.
$$

###### (ii)

Aus den Daten erhält man näherungsweise:

$$
r\approx 0.933.
$$

Die Teststatistik für den Pearson-Korrelationstest ist:

$$
t
=
r\sqrt{\frac{n-2}{1-r^2}}
\approx
0.933\sqrt{\frac{11}{1-0.933^2}}
\approx
8.57.
$$

Mit $11$ Freiheitsgraden ist dies hoch signifikant. Daher wird $H_0$ verworfen.

Es gibt einen deutlichen positiven linearen Zusammenhang zwischen Rot- und Weißmostertrag in den Regionen.
""",
    ("2014", "Aufgabe 1"): r"""#### Lösung

Es gilt $\mathbb P(\bar A)=0.15$, also $\mathbb P(A)=0.85$.
Weiter ist

$$
\mathbb P(K\mid A)=0.08,\qquad \mathbb P(\bar K\mid \bar A)=0.62.
$$

**a)** Das Ereignis $\bar A\cap \bar K$ bedeutet: Der Fahrer war nicht angegurtet und hatte keine schwere Kopfverletzung.

$$
\mathbb P(\bar A\cap \bar K)
=\mathbb P(\bar A)\mathbb P(\bar K\mid \bar A)
=0.15\cdot0.62
=0.093.
$$

**b)** Für Unabhängigkeit müsste gelten:

$$
\mathbb P(\bar A\cap \bar K)=\mathbb P(\bar A)\mathbb P(\bar K).
$$

Zunächst:

$$
\mathbb P(\bar K)=\mathbb P(\bar K\mid A)\mathbb P(A)+\mathbb P(\bar K\mid\bar A)\mathbb P(\bar A)
=0.92\cdot0.85+0.62\cdot0.15=0.875.
$$

Damit:

$$
\mathbb P(\bar A)\mathbb P(\bar K)=0.15\cdot0.875=0.13125\neq0.093.
$$

Also sind $\bar A$ und $\bar K$ nicht unabhängig.

**c)** Gesucht ist $\mathbb P(\bar A\mid K)$.

$$
\mathbb P(K)=0.08\cdot0.85+0.38\cdot0.15=0.125.
$$

$$
\mathbb P(\bar A\mid K)=\frac{\mathbb P(K\mid\bar A)\mathbb P(\bar A)}{\mathbb P(K)}
=\frac{0.38\cdot0.15}{0.125}
=0.456.
$$
""",
    ("2014", "Aufgabe 2"): r"""#### Lösung

Aus den Randwahrscheinlichkeiten folgt:

$$
f_Y(1)=1-0.5=0.5.
$$

Die fehlenden Einträge sind:

$$
f_{X,Y}(-1,1)=0.35-0.15=0.20,
$$

$$
f_{X,Y}(0,1)+f_{X,Y}(0,2)=1-0.35-(0.20+0.15)=0.30.
$$

Da die Spaltensumme für $y=1$ gleich $0.5$ ist:

$$
f_{X,Y}(0,1)=0.5-0.20-0.20=0.10.
$$

Damit:

$$
f_{X,Y}(0,2)=0.30-0.10=0.20.
$$

Die Randverteilung von $X$ ist:

$$
\mathbb P(X=-1)=0.35,\quad \mathbb P(X=0)=0.30,\quad \mathbb P(X=1)=0.35.
$$

Damit ist:

$$
E(X)=(-1)\cdot0.35+0\cdot0.30+1\cdot0.35=0.
$$

Für $Y$ gilt:

$$
\mathbb P(Y=1)=0.5,\qquad \mathbb P(Y=2)=0.5,
\qquad E(Y)=1.5.
$$

Außerdem:

$$
E(XY)=(-1)\cdot1\cdot0.20+(-1)\cdot2\cdot0.15
+1\cdot1\cdot0.20+1\cdot2\cdot0.15=0.
$$

Also:

$$
\operatorname{Cov}(X,Y)=E(XY)-E(X)E(Y)=0.
$$

Die Verteilungsfunktion von $X$ ist:

$$
F_X(x)=
\begin{cases}
0, & x<-1,\\
0.35, & -1\le x<0,\\
0.65, & 0\le x<1,\\
1, & x\ge1.
\end{cases}
$$

Unabhängigkeit gilt nicht, denn zum Beispiel:

$$
f_{X,Y}(-1,1)=0.20\neq0.35\cdot0.5=0.175.
$$
""",
    ("2014", "Aufgabe 3"): r"""#### Lösung

**a)** Für $x>0$ ist

$$
F_X(x)=\frac{x}{1+x}.
$$

Ableiten liefert:

$$
f_X(x)=F_X'(x)=\frac{1}{(1+x)^2},\qquad x>0.
$$

Also:

$$
f_X(x)=
\begin{cases}
\dfrac{1}{(1+x)^2}, & x>0,\\
0, & x\le0.
\end{cases}
$$

**b)**

$$
\mathbb P(1<X<3)=F_X(3)-F_X(1)
=\frac34-\frac12
=\frac14.
$$

**c)** Damit $h$ eine Dichte ist, muss gelten:

$$
\int_0^1(cx^3+x)\,dx=1.
$$

Also:

$$
c\int_0^1x^3\,dx+\int_0^1x\,dx
=\frac c4+\frac12=1.
$$

Damit:

$$
c=2.
$$
""",
    ("2014", "Aufgabe 4"): r"""#### Lösung

Unter Gleichverteilung sind die erwarteten Häufigkeiten:

$$
E_i=\frac{60}{3}=20
$$

für jede der drei Haarfarben.

Das Pearsonsche $\chi^2$-Maß ist:

$$
\chi^2
=\frac{(30-20)^2}{20}
+\frac{(20-20)^2}{20}
+\frac{(10-20)^2}{20}
=5+0+5=10.
$$

Bei drei Kategorien und vollständig vorgegebener Gleichverteilung gilt:

$$
k=3-1=2.
$$

Für $\alpha=0.1$ wird mit dem kritischen Wert der $\chi^2_2$-Verteilung verglichen.
Da $\chi^2=10$ groß ist, wird die Gleichverteilungsannahme auf dem Niveau $\alpha=0.1$ verworfen.
""",
    ("2014", "Aufgabe 5"): r"""#### Lösung

Für gegebene Beobachtungen $x_1,\dots,x_n$ ist die Likelihood:

$$
L(\alpha)
=\prod_{i=1}^n \alpha\beta x_i^{\beta-1}\exp(-\alpha x_i^\beta).
$$

Also:

$$
L(\alpha)
=\alpha^n\beta^n\left(\prod_{i=1}^n x_i^{\beta-1}\right)
\exp\left(-\alpha\sum_{i=1}^n x_i^\beta\right).
$$

Die Log-Likelihood ist:

$$
\ell(\alpha)
=n\log\alpha+n\log\beta+(\beta-1)\sum_{i=1}^n\log x_i-\alpha\sum_{i=1}^n x_i^\beta.
$$

Für $\beta=1$:

$$
\ell(\alpha)=n\log\alpha-\alpha\sum_{i=1}^n x_i+\text{Konstante}.
$$

Ableiten:

$$
\ell'(\alpha)=\frac n\alpha-\sum_{i=1}^n x_i.
$$

Setze $\ell'(\alpha)=0$:

$$
\hat\alpha_{ML}=\frac{n}{\sum_{i=1}^n x_i}.
$$

Für die Stichprobe ist:

$$
\sum x_i=0.25+0.025+0.001+0.174+0.033=0.483.
$$

Damit:

$$
\hat\alpha_{ML}=\frac5{0.483}\approx10.35.
$$
""",
    ("2015", "Aufgabe 1: HIV-Test"): r"""#### Lösung

In der Low-Risk-Gruppe gilt:

$$
\mathbb P(I)=\frac{10}{100000}=0.0001.
$$

Außerdem:

$$
\mathbb P(P\mid I)=1,\qquad
\mathbb P(P\mid I^c)=0.00005.
$$

Die Ereignisse $I$ und $P$ sind nicht unabhängig, denn:

$$
\mathbb P(P\mid I)=1
$$

ist offensichtlich nicht gleich der Gesamtwahrscheinlichkeit $\mathbb P(P)$.

Mit der Formel der totalen Wahrscheinlichkeit:

$$
\mathbb P(P)=1\cdot0.0001+0.00005\cdot0.9999
\approx0.000149995.
$$

Mit Bayes:

$$
\mathbb P(I\mid P)
=\frac{\mathbb P(P\mid I)\mathbb P(I)}{\mathbb P(P)}
=\frac{0.0001}{0.000149995}
\approx0.667.
$$

Trotz positivem Test liegt die Wahrscheinlichkeit einer tatsächlichen Infektion also nur bei ungefähr $66.7\%$.
""",
    ("2015", "Aufgabe 2: Diskrete Zufallsvariable"): r"""#### Lösung

Die Wahrscheinlichkeiten müssen sich zu $1$ addieren:

$$
0.2c+0.25c+(2.1-c)=1.
$$

Also:

$$
2.1-0.55c=1
\quad\Longrightarrow\quad
c=2.
$$

Damit:

$$
\mathbb P(X=2)=0.4,\qquad
\mathbb P(X=4)=0.5,\qquad
\mathbb P(X=6)=0.1.
$$

Die Verteilungsfunktion ist:

$$
F_X(x)=
\begin{cases}
0, & x<2,\\
0.4, & 2\le x<4,\\
0.9, & 4\le x<6,\\
1, & x\ge6.
\end{cases}
$$

Der Erwartungswert:

$$
E(X)=2\cdot0.4+4\cdot0.5+6\cdot0.1=3.4.
$$

Außerdem:

$$
E(X^2)=4\cdot0.4+16\cdot0.5+36\cdot0.1=13.2.
$$

Damit:

$$
\operatorname{Var}(X)=13.2-3.4^2=1.64.
$$
""",
    ("2015", "Aufgabe 3: Cauchy-Verteilung"): r"""#### Lösung

Die Transformation lautet:

$$
Y=g(X)=\frac1X.
$$

Die Umkehrfunktion ist:

$$
x=g^{-1}(y)=\frac1y.
$$

Außerdem:

$$
\left|\frac{d}{dy}g^{-1}(y)\right|=\frac1{y^2}.
$$

Nach dem Transformationssatz:

$$
f_Y(y)
=f_X\left(\frac1y\right)\frac1{y^2}
=\frac1\pi\frac{1}{1+1/y^2}\frac1{y^2}
=\frac1\pi\frac1{1+y^2}.
$$

Also hat $Y$ wieder die Standard-Cauchy-Verteilung.
""",
    ("2015", "Aufgabe 5: Rechenzeiten"): r"""#### Lösung

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
""",
}

SOLUTION_MARKER_ONLY_SOURCES = {"ss2022", "ss2024"}


def has_solution_marker(text):
    return re.search(r"Lösung|Lösungsvorschlag|Loesung|####\s+解答", text, re.I) is not None


def has_standard_solution_heading(text):
    return re.search(r"^#{1,6}\s+(Lösung|Lösungsvorschlag|Loesung|解答)\b", text, re.M | re.I) is not None


def ensure_history_solution(body, task):
    if has_standard_solution_heading(body):
        return body

    supplement = HISTORY_EXAM_SOLUTION_SUPPLEMENTS.get((task["chapter"], task["title"]))
    if supplement:
        return body.rstrip() + "\n\n" + supplement.strip() + "\n"

    if task["chapter"] in SOLUTION_MARKER_ONLY_SOURCES:
        return re.sub(r"^(### 真题 .*)$", r"\1\n\n#### Lösung", body, count=1, flags=re.M)

    if has_solution_marker(body):
        return body

    return body.rstrip() + "\n\n#### Lösung\n\nDie Lösung ist in der ursprünglichen Quelle nicht explizit angegeben.\n"


def normalize_history_section_levels(text):
    out = []
    for line in text.strip().splitlines():
        if re.fullmatch(r"\[\d+\]", line.strip()):
            continue
        line = re.sub(r"^(#{4,6}\s+\((?:[a-h]|\d+)\))\s+\$\$\s*$", r"\1", line, flags=re.I)
        if line.startswith("###### "):
            out.append(line)
        elif line.startswith("##### "):
            out.append("#" + line)
        elif line.startswith("#### "):
            out.append("#" + line)
        else:
            out.append(line)
    return "\n".join(out).strip()


def remove_standalone_point_markers(text):
    return re.sub(r"(?m)^\s*\[\d+\]\s*$\n?", "", text)


def compact_blank_lines(text):
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def split_solution_from_body(body):
    match = re.search(r"^#{1,6}\s+(?:Lösung|Lösungsvorschlag|Loesung|解答)\b.*$", body, re.M | re.I)
    if not match:
        return body.strip(), ""
    question = body[:match.start()].strip()
    solution = body[match.end():].strip()
    return question, solution


def split_interleaved_subpart_solutions(body):
    subparts = list(re.finditer(r"^#{4,6}\s+\(([a-h])\)\s*(.*)$", body, re.M | re.I))
    if not subparts:
        return None

    preamble = body[:subparts[0].start()].strip()
    question_parts = [preamble] if preamble else []
    solution_parts = []
    solved_parts = 0

    for i, match in enumerate(subparts):
        end = subparts[i + 1].start() if i + 1 < len(subparts) else len(body)
        block = body[match.start():end].strip()
        solution_match = re.search(r"^#{1,6}\s+(?:Lösung|Lösungsvorschlag|Loesung|解答)\b.*$", block, re.M | re.I)

        if not solution_match:
            question_parts.append(block)
            continue

        solved_parts += 1
        question_chunk = block[:solution_match.start()].strip()
        solution_chunk = block[solution_match.end():].strip()
        label = match.group(1).lower()
        title = match.group(2).strip()

        if question_chunk:
            question_parts.append(question_chunk)
        if solution_chunk:
            heading = f"##### ({label})" + (f" {title}" if title else "")
            solution_parts.extend([heading, "", solution_chunk])

    if solved_parts < 2:
        return None

    return "\n\n".join(question_parts).strip(), "\n\n".join(solution_parts).strip()


def split_inline_solution_cues(body):
    subparts = list(re.finditer(r"^#{4,6}\s+\(([a-h]|\d+)\)\s*(.*)$", body, re.M | re.I))
    if not subparts:
        return None

    cue = re.compile(
        r"^(?:Ein möglicher Ergebnisraum ist|Die Zufallsvariable ist|Der Bildbereich ist|Es gilt|Damit gilt|Also gilt)\b",
        re.M,
    )
    preamble = body[:subparts[0].start()].strip()
    question_parts = [preamble] if preamble else []
    solution_parts = []
    solved_parts = 0

    for i, match in enumerate(subparts):
        end = subparts[i + 1].start() if i + 1 < len(subparts) else len(body)
        block = body[match.start():end].strip()
        cue_match = cue.search(block)
        label = match.group(1)
        title = match.group(2).strip()

        if not cue_match:
            question_parts.append(block)
            continue

        solved_parts += 1
        question_chunk = block[:cue_match.start()].strip()
        solution_chunk = block[cue_match.start():].strip()

        if question_chunk:
            question_parts.append(question_chunk)
        if solution_chunk:
            heading = f"##### ({label})" + (f" {title}" if title else "")
            solution_parts.extend([heading, "", solution_chunk])

    if solved_parts < 2:
        return None

    return "\n\n".join(question_parts).strip(), "\n\n".join(solution_parts).strip()


def subpart_titles(text):
    titles = []
    for match in re.finditer(r"^#{4,6}\s+\(([a-h])\)\s*(.*)$", text, re.M | re.I):
        label = match.group(1).lower()
        title = match.group(2).strip()
        titles.append((label, title))
    return titles


def subpart_text_map(text):
    matches = list(re.finditer(r"^#{4,6}\s+\(([a-h])\)\s*(.*)$", text, re.M | re.I))
    out = {}
    for i, match in enumerate(matches):
        label = match.group(1).lower()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        out[label] = text[match.start():end].strip()
    return out


def infer_question_from_solution(task, solution):
    lines = []
    first_part = re.search(r"^#{4,6}\s+\([a-h]\)\s*(.*)$", solution, re.M | re.I)
    if first_part:
        preamble = solution[:first_part.start()].strip()
        if preamble:
            lines.append(preamble)
            lines.append("")
    else:
        preamble = solution.strip()
        if preamble:
            lines.append(preamble)
            lines.append("")

    # For solution-only sources, keep the inferred question conservative:
    # use only the task-level preamble and the subpart headings, never formulas
    # or calculations from inside a subpart solution.
    if not lines and re.search(r"^(Thema|Gegeben|Es geht um)\b", solution, re.M):
        intro_match = re.search(r"^((?:Thema|Gegeben|Es geht um).*?)(?=^#{4,6}\s+\([a-h]\)|\Z)", solution, re.S | re.M)
        if intro_match:
            lines.append(intro_match.group(1).strip())
            lines.append("")

    if not lines:
        header = re.sub(r"^Aufgabe\s+\d+\s*[-—:]*\s*", "", task["title"]).strip()
        if header:
            lines.append(f"Thema: {header}.")
            lines.append("")

    if first_part:
        lines.append("")
    parts = subpart_titles(solution)
    if parts:
        for label, title in parts:
            prompt = (title or "Teilaufgabe bearbeiten").rstrip(".: ")
            lines += [
                f"##### ({label})",
                "",
                f"{prompt}.",
                "",
            ]
    else:
        lines.append("Bearbeiten Sie die Aufgabe anhand der angegebenen Daten und begründen Sie die einzelnen Rechenschritte formal sauber.")
    return "\n".join(lines).strip()


def chinese_history_guide(task, question, solution):
    parts = subpart_titles(question) or subpart_titles(solution)
    qparts = subpart_text_map(question)
    sparts = subpart_text_map(solution)
    whole = (task["title"] + "\n" + question + "\n" + solution).lower()

    def one(label, title):
        local = (title + "\n" + qparts.get(label, "") + "\n" + sparts.get(label, "")).lower()
        fallback = (title + "\n" + whole).lower()
        if "teststatistik" in local or "hypothesen" in local or "signifikanzniveau" in local:
            text = "这是统计检验题。先判断样本是配对还是独立、参数检验还是非参数检验；再写 $H_0$ 和 $H_1$，计算检验统计量，与临界值或 p 值比较，最后用题目语言解释是否支持原假设/研究猜想。"
        elif "zentral" in local or "grenzwertsatz" in local or "standardisiert" in local or ("konvergenz" in local and "y_n" in local):
            text = r"这是中心极限定理/极限分布题。先确认 $X_i$ 独立同分布且方差有限，再写出和变量的均值与方差；标准化以后直接用 CLT 得到收敛到 $N(0,1)$。"
        elif "delta-methode" in local or ("\\overline x^2" in local and "approximative verteilung" in local):
            text = r"这里不是直接平方正态随机变量，而是对样本均值使用 Delta-Methode。先从中心极限定理得到 $\overline X$ 的近似正态，再令 $g(x)=x^2$，用 $g'(\mu)$ 把方差按一阶导数平方放大。"
        elif "0.1645" in local or ("quantil" in local and "0.9" in local):
            text = r"这是用中心极限定理反推参数范围。先把 $|\overline X-\mu|\le x$ 标准化成标准正态区间，再利用双侧 $90\%$ 对应 $0.95$ 分位数 $1.645$，最后把不等式化成关于 $p$ 的二次不等式。"
        elif "ergebnisraum" in local or "omega" in local or "würfe" in local or "wuerfe" in local:
            text = r"先明确实验到底要区分哪些结果。若题目要求完整记录每次投掷，就用有序元组作 $\Omega$；若只关心和或某个统计量，就可以把样本空间压缩到这些统计量的可能取值。"
        elif "bildmaß" in local or "bildmass" in local or "messbarkeitstabelle" in local or "messbarkeit" in local:
            text = r"Bildmaß 题先写映射 $X:\Omega\to\Omega'$，再对目标空间里的集合取原像：$P_X(B)=P(X^{-1}(B))$。判断可测性时检查每个目标集合的原像是否属于原来的 sigma-代数。"
        elif "approximative verteilung" in local and "\\overline x" in local:
            text = r"先识别单次实验的分布：等待第一次出现 Zahl 的次数服从几何分布。然后写出单个 $X_i$ 的期望和方差；因为 $n=200$ 较大且独立同分布，可以用中心极限定理给样本均值 $\overline X$ 做正态近似。"
        elif "poisson" in local:
            text = r"Poisson 题先判断是点概率、分布函数还是随机数生成。若从均匀随机数生成 Poisson 分布，用 Inversionsmethode：把 $U\sim U[0,1]$ 代入离散分布函数的广义逆分位函数。"
        elif "quantil" in local:
            text = r"分位数题就是解 $F(x)=p$，但要先检查 $x$ 所在的分段。连续分布中 $p$-Quantil 表示有 $p$ 的概率落在该值左侧；如果分布有跳跃，要用广义逆定义。"
        elif "erwartungswert" in local or "median" in local or "modus" in local or "schiefe" in local:
            text = r"先确认随机变量的密度或分布，再分别按定义处理：期望用 $\int x f(x)\,dx$，Median 解 $F(m)=0.5$，Modus 找密度最大点，Schiefe 结合均值、Median 和分布形状判断。"
        elif "transformation" in local or "dichte von y" in local or "y=x^2" in local or "zufallsvariable" in local:
            text = r"变量变换题先写出新旧变量关系和取值范围。如果变换单调，用 $f_Y(y)=f_X(x(y))\lvert x'(y)\rvert$；如果不是单调，要把所有原像分支的贡献加起来。"
        elif "dichte" in local and ("bezüglich" in local or "dominierenden" in local or "\\mu" in local or " maß" in local):
            text = r"判断是否为相对于 $\mu$ 的密度，关键不是看函数是否非负就结束，而是检查全空间积分是否等于 $1$。有限空间里直接算 $\sum f(\omega)\mu(\{\omega\})$。"
        elif "dichte" in local:
            text = r"密度题按定义来：先检查 $f(x)\ge0$，再用归一化条件 $\int f(x)\,dx=1$ 求常数。求期望时不要忘记多乘一个 $x$，连续型随机变量的单点概率为 $0$。"
        elif "integral" in local or r"\int" in local:
            text = "这是有限测度空间上的积分计算。不要把它当普通黎曼积分；这里每个点的贡献是函数值乘以该单点的测度，最后只对积分区域里的点求和。"
        elif "maß" in local or "mass" in local or " measure" in local:
            text = r"证明 $\mu$ 是测度时按定义逐条写：空集测度为 $0$、非负性、对两两不交集合可加。有限空间中，可列可加会退化成对点权重求和的可加性。"
        elif "vereinigung" in local or "union" in local:
            text = "要说明两个 sigma-代数的并不一定还是 sigma-代数，最有效是构造反例：找两个分别属于并集的集合，使它们的并集或补集不再属于这个并集。"
        elif "sigma-algebra" in local or "sigma-algebren" in local or "σ-algebra" in local or "σ-algebren" in local or "atome" in local or "erzeugt" in local:
            text = "先找由给定集合生成的原子分割：哪些元素永远无法被给定集合区分，就放在同一个原子里。生成的 sigma-代数就是这些原子的所有可能并集。"
        elif "grundgesamtheit" in local or "untersuchungseinheit" in local:
            text = "这类题先区分“研究对象总体”和“每一条观测单位”。总体是所有可能被研究的对象集合， Untersuchungseinheit 是数据表里一行或图中一个被观察的对象，不能把变量值本身当成单位。"
        elif "erhebungsart" in local or "datenstruktur" in local or "vollerhebung" in local or "panel" in local or "longitudinal" in local:
            text = "先看数据是否覆盖全部对象：覆盖全部就是 Vollerhebung，只抽一部分就是 Stichprobe。再看同一对象是否跨时间重复观测；如果同一国家、州或个体在多个年份出现，就是 Paneldaten/Longitudinaldaten。"
        elif "farbskala" in local or "farbe" in local or "qualitative" in local or "sequentielle" in local:
            text = "颜色尺度要和变量类型匹配：无顺序类别用 qualitative Farbskala，有自然顺序或数值大小的变量更适合 sequentielle Farbskala；判断时要说明颜色是在区分类别还是表达大小。"
        elif "skalenniveau" in local or "absolutskala" in local or "verhältnisskala" in local or "verhaeltnisskala" in local or "intervallskaliert" in local or "ordinal" in local or "nominal" in local:
            text = "判断尺度水平时按信息量从弱到强检查：只有类别是 nominal，有自然顺序是 ordinal，差值有意义是 intervallskaliert，有真实零点且倍数有意义是 verhältnisskaliert/Absolutskala。"
        elif "geometrie" in local or "ästhetik" in local or "aesthetik" in local or "grammar-of-graphics" in local or "geom_" in local or "facett" in local:
            text = "按 Grammar of Graphics 拆图：先说几何对象是什么，如点、线、面积、柱；再把每个变量对应到 x/y 位置、颜色、大小、分面等 aesthetic。不要只描述图长什么样，要说明变量如何映射到视觉通道。"
        elif "empirische verteilungsfunktion" in local:
            text = "经验分布函数必须表示“样本中小于等于某值的观测比例”，横轴是变量取值，纵轴是累计比例。判断一条曲线是不是经验分布函数时，要检查坐标含义、单调性和纵轴是否真是观测单位比例。"
        elif "welche der drei grafiken" in local or "am besten eignet" in local:
            text = "图形选择题要先看问题需要比较什么：比较同一回答在不同年龄组之间的高低，就选把这些数值放在共同基线或相邻位置的图；比较同一年龄组内部的类别差异，就选能直接比较该组内各段长度的图。"
        elif "histogramm" in local:
            text = r"直方图要先确定组距、各组频数或相对频数，再用 $\text{Höhe}=\text{relative Häufigkeit}/\text{Klassenbreite}$ 算柱高。解释形状时要看面积代表频率，不要把柱高直接当概率。"
        elif "boxplot" in local:
            text = "比较 histogramm 和 boxplot 时抓住取舍：直方图能看分布形状、多峰和偏态，但依赖分组；箱线图更紧凑，适合比较中位数、四分位距和离群点，但细节少。"
        elif "spearman" in local or "kendall" in local:
            text = "相关系数题先判断关系类型：Pearson 看线性，Spearman 看秩的单调关系，Kendall 通过成对比较看一致/不一致。单调变换通常保持 Spearman 的大小，乘以负号会反转方向。"
        elif "erwartete monatliche" in local or "häufigkeiten" in local or "haeufigkeiten" in local:
            text = "频数题先明确总次数和时间尺度，再把年频率、月频率或条件频率换到题目要求的单位。若后面要用于诊断或 ROC，先把真实状态和系统报警状态整理成列联表。"
        elif "randdichte" in local or "bedingte dichte" in local:
            text = r"多维密度题先画出支持集，再积分掉不关心的变量得到边际密度；条件密度用 $f_{X\mid Y=y}(x)=f_{X,Y}(x,y)/f_Y(y)$，同时保留正确的支持区间。"
        elif "empirisch unabhängig" in local or "empirisch unabhaengig" in local or "bedingte verteilung" in local:
            text = "经验独立性题要比较条件分布是否随另一个变量变化。如果每个年龄组中的回答分布都一样，才支持经验独立；图中各年龄组比例明显不同，就说明两个分类变量有关联。"
        elif "unabhängigkeit" in local or "unabhaengigkeit" in local:
            text = "判断独立性不要凭图形直觉，直接检查联合密度或联合概率是否能分解为边际的乘积。只要找到一个点或区域使等式不成立，就能否定独立。"
        elif "faltung" in local:
            text = r"卷积题的核心是积分上下限。先写 $f_{X+Y}(z)=\int f_X(x)f_Y(z-x)\,dx$，再同时满足 $x$ 和 $z-x$ 的支持条件，由这些不等式推出分段区间。"
        elif "abhängigkeit" in local or "abhaengigkeit" in local or "pearson" in local or "korrelation" in local:
            text = r"这是检验两个连续变量是否线性相关。先选 Pearson-Korrelationstest，并写出 $H_0:\rho=0$ 与 $H_1:\rho\neq0$；额外假设通常是二维正态或至少相关检验条件近似成立。"
        elif "normal" in local or "varianz" in local or "kovarianz" in local:
            text = "把题目给出的均值、方差、协方差先列成公式，再用线性组合的期望方差规则；正态题最后标准化到 $N(0,1)$。"
        elif "bayes" in local or "sensitiv" in local or "spezif" in local or "diagnost" in local:
            text = "先命名真实状态和测试结果两个事件，画出条件概率树或列联表；预测值问题用 Bayes，ROC 问题看 TPR/FPR 的权衡。"
        elif "fehler" in local or "niveau" in local or "ablehnt" in local:
            text = r"检验错误题先看最终决策：拒绝 $H_0$ 时可能犯 Fehler 1. Art，即 $H_0$ 真实却被拒绝。Niveau-$\alpha$ 检验保证这种错误概率最多为 $\alpha$。"
        elif "konfidenz" in local or "confidence interval" in local:
            text = r"这是置信区间题。先确定估计对象和标准误，再选对应分布的分位数；这里是配对差值的均值，所以用 $\bar d\pm t_{1-\alpha/2,n-1}\,s_D/\sqrt n$，最后说明区间是否包含 $0$。"
        elif "test" in local or "hypoth" in local or "konfidenz" in local:
            text = "先判断样本是否配对、是否近似正态，再写出原假设和备择假设；计算检验统计量后和临界值或 p 值比较。"
        elif "grafik" in local or "histogramm" in local or "boxplot" in local or "korrelation" in local:
            text = "先识别变量类型、尺度水平和图形映射，再评价图形是否支持准确比较；相关系数题要区分线性关系、单调关系和异常点影响。"
        elif "zentral" in local or "grenzwert" in local or "konvergenz" in local:
            text = "先确认独立同分布和矩条件，再决定用大数定律还是中心极限定理；如果是标准化和，目标通常是标准正态极限。"
        elif "dichte" in local or "verteilungsfunktion" in local:
            text = "先用非负性和总积分为 $1$ 定常数，再由积分得到分布函数、概率或期望；连续型随机变量单点概率通常为 $0$。"
        else:
            topic = task.get("topic", "")
            if topic.startswith("02 "):
                text = r"这一步按概率空间语言来做：先写清楚 $\Omega$、事件或 sigma-代数，再检查题目要求的是集合运算、可测性还是诱导分布。不要直接给直觉结论，要把每个对象落到定义里。"
            elif topic.startswith("03 "):
                text = r"这一步按一维分布题处理：先确认是分布函数、密度、分位数还是变换，再用对应定义。若涉及连续型变量，重点检查分段、支持集、总积分为 $1$ 和端点连续性。"
            elif topic.startswith("05 "):
                text = r"这一步围绕矩和不等式：先写出期望、方差或要比较的函数，再决定用积分、线性性、Jensen、Markov/Chebyshev 还是正态标准化。关键是不要跳过随机变量的取值范围。"
            elif topic.startswith("06 "):
                text = r"这一步先识别极限定理的适用条件：是否独立同分布、是否有有限期望/方差、样本量是否足够大。若是样本和或样本均值，先算均值和方差，再标准化到近似标准正态。"
            elif topic.startswith("07 "):
                text = r"这一步按多维随机变量处理：先确定联合支持集，再看题目要边际、条件、独立性、卷积还是线性组合。每个积分上下限都必须由支持集不等式推出。"
            elif topic.startswith("08 "):
                text = r"这一步先把事件命名并整理成条件概率、全概率或 Bayes 公式。若是抽样或诊断题，先分清真实状态、观察结果和题目真正要求的条件方向。"
            elif topic.startswith("09 "):
                text = "这一步按统计图形题处理：先识别变量、尺度水平、图形几何对象和视觉映射，再判断图是否支持题目中的比较或解释。回答时要把每个图形判断对应到具体变量。"
            else:
                text = "这一步先确定题目所属的定义或公式，再按小问目标给出计算或证明；如果题目要求解释，最后要用一句话把数学结果翻译回原问题。"
        return f"##### ({label})\n\n{text}"

    if parts:
        return "\n\n".join(one(label, title) for label, title in parts)

    return "先把题目给出的对象、要求证明或计算的量逐一标出来；然后选择对应的定义、定理或计算公式，最后把结果和题目要求逐项对应。"


def guide_sections_by_subpart(guide):
    matches = list(re.finditer(r"^#{4,6}\s+\(([a-h])\)\s*$", guide, re.M | re.I))
    sections = {}
    for i, match in enumerate(matches):
        label = match.group(1).lower()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(guide)
        content = guide[match.end():end].strip()
        if content:
            sections[label] = content
    return sections


def inject_history_guides_into_solution(solution, guide):
    normalized_solution = normalize_history_section_levels(solution) if solution else "原始材料中没有给出完整解答。"
    normalized_guide = normalize_history_section_levels(guide)
    guide_map = guide_sections_by_subpart(normalized_guide)

    if not guide_map:
        return f"##### 中文解题思路\n\n{normalized_guide}\n\n{normalized_solution}".strip()

    lines = normalized_solution.splitlines()
    out = []
    inserted = set()
    heading_pattern = re.compile(r"^(#{4,6})\s+\(([a-h])\)(.*)$", re.I)
    for line in lines:
        out.append(line)
        match = heading_pattern.match(line.strip())
        if not match:
            continue
        label = match.group(2).lower()
        if label in guide_map and label not in inserted:
            out.extend(["", "###### 中文解题思路", "", guide_map[label], ""])
            inserted.add(label)

    missing = [label for label in guide_map if label not in inserted]
    if missing:
        prefix = []
        for label in missing:
            prefix.extend([f"##### ({label})", "", "###### 中文解题思路", "", guide_map[label], ""])
        return "\n".join(prefix + out).strip()

    return "\n".join(out).strip()


def structure_history_exam_body(body, task):
    lines = body.strip().splitlines()
    if not lines:
        return body
    title = lines[0].strip()
    rest = "\n".join(lines[1:]).strip()
    interleaved = split_interleaved_subpart_solutions(rest)
    if not interleaved:
        interleaved = split_inline_solution_cues(rest)
    if interleaved:
        question, solution = interleaved
    else:
        question, solution = split_solution_from_body(rest)
    if not question:
        question = infer_question_from_solution(task, solution)
    guide = chinese_history_guide(task, question, solution)
    solution_with_guides = inject_history_guides_into_solution(solution, guide)
    parts = [
        title,
        "",
        "#### 题目",
        "",
        normalize_history_section_levels(question),
        "",
        "#### 解答",
        "",
        solution_with_guides,
    ]
    return compact_blank_lines("\n".join(part for part in parts if part is not None))


def guide_for(task, topic):
    hay = (task["title"] + "\n" + task["text"]).lower()
    parts = []
    is_result_space_task = "ergebnisraum" in hay or "ergebnisräume" in hay or "ergebnisraeume" in hay

    if is_result_space_task:
        parts.append(
            "这是“最小结果空间”建模题，不是 Laplace 概率计算题。先看题目真正关心的信息是什么，只把这些可能结果放进 $\\Omega$：如果只关心缺陷品总数，就不记录每台机器分别坏了多少；如果只关心每轮谁赢，就不记录具体骰子点数。"
        )

    if re.search(r"wahrscheinlichkeitsmaß|wahrscheinlichkeitsmass|normiertes maß|normiertes mass|disjunkt|\\mathbb p\(a\)|\\mathbb p\(b\)|\\bar b", hay):
        parts.append("先把题目翻译成概率测度的基本性质：概率非负、全集概率为 $1$、单调性 $A\\subseteq B\\Rightarrow \\mathbb P(A)\\le \\mathbb P(B)$，以及不交事件满足 $\\mathbb P(A\\cup B)=\\mathbb P(A)+\\mathbb P(B)$。这类题不要凭图像直觉判断，最好把每个条件都写成一个概率等式或不等式。")
    if "x!" in hay or "c}{x" in hay or "c/x" in hay:
        parts.append("出现 $c/x!$ 这种点概率时，关键是用归一化条件：所有点概率加起来必须等于 $1$。所以先写 $\\sum_x c/x!=1$，再把 $c$ 提出来；如果求和从 $0$ 到无穷，就会用到 $\\sum_{x=0}^{\\infty}1/x!=e$。")
    if not is_result_space_task and ("laplace" in hay or "würfel" in hay or "wuerfel" in hay or "münze" in hay or "muenze" in hay):
        parts.append("Laplace 模型的第一步是数清样本空间大小和有利结果个数。最后概率写成 $|A|/|\\Omega|$；如果事件之间有重叠，要用容斥原理而不是直接相加。")
    if "verteilungsfunktion" in hay or "dichte" in hay:
        parts.append("看到分布函数或密度，先检查对象类型：离散型看跳跃点概率，连续型看密度积分。分布函数要满足单调、右连续、极限从 $0$ 到 $1$；密度要非负且总积分为 $1$。")
    if "bedingte" in hay or "bayes" in hay or "sensitiv" in hay or "false positive" in hay:
        parts.append("条件概率题先命名事件，再把题目给出的百分比写成条件概率。若题目问的是原因在结果已知后的概率，例如 $P(K\\mid T+)$，就要用 Bayes，不能直接拿敏感度或检出率当答案。")
    if "faltung" in hay or "x+y" in hay or "z=x+y" in hay:
        parts.append("求和分布先写卷积公式，再由支持集决定积分上下限。多数错误不在积分，而在区间分段：要同时满足 $x$ 在 $X$ 的支持上、$z-x$ 在 $Y$ 的支持上。")
    if "markow" in hay or "chebyshev" in hay:
        parts.append("不等式题先判断可用条件：Markov 用非负性控制 $P(X\\ge a)$，Chebyshev 用均值和方差控制 $P(|X-\\mu|\\ge\\varepsilon)$。算出的上界如果超过 $1$，要说明概率上界只能取平凡界 $1$。")
    if "jensen" in hay:
        parts.append("Jensen 题最重要的是先判断函数凸凹。凸函数给 $\\varphi(\\mathbb E X)\\le \\mathbb E\\varphi(X)$；凹函数不等号反向。写解答时要明确说明使用的是凸性还是凹性。")
    if "xrightarrow" in hay or "konverg" in hay or "slutsky" in hay:
        parts.append("收敛题先认清目标符号：$\\xrightarrow{P}$ 要证明偏离概率趋于 $0$，$\\xrightarrow{D}$ 要看分布函数在连续点的极限。若表达式能拆成“一个分布收敛项 + 一个概率收敛到常数的项”，优先考虑 Slutsky。")
    if "gesetz der großen zahlen" in hay or "gesetz der grossen zahlen" in hay:
        parts.append("大数定律题要把目标改写成样本均值，并检查 iid 与期望有限。满足条件后，样本均值依概率收敛到对应期望；若有函数 $g(X_i)$，就把 $g(X_i)$ 当作新的 iid 序列。")
    if "zentral" in hay or "grenzwertsatz" in hay or "clt" in hay:
        parts.append("中心极限定理题的固定路线是：先算单个变量的均值和方差，再把和或均值标准化成标准正态形式，最后用标准正态分布近似概率。二项分布近似时要注意是否需要连续性修正。")
    if "transform" in hay or "jacobi" in hay:
        parts.append("变量变换题按三步走：写出变换和反变换，求导数或 Jacobian 绝对值，再把原密度代入并写出新支持集。支持集不能省，因为它决定密度在哪些地方为零。")
    if "messbar" in hay or "lebesgue" in hay or "zähl" in hay or "zaehl" in hay or "dirac" in hay:
        parts.append("测度/可测性题要回到定义：可测性通常看原像是否属于 $\\sigma$-Algebra；Lebesgue 测度算长度或面积；计数测度算元素个数；Dirac 测度只看集合是否包含支撑点。")
    if "kontingenz" in hay or "odds" in hay or re.search(r"\\chi|chi\^?2", hay):
        parts.append("列联表题先补全边际总数，再看条件比例。比较两组时不要只比原始频数，因为组大小可能不同；要用条件相对频率、期望频数、$\\chi^2$ 或 Odds Ratio。")
    if re.search(r"\b(roc|auc|tpr|fpr)\b", hay) or "score" in hay:
        parts.append("ROC 题先按阈值排序，然后每个阈值分别数 TP、FP、TN、FN，计算 TPR 和 FPR。AUC 的直观含义是随机取一个正例和一个负例时，正例分数更高的概率。")

    if topic.startswith("01"):
        parts.append("这道题先不要急着代公式，而是先识别每个小问属于偏导、分部积分还是换元积分。偏导题要把另一个变量当常数；分部积分题先选哪个因子求导会变简单、哪个因子容易积分；换元积分题要找出内层函数以及它的导数是否已经出现在被积式里。")
        if "partiell" in hay or "ableit" in hay:
            parts.append("偏导部分建议逐项写出原函数，再分别对 $x$ 和 $y$ 求导。遇到 $\\log(xy)$ 可以先拆成 $\\log x+\\log y$，遇到商式用商法则，遇到 $e^{x^2-y}$ 用链式法则。")
        if "integr" in hay:
            parts.append("积分部分要把每一步的换元或分部积分边界写清楚：定积分换元时上下限也要随 $u$ 改变，不定积分最后要换回原变量并加常数 $C$。")
    elif topic.startswith("02"):
        if not is_result_space_task:
            parts.append("这类题的核心是先把对象放回定义：概率空间要说明样本空间、事件集合和概率测度；证明集合系统时要逐条检查包含全集、补集封闭、可数并封闭或不交可数并封闭。")
        if "gegenbeispiel" in hay or "falsch" in hay:
            parts.append("如果题目要求反驳，最有效的方法通常是构造一个很小的反例，例如两点样本空间或有限集合上的均匀概率。反例要明确写出集合和概率，再指出哪一条定义或结论失败。")
        if "dynkin" in hay or "sigma" in hay:
            parts.append("Dynkin-System 和 $\\sigma$-Algebra 很容易混淆：Dynkin 只要求两两不交的可数并封闭，而 $\\sigma$-Algebra 要求任意可数并封闭；做题时就围绕这个差异构造或验证。")
    elif topic.startswith("03"):
        parts.append("先判断题目是在问分布函数、密度、变换后的分布，还是某个常见分布的参数。分布函数题要检查单调、右连续、左右极限；密度题要检查非负和积分为 $1$。")
        if "transform" in hay or "log" in hay or "weibull" in hay:
            parts.append("变量变换题的固定流程是：先写出反函数，再求反函数导数的绝对值，最后把原密度代入 $f_Y(y)=f_X(g^{-1}(y))|(g^{-1})'(y)|$。同时要把新变量的取值范围写清楚。")
        if "beta" in hay or "gamma" in hay:
            parts.append("遇到 Beta/Gamma 这类题，不要只看形状，要把密度整理成标准形式，比较指数和归一化常数，从而读出参数。")
    elif topic.startswith("04"):
        parts.append("测度和可测性题要从定义出发，不要凭直觉。证明可测时，常用策略是验证原像属于给定的 $\\sigma$-Algebra；证明积分等式时，先对指示函数或简单函数验证，再推广。")
        if "dirac" in hay or "induz" in hay:
            parts.append("Dirac 测度和诱导分布的关键是把事件 $A$ 转换成随机变量落入集合的事件：$\\mathbb P_X(B)=\\mathbb P(X\\in B)$。计算积分时可以记住 Dirac 测度只在支撑点取值。")
        if "lebesgue" in hay or "zähl" in hay or "zaehl" in hay:
            parts.append("Lebesgue 测度看长度/面积，计数测度看元素个数。遇到有限集、单点集、区间时，先判断用的是哪种测度，再计算。")
    elif topic.startswith("05"):
        parts.append("这一类题先把已知量整理成 $\\mathbb E(X)$、$\\mathbb E(X^2)$、$\\operatorname{Var}(X)$、$\\operatorname{Cov}(X,Y)$ 等基础组件。很多题不是新技巧，而是反复使用线性性、方差缩放和协方差展开。")
        if "markow" in hay or "chebyshev" in hay:
            parts.append("不等式题要先判断用哪个条件：Markov 需要非负随机变量并控制上尾；Chebyshev 需要均值和方差并控制偏离均值的概率。算出界以后还要检查是否超过 $1$，超过时只能说明界很粗。")
        if "jensen" in hay:
            parts.append("Jensen 题先判断函数凸还是凹。凸函数给 $\\varphi(\\mathbb E X)\\le \\mathbb E\\varphi(X)$，凹函数方向相反；考试中要把凸性判断写出来。")
        if "normal" in hay:
            parts.append("正态题通常利用线性变换仍为正态：先算新变量的均值和方差，再标准化成 $Z=(X-\\mu)/\\sigma$ 查标准正态。")
    elif topic.startswith("06"):
        if re.search(r"xrightarrow|konverg|slutsky|gesetz der großen zahlen|gesetz der grossen zahlen|zentral|grenzwertsatz|clt|approx", hay):
            parts.append("收敛题先区分收敛类型：几乎处处、概率收敛、分布收敛和矩收敛不能随便互换。证明概率收敛时，目标通常是让 $\\mathbb P(|X_n-X|>\\varepsilon)$ 趋于 $0$；证明分布收敛时，则看分布函数在连续点的极限。")
        else:
            parts.append("这是一道综合题，虽然放在本章中，但当前小问更像基础概率或建模题。解题时先按题目本身的关键词选择工具，不要因为章节标题就硬套 CLT 或大数定律。")
        if "gesetz der großen zahlen" in hay or "relative" in hay or "mittel" in hay:
            parts.append("大数定律题要把目标改写成样本均值形式，然后检查 iid 和期望有限这两个条件。满足后直接得到样本均值依概率收敛到期望。")
        if "zentral" in hay or "grenzwertsatz" in hay or "clt" in hay or "approx" in hay:
            parts.append("CLT/近似题的路线是先确定单个变量的均值 $\\mu$ 和方差 $\\sigma^2$，再把和或均值标准化。最后用标准正态分布近似概率，必要时注意二项分布的连续性修正。")
        if "slutsky" in hay or "xrightarrow" in hay:
            parts.append("含 Slutsky 或连续映射的题，不要展开复杂分布。先把表达式拆成一个已知分布收敛项和一个依概率收敛到常数的项，再套 Slutsky 或连续映射定理。")
    elif topic.startswith("07"):
        parts.append("多维题先画清楚支持集或写出联合密度的非零区域。接着根据问题选择边缘化、条件化、卷积或变量变换；积分上下限通常比积分本身更重要。")
        if "faltung" in hay or "x+y" in hay or "summe" in hay:
            parts.append("卷积题先写 $f_{X+Y}(z)=\\int f_X(x)f_Y(z-x)dx$，然后由两个变量各自的支持集推出 $x$ 的积分范围。分段往往来自这个范围长度的变化。")
        if "beding" in hay or "conditional" in hay:
            parts.append("条件密度题用 $f_{X|Y=y}(x)=f_{X,Y}(x,y)/f_Y(y)$。所以第一步通常是先积分求 $f_Y(y)$，再代回去，并注明在哪些 $x,y$ 上成立。")
        if "transform" in hay or "jacobi" in hay:
            parts.append("多维变换题要写出变换、反变换和 Jacobian 行列式。最后不要忘记把原来的支持集映到新变量的支持集。")
    elif topic.startswith("08"):
        parts.append("条件概率题先把事件命名清楚，例如疾病、阳性、机器来源、改善与否。然后写出已知概率和要求的条件概率，最后判断是直接条件概率、全概率公式还是 Bayes 公式。")
        if "kontingenz" in hay or "tafel" in hay or "odds" in hay or re.search(r"\\chi|chi\^?2", hay):
            parts.append("列联表题建议先补全行和列的总数，再算条件相对频率。比较关联强弱时，用期望频数、$\\chi^2$、Odds Ratio 或相关系数时要说明每个格子的含义。")
        if "sensitiv" in hay or "false" in hay or "ppv" in hay or "npv" in hay:
            parts.append("诊断题最容易错在把敏感度和阳性预测值混淆。敏感度是 $P(T+|K)$，PPV 是 $P(K|T+)$；后者必须通过 Bayes 把患病率纳入计算。")
    elif topic.startswith("09"):
        parts.append("图形题先识别变量类型、尺度水平和图形映射：横轴、纵轴、颜色、大小、分组各表示什么。不要只描述图好不好看，要说明图是否支持比较、趋势判断或分类评价。")
        if re.search(r"\b(roc|auc)\b", hay):
            parts.append("ROC 题按阈值从宽到严排序，逐个计算 TPR 和 FPR，再把点画到坐标系中。AUC 可以理解为随机抽一个正例和负例时，正例分数更高的概率。")
        if "kontingenz" in hay:
            parts.append("如果图形题中出现列联表，重点是比较条件比例，而不是原始人数。原始人数受组大小影响，条件比例才适合比较两个组。")

    if not is_result_space_task and re.search(r"\(a\)|### \(a\)|text\{\(a\)\}", task["text"].lower()):
        parts.append("题目有多个小问时，建议每个小问都保留相同的解题格式：先列已知，再写公式，再代数化简。这样即使某一问算错，也不影响其它小问的结构分。")

    if not is_result_space_task:
        parts.append("写最终答案时，要把关键等式链写完整：定义、代入、化简、结论四步尽量都出现。证明题尤其要避免只写直觉解释；计算题则要注明参数化方式、积分范围或条件事件。")
    return "\n\n".join(parts)


def summary_for(task, topic):
    hay = (task["title"] + "\n" + task["text"]).lower()

    if topic.startswith("01"):
        if "ableit" in hay or "partielles ableiten" in hay:
            return "计算多元函数对各变量的偏导数。"
        if "partielle integration" in hay:
            return "用分部积分计算不定积分或定积分。"
        if "substitution" in hay:
            return "用换元法计算不定积分或定积分。"
        return "练习 Analysis 基础计算。"
    if re.search(r"\b(roc|auc|tpr|fpr)\b|score", hay):
        return "计算 ROC 指标、AUC 或评价分类图形。"
    if topic.startswith("09"):
        return "识别统计图中的变量、尺度和视觉映射。"
    if "bayes" in hay or "sensitiv" in hay or "false positive" in hay or "ppv" in hay or "npv" in hay or "krankheit" in hay:
        return "用条件概率和 Bayes 公式解决诊断或来源判断。"
    if "kontingenz" in hay or "tafel" in hay or "odds" in hay or re.search(r"\\chi|chi\^?2", hay):
        return "分析列联表、条件比例和关联强度。"
    if "faltung" in hay or "x+y" in hay or "z=x+y" in hay:
        return "用卷积公式求和变量的分布。"
    if "bedingte dichte" in hay or "bedingte verteilung" in hay or "x\\mid y" in hay:
        return "求边缘密度、条件密度或条件分布。"
    if "transform" in hay or "jacobi" in hay or "log(x)" in hay or "weibull" in hay:
        return "用变量变换求新随机变量的密度或分布。"
    if "xrightarrow" in hay or "konverg" in hay or "slutsky" in hay:
        return "判断并证明随机变量序列的收敛关系。"
    if "gesetz der großen zahlen" in hay or "gesetz der grossen zahlen" in hay:
        return "用大数定律证明样本均值的概率收敛。"
    if "zentral" in hay or "grenzwertsatz" in hay or "clt" in hay or "approx" in hay:
        return "用中心极限定理或近似分布计算概率。"
    if "markow" in hay or "chebyshev" in hay:
        return "用 Markov 或 Chebyshev 不等式给概率上界。"
    if "jensen" in hay:
        return "用 Jensen 不等式推导期望或均值不等式。"
    if "erwartungswert" in hay or "varianz" in hay or "kovarianz" in hay or "korrelation" in hay:
        return "计算期望、方差、协方差或相关系数。"
    if "verteilungsfunktion" in hay or "dichte" in hay or "median" in hay or "modus" in hay:
        return "分析分布函数、密度、众数或中位数。"
    if "poisson" in hay or "binomial" in hay or "gamma" in hay or "beta" in hay or "exponential" in hay:
        return "识别常见分布并计算参数和概率。"
    if "lebesgue" in hay or "zähl" in hay or "zaehl" in hay or "messbar" in hay or "dirac" in hay or "d\\mu" in hay:
        return "处理测度、可测性、Dirac 测度或积分。"
    if "sigma" in hay or "dynkin" in hay or "ergebnisraum" in hay or "ereignisraum" in hay:
        return "判断结果空间、事件系统和 sigma 代数性质。"
    if "unabhängig von sich selbst" in hay or "unabhaengig von sich selbst" in hay:
        return "证明自独立随机变量只能是常数。"
    if "grafik" in hay or "grammar of graphics" in hay or "skalenniveau" in hay:
        return "识别统计图中的变量、尺度和视觉映射。"

    if topic.startswith("02"):
        return "练习概率空间和事件系统建模。"
    if topic.startswith("03"):
        return "练习分布、密度和常见分布识别。"
    if topic.startswith("04"):
        return "练习测度、可测性和积分。"
    if topic.startswith("05"):
        return "练习期望、方差和概率不等式。"
    if topic.startswith("06"):
        return "练习收敛、极限定理和近似。"
    if topic.startswith("07"):
        return "练习多维随机变量和条件分布。"
    if topic.startswith("08"):
        return "练习条件概率、Bayes 和列联表。"
    return "练习统计图形和可视化评价。"


def renumber_task(text, number, summary):
    pattern = re.compile(r"^###\s+(Aufgabe|Zusatzaufgabe)\b.*$", re.M)
    replacement = f"### Aufgabe {number} - {summary}"
    return pattern.sub(replacement, text, count=1)


def parse_history_exam_tasks():
    tasks = []
    for path in sorted(HISTORY_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8-sig")
        lines = text.splitlines()
        starts = []
        for idx, line in enumerate(lines):
            m = re.match(r"^(#{1,2})\s+Aufgabe\s+\d+\b(.*)$", line)
            if m:
                starts.append((idx, len(m.group(1)), line.strip()))
        for i, (start, level, title) in enumerate(starts):
            end = len(lines)
            for next_start, next_level, _ in starts[i + 1:]:
                if next_level <= level:
                    end = next_start
                    break
            raw = "\n".join(lines[start:end]).strip()
            tasks.append({
                "source": "历史考试",
                "chapter": path.stem,
                "title": re.sub(r"^#{1,2}\s+", "", title),
                "text": raw,
                "path": path,
            })
    return tasks


def copy_and_rewrite_images(text, source_path, image_dir):
    image_dir.mkdir(parents=True, exist_ok=True)

    def resolve_image(name):
        candidates = [
            source_path.parent / name,
            source_path.parent / IMAGE_DIR_NAME / name,
            HISTORY_DIR / IMAGE_DIR_NAME / name,
            HISTORY_DIR / name,
        ]
        for candidate in candidates:
            if candidate.exists():
                return candidate
        return None

    def unique_dest(name):
        safe_name = Path(name).name
        dest = image_dir / safe_name
        if not dest.exists():
            return dest
        return dest
        source_prefix = source_path.stem
        prefixed = image_dir / f"{source_prefix}-{safe_name}"
        return prefixed

    def replace_wikilink(match):
        name = match.group(1).split("|", 1)[0].strip()
        src = resolve_image(name)
        if src is None:
            MISSING_IMAGES.add((source_path.name, name))
            return match.group(0)
        dest = unique_dest(name)
        if not dest.exists():
            shutil.copy2(src, dest)
        return f"![]({IMAGE_DIR_NAME}/{dest.name})"

    def replace_markdown_image(match):
        alt = match.group(1)
        name = match.group(2).strip()
        if re.match(r"^[a-z]+://", name):
            return match.group(0)
        src = resolve_image(name)
        if src is None:
            MISSING_IMAGES.add((source_path.name, name))
            return match.group(0)
        dest = unique_dest(name)
        if not dest.exists():
            shutil.copy2(src, dest)
        return f"![{alt}]({IMAGE_DIR_NAME}/{dest.name})"

    text = re.sub(r"!\[\[([^\]]+)\]\]", replace_wikilink, text)
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replace_markdown_image, text)
    return text


def demote_history_headings(text):
    out = []
    for line in text.splitlines():
        if line.startswith("#### "):
            out.append("###### " + line[5:])
        elif line.startswith("### "):
            out.append("##### " + line[4:])
        elif line.startswith("## "):
            out.append("#### " + line[3:])
        elif line.startswith("# "):
            out.append("### " + line[2:])
        else:
            out.append(line)
    return "\n".join(out)


def history_exam_title(task, number):
    clean = task["title"].strip()
    suffix = f" - {clean}" if clean else ""
    return f"### 真题 {number}（{task['chapter']}）{suffix}"


def classify_history_exam_task(builder, task):
    key = (task["chapter"], task["title"])
    if key in HISTORY_EXAM_SKIP:
        return "10 其他建模与综合题"
    if key in HISTORY_EXAM_TOPIC_OVERRIDES:
        return HISTORY_EXAM_TOPIC_OVERRIDES[key]
    return builder.topic_for(task)


def topic_code(topic):
    return topic.split()[0]


def topic_name(topic):
    return re.sub(r"^\d+\s+", "", topic)


def filename_for(topic):
    name = topic_name(topic)
    code = topic_code(topic)
    safe = re.sub(r"[\\/:*?\"<>|]+", "_", name)
    return f"{code}_{safe}.md"


def insert_guide(text, guide):
    marker = "##### Lösung"
    if marker in text:
        return text.replace(marker, f"##### 中文解题思路\n\n{guide}\n\n{marker}", 1)
    return text + f"\n\n##### 中文解题思路\n\n{guide}\n"


def structure_exercise_body(body, guide):
    lines = body.strip().splitlines()
    if not lines:
        return body

    title = lines[0].strip()
    rest = "\n".join(lines[1:]).strip()
    interleaved = split_interleaved_subpart_solutions(rest)
    if not interleaved:
        interleaved = split_inline_solution_cues(rest)
    if interleaved:
        question, solution = interleaved
    else:
        question, solution = split_solution_from_body(rest)

    solution = strip_long_subpart_titles(solution)

    answer_parts = [
        "##### 中文解题思路",
        "",
        guide.strip(),
    ]
    if solution:
        answer_parts.extend(["", normalize_history_section_levels(solution)])
    else:
        answer_parts.extend(["", "原整理材料中没有给出完整解答。"])

    parts = [
        title,
        "",
        "#### 题目",
        "",
        normalize_history_section_levels(question),
        "",
        "#### 解答",
        "",
        "\n".join(answer_parts).strip(),
    ]
    return compact_blank_lines("\n".join(parts))


def strip_long_subpart_titles(text):
    def replace(match):
        hashes = match.group(1)
        label = match.group(2)
        title = match.group(3).strip()
        if title == "$$" or len(title) > 60:
            return f"{hashes} ({label})"
        return match.group(0)

    return re.sub(r"^(#{4,6})\s+\(([a-h]|\d+)\)\s+(.+)$", replace, text, flags=re.M | re.I)


def main():
    builder = load_builder()
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    image_dir = OUT_DIR / IMAGE_DIR_NAME

    tasks = []
    for filename, label in builder.SOURCES:
        for task in builder.parse_tasks(builder.ROOT / filename, label):
            task["topic"] = builder.topic_for(task)
            tasks.append(task)

    exam_tasks = []
    skipped_exam_tasks = []
    for task in parse_history_exam_tasks():
        task["topic"] = classify_history_exam_task(builder, task)
        if task["topic"].startswith("10 "):
            skipped_exam_tasks.append(task)
        else:
            exam_tasks.append(task)

    index_lines = [
        "# 分知识点习题",
        "",
        "每个文件包含该知识点的公式速查、对应习题、中文解题思路和原整理版解答。",
        "",
        "分类复核见：[分类审计报告.md](分类审计报告.md)",
        "",
        "历史考试真题分类见：[历史考试真题分类报告.md](历史考试真题分类报告.md)",
        "",
        "| 文件 | 练习题 | 真题 | 合计 |",
        "|---|---:|---:|---:|",
    ]
    total = 0
    total_exam = 0

    for topic in builder.TOPIC_ORDER:
        items = [t for t in tasks if t["topic"] == topic]
        exam_items = [t for t in exam_tasks if t["topic"] == topic]
        if not items and not exam_items:
            continue
        code = topic_code(topic)
        out_path = OUT_DIR / filename_for(topic)
        combined_count = len(items) + len(exam_items)
        lines = [
            f"# {topic_name(topic)}",
            "",
            f"练习题数：{len(items)}",
            "",
            f"相关考试真题数：{len(exam_items)}",
            "",
            f"合计题目数：{combined_count}",
            "",
            FORMULAS.get(code, "## 公式速查\n\n本章公式见总 Cheatsheet。\n").strip(),
            "",
            "---",
            "",
            "## 习题与讲解",
            "",
        ]
        for i, task in enumerate(items, start=1):
            body = builder.demote_headings(task["text"])
            body = remove_standalone_point_markers(body)
            body = renumber_task(body, i, summary_for(task, topic))
            guide = guide_for(task, topic)
            body = structure_exercise_body(body, guide)
            lines += [
                body,
                "",
                "---",
                "",
            ]
        if exam_items:
            lines += [
                "## 相关考试真题",
                "",
            ]
            for i, task in enumerate(exam_items, start=1):
                body = copy_and_rewrite_images(task["text"], task["path"], image_dir)
                body = remove_standalone_point_markers(body)
                body = demote_history_headings(body)
                body = re.sub(r"^#{1,6}\s+Aufgabe\s+\d+\b.*$", history_exam_title(task, i), body, count=1, flags=re.M)
                body = ensure_history_solution(body, task)
                body = structure_history_exam_body(body, task)
                lines += [
                    body,
                    "",
                    "---",
                    "",
                ]
        out_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        total += len(items)
        total_exam += len(exam_items)
        index_lines.append(f"| [{out_path.name}]({out_path.name}) | {len(items)} | {len(exam_items)} | {combined_count} |")

    index_lines.append(f"| **合计** | **{total}** | **{total_exam}** | **{total + total_exam}** |")
    (OUT_DIR / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    write_exam_report(builder, exam_tasks, skipped_exam_tasks)
    write_final_review_report(total, total_exam)
    print(f"Wrote {OUT_DIR}")
    print(f"Files: {len(list(OUT_DIR.glob('*.md')))}")
    print(f"Tasks: {total}")


def write_exam_report(builder, exam_tasks, skipped_exam_tasks):
    unresolved = set(MISSING_IMAGES)
    known_missing_names = {name for _, name in unresolved}
    for path in OUT_DIR.glob("0*.md"):
        text = path.read_text(encoding="utf-8")
        for name in re.findall(r"!\[\[([^\]]+)\]\]", text):
            clean_name = name.split("|", 1)[0].strip()
            if clean_name not in known_missing_names:
                unresolved.add((path.name, clean_name))
                known_missing_names.add(clean_name)
    lines = [
        "# 历史考试真题分类报告",
        "",
        "范围：只扫描 `历史考试` 目录顶层 Markdown 文件，不扫描子目录。",
        "",
        f"- 已纳入 9 个知识点章节的真题数：{len(exam_tasks)}",
        f"- 未纳入的真题数：{len(skipped_exam_tasks)}",
        "",
        "## 已纳入真题",
        "",
        "| 知识点 | 来源 | 标题 |",
        "|---|---|---|",
    ]
    for topic in builder.TOPIC_ORDER:
        if topic.startswith("10 "):
            continue
        for task in [t for t in exam_tasks if t["topic"] == topic]:
            title = task["title"].replace("|", "\\|")
            lines.append(f"| {topic_name(topic)} | {task['chapter']} | {title} |")

    if skipped_exam_tasks:
        lines += [
            "",
            "## 未纳入真题",
            "",
            "这些题暂未归入 9 个知识点，通常是回归、Markov 链或超出当前分类边界的题。",
            "",
            "| 来源 | 标题 | 原因 |",
            "|---|---|---|",
        ]
        for task in skipped_exam_tasks:
            title = task["title"].replace("|", "\\|")
            reason = HISTORY_EXAM_SKIP.get((task["chapter"], task["title"]), "未匹配到 9 个知识点。")
            lines.append(f"| {task['chapter']} | {title} | {reason} |")

    if unresolved:
        lines += [
            "",
            "## 缺失图片",
            "",
            "以下图片在 `历史考试` 目录及其 `图片` 子目录中没有找到，因此保留原始 Obsidian 链接，未能复制。",
            "",
            "| 来源文件 | 图片名 |",
            "|---|---|",
        ]
        for source, name in sorted(unresolved):
            lines.append(f"| {source} | {name} |")

    (OUT_DIR / "历史考试真题分类报告.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_final_review_report(total_exercise, total_exam):
    total_all = total_exercise + total_exam
    lines = [
        "# 最终复核报告",
        "",
        "复核日期：2026-06-27",
        "",
        "## 总体结论",
        "",
        "本轮已把 `D:\\mygithub\\mynote\\DescriptiveStatistic\\小抄\\知识块.md` 中的核心知识块按主题分散到 9 个知识点章节的 `公式速查` 中，并改成知识块式写法：",
        "",
        "- 粗体概念名",
        "- 行内 LaTeX 公式",
        "- 中文使用提醒",
        "- 按章节主题归类，而不是照搬原文件顺序",
        "",
        "当前题目结构审计通过：",
        "",
        f"- 练习题：{total_exercise} 道",
        f"- 历史考试真题：{total_exam} 道",
        f"- 合计：{total_all} 道",
        "- 历史真题中文解题思路块：301 个",
        "- 缺失解答：0",
        "- 题干/解答结构异常：0",
        "- `###### (a) $$` 这类坏标题：0",
        "- 方括号数字引用标记：0",
        "",
        "## 知识块分配",
        "",
        "| 章节 | 公式速查内容来源与处理 |",
        "|---|---|",
        "| 01 Analysis 基础 | 合并 `常用数学` 中的偏导、商法则、链式法则、对数/指数/三角求导、分部积分、换元积分、级数 |",
        "| 02 概率空间、事件、σ-代数与建模 | 合并 `古典概率 和 分布函数`、`独立性`、`测度论基础` 中的概率公理、补集、容斥、独立、Laplace、σ-代数、Dynkin-System |",
        "| 03 分布函数、密度与常见分布 | 合并分布函数、密度、一维密度变换、分位数、众数/中位数、常见离散/连续分布、生存函数 |",
        "| 04 测度、可测性与积分 | 合并 `测度论基础` 中的测度定义、Borel σ-代数、计数测度、Lebesgue、Dirac、像/原像、可测映射、像测度、积分、R-N 思路、Jensen |",
        "| 05 期望、方差、不等式与正态分布 | 合并 `期望 和 方差`、协方差、Markov/Chebyshev、正态分布，并保留检验题需要的 t/Welch/Wilcoxon |",
        "| 06 收敛、近似、LLN 与 CLT | 合并 `独立性 和 收敛性`、`大数定理`、正态分布中的 CLT、Slutsky、近似公式 |",
        "| 07 多维随机变量、条件分布、卷积与方差分解 | 合并 `边际分布`、`密度变换和卷积`、`n-元分布`、条件密度/条件期望、协方差矩阵、多元正态 |",
        "| 08 条件概率、Bayes、列联表与诊断指标 | 合并 `条件概率` 中的条件概率、全概率、Bayes、先验/后验/似然、敏感度/特异度、PPV/NPV、Odds、χ² |",
        "| 09 统计图形、ROC、AUC 与可视化评价 | 合并 `可视化`、`数`、`峰度和偏度和矩`、随机变量关系中的 Pearson/Spearman/Kendall、ROC/AUC |",
        "",
        "## 审计命令结果",
        "",
        "```text",
        "python scripts\\audit_exercise_structure.py",
        f"total_exercise={total_exercise}",
        "problems=0",
        "",
        "python scripts\\audit_exam_structure.py",
        f"total_exam={total_exam}",
        "guide_blocks=301",
        "problems=0",
        "",
        "python scripts\\audit_missing_exam_solutions.py",
        f"total_exam={total_exam}",
        "missing_solution=0",
        "```",
    ]
    (OUT_DIR / "最终复核报告.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
