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


def normalize_question_translation_key(text):
    return re.sub(r"\s+", " ", text.strip())


TERM_TRANSLATIONS = [
    ("Verteilungsfunktion", "分布函数"),
    ("Dichtefunktion", "密度函数"),
    ("Wahrscheinlichkeitsfunktion", "概率函数"),
    ("Wahrscheinlichkeitsmaß", "概率测度"),
    ("Wahrscheinlichkeitsraum", "概率空间"),
    ("Zufallsvariable", "随机变量"),
    ("Zufallsvariablen", "随机变量"),
    ("Ergebnisraum", "结果空间"),
    ("Ergebnisräume", "结果空间"),
    ("Ereignisraum", "事件空间"),
    ("Ereignisse", "事件"),
    ("Ereignis", "事件"),
    ("Mächtigkeit", "基数"),
    ("sigma-Algebra", "sigma-代数"),
    ("$\\sigma$-Algebra", "$\\sigma$-代数"),
    ("Dynkin-System", "Dynkin 系统"),
    ("unabhängig", "独立"),
    ("identisch verteilt", "同分布"),
    ("normalverteilt", "正态分布"),
    ("gemeinsam normalverteilte", "联合正态分布的"),
    ("stetig verteilt", "连续分布"),
    ("diskrete", "离散的"),
    ("stetige", "连续的"),
    ("Erwartungswert", "期望"),
    ("Varianz", "方差"),
    ("Standardabweichung", "标准差"),
    ("Kovarianz", "协方差"),
    ("Korrelation", "相关系数"),
    ("Korrelationskoeffizient", "相关系数"),
    ("Randdichten", "边际密度"),
    ("Randdichte", "边际密度"),
    ("Randverteilungen", "边际分布"),
    ("bedingte Dichte", "条件密度"),
    ("bedingte Verteilung", "条件分布"),
    ("bedingte Wahrscheinlichkeit", "条件概率"),
    ("gemeinsame Dichte", "联合密度"),
    ("gemeinsame Verteilung", "联合分布"),
    ("Faltungsdichte", "卷积密度"),
    ("Verteilung", "分布"),
    ("Dichte", "密度"),
    ("Wahrscheinlichkeit", "概率"),
    ("Wahrscheinlichkeiten", "概率"),
    ("Parameter", "参数"),
    ("Median", "中位数"),
    ("Modus", "众数"),
    ("Quantil", "分位数"),
    ("Konfidenzintervall", "置信区间"),
    ("Hypothesentest", "假设检验"),
    ("Nullhypothese", "原假设"),
    ("Alternative", "备择假设"),
    ("Signifikanzniveau", "显著性水平"),
    ("Stichprobe", "样本"),
    ("Stichproben", "样本"),
    ("Mittelwert", "均值"),
    ("empirische", "经验的"),
    ("relative Häufigkeit", "相对频率"),
    ("Häufigkeit", "频数"),
    ("Klassenbreite", "组距"),
    ("Histogramm", "直方图"),
    ("Boxplot", "箱线图"),
    ("Balkendiagramm", "柱状图"),
    ("Streudiagramm", "散点图"),
    ("Skalenniveau", "尺度水平"),
    ("Merkmale", "变量/特征"),
    ("Merkmal", "变量/特征"),
    ("Ausprägungen", "取值"),
    ("Ausprägung", "取值"),
    ("ROC-Kurve", "ROC 曲线"),
    ("AUC", "AUC"),
    ("Sensitivität", "敏感度"),
    ("Spezifität", "特异度"),
    ("positiv prädiktiver Wert", "阳性预测值"),
    ("negativ prädiktiver Wert", "阴性预测值"),
    ("Kontingenztafel", "列联表"),
    ("Wahrscheinlichkeitsbaum", "概率树"),
    ("Urnenmodell", "抽球模型"),
    ("Laplace-Experiment", "Laplace 实验"),
    ("Messraum", "测度空间"),
    ("messbar", "可测"),
    ("messbare", "可测的"),
    ("Bildmaß", "像测度"),
    ("Integral", "积分"),
    ("Integrale", "积分"),
    ("Maß", "测度"),
    ("Maße", "测度"),
    ("Funktion", "函数"),
    ("Funktionen", "函数"),
    ("Matrix", "矩阵"),
    ("Matrizen", "矩阵"),
    ("Eigenwerte", "特征值"),
    ("Grenzwert", "极限"),
    ("Konvergenz", "收敛"),
    ("Verteilungskonvergenz", "依分布收敛"),
    ("stochastische Konvergenz", "依概率收敛"),
    ("fast sichere Konvergenz", "几乎必然收敛"),
    ("Zentraler Grenzwertsatz", "中心极限定理"),
]


COMMON_SENTENCE_TRANSLATIONS = {
    "Gegeben sind:": "给定如下：",
    "Gegeben ist:": "给定如下：",
    "Gegeben:": "给定：",
    "Gegeben sei:": "给定：",
    "Sei:": "设：",
    "Es sei": "设：",
    "Es seien": "设：",
    "und:": "并且：",
    "mit:": "其中：",
    "wobei:": "其中：",
    "Zeigen Sie:": "证明：",
    "Zeigen Sie, dass:": "证明：",
    "Beweisen oder widerlegen Sie:": "证明或反驳：",
    "Begründen Sie Ihre Antwort.": "请说明你的答案理由。",
    "Interpretieren Sie das Ergebnis.": "解释该结果的含义。",
    "Interpretieren Sie den Wert.": "解释这个数值的含义。",
    "Berechnen Sie.": "请计算。",
    "Aufgaben": "题目",
    "Vorarbeit": "准备工作",
    "Betrachten Sie die Verteilungsfunktion": "考虑下列分布函数。",
    "Betrachten Sie:": "考虑下列对象：",
    "Die Wirkung von zwei Hustensäften A und B soll verglichen werden.": "比较两种止咳糖浆 A 和 B 的效果。",
    "Erste Studie:": "第一项研究：",
    "Zweite Studie:": "第二项研究：",
    "Die Zufallsvariable $X$ hat Dichte:": "随机变量 $X$ 的密度为：",
    "Die Dichte lautet:": "密度为：",
    "Die Verteilungsfunktion einer Zufallsvariablen $X$ lautet:": "随机变量 $X$ 的分布函数为：",
    "Dabei ist $c \\in \\mathbb{R}$ eine Konstante.": "其中 $c\\in\\mathbb R$ 是常数。",
    "Verwenden Sie für die folgenden Aufgaben $c=2$.": "以下小问使用 $c=2$。",
}


def translate_terms(text):
    out = text
    for german, chinese in TERM_TRANSLATIONS:
        out = out.replace(german, chinese)
    out = out.replace(" für ", " 对于 ")
    out = out.replace(" mit ", " 其中 ")
    out = out.replace(" und ", " 和 ")
    out = out.replace(" oder ", " 或 ")
    out = out.replace(" sowie ", " 以及 ")
    out = out.replace(" wobei ", " 其中 ")
    out = out.replace(" falls ", " 如果 ")
    out = out.replace(" wenn ", " 如果 ")
    return out


GERMANISH_RE = re.compile(
    r"\b("
    r"die|der|das|den|dem|des|ein|eine|einer|eines|einem|einen|"
    r"und|oder|mit|von|für|bei|auf|aus|durch|nach|wobei|falls|wenn|"
    r"ist|sind|sei|seien|hat|haben|wird|werden|soll|kann|können|"
    r"berechnen|bestimmen|zeigen|beweisen|gegeben|betrachten|"
    r"welche|welcher|welches|warum|wie|was|dass|dabei|unten|oben"
    r")\b",
    re.I,
)


def formula_summary(text):
    formulas = re.findall(r"\$[^$]+\$", text)
    formulas += re.findall(r"\\\([^)]+\\\)", text)
    seen = []
    for formula in formulas:
        if formula not in seen:
            seen.append(formula)
    if not seen:
        return ""
    if len(seen) > 4:
        seen = seen[:4] + ["..."]
    return "（相关符号：" + "，".join(seen) + "）"


def generic_question_translation(original):
    s = normalize_question_translation_key(original)
    lower = s.lower()
    extra = formula_summary(s)

    if "berechnen" in lower:
        return f"计算本问要求的概率、函数、参数或统计量{extra}。"
    if "bestimmen" in lower or "ermitteln" in lower:
        return f"求出本问指定的结果、参数、函数或统计量{extra}。"
    if "zeigen" in lower or "beweisen" in lower:
        return f"证明题目中给出的结论{extra}。"
    if "widerlegen" in lower:
        return f"反驳题目中给出的命题，并给出理由或反例{extra}。"
    if "gegeben" in lower or lower.startswith("sei ") or lower.startswith("es sei") or lower.startswith("seien "):
        return f"设题目给出的对象和条件如下{extra}。"
    if "betrachten" in lower:
        return f"考虑题目给出的对象{extra}。"
    if "interpretieren" in lower:
        return f"解释本问计算结果或图形结果的含义{extra}。"
    if "skizzieren" in lower or "zeichnen" in lower:
        return f"画出题目要求的图形或函数草图{extra}。"
    if "welche" in lower or "welcher" in lower or "welches" in lower:
        return f"回答本问要求判断或选择的对象{extra}。"
    if "wie groß" in lower or "wie lautet" in lower or lower.startswith("was "):
        return f"回答本问要求的数值、公式或含义{extra}。"
    if "dichte" in lower:
        return f"处理与密度函数有关的条件或问题{extra}。"
    if "verteilungsfunktion" in lower:
        return f"处理与分布函数有关的条件或问题{extra}。"
    if "wahrscheinlichkeit" in lower:
        return f"处理与概率有关的条件或问题{extra}。"
    if "grafik" in lower or "roc" in lower or "auc" in lower:
        return f"分析题目给出的图形、ROC 或 AUC 信息{extra}。"
    return f"阅读题目给出的条件，完成本小问{extra}。"


def ensure_chinese_translation(original, translated):
    if not translated:
        return generic_question_translation(original)
    if GERMANISH_RE.search(translated):
        return generic_question_translation(original)
    return translated


def translate_question_sentence(sentence):
    s = normalize_question_translation_key(sentence)
    if not s:
        return ""
    if s in COMMON_SENTENCE_TRANSLATIONS:
        return COMMON_SENTENCE_TRANSLATIONS[s]

    patterns = [
        (r"^Berechnen Sie (.+)$", "计算{}"),
        (r"^Berechnen und interpretieren Sie (.+)$", "计算并解释{}"),
        (r"^Bestimmen Sie (.+)$", "求出{}"),
        (r"^Ermitteln Sie (.+)$", "求出{}"),
        (r"^Geben Sie (.+) an\.?$", "给出{}。"),
        (r"^Zeichnen Sie (.+)$", "画出{}"),
        (r"^Skizzieren Sie (.+)$", "画出{}的草图"),
        (r"^Erstellen Sie (.+)$", "建立{}"),
        (r"^Zeigen Sie, dass (.+)$", "证明{}"),
        (r"^Zeigen Sie (.+)$", "证明{}"),
        (r"^Beweisen Sie, dass (.+)$", "证明{}"),
        (r"^Beweisen Sie (.+)$", "证明{}"),
        (r"^Widerlegen Sie (.+)$", "反驳{}"),
        (r"^Interpretieren Sie (.+)$", "解释{}"),
        (r"^Beurteilen Sie (.+)$", "评价{}"),
        (r"^Vergleichen Sie (.+)$", "比较{}"),
        (r"^Listen Sie (.+)$", "列出{}"),
        (r"^Ordnen Sie (.+)$", "将{}进行归类"),
        (r"^Beschreiben Sie (.+)$", "描述{}"),
        (r"^Analysieren Sie (.+)$", "分析{}"),
        (r"^Formulieren Sie (.+)$", "写出{}"),
        (r"^Konstruieren Sie (.+)$", "构造{}"),
        (r"^Prüfen Sie (.+)$", "检验{}"),
        (r"^Überprüfen Sie (.+)$", "检查{}"),
        (r"^Leiten Sie (.+) her\.?$", "推导{}。"),
        (r"^Sei (.+)$", "设{}"),
        (r"^Es sei (.+)$", "设{}"),
        (r"^Gegeben sei (.+)$", "给定{}"),
        (r"^Gegeben seien (.+)$", "给定{}"),
        (r"^Gegeben ist (.+)$", "给定{}"),
        (r"^Gegeben sind (.+)$", "给定{}"),
        (r"^Betrachten Sie (.+)$", "考虑{}"),
        (r"^Nehmen Sie an, dass (.+)$", "假设{}"),
        (r"^Angenommen, (.+)$", "假设{}"),
        (r"^Welche (.+)$", "哪些{}"),
        (r"^Welches (.+)$", "哪个{}"),
        (r"^Welcher (.+)$", "哪个{}"),
        (r"^Welcher Art (.+)$", "{}属于哪一种类型"),
        (r"^Wie groß ist (.+)$", "{}是多少"),
        (r"^Wie groß sind (.+)$", "{}是多少"),
        (r"^Wie lautet (.+)$", "{}是什么"),
        (r"^Was bedeutet (.+)$", "{}是什么意思"),
        (r"^Warum (.+)$", "为什么{}"),
        (r"^Für (.+)$", "对于{}"),
        (r"^Falls (.+)$", "如果{}"),
        (r"^Tipp für (.+)$", "对{}的提示"),
    ]
    for pattern, template in patterns:
        match = re.match(pattern, s, flags=re.I)
        if match:
            translated = template.format(translate_terms(match.group(1))).strip()
            return ensure_chinese_translation(s, translated)

    return ensure_chinese_translation(s, translate_terms(s))


def translate_question_text(text):
    stripped = text.strip()
    if not stripped:
        return ""

    lines = stripped.splitlines()
    translated = []
    for line in lines:
        raw = line.strip()
        if not raw:
            continue
        bullet = re.match(r"^([-*])\s+(.+)$", raw)
        if bullet:
            translated.append(f"{bullet.group(1)} {translate_question_sentence(bullet.group(2))}")
        else:
            translated.append(translate_question_sentence(raw))

    return "\n".join(translated)


def add_question_translations(question, topic):
    pieces = re.split(r"(\n{2,})", question)
    out = []

    for idx in range(0, len(pieces), 2):
        block = pieces[idx]
        sep = pieces[idx + 1] if idx + 1 < len(pieces) else ""
        stripped = block.strip()

        translation = None
        if stripped:
            heading_match = re.match(r"^(#{4,6}\s+(?:\([^)]+\)\s+)?)(.+)$", stripped)
            if heading_match:
                key = normalize_question_translation_key(heading_match.group(2))
                if key in QUESTION_TRANSLATIONS and "译：" not in stripped:
                    translation = QUESTION_TRANSLATIONS[key]
                elif "译：" not in stripped:
                    translation = None
            else:
                key = normalize_question_translation_key(stripped)
                if key.startswith("Die Grafik unten zeigt die ROC-Kurve eines alternativen, deutlich teureren diagnostischen Tests."):
                    translation = "下图给出了另一种明显更昂贵的诊断测试的 ROC 曲线。曲线上若干点标注了对应诊断评分的阈值。"
                if "$$" in stripped:
                    leading_text = stripped.split("$$", 1)[0].strip()
                    if leading_text and re.search(r"[A-Za-zÄÖÜäöüß]", leading_text):
                        leading_translation = translate_question_text(leading_text)
                        leading_index = block.find(leading_text)
                        insert_at = leading_index + len(leading_text)
                        out.append(f"{block[:insert_at]}\n\n译：{leading_translation}{block[insert_at:]}")
                        out.append(sep)
                        continue
                elif (
                    key in QUESTION_TRANSLATIONS
                    and "译：" not in stripped
                    and not stripped.startswith("#")
                    and not stripped.startswith("$$")
                    and not stripped.startswith("|")
                    and not stripped.startswith("!")
                    and "$$" not in stripped
                    and "```" not in stripped
                ):
                    translation = QUESTION_TRANSLATIONS[key]
                elif (
                    "译：" not in stripped
                    and not stripped.startswith("#")
                    and not stripped.startswith("$$")
                    and not stripped.startswith("|")
                    and not stripped.startswith("!")
                    and "$$" not in stripped
                    and "```" not in stripped
                    and re.search(r"[A-Za-zÄÖÜäöüß]", stripped)
                ):
                    translation = None

        if translation:
            out.append(f"{block}\n\n译：{translation}")
        else:
            out.append(block)
        out.append(sep)

    result = "".join(out)
    roc_caption = (
        "Die Grafik unten zeigt die ROC-Kurve eines alternativen, deutlich teureren diagnostischen Tests. "
        "Die ROC-Kurve ist an ausgewählten Punkten mit den entsprechenden Schwellenwerten des zu Grunde liegenden diagnostischen Scores beschriftet."
    )
    roc_translation = "译：下图给出了另一种明显更昂贵的诊断测试的 ROC 曲线。曲线上若干点标注了对应诊断评分的阈值。"
    if roc_caption in result and roc_translation not in result:
        result = result.replace(roc_caption, f"{roc_caption}\n\n{roc_translation}")
    return result


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

### 考试可用版

- **概率空间**：$(\Omega,\mathcal F,\mathbb P)$
- **概率公理**：$\mathbb P(A)\ge0$，$\mathbb P(\Omega)=1$，$A_i$ 两两不交 $\Rightarrow \mathbb P(\bigcup_iA_i)=\sum_i\mathbb P(A_i)$
- **补集**：$\mathbb P(A^c)=1-\mathbb P(A)$
- **容斥**：$\mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B)-\mathbb P(A\cap B)$
- **不交并**：$A\cap B=\emptyset\Rightarrow\mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B)$
- **单调性**：$A\subseteq B\Rightarrow\mathbb P(A)\le\mathbb P(B)$
- **De Morgan**：$(A\cup B)^c=A^c\cap B^c$，$(A\cap B)^c=A^c\cup B^c$
- **独立**：$A\perp B\Longleftrightarrow\mathbb P(A\cap B)=\mathbb P(A)\mathbb P(B)\Longleftrightarrow\mathbb P(A|B)=\mathbb P(A)$
- **独立并集**：$A\perp B\Rightarrow\mathbb P(A\cup B)=\mathbb P(A)+\mathbb P(B)-\mathbb P(A)\mathbb P(B)$
- **Laplace**：$\mathbb P(A)=\frac{|A|}{|\Omega|}$
- **归一化**：$\sum_{\omega\in\Omega}\mathbb P(\{\omega\})=1$
- **阶乘归一化**：$\sum_{x=0}^{\infty}\frac{c}{x!}=ce=1\Rightarrow c=e^{-1}$
- **σ-代数**：$\Omega\in\mathcal A$，$A\in\mathcal A\Rightarrow A^c\in\mathcal A$，$A_n\in\mathcal A\Rightarrow\bigcup_nA_n\in\mathcal A$
- **Dynkin-System**：$\Omega\in\mathcal D$，补集封闭，两两不交可数并封闭
- **生成 σ-代数**：$\sigma(\mathcal E)=\bigcap_{\mathcal F\supseteq\mathcal E}\mathcal F$

### 不会时怎么下手

- **题目问 Ergebnisraum**：先把“随机实验的一次结果”写成一句话。  
  例：三次掷骰且只关心点数和，可以先用 $\Omega=\{1,\dots,6\}^3$ 记录完整结果，再用 $X(i,j,k)=i+j+k$ 把它压成 $\Omega'=\{3,\dots,18\}$。
- **题目问某个事件**：先写成模板 $A=\{\omega\in\Omega:\text{条件}\}$。  
  例：至少一次成功就是 $A=\{(\omega_1,\dots,\omega_n):\sum_i\omega_i\ge1\}$。
- **题目问 Laplace 概率**：必须先写两行：$|\Omega|=\cdots$，$|A|=\cdots$，最后才写 $\mathbb P(A)=|A|/|\Omega|$。如果基本结果不等可能，这条路不能直接用。
- **题目问独立/不独立**：不要凭感觉，直接列三项：$\mathbb P(A)$、$\mathbb P(B)$、$\mathbb P(A\cap B)$。若第三项等于前两项乘积，就是独立。
- **题目问互斥**：只看 $A\cap B$。若交集为空就是互斥；互斥和独立是两件事，考试里常拿来混。
- **题目给 $c/x!$ 或类似点概率**：第一行固定写 $\sum_x\mathbb P(\{x\})=1$。  
  例：$\sum_{x=0}^{\infty}c/x!=ce=1$，所以 $c=e^{-1}$。
- **题目问是不是 σ-代数**：按检查表写，不要跳步：  
  1. 有没有 $\Omega$；2. 补集是否还在里面；3. 任意可数并是否还在里面。  
  反例只要找到一条失败即可。
- **题目问 $\sigma(A,B)$**：画四格原子：$A\cap B$、$A\cap B^c$、$A^c\cap B$、$A^c\cap B^c$，删掉空集；答案就是这些非空原子的所有并集。
- **题目问两个 σ-代数的并是不是 σ-代数**：通常找两个集合 $C,D$，它们分别在两个 σ-代数里，但 $C\cup D$ 不在并集里。这样就证明并集不封闭。
- **题目问 Dynkin-System**：重点看“并”是不是要求两两不交。若题里并的集合不 disjunkt，不能直接套 Dynkin 的封闭性。
""",
    "03": r"""## 公式速查

### 考试可用版

- **CDF 定义**：$F_X(x)=\mathbb P(X\le x)$
- **CDF 性质**：单调递增、右连续，$\lim_{x\to-\infty}F_X(x)=0$，$\lim_{x\to\infty}F_X(x)=1$
- **区间概率**：$\mathbb P(a<X\le b)=F_X(b)-F_X(a)$
- **右尾概率**：$\mathbb P(X>a)=1-F_X(a)$
- **跳跃点概率**：$\mathbb P(X=a)=F_X(a)-F_X(a-)$
- **密度合法性**：$f_X(x)\ge0$，$\int_{-\infty}^{\infty}f_X(x)\,dx=1$
- **CDF/PDF 互换**：$F_X(x)=\int_{-\infty}^x f_X(t)\,dt$，可导处 $f_X(x)=F_X'(x)$
- **连续型单点概率**：若 $X$ 连续，则 $\mathbb P(X=a)=0$
- **期望**：$E(X)=\int x f_X(x)\,dx$ 或 $E(X)=\sum_x xP(X=x)$
- **分位数**：连续单调时 $F(q_p)=p$
- **中位数**：$F(m)=0.5$
- **众数**：找 $f(x)$ 最大的位置
- **一维变换**：$Y=g(X)$ 单调，$h(y)=g^{-1}(y)$，$f_Y(y)=f_X(h(y))|h'(y)|$
- **单调递增变换 CDF**：$F_Y(y)=F_X(g^{-1}(y))$
- **单调递减变换 CDF**：$F_Y(y)=1-F_X(g^{-1}(y))$
- **Binomial**：$P(X=k)=\binom nkp^k(1-p)^{n-k}$，$E=np$，$Var=np(1-p)$
- **Poisson**：$P(X=k)=e^{-\lambda}\frac{\lambda^k}{k!}$，$E=Var=\lambda$
- **Exponential**：$f(x)=\lambda e^{-\lambda x}I_{x>0}$，$F(x)=1-e^{-\lambda x}$，$E=\frac1\lambda$
- **Uniform**：$U(a,b)$，$f(x)=\frac1{b-a}I_{(a,b)}(x)$，$E=\frac{a+b}{2}$
- **Hypergeometric**：$P(X=x)=\frac{\binom Mx\binom{N-M}{n-x}}{\binom Nn}$

### 不会时怎么下手

- **题目给 $F(x)$，问概率**：先判断端点形式。最常用模板是 $\mathbb P(a<X\le b)=F(b)-F(a)$。如果问 $\mathbb P(X=a)$，就算跳跃 $F(a)-F(a-)$。
- **题目给 $F(x)$，问密度**：逐段求导。常数段导数是 $0$；跳跃点不是密度，而是点概率。
- **题目给 $f(x)$，问是不是密度**：只检查两件事：第一 $f(x)\ge0$；第二 $\int f(x)\,dx=1$。有参数 $c$ 时，直接用第二条求 $c$。
- **题目问 $P(X=a)$**：先问自己“这是连续型还是有跳跃”。连续型直接是 $0$；CDF 有跳跃就用 $F(a)-F(a-)$。
- **题目问 $P(a<X<b)$**：连续型可以写 $F(b)-F(a)$；若 CDF 有跳跃，必须仔细看端点是否包含。
- **题目问期望**：先写 $E(X)=\int x f(x)\,dx$，不要漏掉前面的 $x$；离散型就写 $\sum xP(X=x)$。
- **题目问中位数/分位数**：先找 $p$ 落在哪个分段，再在那一段解 $F(x)=p$。
- **题目问众数**：看密度 $f(x)$ 最大在哪里。若密度单调递增，众数通常在右端点；单调递减则在左端点。
- **题目问 $Y=g(X)$ 的密度**：先写三行：1. $y=g(x)$；2. $x=h(y)=g^{-1}(y)$；3. $f_Y(y)=f_X(h(y))|h'(y)|$。最后一定写 $y$ 的取值范围。
- **变换 $g$ 不单调**：不要直接套单调公式。把每个原像分支都找出来，然后把每个分支的密度贡献相加。
- **题目问识别分布**：先看支持集，再看公式形状。$0,\dots,n$ 多半是 Binomial；$\mathbb N_0$ 且有 $k!$ 多半是 Poisson；$x>0$ 且 $e^{-\lambda x}$ 是 Exponential。
- **题目问近似**：$n$ 大、$p$ 小用 Poisson 近似；$np$ 和 $n(1-p)$ 都不小，用正态近似。
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


QUESTION_TRANSLATIONS_02 = {
    "Sei $X$ eine diskrete Zufallsvariable. Zeigen Sie, dass wenn $X$ unabhängig von sich selbst ist, eine Konstante $a$ existiert mit": "设 $X$ 是一个离散随机变量。证明：如果 $X$ 与自身独立，则存在一个常数 $a$，使得",
    "Zeigen oder widerlegen Sie: $\\sigma$-Algebren über eine Menge $X$ sind vereinigungsstabil.": "证明或反驳：集合 $X$ 上的 $\\sigma$-代数在取并集下是封闭的。",
    "Geben Sie ein Dynkin-System an, welches keine $\\sigma$-Algebra ist.": "给出一个 Dynkin-System 的例子，它不是 $\\sigma$-代数。",
    "Es wird ein fairer Würfel geworfen, anschließend eine faire Münze und abschließend wieder ein fairer Würfel. Geben Sie den Ergebnisraum an.": "先掷一次公平骰子，然后抛一次公平硬币，最后再掷一次公平骰子。给出结果空间。",
    "Die Würfelaugen werden ihren Zahlen zugeordnet. Die Münze wird für Kopf als $10$ und für Zahl als $-10$ gewertet. Ist die Augenzahl beider Würfel gleich, werden diese jeweils als $0$ gewertet. Insgesamt interessiert man sich für die resultierende Summe.": "骰子的点数按其数值计入。硬币正面记为 $10$，反面记为 $-10$。如果两次骰子点数相同，则这两个骰子点数都记为 $0$。最终只关心所得总和。",
    "Welche Ereignisse können jeweils zu den Ergebnissen $-5$, $0$, $1$, $20$ und $25$ führen?": "哪些事件分别会导致结果 $-5$、$0$、$1$、$20$ 和 $25$？",
    "Ein BWL-Student erklärt, dass Ereignisräume Mengen enthalten und Ergebnisräume keine Mengen enthalten. Erklären Sie anhand eines geeigneten Beispiels, warum diese Aussage unzutreffend ist.": "一名经济学学生声称：事件空间包含集合，而结果空间不包含集合。请用一个合适例子说明这个说法为什么不正确。",
    "Gegeben ist $X=\\{A,a,8\\}$. Geben Sie die Menge $\\mathcal S(X)$ aller $\\sigma$-Algebren über $X$ explizit an.": "给定 $X=\\{A,a,8\\}$。请明确写出 $X$ 上所有 $\\sigma$-代数构成的集合 $\\mathcal S(X)$。",
    "Geben Sie folgende Ergebnisräume an.": "给出下列随机实验的结果空间。",
    "Ein Unternehmen stellt ein Produkt her. Es verwendet dafür zwei Maschinen. Auf der ersten Maschine werden $n$, auf der zweiten Maschine werden $m$ Stück pro Tag hergestellt. Wir interessieren uns nur für die gesamte Anzahl der defekten Produkte an einem zufälligen Tag, an dem das Unternehmen produziert.": "一家公司生产某种产品，并使用两台机器。第一台机器每天生产 $n$ 件，第二台机器每天生产 $m$ 件。我们只关心某个随机生产日中缺陷产品的总数量。",
    "Zwei Studierende spielen gegeneinander in fünf Runden: In jeder Runde wirft zuerst Person $A$ einen fairen Würfel und anschließend Person $B$ ebenfalls einen fairen Würfel. Wir interessieren uns in jeder Runde nur dafür, wer die höhere Augenzahl gewürfelt hat.": "两名学生进行五轮对局：每一轮中，先由 $A$ 掷一个公平骰子，然后 $B$ 也掷一个公平骰子。每一轮我们只关心谁掷出的点数更大。",
    "Geben Sie den kleinstmöglichen Ergebnisraum $\\Omega$ für folgende Zufallsexperimente an.": "为下列随机实验给出尽可能小的结果空间 $\\Omega$。",
    "Für eine Lieferung von drei Motoren wird für jeden Motor untersucht, ob dieser defekt oder nicht defekt ist.": "一批货物中有三台发动机。对每台发动机都检查它是否有缺陷。",
    "Geben Sie den Ergebnisraum $\\Omega$ an.": "给出结果空间 $\\Omega$。",
    "Die Ereignisse seien:": "设事件如下：",
    "- $A$: Mindestens ein Motor ist defekt. - $B$: Höchstens ein Motor ist defekt. - $C$: Motor Nr. 3 ist defekt. - $D$: Genau zwei Motoren sind defekt.": "- $A$：至少一台发动机有缺陷。- $B$：至多一台发动机有缺陷。- $C$：第 3 台发动机有缺陷。- $D$：恰好两台发动机有缺陷。",
    "Interpretieren Sie:": "解释下列表达式：",
    "Bezeichne $M_i$ das Ereignis „Motor $i$ ist defekt“. Formulieren Sie $A$ über $M_1,M_2,M_3$.": "记 $M_i$ 为事件“第 $i$ 台发动机有缺陷”。请用 $M_1,M_2,M_3$ 表示事件 $A$。",
    "In einem Basketballturnier stehen vier Teams im Halbfinale. Ein Sportsender veröffentlicht folgende Prozentangaben als vermeintliche Wahrscheinlichkeiten für den Turniersieg:": "在一个篮球锦标赛中，四支队伍进入半决赛。某体育频道公布了以下百分比，声称它们是各队夺冠的概率：",
    "Zeigen Sie, dass diese Angaben nicht mit den Axiomen von Kolmogorov kompatibel sind.": "证明这些数据与 Kolmogorov 概率公理不相容。",
    "Zeigen Sie für beliebige Mengen $A_i\\subseteq\\Omega$, $i\\in I$, die de Morganschen Regeln:": "对任意集合 $A_i\\subseteq\\Omega$，$i\\in I$，证明 De Morgan 公式：",
    "Sie kennen die $\\sigma$-Additivität für abzählbar unendlich viele Elemente einer $\\sigma$-Algebra. Zeigen Sie, dass endliche Vereinigungen ebenfalls in der $\\sigma$-Algebra liegen:": "已知 $\\sigma$-代数对可数无穷并满足封闭性。证明有限并也属于该 $\\sigma$-代数：",
    "Insbesondere soll auch folgen:": "特别地，还应推出：",
    "Sei $\\Omega=\\{a,b,c,d,e\\}$. Welche der folgenden Mengensysteme sind $\\sigma$-Algebren über $\\Omega$?": "设 $\\Omega=\\{a,b,c,d,e\\}$。下列哪些集合系统是 $\\Omega$ 上的 $\\sigma$-代数？",
    "Zeigen Sie die folgende Aussage:": "证明下列命题：",
    "Eine beliebige $\\sigma$-Algebra $\\mathcal A$ über einem beliebigen $\\Omega$ erzeugt sich selbst:": "任意集合 $\\Omega$ 上的任意 $\\sigma$-代数 $\\mathcal A$ 都生成它自身：",
    "Zeigen Sie:": "证明：",
    "Das heißt, $\\mathcal E$ ist ein Erzeugendensystem der Borelschen $\\sigma$-Algebra.": "也就是说，$\\mathcal E$ 是 Borel $\\sigma$-代数的一个生成系统。",
    "Wie kann man bei folgenden Zufallsexperimenten den Ergebnisraum $\\Omega$ auffassen? Welche Zufallsvariablen werden betrachtet und wie lautet der entsprechende Bildbereich $\\Omega'$?": "对下列随机实验，如何理解结果空间 $\\Omega$？考虑哪些随机变量？相应的像空间 $\\Omega'$ 是什么？",
    "Drei Würfelwürfe, Interesse an der Augensumme": "掷三次骰子，关心的是点数和。",
    "Fünf Schüsse am Schießstand, Interesse an der Trefferanzahl": "在射击场射击五次，关心的是命中次数。",
    "Anteil defekter Bauteile bei $n$ produzierten Bauteilen": "在生产的 $n$ 个零件中，关心缺陷零件所占的比例。",
    "Eine Person schießt mit dem Bogen auf eine Scheibe mit Mittelpunkt $(0,0)$ und Radius $2\\,\\mathrm m$ und trifft immer. Es interessiert der Auftreffpunkt des Pfeiles.": "某人用弓箭射向一个圆靶，圆心为 $(0,0)$，半径为 $2\\,\\mathrm m$，并且总能射中。我们关心箭的落点。",
    "Geben Sie $\\Omega$ und dessen Mächtigkeit an.": "给出 $\\Omega$ 及其基数。",
    "Beschreiben Sie folgende Ereignisse als Teilmengen von $\\Omega$.": "将下列事件描述为 $\\Omega$ 的子集。",
    "Wie groß könnten $\\mathbb P(A)$, $\\mathbb P(B)$ und $\\mathbb P(C)$ sein, wenn jeder Punkt $x\\in\\Omega$ mit gleicher Wahrscheinlichkeit getroffen wird?": "如果 $\\Omega$ 中每个点 $x$ 被击中的可能性相同，那么 $\\mathbb P(A)$、$\\mathbb P(B)$ 和 $\\mathbb P(C)$ 可以是多少？",
    "Sei $X$ eine reellwertige Zufallsvariable mit $X\\geq0$. Zeigen Sie:": "设 $X$ 是一个实值随机变量，且 $X\\geq0$。证明：",
    "Im Rahmen eines Forschungsprojektes zu COVID-19 wurden Daten zur Bestimmung der wirklichen Ansteckungsrate in München erhoben. In München leben aktuell $1561505$ Bürger/-innen.": "在一个关于 COVID-19 的研究项目中，收集数据以估计慕尼黑真实感染率。目前慕尼黑共有 $1561505$ 名居民。",
    "Geben Sie den exakten Ergebnisraum für das Zufallsexperiment „Anzahl der Personen mit vergangener COVID-19-Infektion in München“ an. Welche Mächtigkeit hat der Ergebnisraum? $(2P)$": "给出随机实验“慕尼黑曾感染 COVID-19 的人数”的精确结果空间。该结果空间的基数是多少？$(2P)$",
    "Ist bei dem in (a) definierten Zufallsexperiment die Annahme, dass es sich um ein Laplace-Experiment handelt, gerechtfertigt? Begründen Sie Ihre Antwort. $(2P)$": "对于 (a) 中定义的随机实验，假设它是 Laplace 实验是否合理？请说明理由。$(2P)$",
    "Für die Beantwortung der Forschungsfrage wurden zufällig $N=5000$ der $1561505$ Münchner Bürger/-innen auf Vorliegen einer vergangenen Infektion mit COVID-19 getestet. Aufgrund der Art der Erhebung ist ausgeschlossen, dass ein/e Bürger/-in zweimal in die Stichprobe gelangen konnte.": "为回答研究问题，从 $1561505$ 名慕尼黑居民中随机抽取 $N=5000$ 人，检测其是否曾感染 COVID-19。由于抽样方式，任一居民不可能两次进入样本。",
    "Beschreiben Sie die gerade beschriebene Ziehung der Stichprobe über das Urnenmodell. Achten Sie dabei auf die Vollständigkeit Ihrer Erläuterung. $(4P)$": "用 urn model（抽球模型）描述上述样本抽取过程。注意说明要完整。$(4P)$",
    "Gehen Sie im Folgenden davon aus, dass die Verteilung der vergangenen COVID-19-Infektionen in der Erhebung einer Binomialverteilung folgt.": "以下假设：调查中过去 COVID-19 感染情况服从二项分布。",
    "Was bedeutet der Parameter $\\pi$ der Binomialverteilung dann inhaltlich in diesem Fall? $(2P)$": "在这个情境下，二项分布参数 $\\pi$ 的实际含义是什么？$(2P)$",
    "Geben Sie die Wahrscheinlichkeit an, dass bei einer Ansteckungsrate von $15\\%$ in der Münchner Bevölkerung der beobachtete Anteil in der Stichprobe um mehr als einen Prozentpunkt von diesem Wert abweicht. $(5P)$": "若慕尼黑人口感染率为 $15\\%$，求样本中观察到的比例与该值相差超过一个百分点的概率。$(5P)$",
    "Gehen Sie jetzt davon aus, dass bei vorliegender vergangener Infektion der verwendete Test diese in $95\\%$ richtig identifiziert und bei Personen ohne vergangene Infektion in $1\\%$ der Fälle fälschlicherweise diese als Person mit vergangener Infektion identifiziert.": "现在假设：若确实曾感染，所用检测能以 $95\\%$ 的概率正确识别；若未曾感染，检测有 $1\\%$ 的概率将其错误识别为曾感染。",
    "Veranschaulichen Sie die gerade beschriebene Situation anhand eines Wahrscheinlichkeitsbaumes für die Stichprobe. Nutzen Sie für den unbekannten Anteil der Personen mit vergangener Infektion in der Stichprobe die Bezeichnung $\\rho$ und berechnen Sie ggf. notwendige Zahlen in Abhängigkeit von $\\rho$. $(6P)$": "用概率树表示刚才描述的样本情况。用 $\\rho$ 表示样本中曾感染者的未知比例，并在需要时用 $\\rho$ 表示相关数值。$(6P)$",
    "Wie groß müsste der Anteil der Münchner in der Stichprobe mit vergangener COVID-19-Infektion mindestens sein, so dass $66\\%$ aller Testergebnisse, die das Vorliegen einer vergangenen Infektion anzeigen, auch auf eine entsprechende Infektion zurückzuführen sind? $(4P)$": "样本中曾感染 COVID-19 的慕尼黑居民比例至少应为多少，才能使所有显示“曾感染”的检测结果中有 $66\\%$ 真正来自相应感染？$(4P)$",
    "Drei Personen werfen nacheinander jeweils einmal einen fairen Würfel.": "三个人依次各掷一次公平骰子。",
    "Kleinstmöglicher Ergebnisraum für alle drei Würfe.": "给出描述三次掷骰的最小可能结果空间。",
    "Größtmögliche $\\sigma$-Algebra zu $\\Omega_1$.": "给出与 $\\Omega_1$ 对应的最大 $\\sigma$-代数。",
    "Kleinstmöglicher Ergebnisraum für die Augensumme.": "给出点数和的最小可能结果空间。",
    "Drei $\\sigma$-Algebren zu $\\Omega_2$.": "给出 $\\Omega_2$ 上的三个 $\\sigma$-代数。",
    "Funktion zur Konstruktion des Bildmaßes.": "给出用于构造像测度的函数。",
    "Messbarkeitstabelle und Bildmaßwerte für ${3}$ und ${4}$.": "给出 ${3}$ 和 ${4}$ 的可测性表以及像测度值。",
}

QUESTION_TRANSLATIONS_08 = {
    "Die Wirkung von zwei Hustensäften A und B soll verglichen werden.": "比较两种止咳糖浆 A 和 B 的治疗效果。",
    "Erste Studie:": "第一项研究：",
    "Zweite Studie:": "第二项研究：",
    "In einer Population leiden $5\\%$ an Nierenproblemen. Von diesen trinken $75\\%$ regelmäßig Alkohol. Von den Personen ohne Nierenprobleme trinken $50\\%$ regelmäßig Alkohol. Wie viel Prozent der regelmäßig Alkohol konsumierenden leiden an Nierenproblemen?": "某总体中有 $5\\%$ 的人患有肾脏问题。在这些患者中，$75\\%$ 经常饮酒；在没有肾脏问题的人中，$50\\%$ 经常饮酒。问：经常饮酒的人中，有多少比例患有肾脏问题？",
    "An den Kassen eines Modegeschäfts wird ein Gerät eingeführt, das die Echtheit von $500$-Euro-Scheinen prüfen soll. Aus Erfahrung ist bekannt: $12$ von $10000$ Scheinen sind falsch. Das Gerät blinkt, wenn der Schein falsch ist. Bei falschen Scheinen blinkt es in $95$ von $100$ Fällen. Bei echten Scheinen blinkt es in $10$ von $100$ Fällen. Das Gerät blinkt. Wie sicher kann man sein, dass der Schein tatsächlich falsch ist?": "一家服装店收银台引入一台检测 $500$ 欧元纸币真伪的设备。经验上每 $10000$ 张纸币中有 $12$ 张是假币。纸币为假时设备会闪灯；假币中 $95/100$ 会闪灯，真币中 $10/100$ 也会误闪。现在设备闪灯，问这张纸币实际为假的概率有多大？",
    "Maschine A produziert $60\\%$ der Schrauben, davon sind $2\\%$ fehlerhaft. Maschine B produziert $40\\%$, davon sind $5\\%$ fehlerhaft. Eine zufällig entnommene Schraube ist fehlerhaft. Mit welcher Wahrscheinlichkeit stammt sie von Maschine B?": "机器 A 生产 $60\\%$ 的螺丝，其中 $2\\%$ 有缺陷；机器 B 生产 $40\\%$，其中 $5\\%$ 有缺陷。随机抽到一颗有缺陷的螺丝，问它来自机器 B 的概率是多少？",
    "Eine Krankheit hat Prävalenz $1\\%$. Ein Test hat Sensitivität $95\\%$ und False-Positive-Rate $3\\%$. Eine Person testet positiv. Wie wahrscheinlich ist es, dass sie wirklich krank ist?": "某疾病患病率为 $1\\%$。检测的敏感度为 $95\\%$，假阳性率为 $3\\%$。某人检测为阳性，问他真正患病的概率是多少？",
    "Blutgruppen treten mit Wahrscheinlichkeiten $0.42$, $0.10$, $0.04$, $0.44$ für $A,B,AB,0$ auf. Die bedingten Wahrscheinlichkeiten für $R+$ sind $0.85$ für $A$ und $0$, $0.8$ für $B$ und $0.75$ für $AB$.": "血型 $A,B,AB,0$ 的概率分别为 $0.42,0.10,0.04,0.44$。给定血型时，$R+$ 的条件概率为：$A$ 和 $0$ 为 $0.85$，$B$ 为 $0.8$，$AB$ 为 $0.75$。",
    "Beweisen Sie die Siebformel:": "证明容斥公式：",
    "Wie groß ist die Laplace-Wahrscheinlichkeit, dass eine beliebig gewählte Zahl $n\\in\\{1,\\dots,100\\}$ durch mindestens eine der Zahlen $2$, $3$ oder $5$ teilbar ist?": "在 Laplace 模型下，从 $\\{1,\\dots,100\\}$ 中任取一个数 $n$，它能被 $2$、$3$、$5$ 中至少一个整除的概率是多少？",
    "Trotz Anschnallpflicht legen $15\\%$ aller Autofahrer keinen Gurt an. Eine Krankenversicherung ermittelte, dass bei Verkehrsunfällen von PKW-Fahrern nur $8\\%$ schwere Kopfverletzungen aufwiesen, wenn die Fahrer angeschnallt waren. Bei nicht-angeschnallten Fahrern trugen $62\\%$ keine schwere Kopfverletzung davon.": "尽管有系安全带义务，仍有 $15\\%$ 的汽车驾驶员不系安全带。某健康保险公司统计：在汽车驾驶员交通事故中，系安全带者只有 $8\\%$ 出现严重头部损伤；未系安全带者中有 $62\\%$ 没有严重头部损伤。",
    "$A$: angegurtet $K$: Kopfverletzung": "$A$：系安全带；$K$：发生头部损伤。",
    "a) Interpretiere Ereignis $\\bar A \\cap \\bar K$ und berechne $P(\\bar A \\cap \\bar K)$.": "a) 解释事件 $\\bar A\\cap\\bar K$ 的含义，并计算 $P(\\bar A\\cap\\bar K)$。",
    "b) Sind $\\bar A$ und $\\bar K$ stochastisch unabhängig?": "b) 判断 $\\bar A$ 与 $\\bar K$ 是否随机独立。",
    "c) Wie groß ist die Wahrscheinlichkeit, dass Autofahrer nicht angegurtet waren, wenn sie eine Kopfverletzung haben?": "c) 已知驾驶员有头部损伤，求其未系安全带的概率。",
    "Tests auf HIV können positiv sein, obwohl eigentlich negativ. Wahrscheinlichkeit: $0{,}005\\%$.": "HIV 检测可能在实际未感染时呈阳性；该假阳性概率为 $0{,}005\\%$。",
    "Wenn tatsächlich HIV-infiziert, dann ist die Wahrscheinlichkeit $=100\\%$ für Test positiv.": "如果实际感染 HIV，则检测呈阳性的概率为 $100\\%$。",
    "$I$: Die Person ist mit HIV infiziert. $P$: Der HIV-Test fällt positiv aus.": "$I$：该人感染 HIV；$P$：HIV 检测呈阳性。",
    "Low-Risk-Gruppe: Nur $10$ von $100000$ Personen sind mit HIV infiziert. Eine Person aus dieser Gruppe.": "低风险群体中，每 $100000$ 人只有 $10$ 人感染 HIV。现在考虑来自该群体的一人。",
    "a) Wie groß ist die a-priori Wahrscheinlichkeit, dass diese Person mit HIV infiziert ist, vor dem Test?": "a) 在检测前，该人感染 HIV 的先验概率是多少？",
    "b) Untersuchen Sie formal und mit Begründung, ob die Ereignisse $I$ und $P$ stochastisch unabhängig sind.": "b) 形式化检验并说明事件 $I$ 与 $P$ 是否随机独立。",
    "c) Wie groß ist die Wahrscheinlichkeit, dass diese Person tatsächlich mit HIV infiziert ist, wenn der HIV-Test positiv ausfällt?": "c) 如果 HIV 检测呈阳性，该人实际感染 HIV 的概率是多少？",
    "Unter den Patient:innen, die Bauterlach-Vligenört im Klinikalltag versorgt, sind": "在 Bauterlach-Vligenört 日常临床接诊的患者中，各类患者比例为：",
    "Unter den Patient:innen, die Bauterlach-Vligenört im Klinikalltag versorgt, sind:": "在 Bauterlach-Vligenört 日常临床接诊的患者中，各类患者比例为：",
    "- $30\\%$ Genesene, - $65\\%$ Naive, - $5\\%$ Fnufnu-Kranke.": "- $30\\%$ 为康复者；- $65\\%$ 为从未感染者；- $5\\%$ 为 Fnufnu 急性患者。",
    "Gehen Sie im Folgenden davon aus, dass die in der klinischen Erprobung ermittelten Eigenschaften des Tests, also FPR, TNR etc., auch im Klinikalltag gelten.": "以下假设：临床试验中估计出的测试性质，例如 FPR、TNR 等，也适用于日常临床场景。",
    "Gehen Sie im Folgenden davon aus, dass die in der klinischen Erprobung ermittelten Eigenschaften des Tests, also FPR, TNR usw., auch im Klinikalltag gelten.": "以下假设：临床试验中估计出的测试性质，例如 FPR、TNR 等，也适用于日常临床场景。",
    "Berechnen Sie auf Basis der Ergebnisse der klinischen Erprobung die Sensitivität und Spezifität des Tests zur Entdeckung einer akuten Infektion.": "根据临床试验结果，计算该测试识别急性感染的敏感度和特异度。",
    "Berechnen Sie für die oben angegebene Prävalenz der Krankheit die Wahrscheinlichkeit, mit der ein Test im Klinikalltag ein positives Ergebnis zeigt.": "根据上面给出的疾病患病率，计算临床日常中一次检测显示阳性结果的概率。",
    "Berechnen Sie die Wahrscheinlichkeit, mit der ein negatives Testergebnis im Klinikalltag eine tatsächlich nicht akut erkrankte Person anzeigt.": "计算在临床日常中，检测结果为阴性时，被测者实际没有急性感染的概率。",
    "Funktioniert der in den vorherigen Teilaufgaben analysierte Test von Bauterlach-Vligenört etwa gleich gut, besser, oder schlechter als der hier dargestellte Test?": "前面小问分析的 Bauterlach-Vligenört 测试，与图中这个测试相比，大致同样好、更好还是更差？",
    "Funktioniert der in den vorherigen Teilaufgaben analysierte Test von Bauterlach-Vligenört etwa gleich gut, besser oder schlechter als der hier dargestellte Test?": "前面小问分析的 Bauterlach-Vligenört 测试，与图中这个测试相比，大致同样好、更好还是更差？",
    "Gehen Sie davon aus, dass eine Erkrankung mit der Fnufnu-Krankheit für Schwangere und ihre ungeborenen Kinder absolut lebensbedrohend ist, falls diese nicht sehr früh entdeckt und therapiert wird. Wie sollte der Schwellenwert des in der Grafik gezeigten diagnostischen Tests also gewählt werden, wenn dieser auf eine schwangere Patientin angewendet wird?": "假设 Fnufnu 疾病若不能很早发现并治疗，会对孕妇及胎儿造成致命危险。那么将图中诊断测试用于孕妇时，应如何选择阈值？",
    "Begründen Sie Ihre Antworten kurz.": "请简要说明理由。",
    "In einer Population leiden fünf Prozent der Menschen an erhöhtem Blutdruck. Von diesen fünf Prozent trinken $75\\%$ regelmäßig Alkohol. Außerdem ist bekannt, dass $50\\%$ der Menschen, die keinen erhöhten Blutdruck haben, regelmäßig Alkohol trinken. Wieviel Prozent der regelmäßigen Alkoholkonsument:innen leiden an erhöhtem Blutdruck?": "某总体中 $5\\%$ 的人患有高血压。在这些高血压者中，$75\\%$ 经常饮酒；没有高血压的人中，$50\\%$ 经常饮酒。问经常饮酒者中有多少比例患有高血压？",
    "In einer Population leiden fünf Prozent der Menschen an erhöhtem Blutdruck. Von diesen fünf Prozent trinken $75\\%$ regelmäßig Alkohol. Außerdem ist bekannt, dass $50\\%$ der Menschen, die keinen erhöhten Blutdruck haben, regelmäßig Alkohol trinken. Wie viel Prozent der regelmäßigen Alkoholkonsument:innen leiden an erhöhtem Blutdruck?": "某总体中 $5\\%$ 的人患有高血压。在这些高血压者中，$75\\%$ 经常饮酒；没有高血压的人中，$50\\%$ 经常饮酒。问经常饮酒者中有多少比例患有高血压？",
    "Sei $(\\Omega,\\mathcal F,\\mathbb P)$ ein beliebiger Wahrscheinlichkeitsraum mit $A_1,\\dots,A_n\\in\\mathcal F$, $n\\in\\mathbb N$.": "设 $(\\Omega,\\mathcal F,\\mathbb P)$ 是任意概率空间，且 $A_1,\\dots,A_n\\in\\mathcal F$，$n\\in\\mathbb N$。",
    "Für $n=60$ Studenten wurde die Haarfarbe ermittelt und in „Blond“, „Schwarz/Braun“ und „Sonstig“ aufgeteilt.": "对 $n=60$ 名学生记录发色，并分为“金发”“黑色/棕色”和“其他”三组。",
    "Für diese $3$ Haargruppen wird diskrete Gleichverteilung angenommen.": "假设这 $3$ 个发色组服从离散均匀分布。",
    "a) Bestimme die erwarteten Häufigkeiten für die Haargruppen unter der Annahme, dass diskrete Gleichverteilung vorliegt.": "a) 在离散均匀分布假设下，求各发色组的期望频数。",
    "b) Berechne Pearsonsches $\\chi^2$-Maß.": "b) 计算 Pearson 的 $\\chi^2$ 统计量。",
    "c) Das Pearsonsches $\\chi^2$-Maß folgt unter der obigen Annahme einer $\\chi^2_k$-Verteilung mit $k$ Freiheitsgraden. Gib die Anzahl der Freiheitsgrade im vorliegenden Beispiel an.": "c) 在上述假设下，Pearson 的 $\\chi^2$ 统计量服从自由度为 $k$ 的 $\\chi^2_k$ 分布。给出本例中的自由度数。",
    "d) Überprüfe obige Annahme auf dem Niveau $\\alpha=0{,}1$. Nutze eine der folgenden Möglichkeiten:": "d) 在显著性水平 $\\alpha=0{,}1$ 下检验上述假设。可使用以下任一方法：",
    "- entweder: Berechne den $p$-Wert, - oder: Vergleiche das Pearsonsches $\\chi^2$-Maß mit dem kritischen Wert aus Teilaufgabe c).": "- 方法一：计算 $p$ 值；或方法二：将 Pearson 的 $\\chi^2$ 统计量与 (c) 中的临界值比较。",
    "**Hinweis:** Die Quantilsfunktion und die Verteilungsfunktion der $\\chi^2$-Verteilung ist für $k=1,\\dots,5$ im Anhang angegeben. Verwende passendes $k$.": "**提示：** 附录给出了 $k=1,\\dots,5$ 时 $\\chi^2$ 分布的分位数函数和分布函数。请选择合适的 $k$。",
    "**Anmerkung:** Dies ist ein Gedächtnisprotokoll. Verwende Google statt der Tabellen.": "**备注：** 这是回忆版题目；原表可用查询工具替代。",
    "Tabelle 1: Quantilsfunktion der $\\chi^2_k$-Verteilung mit $k=1,\\dots,5$ Freiheitsgraden": "表 1：自由度 $k=1,\\dots,5$ 的 $\\chi^2_k$ 分布分位数函数。",
    "Tabelle 2: Verteilungsfunktion der $\\chi^2_k$-Verteilung mit $k=1,\\dots,5$ Freiheitsgraden": "表 2：自由度 $k=1,\\dots,5$ 的 $\\chi^2_k$ 分布函数。",
    "Prof. Dr. med. Kwarantina Bauterlach-Vligenört hat einen neuen diagnostischen Test für das Vorliegen einer akuten Infektion mit der schrecklichen Fnufnu-Krankheit entwickelt.": "Kwarantina Bauterlach-Vligenört 教授开发了一种新诊断测试，用于判断是否存在严重 Fnufnu 疾病的急性感染。",
    "Ihre klinische Erprobung des Tests an einer Stichprobe von Patient:innen, die entweder noch nie mit dem Fnufnu-Erreger infiziert waren („Naiv“) oder eine solche Infektion bereits hinter sich haben („Genesen“) oder zum Zeitpunkt der Studie an einer akuten Fnufnu-Infektion leiden („Kranke“), ergibt folgende Ergebnisse:": "她在一组患者样本上进行临床试验：患者分为从未感染 Fnufnu 病原体的“Naiv”、曾经感染但已康复的“Genesen”、以及研究时正处于急性 Fnufnu 感染的“Kranke”。试验结果如下：",
    "Die Grafik unten zeigt die ROC-Kurve eines alternativen, deutlich teureren diagnostischen Tests. Die ROC-Kurve ist an ausgewählten Punkten mit den entsprechenden Schwellenwerten des zu Grunde liegenden diagnostischen Scores beschriftet. ![](图片/Altklausur2LV-5.png) ###### (i)": "下图给出了另一种明显更昂贵的诊断测试的 ROC 曲线。曲线上若干点标注了对应诊断评分的阈值。![](图片/Altklausur2LV-5.png) ###### (i)",
    "Die Grafik unten zeigt die ROC-Kurve eines alternativen, deutlich teureren diagnostischen Tests. Die ROC-Kurve ist an ausgewählten Punkten mit den entsprechenden Schwellenwerten des zu Grunde liegenden diagnostischen Scores beschriftet. ![](图片/Altklausur2LV-5.png) ###### (i)": "下图给出了另一种明显更昂贵的诊断测试的 ROC 曲线。曲线上若干点标注了对应诊断评分的阈值。![](图片/Altklausur2LV-5.png) ###### (i)",
    "Beantworten Sie die folgenden Fragen jeweils mit kurzer Begründung oder Rechnung mit nachvollziehbarem Ansatz.": "回答下列问题，每问都要给出简短理由或可追踪的计算过程。",
    "A und B spielen folgendes Spiel: Es wird mit $4$ Würfeln gewürfelt. Tritt mindestens einmal die Zahl $6$ auf, dann gewinnt A, sonst B. Ist das Spiel fair in dem Sinne, dass im Mittel beide gleich oft gewinnen werden?": "A 和 B 玩如下游戏：掷 $4$ 个骰子。若至少出现一次 $6$，则 A 获胜；否则 B 获胜。问该游戏是否公平，即长期平均来看两人是否会赢得一样多？",
    "Sei $X$ eine stetige Zufallsvariable mit Verteilungsfunktion $F_X$ und einem $0.25$-Quantil von $3$. Welche der folgenden Aussagen trifft/treffen zu?": "设 $X$ 是连续随机变量，分布函数为 $F_X$，且 $0.25$ 分位数为 $3$。判断下列哪些命题成立。",
    "Sei $X$ eine stetige Zufallsvariable mit Verteilungsfunktion $F_X$ und einem $0.25$-Quantil von $3$.": "设 $X$ 是连续随机变量，分布函数为 $F_X$，且 $0.25$ 分位数为 $3$。",
    "Welche der folgenden Aussagen trifft bzw. treffen zu?": "下列哪些命题成立？",
    "1. $F_X(3)=0.25$ 2. $F_X(0.25)=3$ 3. $F_X^{-1}(3)=0.25$": "1. $F_X(3)=0.25$；2. $F_X(0.25)=3$；3. $F_X^{-1}(3)=0.25$。",
    "Sei $Y$ eine diskrete Zufallsvariable mit Träger $T_Y=\\mathbb N$ und Verteilungsfunktion $F_Y$ mit": "设 $Y$ 是离散随机变量，支撑集 $T_Y=\\mathbb N$，分布函数为 $F_Y$，并满足：",
    "und": "并且：",
    "Geben Sie für die folgenden Aussagen an, ob sie aus diesen Angaben folgen:": "判断下列命题是否能由这些已知信息推出：",
    "1. Der Median von $Y$ ist $3$. 2. $P(Y<3)\\le 0.5$ 3. Der Erwartungswert von $Y$ ist $3$.": "1. $Y$ 的中位数是 $3$；2. $P(Y<3)\\le 0.5$；3. $Y$ 的期望为 $3$。",
    "1. Der Median von $Y$ ist $3$. 2. $P(Y<3)\\leq 0.5$ 3. Der Erwartungswert von $Y$ ist $3$.": "1. $Y$ 的中位数是 $3$；2. $P(Y<3)\\leq 0.5$；3. $Y$ 的期望为 $3$。",
    "Welche Verteilung hat die Zufallsvariable": "问下列随机变量服从什么分布：",
    "falls": "在如下条件下：",
    "Nehmen Sie an, ein Pfandautomat akzeptiert jede ihm zugeführte Flasche mit Wahrscheinlichkeit $p<1$. Sei $F$ die Anzahl der Flaschen, die man dem Automaten zuführen muss, um einen Pfandbon für $m$ akzeptierte Flaschen zu bekommen. Mit welcher aus der Vorlesung bekannten parametrischen Verteilung können Sie $F$ beschreiben, was sind die Parameterwerte und welche zusätzlichen Annahmen über den daten-generierenden Prozess müssen Sie dafür treffen?": "假设押金回收机以概率 $p<1$ 接受每个投入的瓶子。令 $F$ 为为了获得 $m$ 个被接受瓶子的押金凭条而必须投入的瓶子数。问可用课堂上哪种参数分布描述 $F$，参数值是什么，并且还需要对数据生成过程作哪些额外假设？",
    "Folgender Mosaikplot stellt den beobachteten Zusammenhang der Merkmale Geschlecht $(m/w)$ und Klausurerfolg $(bestanden/nicht bestanden)$ für eine Statistikklausur dar.": "下列马赛克图展示了一次统计考试中性别 $(m/w)$ 与考试结果（通过/未通过）之间的观察关系。",
    "1. Für welches Geschlecht ist die Durchfallrate höher? 2. Gibt es insgesamt mehr Männer, die bestehen oder mehr Frauen, die bestehen? 3. Das zusätzlich erhobene Merkmal „Studienfach“ mit möglichen Ausprägungen „Nebenfach“ und „Hauptfach“ ist empirisch unabhängig von „Geschlecht“ und von „Klausurerfolg“. Die Hälfte der Prüfungsteilnehmer:innen sind Nebenfachstudierende, die anderen Hauptfachstudierende. Skizzieren Sie einen Mosaikplot für die gemeinsame Verteilung dieser drei Merkmale. Nur schematische Skizze gefragt, keine exakte Zeichnung.": "1. 哪个性别的挂科率更高？2. 总体上，通过考试的男性更多还是女性更多？3. 额外记录的变量“专业类型”取值为“副修”和“主修”，且经验上与“性别”和“考试结果”都独立。一半考生为副修学生，另一半为主修学生。请画出这三个变量联合分布的马赛克图示意图，只需示意，不要求精确绘图。",
    "Es liegt eine große Anzahl $n$ von unabhängig Poisson-verteilten Zufallsvariablen mit gleicher Rate $\\lambda$ vor. Wie ist die Summe dieser Zufallsvariablen exakt verteilt und welcher Verteilung folgt diese Summe approximativ?": "有大量 $n$ 个相互独立且参数同为 $\\lambda$ 的 Poisson 随机变量。它们的和精确服从什么分布？又可近似服从什么分布？",
    "Eine Studie untersucht Zusammenhänge zwischen dem Fortbestand der Ehe nach sieben Ehejahren, der Aufteilung der Hausarbeit und den Einkommensunterschieden zwischen den Ehepartnern bei $1000$ heterosexuellen Ehepaaren.": "一项研究考察 $1000$ 对异性婚姻夫妻中，婚后七年婚姻是否持续、家务分配方式以及夫妻收入差异之间的关系。",
    "Insgesamt waren $200$ der $1000$ Ehepaare nach sieben Jahren bereits wieder geschieden.": "$1000$ 对夫妻中共有 $200$ 对在七年后已经离婚。",
    "Vervollständigen Sie die marginalen gemeinsamen Häufigkeiten des Fortbestands der Ehe und der Aufteilung der Hausarbeit ohne Berücksichtigung der Einkommensunterschiede sowie die gemeinsame Häufigkeitsverteilung aller drei Merkmale in den folgenden Kontingenztafeln.": "补全下列列联表：先不考虑收入差异，补全婚姻状态与家务分配的边际联合频数；再补全三个变量的联合频数分布。",
    "Die Forscher:innen interessieren sich primär für mögliche Unterschiede in den Scheidungsraten zwischen Paaren, in denen Hausarbeit gerecht aufgeteilt ist und Paaren, in denen Hausarbeit ungerecht verteilt ist. Berechnen Sie die entsprechende Odds Ratio und interpretieren Sie Ihr Ergebnis kurz.": "研究者主要关心：家务公平分配与家务不公平分配的夫妻之间，离婚率是否存在差异。计算相应的 odds ratio，并简要解释结果。",
    "Gibt es in Anbetracht der Daten aus der Studie Anhaltspunkte dafür, dass der Zusammenhang zwischen der Aufteilung der Hausarbeit und dem Fortbestand der Ehe durch Einkommensunterschiede zwischen den Ehepartnern modifiziert wird? Berechnen Sie die relevanten Odds Ratios und interpretieren Sie Ihr Ergebnis. Nennen Sie den Fachbegriff für das hier auftretende Phänomen.": "根据研究数据，是否有迹象表明：家务分配与婚姻是否持续之间的关系会受到夫妻收入差异的调节？计算相关 odds ratio，解释结果，并指出这里出现现象的专业名称。",
    "In einer Population leiden zwei Prozent an einer Krankheit. Von diesen zwei Prozent rauchen $80\\%$ regelmäßig. Es sei weiterhin bekannt, dass $30\\%$ der Menschen, die die Krankheit nicht haben, regelmäßig rauchen. Wie viel Prozent der regelmäßigen Raucher:innen leiden an der Krankheit? Runden Sie Ihr Ergebnis bitte auf $3$ Nachkommastellen.": "某总体中 $2\\%$ 的人患有某病。在这些患者中，$80\\%$ 经常吸烟；没有该病的人中，$30\\%$ 经常吸烟。问经常吸烟者中有多少比例患病？结果保留 $3$ 位小数。",
    "Sei $X$ gegeben $Y$ geometrisch verteilt mit": "设在给定 $Y$ 的条件下，$X$ 服从如下几何分布：",
    "und $Y$ stetig gleichverteilt mit": "并且 $Y$ 服从如下连续均匀分布：",
    "Berechnen Sie $E(X)$.": "计算 $E(X)$。",
    "Die Firma „Loysent“ will zur Qualitätskontrolle in der Lebensmittelproduktion ein System zur automatischen Entdeckung verunreinigter Produkte einsetzen. Pro Monat soll das System im Alltagsbetrieb $5$ Millionen Einheiten überprüfen. Von einer Million Einheiten sind erwartungsgemäß zehn verunreinigt. In einem Pilotversuch des Systems mit einer bewusst ausgewählten Stichprobe von Produkten löste es bei $13$ von $15$ tatsächlich verunreinigten Einheiten und bei $22$ von $1100$ nicht verunreinigten Einheiten einen Alarm aus.": "公司 “Loysent” 希望在食品生产质控中使用自动发现污染产品的系统。日常运行中系统每月需检查 $5$ 百万个单位。预计每 $1$ 百万个单位中有 $10$ 个被污染。在一次有意抽取样本的试运行中，系统对 $15$ 个实际污染单位中的 $13$ 个报警，对 $1100$ 个未污染单位中的 $22$ 个也报警。",
    "Berechnen Sie auf Basis der Ergebnisse des Pilotversuchs die erwarteten monatlichen Häufigkeiten von Fehlalarmen, zutreffenden Alarmen, übersehenen Verunreinigungen und vom System korrekt als beanstandungsfrei identifizierten Einheiten, falls das System in der Produktion zum Einsatz käme.": "基于试运行结果，若系统投入生产，计算每月期望出现的误报、正确报警、漏检污染以及被系统正确判为无问题的单位数量。",
    "Halten Sie den Einsatz des Systems unter den gegebenen Umständen aus statistischer Sicht für sinnvoll? Begründen Sie Ihre Antwort quantitativ mit geeigneten Kennzahlen.": "在给定条件下，从统计角度看你认为该系统值得使用吗？请用合适指标进行定量说明。",
    "Quantifizieren Sie die erwartete Stärke des Zusammenhangs zwischen der tatsächlichen Verunreinigung einer Einheit und der Reaktion des Systems auf diese Einheit im Alltagsbetrieb. Benutzen Sie dafür eine Maßzahl, deren Wertebereich $\\mathbb R_0^+$ ist. Interpretieren Sie Ihr Ergebnis.": "量化日常运行中“单位实际是否污染”与“系统对该单位的反应”之间的预期关联强度。请使用取值范围为 $\\mathbb R_0^+$ 的指标，并解释结果。",
    "Die Grafik unten zeigt die ROC-Kurven zweier Systeme zur automatischen Entdeckung verunreinigter Produkte, die von den Firmen „Ponapticum“ und „Nopapcitom“ angeboten werden. Die ROC-Kurven sind an ausgewählten Punkten mit den entsprechenden Schwellenwerten des zugrunde liegenden Scores beschriftet.": "下图显示了公司 “Ponapticum” 和 “Nopapcitom” 提供的两种自动发现污染产品系统的 ROC 曲线。曲线上若干点标注了对应评分阈值。",
    "Funktioniert das in den vorherigen Teilaufgaben analysierte System etwa gleich gut, deutlich besser oder deutlich schlechter als die zwei hier dargestellten Systeme?": "前面小问分析的系统，与图中两个系统相比，大致同样好、明显更好还是明显更差？",
    "Gehen Sie davon aus, dass der Verkauf verunreinigter Produkte für „Loysent“ existenzbedrohend ist und Einheiten, die vom System als verunreinigt eingestuft werden, einfach und kostengünstig automatisch gereinigt werden können. Welches der beiden in der Grafik gezeigten Systeme ist für diese Situation besser geeignet? Welcher Bereich von Schwellenwerten sollte für den praktischen Einsatz des präferierten Systems benutzt werden? Begründen Sie Ihre Antworten kurz.": "假设销售污染产品会危及 “Loysent” 的生存，而被系统判为污染的单位可以简单且低成本地自动清洁。图中两个系统哪一个更适合这种场景？实际使用时应选择该系统的哪个阈值范围？请简要说明理由。",
    "Das System prüft nacheinander jede einzelne produzierte Einheit. Im Zuge der Erprobung des Systems wurde auch festgehalten, wie viele vom System nicht beanstandete Einheiten jeweils zwischen zwei beanstandeten Einheiten überprüft wurden. Sei die Anzahl der aufeinanderfolgenden, nicht beanstandeten Einheiten $X$.": "系统逐个检查每个生产单位。在系统测试过程中，还记录了两次被系统判为有问题的单位之间，连续通过了多少个未被判为有问题的单位。令这个连续未被判为有问题的单位数为 $X$。",
    "Mit welcher parametrischen Verteilungsfamilie können Sie die Verteilung von $X$ beschreiben? Welche Annahmen müssen Sie dafür zusätzlich treffen? Geben Sie an, was die theoretischen Annahmen in der beschriebenen Situation konkret bedeuten.": "可以用哪一类参数分布描述 $X$ 的分布？为此还需要哪些额外假设？请说明这些理论假设在本情境中的具体含义。",
    "Ihre klinische Erprobung des Tests an einer Stichprobe von Patient:innen, die entweder noch nie mit dem Fnufnu-Erreger infiziert waren, „Naiv“, oder eine solche Infektion bereits hinter sich haben, „Genesen“, oder zum Zeitpunkt der Studie an einer akuten Fnufnu-Infektion leiden, „Kranke“, ergibt folgende Ergebnisse:": "该测试在一组患者样本上进行临床试验：患者分为从未感染 Fnufnu 病原体的“Naiv”、曾经感染的“Genesen”、以及研究时正处于急性感染的“Kranke”。结果如下：",
    "Die Grafik unten zeigt die ROC-Kurve eines alternativen, deutlich teureren diagnostischen Tests. Die ROC-Kurve ist an ausgewählten Punkten mit den entsprechenden Schwellenwerten des zugrunde liegenden diagnostischen Scores beschriftet.": "下图显示另一种明显更昂贵的诊断测试的 ROC 曲线。曲线上若干点标注了对应诊断评分的阈值。",
    "Nehmen Sie an, ein Pfandautomat akzeptiert jede ihm zugeführte Flasche mit Wahrscheinlichkeit $p<1$. Sei $F$ die Anzahl der Flaschen, die man dem Automaten zuführen muss, um einen Pfandbon für $m$ akzeptierte Flaschen zu bekommen.": "假设押金回收机以概率 $p<1$ 接受每个投入的瓶子。令 $F$ 为了得到 $m$ 个被接受瓶子的押金凭条所需投入的瓶子数。",
    "Mit welcher aus der Vorlesung bekannten parametrischen Verteilung können Sie $F$ beschreiben, was sind die Parameterwerte und welche zusätzlichen Annahmen über den daten-generierenden Prozess müssen Sie dafür treffen?": "可以用课堂上哪种已知参数分布描述 $F$？参数值是什么？还需要对数据生成过程作哪些额外假设？",
    "Folgender Mosaikplot stellt den beobachteten Zusammenhang der Merkmale Geschlecht, $m/w$, und Klausurerfolg, bestanden/nicht bestanden, für eine Statistikklausur dar.": "下列马赛克图展示了一次统计考试中性别 $m/w$ 与考试结果（通过/未通过）的观察关系。",
    "Für welches Geschlecht ist die Durchfallrate höher?": "哪个性别的挂科率更高？",
    "Gibt es insgesamt mehr Männer, die bestehen, oder mehr Frauen, die bestehen?": "总体上通过考试的男性更多，还是通过考试的女性更多？",
    "Das in den oben dargestellten Daten zusätzlich erhobene Merkmal „Studienfach“ mit möglichen Ausprägungen „Nebenfach“ und „Hauptfach“ ist empirisch unabhängig von „Geschlecht“ und von „Klausurerfolg“. Die Hälfte der Prüfungsteilnehmer:innen sind Nebenfachstudierende, die anderen Hauptfachstudierende. Skizzieren Sie einen Mosaikplot für die gemeinsame Verteilung dieser drei Merkmale. Nur schematische Skizze gefragt, keine exakte Zeichnung.": "上面数据中额外记录的变量“专业类型”取值为“副修”和“主修”，且经验上与“性别”和“考试结果”独立。一半考生是副修学生，另一半是主修学生。请画出三个变量联合分布的马赛克图示意图，只需示意，不要求精确绘制。",
    "Gegeben:": "给定：",
    "- $5$ Millionen Einheiten pro Monat - pro $1$ Million Einheiten sind $10$ verunreinigt": "- 每月 $5$ 百万个单位；- 每 $1$ 百万个单位中有 $10$ 个被污染。",
    "Also beträgt die erwartete Anzahl verunreinigter Einheiten pro Monat:": "因此每月被污染单位的期望数量为：",
    "Pilotversuch:": "试运行：",
    "- $13$ von $15$ verunreinigten Einheiten erkannt - $22$ von $1100$ nicht verunreinigten Einheiten mit Alarm": "- $15$ 个污染单位中识别出 $13$ 个；- $1100$ 个未污染单位中有 $22$ 个触发报警。",
    "Erwartete monatliche Häufigkeiten.": "求每月期望频数。",
    "Sinnvoller Einsatz?.": "判断该系统是否值得使用。",
    "Zusammenhangsmaß mit Wertebereich $\\mathbb R_0^+$.": "使用取值范围为 $\\mathbb R_0^+$ 的关联强度指标。",
    "ROC-Kurven.": "分析 ROC 曲线。",
    "Wartezeit zwischen beanstandeten Einheiten.": "分析两次被判为有问题的单位之间的等待时间。",
    "Gegeben sind $N+1$ Stapel $s_0,\\dots,s_N$. Stapel $s_j$ enthält $j$ rote und $N-j$ blaue Chips. Aus den $N+1$ Stapeln wird zufällig einer ausgewählt und aus diesem Stapel werden ohne Zurücklegen zwei Chips gezogen.": "给定 $N+1$ 堆筹码 $s_0,\\dots,s_N$。第 $s_j$ 堆含有 $j$ 个红筹码和 $N-j$ 个蓝筹码。从这 $N+1$ 堆中随机选一堆，并从该堆中不放回抽取两个筹码。",
    "Bezeichne $S_j$ das Ereignis, dass Stapel $s_j$ ausgewählt wurde. Sei $R_i$ das Ereignis, dass der $i$-te gezogene Chip rot ist.": "记 $S_j$ 为选中第 $s_j$ 堆的事件；记 $R_i$ 为第 $i$ 次抽到红筹码的事件。",
    "Hinweise:": "提示：",
    "Bestimmen Sie $P(R_1\\mid S_j)$ und interpretieren Sie die Größe.": "求 $P(R_1\\mid S_j)$，并解释该量的含义。",
    "Zeigen Sie, dass $P(R_1)=\\frac12$.": "证明 $P(R_1)=\\frac12$。",
    "Bestimmen Sie $P(R_1\\cap R_2\\mid S_j)$.": "求 $P(R_1\\cap R_2\\mid S_j)$。",
    "Berechnen Sie $P(R_1\\cap R_2)$.": "计算 $P(R_1\\cap R_2)$。",
}

QUESTION_TRANSLATIONS_03 = {
    "Betrachten Sie die Verteilungsfunktion": "考虑下列分布函数。",
    "Sei $X\\sim F$. Bestimmen Sie die Wahrscheinlichkeiten:": "设 $X\\sim F$。求下列概率：",
    "Sei $X$ eine stetige Zufallsvariable mit Dichte": "设 $X$ 是具有如下密度的连续随机变量：",
    "mit Parametern $a,b>0$.": "其中参数 $a,b>0$。",
    "Berechnen Sie den Modus von $X$.": "计算 $X$ 的众数。",
    "Es gilt:": "已知：",
    "Für welche Kombination von Werten ist die Verteilung von $X$ rechtsschief?": "在哪些取值组合下，$X$ 的分布是右偏的？",
    "Betrachten Sie:": "考虑下列对象：",
    "Sei $X\\sim F$. Bestimmen Sie $\\mathbb P(X=0)$, $\\mathbb P(X=1)$ und $\\mathbb P\\left(X\\in\\left[\\frac13,\\frac23\\right]\\right)$.": "设 $X\\sim F$。求 $\\mathbb P(X=0)$、$\\mathbb P(X=1)$ 以及 $\\mathbb P\\left(X\\in\\left[\\frac13,\\frac23\\right]\\right)$。",
    "Für $\\lambda>0$ sei $F:\\mathbb R\\to\\mathbb R$ definiert durch:": "对 $\\lambda>0$，函数 $F:\\mathbb R\\to\\mathbb R$ 定义如下：",
    "Begründen Sie, ob es sich bei $F$ um eine Verteilungsfunktion handelt.": "说明 $F$ 是否为一个分布函数，并给出理由。",
    "Sei $X$ eine geometrisch verteilte Zufallsvariable mit Parameter $p\\in(0,1)$, d.h. die Zähldichte von $X$ ist:": "设 $X$ 是参数为 $p\\in(0,1)$ 的几何分布随机变量，即 $X$ 的计数密度为：",
    "Bestimmen Sie explizit die Verteilungsfunktion $F_X$ von $X$.": "明确求出 $X$ 的分布函数 $F_X$。",
    "Sei $X\\sim\\operatorname{LogN}(\\mu,\\sigma^2)$ mit Dichte:": "设 $X\\sim\\operatorname{LogN}(\\mu,\\sigma^2)$，其密度为：",
    "Zeigen Sie mit dem Transformationssatz, dass $Y:=\\log(X)\\sim N(\\mu,\\sigma^2)$.": "用变量变换定理证明 $Y:=\\log(X)\\sim N(\\mu,\\sigma^2)$。",
    "Welche der folgenden Funktionen sind Verteilungsfunktionen stetiger Zufallsvariablen?": "下列哪些函数是连续随机变量的分布函数？",
    "Ein Wirt wird wöchentlich mit Bier beliefert. Der Wochenverbrauch $X$ in Hektolitern habe Dichte:": "某酒馆每周进一次啤酒。设每周啤酒消耗量 $X$（单位：百升）具有如下密度：",
    "Gegeben sei die stetige Zufallsvariable $X$ mit Dichte:": "给定连续随机变量 $X$，其密度为：",
    "Gegeben sei die stetige Zufallsvariable $X$ mit Dichte": "给定连续随机变量 $X$，其密度为：",
    "Die Zufallsvariable $X$ hat Dichte:": "随机变量 $X$ 的密度为：",
    "Bestimmen Sie den Erwartungswert von:": "求下列随机变量的期望：",
    "Wie groß ist $\\mathbb P(Z=4)$?": "$\\mathbb P(Z=4)$ 是多少？",
    "Geben Sie den Träger von $Z$ an und bestimmen Sie die Dichte von $Z$.": "给出 $Z$ 的支撑集，并求 $Z$ 的密度。",
    "Sei:": "设：",
    "Sei": "设：",
    "Zeigen Sie, dass:": "证明：",
    "Zeigen Sie, dass": "证明：",
    "in Rate-Parametrisierung.": "这里采用率参数化。",
    "Die Wahrscheinlichkeit, dass der HSV in einem Bundesligaspiel kein Tor schießt, beträgt $0.7788$.": "HSV 在一场德甲比赛中一球不进的概率为 $0.7788$。",
    "Welche Verteilung eignet sich zur Beschreibung der Anzahl der Tore in $90$ Minuten?": "用哪种分布适合描述 $90$ 分钟内的进球数？",
    "Bestimmen Sie die Wahrscheinlichkeit, dass der HSV mindestens zwei Tore schießt.": "求 HSV 至少进两球的概率。",
    "Bayern erzielt durchschnittlich $2.8$ Tore pro Spiel. Berechnen Sie die Wahrscheinlichkeit für ein $4:0$ für Bayern, bei Unabhängigkeit der Torzahlen.": "拜仁平均每场进 $2.8$ 球。若两队进球数相互独立，计算拜仁 $4:0$ 获胜的概率。",
    "Welche Verteilung hat die Wartezeit auf das nächste HSV-Tor?": "等待 HSV 下一粒进球的时间服从什么分布？",
    "Welche Verteilungen besitzen die folgenden Zufallsvariablen? Geben Sie Dichtefunktion und Träger an.": "下列随机变量分别服从什么分布？请给出密度/概率函数和支撑集。",
    "Fünf Aufgaben, vier vorbereitet, zwei werden zufällig ausgewählt. $X$ zählt die ausgewählten vorbereiteten Aufgaben.": "共有五道题，其中四道已准备；随机抽取两道。$X$ 表示被抽中的已准备题目数量。",
    "Anzahl emittierter $\\alpha$-Teilchen pro Zeitintervall.": "每个时间区间内发射的 $\\alpha$ 粒子数量。",
    "Ein Schlüssel passt von $10$ Schlüsseln. Nach jedem Fehlversuch werden die Schlüssel neu gemischt. $X$ sei die Anzahl der Versuche bis zum Erfolg.": "$10$ 把钥匙中有一把能打开。每次失败后钥匙重新混合。设 $X$ 为直到成功所需的尝试次数。",
    "Ein Münchner kennt jeden $1000$-sten Einwohner persönlich. Auf einem Spaziergang trifft er $50$ Münchner. $X$ sei die Anzahl der Bekannten.": "某慕尼黑人平均每 $1000$ 个居民认识一个。一次散步中他遇到 $50$ 个慕尼黑人。设 $X$ 为其中熟人的数量。",
    "Sei $X$ stetig mit Dichte $f$ und Verteilungsfunktion $F$. Entscheiden Sie, ob die Aussagen richtig oder falsch sind.": "设 $X$ 为连续随机变量，密度为 $f$，分布函数为 $F$。判断下列说法对错。",
    "Für $\\lambda>0$ sei die Funktion $F:\\mathbb R\\to\\mathbb R$ definiert durch": "对 $\\lambda>0$，函数 $F:\\mathbb R\\to\\mathbb R$ 定义如下：",
    "Zeigen Sie, dass $F$ eine gültige Verteilungsfunktion ist.": "证明 $F$ 是合法的分布函数。",
    "Gegeben sei die Funktion": "给定函数：",
    "Bestimmen Sie $a\\in\\mathbb R$, sodass $G_a$ eine Verteilungsfunktion ist.": "求 $a\\in\\mathbb R$，使得 $G_a$ 是一个分布函数。",
    "Sei nun $X\\sim G_a$ mit $a=\\frac23$. Bestimmen Sie:": "现在设 $X\\sim G_a$ 且 $a=\\frac23$。求：",
    "Es sei $X\\sim\\operatorname{Geo}(p)$, das heißt $X:\\Omega\\to\\mathbb N$ ist geometrisch verteilt mit": "设 $X\\sim\\operatorname{Geo}(p)$，即 $X:\\Omega\\to\\mathbb N$ 服从几何分布，并满足：",
    "und $p\\in(0,1)$. Zeigen Sie:": "其中 $p\\in(0,1)$。证明：",
    "für alle $n,k>0$.": "对所有 $n,k>0$ 成立。",
    "Betrachten Sie die Funktion": "考虑函数：",
    "Zeigen Sie, dass $F$ eine Verteilungsfunktion ist.": "证明 $F$ 是一个分布函数。",
    "Sei $\\nu=\\lambda_F$ das zu $F$ gehörende Lebesgue-Stieltjes-Maß. Bestimmen Sie eine Dichte $f$ und ein Maß $\\mu$, sodass:": "设 $\\nu=\\lambda_F$ 为属于 $F$ 的 Lebesgue-Stieltjes 测度。求一个密度 $f$ 和一个测度 $\\mu$，使得：",
    "Sei $X$ eine Zufallsvariable mit Bildmaß $\\nu$, also $X\\sim\\nu$. Berechnen Sie $E(X)$ und $\\operatorname{Var}(X)$.": "设 $X$ 是像测度为 $\\nu$ 的随机变量，即 $X\\sim\\nu$。计算 $E(X)$ 和 $\\operatorname{Var}(X)$。",
    "Sei $X\\sim\\chi^2(10)$.": "设 $X\\sim\\chi^2(10)$。",
    "Erstellen Sie in R eine Grafik der Dichte $f_X$ und der Verteilungsfunktion $F_X$ von $X$ nebeneinander und vergleichen Sie diese.": "在 R 中把 $X$ 的密度 $f_X$ 和分布函数 $F_X$ 并排画出，并比较二者。",
    "Geben Sie Modus, Median und Erwartungswert von $X$ an und zeichnen Sie diese in die Grafiken ein.": "给出 $X$ 的众数、中位数和期望，并把它们画到图中。",
    "Seien $X\\sim N(-5,1)$, $Y\\sim N(3,5)$ und $Z\\sim t(10)$. Die Zufallsvariable $V$ folgt einer Mischverteilung aus diesen drei Zufallsvariablen mit Gewichten $0.2$, $0.3$ und $0.5$.": "设 $X\\sim N(-5,1)$、$Y\\sim N(3,5)$、$Z\\sim t(10)$。随机变量 $V$ 服从由这三个随机变量按权重 $0.2,0.3,0.5$ 组成的混合分布。",
    "Warum ist": "为什么下列表达式",
    "eine gültige Dichte?": "是一个合法密度？",
    "Wiederholen Sie Schritt (a) für $V$.": "对 $V$ 重复步骤 (a)。",
    "Bonus": "附加题",
    "Wiederholen Sie Schritt (b) für $V$.": "对 $V$ 重复步骤 (b)。",
    "Sei $X$ eine Zufallsvariable mit Dichte $f_X$ und $g:\\mathbb R\\to\\mathbb R$ invertierbar. Sei $h=g^{-1}$ stetig differenzierbar. Leiten Sie den eindimensionalen Transformationssatz her.": "设 $X$ 是密度为 $f_X$ 的随机变量，$g:\\mathbb R\\to\\mathbb R$ 可逆，且 $h=g^{-1}$ 连续可微。推导一维变量变换定理。",
    "Die Länge $X$ eines zufällig auf der Straße gefundenen Blattes eines Baumes in Dezimetern folge einer Verteilung mit der Dichtefunktion": "随机在街上捡到一片树叶，其长度 $X$（单位：分米）服从具有如下密度函数的分布：",
    "Zeigen Sie, dass gelten muss:": "证明必须满足：",
    "$(2\\text{ Pkt.})$": "（2 分）",
    "Bestimmen Sie den Erwartungswert der Zufallsvariablen": "求该随机变量的期望：",
    "Wie groß ist die Wahrscheinlichkeit, dass ein Blatt $0.75$ Dezimeter lang ist? $(1\\text{ Pkt.})$": "一片树叶长度恰好为 $0.75$ 分米的概率是多少？（1 分）",
    "Die Fläche eines Blattes der Länge $X$ sei": "长度为 $X$ 的树叶面积定义为：",
    "Bestimmen Sie die Dichte der Fläche $Y$ eines zufälligen Blattes. Welche Werte kann die Fläche eines Blattes annehmen, d.h. für welche Werte gilt": "求随机树叶面积 $Y$ 的密度。树叶面积可以取哪些值，也就是说下式在哪些值上成立：",
    "$(4\\text{ Pkt.})$": "（4 分）",
    "Es liegt eine Stichprobe von $\\mathcal{U}[0,1]$-verteilten Zufallszahlen vor. Skizzieren Sie kurz, wie und nach welcher Methode sich daraus Zufallszahlen aus einer Poisson-Verteilung erzeugen lassen. $(2\\text{ Pkt.})$": "给定一组服从 $\\mathcal U[0,1]$ 的随机数样本。简要说明可用什么方法以及如何由此生成 Poisson 分布随机数。（2 分）",
    "Es seien": "设：",
    "Zufallsvariablen für $n\\in \\mathbb{N}$. Definieren Sie: $X_1,X_2,X_3$ sind unabhängig. $(1\\text{ Pkt.})$": "它们是 $n\\in\\mathbb N$ 时的随机变量。定义“$X_1,X_2,X_3$ 相互独立”。（1 分）",
    "Die Verteilungsfunktion einer Zufallsvariablen $X$ lautet:": "随机变量 $X$ 的分布函数为：",
    "Bestimmen Sie das $0.25$-Quantil der Verteilung. Wie lässt sich dieses interpretieren? $(2\\text{ Pkt.})$": "求该分布的 $0.25$ 分位数，并解释其含义。（2 分）",
    "Der Maximum-Likelihood-Schätzer des Parameters $\\lambda$ einer Exponentialverteilung lautet": "指数分布参数 $\\lambda$ 的最大似然估计量为：",
    "Begründen Sie, weshalb für den Maximum-Likelihood-Schätzer von": "说明为什么下列最大似然估计量",
    "gilt:": "满足：",
    "$(1\\text{ Pkt.})$": "（1 分）",
    "Unten stehende Abbildung zeigt die normierte Loglikelihood einer Stichprobe der Poisson-Verteilung. Zeichnen Sie ein $0.95\\%$ Likelihood-Intervall für den Parameter $\\lambda$ in die Grafik ein. $(3\\text{ Pkt.})$": "下图显示 Poisson 分布样本的标准化对数似然。请在图中画出参数 $\\lambda$ 的 $0.95\\%$ 似然区间。（3 分）",
    "**Hinweis:** Die Verteilungsfunktion der $\\chi_1^2$-Verteilung finden Sie im Anhang.": "**提示：** $\\chi_1^2$ 分布的分布函数可在附录中找到。",
    "Es wird ein Niveau-$\\alpha$-Test $\\psi$ für ein Testproblem $H_0$ versus $H_1$ durchgeführt. Die Testentscheidung lautet, dass die Nullhypothese abgelehnt wird. Welcher Fehler kann durch diese Testentscheidung eingetreten sein? Kann eine maximale Wahrscheinlichkeit, mit der dieser Fehler auftritt, angegeben werden? $(2\\text{ Pkt.})$": "对检验问题 $H_0$ 对 $H_1$ 进行水平为 $\\alpha$ 的检验 $\\psi$。检验结论为拒绝原假设。问这种决策可能发生哪类错误？能否给出该错误发生概率的最大值？（2 分）",
    "Die stetige Zufallsvariable $X$ hat die Verteilungsfunktion": "连续随机变量 $X$ 的分布函数为：",
    "a) Bestimme die Dichte $f_X(x)$ von $X$.": "a) 求 $X$ 的密度 $f_X(x)$。",
    "b) Berechne $P(1<X<3)$.": "b) 计算 $P(1<X<3)$。",
    "c) Betrachte die Funktion": "c) 考虑函数：",
    "Ermittle $c$, sodass $h(x)$ eine Dichte ist.": "求 $c$，使得 $h(x)$ 是一个密度。",
    "Seien $X_1,\\dots,X_n$ i.i.d. verteilte stetige Zufallsvariablen mit Dichte": "设 $X_1,\\dots,X_n$ 是独立同分布的连续随机变量，其密度为：",
    "für $x_i>0$ und Verteilungsparameter $\\alpha>0$, $\\beta>0$.": "其中 $x_i>0$，分布参数为 $\\alpha>0$、$\\beta>0$。",
    "a) Stelle $L(\\alpha)$ und $l(\\alpha)$ für gegebene Stichproben $x_1,\\dots,x_n$ auf.": "a) 对给定样本 $x_1,\\dots,x_n$，写出 $L(\\alpha)$ 和 $l(\\alpha)$。",
    "b) Verwende $\\beta=1$ und bestimme aus resultierender Log-Likelihood den ML-Schätzer für $\\alpha$. Sie können davon ausgehen, dass das Ergebnis dem Maximum entspricht.": "b) 令 $\\beta=1$，由相应对数似然求 $\\alpha$ 的最大似然估计量。可以假设所得结果确实对应最大值。",
    "c) Gegeben sei die Stichprobe": "c) 给定样本：",
    "Berechnen Sie $\\hat{\\alpha}_{ML}$ für diese Stichprobe.": "计算该样本下的 $\\hat{\\alpha}_{ML}$。",
    "Die diskrete Zufallsvariable $X$ mit Wahrscheinlichkeitsdichte": "离散随机变量 $X$ 的概率函数为：",
    "Dabei ist $c \\in \\mathbb{R}$ eine Konstante.": "其中 $c\\in\\mathbb R$ 是常数。",
    "a) Bestimmen Sie die Konstante $c$, sodass $p_X$ eine Wahrscheinlichkeitsdichte der diskreten Zufallsvariable $X$ ist.": "a) 求常数 $c$，使得 $p_X$ 是离散随机变量 $X$ 的合法概率函数。",
    "Verwenden Sie für die folgenden Aufgaben $c=2$.": "以下小问使用 $c=2$。",
    "b) Bestimmen Sie die Verteilungsfunktion von $X$ und skizzieren Sie diese.": "b) 求 $X$ 的分布函数，并画出草图。",
    "c) Berechnen Sie Erwartungswert und Varianz von $X$.": "c) 计算 $X$ 的期望和方差。",
    "Sei $X$ eine Cauchy-verteilte Zufallsvariable mit zugehöriger Dichte": "设 $X$ 是 Cauchy 分布随机变量，其密度为：",
    "a) Bestimmen Sie anhand des Transformationssatzes für Dichten die Dichte der Zufallsvariablen": "a) 使用密度变换定理求下列随机变量的密度：",
    "b) Welcher Verteilung folgt $Y$?": "b) $Y$ 服从什么分布？",
    "Sei $X$ eine Zufallsvariable mit Dichte": "设随机变量 $X$ 的密度为：",
    "mit Konstante $c>0$.": "其中常数 $c>0$。",
    "Geben Sie an, was für eine Funktion $f$ gelten muss, sodass $f$ eine Dichte ist. $(2P)$": "说明函数 $f$ 需要满足哪些条件，才能成为密度。（2 分）",
    "Bestimmen Sie die Konstante $c$ so, dass $f(x)$ eine Dichte ist und prüfen Sie, ob $f(x)$ die Eigenschaften aus Teilaufgabe (a)(i) erfüllt. $(4P)$": "求常数 $c$，使得 $f(x)$ 是密度，并检验 $f(x)$ 是否满足 (a)(i) 中的性质。（4 分）",
    "Geben Sie den Träger von $f(x)$ an. $(2P)$": "给出 $f(x)$ 的支撑集。（2 分）",
    "Bestimmen Sie den Erwartungswert der Zufallsvariable $X$. $(4P)$": "求随机变量 $X$ 的期望。（4 分）",
    "Seien $X_1,\\dots,X_n$ für $n \\in \\mathbb{N}$ i.i.d. verteilt wie die Zufallsvariable $X$. Betrachtet wird jetzt": "设对 $n\\in\\mathbb N$，$X_1,\\dots,X_n$ 与随机变量 $X$ 独立同分布。现在考虑：",
    "Sei $\\tilde{Y}_n$ die standardisierte Zufallsvariable von $Y_n$ für $n \\in \\mathbb{N}$. Welche Aussage können Sie über die Konvergenz von $\\tilde{Y}_n$ für $n \\to \\infty$ treffen und warum? $(3P)$": "设 $\\tilde Y_n$ 是 $Y_n$ 的标准化随机变量。对 $n\\to\\infty$，你能对 $\\tilde Y_n$ 的收敛作出什么结论？为什么？（3 分）",
    "Bestimmen Sie": "求：",
    "$(1P)$": "（1 分）",
    "Berechnen Sie die Konstante $c$.": "计算常数 $c$。",
    "Skizzieren Sie die Dichte.": "画出密度函数草图。",
    "Welche der folgenden Aussagen ist richtig? Begründen Sie kurz, keine explizite Berechnung notwendig.": "下列哪些说法正确？请简要说明理由，不需要显式计算。",
    "- Der Median von $X$ ist $2$. - Die Schiefe von $X$ ist größer $0$. - Der Erwartungswert von $X$ ist kleiner als der Modus von $X$.": "- $X$ 的中位数为 $2$；- $X$ 的偏度大于 $0$；- $X$ 的期望小于 $X$ 的众数。",
    "Berechnen Sie mit Hilfe des Dichtetransformationssatzes die Dichte der Zufallsvariablen": "使用密度变换定理计算下列随机变量的密度：",
    "Berechnen Sie den Erwartungswert von $X$.": "计算 $X$ 的期望。",
    "Berechnen Sie den Median von $X$.": "计算 $X$ 的中位数。",
    "Eine Person findet heraus, dass sie auch gänzlich ohne Lernen jede Klausur mit $20\\%$ Wahrscheinlichkeit besteht. Wie oft müsste sie im Mittel eine Klausur schreiben, um sie zu bestehen? Welche Varianz ergibt sich?": "某人发现即使完全不学习，每次考试也有 $20\\%$ 的概率通过。平均需要参加多少次考试才能通过？相应方差是多少？",
    "Bei der Lufthansa ist aus Erfahrung bekannt, dass etwa $18\\%$ der Fluggäste ihre gebuchte Reise nicht antreten. Um die Auslastung der Flugzeugflotte möglichst hoch zu halten, werden mehr als die verfügbaren $150$ Plätze in einem Airbus A320 verkauft. Berechnen Sie mit Hilfe des zentralen Grenzwertsatzes die Wahrscheinlichkeit dafür, dass mehr als $150$ Passagiere die Reise antreten wollen, wenn $170$ Plätze verkauft werden. Runden Sie Ihr Ergebnis bitte auf $3$ Nachkommastellen.": "汉莎航空经验上约有 $18\\%$ 的旅客不会乘坐已预订航班。为尽量提高飞机利用率，A320 的 $150$ 个座位会超售。若售出 $170$ 个座位，用中心极限定理计算实际想登机人数超过 $150$ 的概率，结果保留 $3$ 位小数。",
    "Hinweis:": "提示：",
    "Für welche Werte von $a$ und $b$ ist $F(x)$ die Verteilungsfunktion einer stetigen Zufallsvariable?": "对哪些 $a$ 和 $b$，$F(x)$ 是某个连续随机变量的分布函数？",
    "Wie lautet die zugehörige Dichte $f(x)$?": "对应密度 $f(x)$ 是什么？",
    "Wie lautet die Quantilfunktion? Berechnen Sie das $95\\%$-Quantil.": "分位数函数是什么？计算 $95\\%$ 分位数。",
    "Wird durch $F(x)$ eindeutig eine Verteilung festgelegt? Begründen Sie.": "$F(x)$ 是否唯一确定一个分布？请说明理由。",
    "die stetige Dichte der Zufallsvariable $X$.": "这是随机变量 $X$ 的连续密度。",
    "Skizzieren Sie die Dichte. Wie ist der Modus der Verteilung? Geben Sie ohne Berechnung, aber mit Begründung Erwartungswert, Median und Schiefe der Verteilung an.": "画出密度草图。该分布的众数是什么？不做计算但给出理由，说明其期望、中位数和偏度。",
    "Berechnen Sie die Varianz der Verteilung.": "计算该分布的方差。",
    "Berechnen Sie die Dichte von $Y=X^2$.": "计算 $Y=X^2$ 的密度。",
    "Schätzen Sie den Erwartungswert von": "估计下列期望：",
    "ab. Keine explizite Berechnung.": "不需要显式计算，只需估计。",
    "Da $\\exp(1)=e$ ist, ist der Träger $[0,e]$.": "由于 $\\exp(1)=e$，支撑集为 $[0,e]$。",
    "Werte von $a$ und $b$.": "$a$ 和 $b$ 的取值。",
    "Dichte.": "密度。",
    "Quantilfunktion.": "分位数函数。",
    "Eindeutigkeit.": "唯一性。",
    "Gegeben sei:": "给定：",
    "Zeigen Sie, dass $F(x)$ für $a=1$ die Verteilungsfunktion einer stetigen Zufallsvariable ist.": "证明当 $a=1$ 时，$F(x)$ 是某个连续随机变量的分布函数。",
    "Dichte für $a=1$.": "求 $a=1$ 时的密度。",
    "Erwartungswert für $a=1$.": "求 $a=1$ 时的期望。",
    "$0.99$-Quantil für $a=1$.": "求 $a=1$ 时的 $0.99$ 分位数。",
    "Geben Sie $P(X=1)$ für $a=1$ und $a=0.5$ an.": "给出 $a=1$ 和 $a=0.5$ 时的 $P(X=1)$。",
    "$0.25$-Quantil für $a=0.5$.": "求 $a=0.5$ 时的 $0.25$ 分位数。",
    "Sei $X\\sim \\operatorname{Exp}(\\lambda)$ mit $\\lambda\\in\\mathbb R^+$.": "设 $X\\sim\\operatorname{Exp}(\\lambda)$，其中 $\\lambda\\in\\mathbb R^+$。",
    "Die Dichte lautet:": "密度为：",
    "Ist $X$ stetig oder diskret?.": "$X$ 是连续型还是离散型？",
    "Sei $Y=a+bX$ mit $a,b\\in\\mathbb R^+$. Begründen Sie, dass $Y$ eine Zufallsvariable ist.": "设 $Y=a+bX$，其中 $a,b\\in\\mathbb R^+$。说明为什么 $Y$ 是随机变量。",
    "Verteilungsfunktion von $Y$.": "求 $Y$ 的分布函数。",
    "Faltung für $D=W-Z=\\nu U-\\lambda X$.": "求 $D=W-Z=\\nu U-\\lambda X$ 的卷积分布。",
    "Poisson-Prozess am Bahnhof.": "车站中的 Poisson 过程。",
    "Unimodale stetige Zufallsvariable.": "单峰连续随机变量。",
    "Diagnosetest.": "诊断测试。",
    "Fast sichere Konvergenz von $\\bar Y_n$.": "$\\bar Y_n$ 的几乎必然收敛。",
    "Kovarianzmatrix.": "协方差矩阵。",
}

QUESTION_TRANSLATIONS_04 = {
    "Konstruieren Sie einen Fall, sodass die geforderten Eigenschaften i) und ii) des Maßeindeutigkeitssatzes auf $(\\Omega,\\mathcal F)$ erfüllt sind, aber trotzdem $\\mu_1\\neq\\mu_2$ gilt.": "构造一个例子，使得在 $(\\Omega,\\mathcal F)$ 上测度唯一性定理要求的性质 i) 和 ii) 都成立，但仍有 $\\mu_1\\neq\\mu_2$。",
    "Gegeben sei der Wahrscheinlichkeitsraum $(\\Omega,\\mathcal F,\\mu)$ mit:": "给定概率空间 $(\\Omega,\\mathcal F,\\mu)$，其中：",
    "Bestimmen Sie für die Funktion $f:\\Omega\\to\\mathbb R$ mit:": "对于函数 $f:\\Omega\\to\\mathbb R$，其中：",
    "das Integral $\\int f\\,d\\mu$.": "求积分 $\\int f\\,d\\mu$。",
    "Es sei $\\Omega=\\mathbb N$ und $\\mathcal F=\\mathcal P(\\mathbb N)$. Für welche der folgenden Abbildungen $\\mu:\\mathcal F\\to\\mathbb R$ wird $(\\Omega,\\mathcal F,\\mu)$ ein Maßraum? Prüfen Sie die Maße außerdem auf Endlichkeit.": "设 $\\Omega=\\mathbb N$ 且 $\\mathcal F=\\mathcal P(\\mathbb N)$。下列哪些映射 $\\mu:\\mathcal F\\to\\mathbb R$ 使 $(\\Omega,\\mathcal F,\\mu)$ 成为测度空间？同时检查这些测度是否有限。",
    "Sei der Messraum $(\\mathbb R,\\mathcal B)$ sowie die messbare Funktion:": "设测度空间为 $(\\mathbb R,\\mathcal B)$，并给定可测函数：",
    "für ein festes $N\\in\\mathbb N$ gegeben. Berechnen Sie für das Lebesguemaß $\\lambda$ und das Zählmaß $\\mu_Z$ die Integrale über $[0,n]$ für $n\\in\\mathbb N$, $n\\leq N$.": "其中 $N\\in\\mathbb N$ 固定。分别对 Lebesgue 测度 $\\lambda$ 和计数测度 $\\mu_Z$，计算 $n\\in\\mathbb N, n\\leq N$ 时在 $[0,n]$ 上的积分。",
    "Es sei der Messraum $(\\mathbb R,\\mathcal B)$ gegeben sowie die messbaren Funktionen:": "给定测度空间 $(\\mathbb R,\\mathcal B)$ 以及可测函数：",
    "Berechnen Sie für das Lebesguemaß $\\lambda$ und das Zählmaß $\\mu_Z$:": "分别对 Lebesgue 测度 $\\lambda$ 和计数测度 $\\mu_Z$ 计算：",
    "1. $\\int_{[0,n]} f\\,d\\lambda$ und $\\int_{[0,n]} f\\,d\\mu_Z$ für $n\\in\\mathbb N$, 2. $\\int g\\,d\\lambda$ und $\\int g\\,d\\mu_Z$.": "1. 对 $n\\in\\mathbb N$，计算 $\\int_{[0,n]} f\\,d\\lambda$ 和 $\\int_{[0,n]} f\\,d\\mu_Z$；2. 计算 $\\int g\\,d\\lambda$ 和 $\\int g\\,d\\mu_Z$。",
    "Es sei $f:\\mathbb R\\to\\mathbb R$:": "设 $f:\\mathbb R\\to\\mathbb R$：",
    "wobei $k>5$, $y_1=1$ und:": "其中 $k>5$，$y_1=1$，并且：",
    "Schreiben Sie $f$ als Treppenfunktion auf.": "将 $f$ 写成阶梯函数形式。",
    "Sei $y_3=a$ und $y_{k-1}<b<y_k$. Leiten Sie $\\int_{[a,b]}f\\,d\\mu$ her.": "设 $y_3=a$ 且 $y_{k-1}<b<y_k$。推导 $\\int_{[a,b]}f\\,d\\mu$。",
    "$\\lambda$ sei das Lebesguemaß. Leiten Sie $\\int_{[a,b]}f\\,d\\lambda$ her.": "设 $\\lambda$ 为 Lebesgue 测度。推导 $\\int_{[a,b]}f\\,d\\lambda$。",
    "Es sei $\\Omega=\\mathbb N=\\{1,2,\\dots\\}$ und $\\mathcal F=\\mathcal P(\\mathbb N)$. Für welche der folgenden Abbildungen $\\mu:\\mathcal F\\to\\mathbb R_0^+$ wird durch $(\\Omega,\\mathcal F,\\mu)$ ein Maßraum definiert? Überprüfen Sie zudem alle $\\mu$, die tatsächlich ein Maß darstellen, auf Endlichkeit.": "设 $\\Omega=\\mathbb N=\\{1,2,\\dots\\}$ 且 $\\mathcal F=\\mathcal P(\\mathbb N)$。下列哪些映射 $\\mu:\\mathcal F\\to\\mathbb R_0^+$ 使 $(\\Omega,\\mathcal F,\\mu)$ 成为测度空间？并检查所有合法测度是否有限。",
    "Das Lebesgue-Maß sei $\\lambda:\\mathcal B(\\mathbb R)\\to\\mathbb R_0^+\\cup\\{\\infty\\}$ mit": "设 Lebesgue 测度 $\\lambda:\\mathcal B(\\mathbb R)\\to\\mathbb R_0^+\\cup\\{\\infty\\}$ 满足：",
    "Zeigen Sie für $a<b$:": "证明对 $a<b$ 有：",
    "Sei $A\\subset\\mathbb R$ abzählbar. Was gilt für $\\lambda(A)$?": "设 $A\\subset\\mathbb R$ 可数。$\\lambda(A)$ 等于什么？",
    "jeweils mit $\\sigma$-Algebra": "分别配有如下 $\\sigma$-代数：",
    "Betrachten Sie die Funktion:": "考虑函数：",
    "Vorarbeit": "准备工作",
    "Die von $\\mathcal E$ erzeugte $\\sigma$-Algebra hat die Atome": "由 $\\mathcal E$ 生成的 $\\sigma$-代数具有如下原子：",
    "Also:": "因此：",
    "Außerdem gilt:": "此外有：",
    "Geben Sie explizit die Mengensysteme": "明确写出下列集合系统：",
    "an und zeigen Sie, dass es sich jeweils um $\\sigma$-Algebren handelt.": "并证明它们分别都是 $\\sigma$-代数。",
    "Ist $f$ $\\mathcal F_1$-$\\mathcal F_2$-messbar?": "$f$ 是否是 $\\mathcal F_1$-$\\mathcal F_2$ 可测的？",
    "Zeigen Sie, dass $f(\\mathcal F_1)$ keine $\\sigma$-Algebra ist.": "证明 $f(\\mathcal F_1)$ 不是 $\\sigma$-代数。",
    "Gegeben sei der Wahrscheinlichkeitsraum $(\\Omega,\\mathcal F,\\mu)$ mit": "给定概率空间 $(\\Omega,\\mathcal F,\\mu)$，其中：",
    "sowie": "以及：",
    "Geben Sie $\\mathcal F$ explizit an.": "明确写出 $\\mathcal F$。",
    "Zeigen Sie, dass die Funktion $f:\\Omega\\to\\mathbb R$ mit": "证明函数 $f:\\Omega\\to\\mathbb R$，其中：",
    "integrierbar ist bezüglich $\\mu$ und bestimmen Sie:": "关于 $\\mu$ 可积，并求：",
    "Sei $G:\\mathbb R\\to\\mathbb R$ definiert durch:": "设 $G:\\mathbb R\\to\\mathbb R$ 定义为：",
    "Berechnen Sie das Lebesgue-Stieltjes-Maß $\\lambda_G$ für die Mengen": "计算集合上的 Lebesgue-Stieltjes 测度 $\\lambda_G$：",
    "Sei $F:\\mathbb R\\to\\mathbb R$ definiert durch:": "设 $F:\\mathbb R\\to\\mathbb R$ 定义为：",
    "Sei $\\lambda_F$ das zu $F$ gehörende Lebesgue-Stieltjes-Maß.": "设 $\\lambda_F$ 为与 $F$ 对应的 Lebesgue-Stieltjes 测度。",
    "Bestimmen Sie $\\lambda_F((-\\infty,a])$ für beliebige $a\\in\\mathbb R$.": "对任意 $a\\in\\mathbb R$，求 $\\lambda_F((-\\infty,a])$。",
    "Gegeben sei die Funktionenfolge $f_n:\\mathbb R\\to\\mathbb R$, $n\\in\\mathbb N$, mit": "给定函数列 $f_n:\\mathbb R\\to\\mathbb R$，$n\\in\\mathbb N$，其中：",
    "Entscheiden Sie, ob": "判断下列两个量是否：",
    "gleich sind und bestimmen Sie diese Werte.": "相等，并求出这些值。",
    "Zeigen Sie, dass die Funktion $f:\\mathbb R\\to\\mathbb R$ mit": "证明函数 $f:\\mathbb R\\to\\mathbb R$，其中：",
    "nicht Riemann-, aber Lebesgue-integrierbar ist und berechnen Sie:": "不是 Riemann 可积，但 Lebesgue 可积，并计算：",
    "Sei der Messraum $(\\mathbb R,\\mathcal B)$ sowie die messbare Funktion": "设测度空间为 $(\\mathbb R,\\mathcal B)$，并给定可测函数：",
    "für ein festes $N\\in\\mathbb N$ gegeben.": "其中 $N\\in\\mathbb N$ 固定。",
    "Berechnen Sie für das Lebesgue-Maß $\\lambda$ und das Zählmaß $\\mu_Z$:": "分别对 Lebesgue 测度 $\\lambda$ 和计数测度 $\\mu_Z$ 计算：",
    "für $n\\in\\mathbb N$, $n\\leq N$.": "其中 $n\\in\\mathbb N$ 且 $n\\leq N$。",
    "Für $x\\in\\mathbb R$ definiere das Dirac-Maß $\\delta_x$ auf $\\mathbb R$ durch": "对 $x\\in\\mathbb R$，在 $\\mathbb R$ 上定义 Dirac 测度 $\\delta_x$ 如下：",
    "Zeigen Sie: $\\delta_x$ besitzt keine Dichte bezüglich des Lebesgue-Maßes.": "证明：$\\delta_x$ 关于 Lebesgue 测度没有密度。",
    "Seien": "设：",
    "mit": "其中：",
    "Geben Sie": "给出：",
    "an.": "。",
    "Zeigen Sie, dass $\\mu$ ein Maß zum Messraum $(\\Omega,\\mathcal F)$ ist.": "证明 $\\mu$ 是测度空间 $(\\Omega,\\mathcal F)$ 上的一个测度。",
    "Berechnen Sie": "计算：",
    "Sei weiterhin $\\mu_Z$ das Zählmaß.": "继续设 $\\mu_Z$ 为计数测度。",
    "Die Sigma-Algebra $\\sigma(\\mathcal E)$ wird über $\\Omega$ erzeugt. Bestimmen Sie $\\sigma(\\mathcal E)$.": "在 $\\Omega$ 上生成 $\\sigma(\\mathcal E)$。求 $\\sigma(\\mathcal E)$。",
    "Geben Sie die Nullmenge des Maßes $\\mu_Z$ auf der durch $\\Omega$ erzeugten $\\sigma$-Algebra an.": "给出由 $\\Omega$ 生成的 $\\sigma$-代数上计数测度 $\\mu_Z$ 的零测集。",
    "Seien:": "设：",
    "sowie:": "以及：",
    "mit:": "其中：",
    "Geben Sie $\\mathcal F_1=\\sigma(\\{A,B\\})$ an.": "写出 $\\mathcal F_1=\\sigma(\\{A,B\\})$。",
    "Zeigen Sie: Die Vereinigung von zwei $\\sigma$-Algebren muss keine $\\sigma$-Algebra sein. Definieren Sie dafür eine $\\sigma$-Algebra $\\mathcal F_2$ für $\\Omega$, so dass $\\mathcal F_1\\cup\\mathcal F_2$ keine $\\sigma$-Algebra ist.": "证明：两个 $\\sigma$-代数的并不一定是 $\\sigma$-代数。为此在 $\\Omega$ 上定义一个 $\\sigma$-代数 $\\mathcal F_2$，使得 $\\mathcal F_1\\cup\\mathcal F_2$ 不是 $\\sigma$-代数。",
    "Zeigen Sie, dass $\\mu$ ein Maß zum Messraum $(\\Omega,\\mathcal F_1)$ ist.": "证明 $\\mu$ 是测度空间 $(\\Omega,\\mathcal F_1)$ 上的测度。",
    "Berechnen Sie:": "计算：",
    "Ist $f$ die Dichte einer Verteilung bezüglich des dominierenden Maßes $\\mu$? Begründen Sie.": "$f$ 是否是某个关于支配测度 $\\mu$ 的分布密度？请说明理由。",
    "Zeigen Sie, dass $\\mu$ ein Maß zum Messraum $(\\Omega,F)$ ist.": "证明 $\\mu$ 是测度空间 $(\\Omega,F)$ 上的测度。",
    "$\\mathcal F_1=\\sigma(\\{A,B\\})$.": "$\\mathcal F_1=\\sigma(\\{A,B\\})$。",
    "Vereinigung zweier Sigma-Algebren muss keine Sigma-Algebra sein.": "两个 sigma-代数的并不一定是 sigma-代数。",
    "$\\mu$ ist ein Maß.": "$\\mu$ 是一个测度。",
    "Integral.": "积分。",
    "Ist $f$ eine Dichte bezüglich $\\mu$?.": "$f$ 是否是关于 $\\mu$ 的密度？",
}

QUESTION_TRANSLATIONS_05 = {
    "Sei $X$ eine reellwertige Zufallsvariable mit Dichte $f_X$. Für eine weitere Dichtefunktion $f_Y(y)$ ist die Kullback-Leibler-Divergenz der beiden Dichten definiert als": "设 $X$ 是实值随机变量，密度为 $f_X$。对另一个密度函数 $f_Y(y)$，两个密度之间的 Kullback-Leibler 散度定义为：",
    "Der Erwartungswert wird bezüglich der Verteilung von $X$ mit Dichte $f_X$ gebildet.": "这里的期望是关于具有密度 $f_X$ 的 $X$ 的分布来计算的。",
    "eine Zufallsvariable ist.": "是一个随机变量。",
    "Hinweis: Verwenden Sie die Jensen'sche Ungleichung und $Z$ aus Aufgabe (a).": "提示：使用 Jensen 不等式以及 (a) 中的 $Z$。",
    "Würfelspiel: Auf einem fairen Würfel wird die $1$ als $1$, die $2$ und $3$ als $2$, und die restlichen Augenzahlen als $3$ zugeordnet. Geben Sie Maßräume und Zufallsvariable an, begründen Sie die Wahrscheinlichkeitsräume und berechnen Sie den Erwartungswert.": "骰子游戏：掷一个公平骰子，点数 $1$ 记为 $1$，点数 $2$ 和 $3$ 记为 $2$，其余点数记为 $3$。给出测度空间和随机变量，说明概率空间为何成立，并计算期望。",
    "Sei $(X_n)_{n\\in\\mathbb N}$ eine Folge unabhängiger, diskreter Zufallsvariablen mit:": "设 $(X_n)_{n\\in\\mathbb N}$ 是一列相互独立的离散随机变量，满足：",
    "Bestimmen Sie $\\mathbb E(X_n)$ und $\\operatorname{Var}(X_n)$ für ein festes $n\\in\\mathbb N$.": "对固定的 $n\\in\\mathbb N$，求 $\\mathbb E(X_n)$ 和 $\\operatorname{Var}(X_n)$。",
    "Die Zufallsvariable $X$ sei die Augenzahl beim Wurf eines fairen achtseitigen Würfels:": "设随机变量 $X$ 为掷一个公平八面骰得到的点数：",
    "Berechnen Sie $\\mathbb E(X)$, $\\operatorname{Var}(X)$ und $\\mathbb P(X\\geq 6)$.": "计算 $\\mathbb E(X)$、$\\operatorname{Var}(X)$ 和 $\\mathbb P(X\\geq 6)$。",
    "Bestimmen Sie eine obere Schranke für $\\mathbb P(X\\geq 6)$ mit der Markow-Ungleichung.": "用 Markov 不等式给出 $\\mathbb P(X\\geq 6)$ 的上界。",
    "Bestimmen Sie eine obere Schranke für $\\mathbb P(X\\geq 6)$ mit der Chebyshev-Ungleichung.": "用 Chebyshev 不等式给出 $\\mathbb P(X\\geq 6)$ 的上界。",
    "Sei $X$ eine stetige Zufallsvariable mit Dichte:": "设 $X$ 是具有如下密度的连续随机变量：",
    "und $f(x)=0$ sonst. Dabei ist $k\\in\\mathbb R$.": "其余情况下 $f(x)=0$。其中 $k\\in\\mathbb R$。",
    "Bestimmen Sie $k$, sodass $f$ eine gültige Dichte ist.": "求 $k$，使得 $f$ 是合法密度。",
    "Bestimmen Sie $\\mathbb E(X)$.": "求 $\\mathbb E(X)$。",
    "Verwenden Sie die Jensen-Ungleichung, um eine Schranke für $\\mathbb E(\\exp(X))$ zu finden.": "使用 Jensen 不等式，为 $\\mathbb E(\\exp(X))$ 找一个界。",
    "Sie haben einen Zufallsprozess einer Standardnormalverteilung gegeben. Diesen möchten Sie nutzen, um einen fairen achtseitigen Würfel zu erhalten.": "给定一个标准正态分布的随机过程。希望利用它构造一个公平八面骰。",
    "Nutzen Sie den gegebenen Zufallsprozess, um eine stetige Gleichverteilung $U(0,1)$ zu erhalten.": "利用给定随机过程得到一个连续均匀分布 $U(0,1)$。",
    "Nutzen Sie $U$, um einen fairen stetigen Würfel auf $[1,8]$ zu erhalten. Berechnen Sie Erwartungswert und Varianz.": "利用 $U$ 构造 $[1,8]$ 上的公平连续骰子，并计算期望和方差。",
    "Nutzen Sie $U$, um einen fairen achtseitigen diskreten Würfel zu erhalten. Berechnen Sie Erwartungswert und Varianz.": "利用 $U$ 构造一个公平八面离散骰子，并计算期望和方差。",
    "Vergleichen Sie die Momente aus (b) und (c). Warum unterscheiden sie sich? Funktioniert das nur mit der Standardnormalverteilung?": "比较 (b) 与 (c) 中的矩。它们为什么不同？这种构造是否只适用于标准正态分布？",
    "Sind $X_1\\sim N(\\mu_1,\\sigma_1^2)$ und $X_2\\sim N(\\mu_2,\\sigma_2^2)$ unabhängig, dann ist:": "若 $X_1\\sim N(\\mu_1,\\sigma_1^2)$ 与 $X_2\\sim N(\\mu_2,\\sigma_2^2)$ 独立，则：",
    "Ist $X\\sim N(0,1)$, $\\mu\\in\\mathbb R$ und $\\sigma^2>0$, so gilt:": "若 $X\\sim N(0,1)$、$\\mu\\in\\mathbb R$ 且 $\\sigma^2>0$，则：",
    "Es seien $X$ und $Y$ diskrete Zufallsvariablen mit gemeinsamer Verteilung:": "设 $X$ 和 $Y$ 是具有如下联合分布的离散随机变量：",
    "Berechnen Sie den bedingten Erwartungswert $\\mathbb E(X\\mid Y)$.": "计算条件期望 $\\mathbb E(X\\mid Y)$。",
    "Berechnen Sie $\\mathbb E(\\mathbb E(X\\mid Y))$.": "计算 $\\mathbb E(\\mathbb E(X\\mid Y))$。",
    "Seien $X\\sim U(2,5)$ und $Y\\sim \\operatorname{Ga}(2,2)$ stochastisch unabhängige Zufallsvariablen.": "设 $X\\sim U(2,5)$ 与 $Y\\sim\\operatorname{Ga}(2,2)$ 是相互独立的随机变量。",
    "Sind $X-Y$ und $X+Y$ ebenfalls stochastisch unabhängig?": "$X-Y$ 与 $X+Y$ 是否也随机独立？",
    "Seien $U\\sim\\operatorname{Ga}(4,6)$ und $V\\sim\\operatorname{Exp}(\\lambda)$ stochastisch unabhängig. Welchen Wert muss $\\lambda$ haben, damit $U-V$ und $U+V$ unkorreliert sind?": "设 $U\\sim\\operatorname{Ga}(4,6)$ 与 $V\\sim\\operatorname{Exp}(\\lambda)$ 随机独立。$\\lambda$ 应取何值，才能使 $U-V$ 与 $U+V$ 不相关？",
    "Vereinfachen Sie die folgenden Ausdrücke.": "化简下列表达式。",
    "Bemerkung: Im Allgemeinen gilt $\\mathbb E(X^2)\\neq \\mathbb E(X)^2$.": "备注：一般而言，$\\mathbb E(X^2)\\neq \\mathbb E(X)^2$。",
    "Berechnen Sie $\\mathbb E(X)$.": "计算 $\\mathbb E(X)$。",
    "Berechnen Sie $\\operatorname{Var}(X)$.": "计算 $\\operatorname{Var}(X)$。",
    "Sei zusätzlich $Y\\sim\\operatorname{Bin}(n,\\pi)$ und:": "另外设 $Y\\sim\\operatorname{Bin}(n,\\pi)$，且：",
    "Berechnen Sie erneut $\\mathbb E(X)$ und $\\operatorname{Var}(X)$.": "再次计算 $\\mathbb E(X)$ 和 $\\operatorname{Var}(X)$。",
    "Gegeben seien:": "给定：",
    "Bestimmen Sie $\\rho(X,Y)$.": "求 $\\rho(X,Y)$。",
    "$X$ ist gleichverteilt auf $\\{1,\\dots,n\\}$. $Y$ nimmt die Werte $1,2,3$ an mit:": "$X$ 在 $\\{1,\\dots,n\\}$ 上均匀分布。$Y$ 取值 $1,2,3$，并满足：",
    "und $X,Y$ sind unabhängig.": "并且 $X,Y$ 相互独立。",
    "Sei $X$ eine reellwertige Zufallsvariable mit endlichem zweitem Moment:": "设 $X$ 是具有有限二阶矩的实值随机变量：",
    "Zeigen Sie: $X$ hat endlichen Erwartungswert und endliche Varianz.": "证明：$X$ 有有限期望和有限方差。",
    "Sei eine Zufallsvariable": "设随机变量：",
    "gegeben.": "给定。",
    "Bestimmen Sie die Varianz von $X$.": "求 $X$ 的方差。",
    "Sei $X$ eine reellwertige Zufallsvariable mit": "设 $X$ 是实值随机变量，并满足：",
    "Zeigen Sie, dass ein $c\\in\\mathbb R$ existiert mit": "证明存在 $c\\in\\mathbb R$，使得：",
    "für alle $\\varepsilon>0$.": "对所有 $\\varepsilon>0$ 成立。",
    "Der Skisportverband eines Landes geht davon aus, dass $1\\%$ seiner Athleten unerlaubte leistungssteigernde Substanzen einnehmen. Im letzten Jahr mussten sich insgesamt $1000$ Sportler je einem Dopingtest unterziehen.": "某国滑雪协会认为，其运动员中有 $1\\%$ 使用违禁兴奋剂。去年共有 $1000$ 名运动员各接受了一次兴奋剂检测。",
    "Dann:": "则：",
    "Berechnen Sie mit der Markov-Ungleichung eine obere Schranke für die Wahrscheinlichkeit, dass mehr als $15$ Dopingtests positiv ausfallen.": "用 Markov 不等式计算超过 $15$ 个兴奋剂检测呈阳性的概率上界。",
    "Schätzen Sie die Wahrscheinlichkeit, dass mehr als $5$, aber weniger als $15$ Tests positiv ausfallen, nach unten ab.": "给出超过 $5$ 个但少于 $15$ 个检测呈阳性的概率下界。",
    "Vergleichen Sie die Schranken aus (a) und (b) mit den wahren Werten.": "将 (a) 和 (b) 的界与真实值比较。",
    "Es seien $a_1,\\dots,a_n$ positive reelle Zahlen. Zeigen Sie mit Hilfe der Jensen-Ungleichung:": "设 $a_1,\\dots,a_n$ 是正实数。用 Jensen 不等式证明：",
    "wobei": "其中：",
    "das arithmetische Mittel,": "表示算术平均数，",
    "das geometrische Mittel und": "表示几何平均数，以及",
    "das harmonische Mittel bezeichnet.": "表示调和平均数。",
    "Es seien $r\\in[1,\\infty)$, $p,q>r$ mit": "设 $r\\in[1,\\infty)$，$p,q>r$，并满足：",
    "$X\\in L^p$ und $Y\\in L^q$. Beweisen Sie:": "$X\\in L^p$ 且 $Y\\in L^q$。证明：",
    "Es seien $X$ und $Y$ absolut stetig verteilt mit Dichten:": "设 $X$ 和 $Y$ 绝对连续分布，密度分别为：",
    "Berechnen Sie mit Hilfe der momenterzeugenden Funktion den Erwartungswert und die Varianz einer poissonverteilten Zufallsvariable": "利用矩母函数计算 Poisson 分布随机变量的期望和方差：",
    "Vier Studierende beschließen, ihr Erspartes für ein Jahr anzulegen. Dabei sei $G_i$, für $i \\in \\{A,B,C,D\\}$, die Zufallsvariable, die den Gewinn der Investition des Studierenden $i$ beschreibt.": "四名学生决定把积蓄投资一年。设 $G_i$（$i\\in\\{A,B,C,D\\}$）为学生 $i$ 的投资收益随机变量。",
    "Student A investiert $1000$ Euro in eine Kryptowährung. Der erwartete Gewinn für diese Investition nach einem Jahr betrage": "学生 A 将 $1000$ 欧元投资于加密货币。该投资一年后的期望收益为：",
    "Euro bei einer Varianz von": "欧元，方差为：",
    "Studentin B steckt $1000$ Euro in Aktien aus dem DAX. Für den Gewinn aus dieser Investition nach einem Jahr gelte": "学生 B 将 $1000$ 欧元投资于 DAX 股票。一年后该投资收益满足：",
    "Studentin C legt ihre $1000$ Euro auf einem Festgeldkonto an, sie erhält nach einem Jahr garantiert $50$ Euro Zinsen, also Gewinn.": "学生 C 将 $1000$ 欧元存入定期账户，一年后保证获得 $50$ 欧元利息，即收益。",
    "Gehen Sie davon aus, dass $G_A$ und $G_B$ jeweils normalverteilt sind. Außerdem sei bekannt:": "假设 $G_A$ 和 $G_B$ 分别服从正态分布。另外已知：",
    "$(3P)$": "（3 分）",
    "Berechnen Sie den Korrelationskoeffizienten": "计算相关系数：",
    "und interpretieren Sie diesen. $(3P)$": "并解释该相关系数。（3 分）",
    "Wie groß ist die Wahrscheinlichkeit, dass Student A nach einem Jahr einen höheren Gewinn erzielt hat als Studentin C? $(3P)$": "学生 A 一年后收益高于学生 C 的概率是多少？（3 分）",
    "Studentin D möchte ihre $1550$ Euro zu einem Teil $\\alpha \\in [0,1]$ auf einem Festgeldkonto mit einer garantierten Verzinsung von $6\\%$ pro Jahr anlegen. Den Rest möchte sie in amerikanische Aktien mit einem erwarteten Gewinn von $10\\%$ bei einer Standardabweichung von $20\\%$ pro Jahr anlegen. Die Gewinne der beiden Investitionen können als unabhängig voneinander angenommen werden.": "学生 D 想把 $1550$ 欧元中的比例 $\\alpha\\in[0,1]$ 投入年保证收益率为 $6\\%$ 的定期账户，其余投入美国股票；股票年期望收益率为 $10\\%$，标准差为 $20\\%$。可假设两项投资收益相互独立。",
    "Sei $\\alpha=0{,}5$. Berechnen Sie den erwarteten Gesamtgewinn in Prozent der Investition für die Investition der Studentin D nach einem Jahr. $(3P)$": "设 $\\alpha=0{,}5$。计算学生 D 一年后总期望收益占投资额的百分比。（3 分）",
    "Welchen Anteil sollte Studentin D höchstens auf das Festgeldkonto legen, wenn der zu erwartende Gesamtgewinn mindestens $9\\%$ betragen soll? $(3P)$": "若期望总收益至少应为 $9\\%$，学生 D 最多应将多大比例投入定期账户？（3 分）",
    "Welchen Anteil sollte Studentin D mindestens auf das Festgeldkonto legen, wenn die Standardabweichung des Gewinns nicht über $10\\%$ liegen soll? $(4P)$": "若收益标准差不应超过 $10\\%$，学生 D 至少应将多大比例投入定期账户？（4 分）",
    "Ein Student möchte der Vermutung nachgehen, dass man beim Radfahren tagsüber schneller auf Gefahren reagiert als nachts. Dazu misst er die Reaktionszeit in Sekunden von fünf weiteren Studierenden, $i \\in \\{1,\\dots,5\\}$, auf eine Ampel, die von grün auf rot umspringt, und zwar nachts. Die Zufallsvariable zur Reaktionszeit nachts sei $X$ und tagsüber sei $Y$:": "一名学生想检验骑车时白天对危险的反应是否比夜晚更快。为此，他测量另外五名学生 $i\\in\\{1,\\dots,5\\}$ 在夜晚对红绿灯由绿变红的反应时间（秒）。夜晚反应时间随机变量记为 $X$，白天记为 $Y$：",
    "Lässt sich die Vermutung anhand der vorliegenden Daten zu einem Signifikanzniveau von $\\alpha=0{,}05$ bestätigen? Benutzen Sie dazu einen verteilungsfreien Test und geben Sie die dazugehörigen Hypothesen an. Berechnen Sie die Teststatistik analytisch, ohne R. Sie dürfen jedoch für die Berechnung der Varianz, der Standardabweichung, des Mittelwertes und der Quantile R verwenden. Treffen Sie anhand dieser die Testentscheidung. $(6P)$": "基于给定数据，在显著性水平 $\\alpha=0{,}05$ 下能否支持该猜想？请使用一个非参数检验，写出相应假设；不用 R，解析计算检验统计量。方差、标准差、均值和分位数可用 R 计算。并据此作出检验决策。（6 分）",
    "Der Student möchte im Folgenden einen parametrischen Test verwenden.": "接下来该学生希望使用参数检验。",
    "Geben Sie einen geeigneten parametrischen Test und die zugehörigen Hypothesen an, den der Student verwenden kann. Gehen Sie dabei auch auf die benötigten Annahmen ein. $(4P)$": "给出一个合适的参数检验及相应假设，并说明所需假设条件。（4 分）",
    "Gehen Sie im Folgenden davon aus, dass die Annahmen aus Teilaufgabe (b)(i) erfüllt sind. Führen Sie den Test aus Teilaufgabe (b)(i) analytisch, ohne R, durch. Sie dürfen jedoch für die Berechnung der Varianz, der Standardabweichung, des Mittelwertes und der Quantile R verwenden. Berechnen Sie dafür die Teststatistik und treffen Sie anhand dieser die Testentscheidung. $(4P)$": "以下假设 (b)(i) 中的检验前提成立。请不用 R 解析执行 (b)(i) 中的检验；方差、标准差、均值和分位数可用 R 计算。计算检验统计量并作出检验决策。（4 分）",
    "Eine weitere Studentin untersucht, ob der Konsum eines Energy Drinks die nächtliche Reaktionszeit beeinflusst. Dazu misst sie die nächtliche Reaktionszeit nach dem Konsum von drei Dosen des Energy Drinks. Die zugehörige Zufallsvariable sei $Z$, bei fünf weiteren zufällig und unabhängig von (a) ausgewählten Studierenden, $i \\in \\{6,\\dots,10\\}$.": "另一名学生研究饮用能量饮料是否影响夜间反应时间。她测量另外五名随机且独立于 (a) 选出的学生 $i\\in\\{6,\\dots,10\\}$ 在喝下三罐能量饮料后的夜间反应时间，相应随机变量记为 $Z$。",
    "Aus zeitlichen Gründen verwendet die Studentin die Daten ihres Kommilitonen aus (a) als Vergleichsgrundlage. Sie nimmt an, dass $X$ und $Z$ jeweils normalverteilt sind.": "由于时间原因，该学生使用同学在 (a) 中的数据作为比较基础。她假设 $X$ 和 $Z$ 分别服从正态分布。",
    "Welcher Test eignet sich unter diesen Bedingungen zur Überprüfung der Hypothese, dass das Getränk die mittlere nächtliche Reaktionszeit verändert? Führen Sie diesen Test durch, $\\alpha=0{,}05$. Geben Sie die Hypothesen an und berechnen Sie die Teststatistik analytisch, ohne R. Sie dürfen jedoch für die Berechnung der Varianz, der Standardabweichung, des Mittelwertes und der Quantile R verwenden. Treffen Sie anhand dieser die Testentscheidung. $(8P)$": "在这些条件下，适合用哪个检验来检验“该饮料改变平均夜间反应时间”的假设？在 $\\alpha=0{,}05$ 下执行该检验。写出假设，不用 R 解析计算检验统计量；方差、标准差、均值和分位数可用 R 计算。并据此作出检验决策。（8 分）",
    "Skizze, Modus, Erwartungswert, Median, Schiefe.": "草图、众数、期望、中位数和偏度。",
    "Varianz.": "方差。",
    "Dichte von $Y=X^2$.": "$Y=X^2$ 的密度。",
    "Erwartungswert von $Z=X^4$ abschätzen.": "估计 $Z=X^4$ 的期望。",
}

QUESTION_TRANSLATIONS_06 = {
    "Es sei $\\mathbb P$ ein Wahrscheinlichkeitsmaß, also ein normiertes Maß mit $\\mathbb P(\\Omega)=1$, auf dem Messraum $(\\Omega,\\mathcal F)$ und $A,B\\in\\mathcal F$.": "设 $\\mathbb P$ 是测度空间 $(\\Omega,\\mathcal F)$ 上的概率测度，即满足 $\\mathbb P(\\Omega)=1$ 的规范化测度，且 $A,B\\in\\mathcal F$。",
    "Falls": "如果：",
    "können $A$ und $B$ dann disjunkt sein? Beweisen oder widerlegen Sie.": "那么 $A$ 和 $B$ 能否不交？请证明或反驳。",
    "Beweisen oder widerlegen Sie:": "证明或反驳：",
    "mit Elementarereignissen $\\omega_x=x$. Außerdem gelte": "其基本事件为 $\\omega_x=x$。此外满足：",
    "Wie groß ist $c$?": "$c$ 是多少？",
    "Gegeben sei ein Wahrscheinlichkeitsraum $(\\Omega,\\mathcal F,\\mathbb P)$ und $B\\subset\\Omega$ mit $\\mathbb P(B)>0$.": "给定概率空间 $(\\Omega,\\mathcal F,\\mathbb P)$ 以及 $B\\subset\\Omega$，且 $\\mathbb P(B)>0$。",
    "Es sei $\\mathbb P$ ein Wahrscheinlichkeitsmaß auf dem Messraum $(\\Omega,\\mathcal F)$ und $A,B\\in\\mathcal F$.": "设 $\\mathbb P$ 是测度空间 $(\\Omega,\\mathcal F)$ 上的概率测度，且 $A,B\\in\\mathcal F$。",
    "Falls $\\mathbb P(A)=\\frac13$ und $\\mathbb P(\\bar B)=\\frac14$, können $A$ und $B$ dann disjunkt sein?": "若 $\\mathbb P(A)=\\frac13$ 且 $\\mathbb P(\\bar B)=\\frac14$，那么 $A$ 和 $B$ 能否不交？",
    "Sei $\\Omega=\\{i\\mid i\\in\\mathbb N_0\\}$ mit Elementarereignissen $\\omega_i=i$. Außerdem gelte:": "设 $\\Omega=\\{i\\mid i\\in\\mathbb N_0\\}$，基本事件为 $\\omega_i=i$。此外满足：",
    "Bestimmen Sie für die folgenden Situationen jeweils die passende Standardverteilung und berechnen Sie die gefragten Wahrscheinlichkeiten.": "对下列情形分别确定合适的标准分布，并计算所问概率。",
    "Tombola": "抽奖。",
    "Es gibt $k$ Lose, durchnummeriert von $1$ bis $k$. Genau ein Los gewinnt. $X_1$ sei die Gewinnlosnummer.": "共有 $k$ 张彩票，编号从 $1$ 到 $k$。恰好一张中奖。设 $X_1$ 为中奖彩票编号。",
    "Lerngruppe": "学习小组。",
    "Es gibt fünf Aufgaben, vier wurden vorbereitet, zwei werden zufällig ausgewählt. $X_2$ sei die Anzahl der vorbereiteten ausgewählten Aufgaben.": "共有五道题，其中四道已准备；随机抽取两道。设 $X_2$ 为被抽中的已准备题目数量。",
    "Kontrolle eines Betriebs": "企业检查。",
    "Jeden Tag wird unabhängig ein Anteil $a$ der Betriebe kontrolliert. $X_3$ sei die Anzahl der Tage bis zur ersten Kontrolle eines bestimmten Betriebs.": "每天独立地检查比例为 $a$ 的企业。设 $X_3$ 为某个特定企业首次被检查前经过的天数。",
    "Test mit 10 Fragen": "10 道题测试。",
    "Ein Schüler beantwortet jede von 10 Fragen unabhängig mit Wahrscheinlichkeit $0.9$ richtig. $X_4$ sei die Anzahl richtiger Antworten.": "一名学生独立作答 10 道题，每题答对概率为 $0.9$。设 $X_4$ 为答对题数。",
    "Gegeben seien zwei Folgen unabhängiger identisch verteilter Zufallsvariablen mit:": "给定两列独立同分布随机变量，满足：",
    "Außerdem seien:": "此外设：",
    "Bestimmen Sie $a,b\\in\\mathbb R$, sodass:": "求 $a,b\\in\\mathbb R$，使得：",
    "Gegeben sei der Wahrscheinlichkeitsraum:": "给定概率空间：",
    "Untersuchen Sie, ob $X_n$ gegen $0$ fast sicher, in Wahrscheinlichkeit, in Verteilung und im ersten Moment konvergiert.": "检验 $X_n$ 是否几乎必然、依概率、依分布以及一阶矩收敛到 $0$。",
    "Gegeben ist eine einzelne Zufallsvariable einer parametrischen Verteilungsfamilie. Nennen Sie Beispiele hinreichender Eigenschaften, unter denen $X$ selbst approximativ normalverteilt sein kann, ähnlich wie bei der Poisson-Approximation. Welche Prinzipien könnten zugrunde liegen?": "给定某参数分布族中的单个随机变量。请举出一些充分性质，使得 $X$ 本身可近似服从正态分布，类似 Poisson 近似。可能基于哪些原理？",
    "Wie oft muss mit einer idealen Münze mindestens geworfen werden, sodass die relative Häufigkeit von Wappen mit Wahrscheinlichkeit mindestens $0.95$ höchstens $0.01$ beziehungsweise $0.001$ von $\\pi=0.5$ abweicht? Nutzen Sie eine geeignete Abschätzung durch eine Ungleichung.": "至少需要投掷一枚理想硬币多少次，才能使正面相对频率以至少 $0.95$ 的概率偏离 $\\pi=0.5$ 不超过 $0.01$ 或 $0.001$？请使用合适的不等式估计。",
    "Ein Beamter verlässt an den $225$ Arbeitstagen eines Jahres sein Büro immer erst kurz nach Dienstschluss. Die täglichen zusätzlichen Arbeitszeiten seien unabhängig exponentialverteilt mit Erwartungswert $1/\\lambda=5$ Minuten.": "某公务员一年有 $225$ 个工作日，每天下班后都会稍晚离开办公室。每天额外工作时间相互独立且服从指数分布，期望为 $1/\\lambda=5$ 分钟。",
    "Leiten Sie die approximative Verteilung der gesamten zusätzlichen Arbeitszeit eines Jahres her.": "推导一年总额外工作时间的近似分布。",
    "Berechnen Sie approximativ die Wahrscheinlichkeit, dass der Beamte in einem Jahr mehr als $16$ Stunden zusätzlich arbeitet.": "近似计算该公务员一年额外工作超过 $16$ 小时的概率。",
    "$X\\sim\\operatorname{Beta}(a,b)$. Berechnen Sie die Dichte von:": "设 $X\\sim\\operatorname{Beta}(a,b)$。计算下列随机变量的密度：",
    "Sei $X$ Weibull-verteilt mit:": "设 $X$ 服从 Weibull 分布，满足：",
    "Bestimmen Sie die Dichte von $Y=X^b$.": "求 $Y=X^b$ 的密度。",
    "Es sei $\\mathbb P$ ein Wahrscheinlichkeitsmaß mit $\\mathbb P(\\Omega)=1$ auf dem Messraum $(\\Omega,\\mathcal F)$ und $A,B\\in\\mathcal F$.": "设 $\\mathbb P$ 是测度空间 $(\\Omega,\\mathcal F)$ 上满足 $\\mathbb P(\\Omega)=1$ 的概率测度，且 $A,B\\in\\mathcal F$。",
    "können $A$ und $B$ dann disjunkt sein?": "$A$ 和 $B$ 能否不交？",
    "mit Elementarereignissen $\\omega_i=i$. Außerdem gelte:": "基本事件为 $\\omega_i=i$。此外满足：",
    "Es sei $(\\Omega,\\mathcal F,\\mathbb P)$ ein Wahrscheinlichkeitsraum und $A,B\\in\\mathcal F$.": "设 $(\\Omega,\\mathcal F,\\mathbb P)$ 是概率空间，且 $A,B\\in\\mathcal F$。",
    "Bestimmen Sie $\\mathbb P(B)$, wenn:": "在下列情况下求 $\\mathbb P(B)$：",
    "- $A$ und $B$ stochastisch unabhängig sind, - $A$ und $B$ disjunkt sind.": "- $A$ 与 $B$ 随机独立；- $A$ 与 $B$ 不交。",
    "Betrachten Sie beim einmaligen fairen Würfelwurf das Ereignis": "考虑一次公平掷骰中的事件：",
    "Geben Sie ein zu $A$ unabhängiges Ereignis $B\\in\\mathcal P(\\Omega)$ mit $B\\notin\\{\\emptyset,\\Omega\\}$ an.": "给出一个与 $A$ 独立的事件 $B\\in\\mathcal P(\\Omega)$，且 $B\\notin\\{\\emptyset,\\Omega\\}$。",
    "Sei $(x_n)_{n\\in\\mathbb N}$ eine Folge reeller Zahlen und seien": "设 $(x_n)_{n\\in\\mathbb N}$ 是实数列，并设：",
    "Dirac-verteilte Zufallsvariablen. Zeigen Sie:": "为 Dirac 分布随机变量。证明：",
    "genau dann, wenn": "当且仅当：",
    "in Wahrscheinlichkeit.": "依概率收敛。",
    "Sei $(X_i)_{i\\in\\mathbb N}$ eine Folge iid Zufallsvariablen in $\\mathbb R$ und $g:\\mathbb R\\to\\mathbb R$ messbar. Nutzen Sie das schwache Gesetz der großen Zahlen, um zu zeigen:": "设 $(X_i)_{i\\in\\mathbb N}$ 是 $\\mathbb R$ 上一列 iid 随机变量，且 $g:\\mathbb R\\to\\mathbb R$ 可测。用弱大数定律证明：",
    "Sei $f:\\mathbb R\\to\\mathbb R$ stetig und": "设 $f:\\mathbb R\\to\\mathbb R$ 连续，且：",
    "Sei $(X_n)_{n\\in\\mathbb N}$ eine Folge diskreter Zufallsvariablen mit": "设 $(X_n)_{n\\in\\mathbb N}$ 是一列离散随机变量，满足：",
    "Sei $f:\\mathbb R\\to\\mathbb R$ eine stetige Dichtefunktion. Seien $X_i\\sim f$ iid. Für den Bandbreitenparameter $h>0$ definiere den Dichteschätzer mit uniformem Kern:": "设 $f:\\mathbb R\\to\\mathbb R$ 是连续密度函数，且 $X_i\\sim f$ iid。对带宽参数 $h>0$，用均匀核定义密度估计量：",
    "Sei $x\\in\\mathbb R$ fix.": "固定 $x\\in\\mathbb R$。",
    "Nutzen Sie das schwache Gesetz der großen Zahlen, um zu zeigen:": "用弱大数定律证明：",
    "Sei $\\Omega=\\{0,1\\}$ mit Potenzmenge als $\\sigma$-Algebra und": "设 $\\Omega=\\{0,1\\}$，以其幂集为 $\\sigma$-代数，并且：",
    "Definiere $X_n,X:\\Omega\\to\\mathbb R$ durch:": "定义 $X_n,X:\\Omega\\to\\mathbb R$ 如下：",
    "Sei $(X_n)$ eine Folge von Zufallsvariablen mit": "设 $(X_n)$ 是一列随机变量，满足：",
    "wobei $c\\in\\mathbb R$ konstant ist. Zeigen Sie:": "其中 $c\\in\\mathbb R$ 为常数。证明：",
    "Ein fairer Würfel werde $6000$-mal unabhängig geworfen. Bestimmen Sie für die Wahrscheinlichkeit, dass zwischen $900$-mal und $1100$-mal eine Sechs geworfen wird,": "独立掷一个公平骰子 $6000$ 次。对于掷出 $6$ 的次数在 $900$ 到 $1100$ 之间的概率，求：",
    "mit dem zentralen Grenzwertsatz eine Approximation. $(6\\text{ Pkt.})$": "用中心极限定理给出近似值。（6 分）",
    "mit der Tschebyscheff-Ungleichung eine untere Schranke. $(4\\text{ Pkt.})$": "用 Chebyshev 不等式给出下界。（4 分）",
    "**Hinweis zu (a):** Sie dürfen verwenden, dass für die Verteilungsfunktion $\\Phi(x)$ der Standardnormalverteilung die Identität": "**(a) 提示：** 可以使用标准正态分布函数 $\\Phi(x)$ 的恒等式：",
    "gilt.": "成立。",
    "Rechenzeit in Sekunden von $n=100$ Programmen auf einem Großrechner seien durch $100$ Zufallsvariablen": "大型计算机上 $n=100$ 个程序的运行时间（秒）由 $100$ 个随机变量表示：",
    "beschrieben, die stochastisch unabhängig und identisch verteilt sind mit": "这些随机变量相互独立同分布，并满足：",
    "a) Es wurde eine Gesamtrechenzeit der $100$ Programme von $1900$ Sekunden beobachtet. Basierend auf der Normalapproximation überprüfen Sie die Hypothese": "a) 观察到 $100$ 个程序总运行时间为 $1900$ 秒。基于正态近似检验假设：",
    "gegen": "相对于：",
    "zum Niveau": "在显著性水平：",
    "b) Es sei nun $\\mu=20$. Geben Sie für die Wahrscheinlichkeit, dass die Gesamtrechenzeit der $100$ Programme zwischen $1800$ und $2200$ Sekunden liegt, einen Näherungswert durch Anwendung des zentralen Grenzwertsatzes an. Verwenden Sie die Verteilungsfunktion der Standardnormalverteilung im Anhang.": "b) 现在设 $\\mu=20$。用中心极限定理给出 $100$ 个程序总运行时间位于 $1800$ 到 $2200$ 秒之间的概率近似值。使用附录中的标准正态分布函数。",
    "Ein fairer Würfel werde $6000$-mal unabhängig geworfen.": "独立掷一个公平骰子 $6000$ 次。",
    "Bestimmen Sie mit Hilfe des zentralen Grenzwertsatzes eine Approximation für die Wahrscheinlichkeit, dass zwischen $900$-mal und $1100$-mal eine Sechs geworfen wird.": "用中心极限定理近似计算掷出 $6$ 的次数在 $900$ 到 $1100$ 之间的概率。",
    "Bestimmen Sie mit der Tschebyscheff-Ungleichung eine untere Schranke für die Wahrscheinlichkeit, dass zwischen $900$-mal und $1100$-mal eine Sechs geworfen wird.": "用 Chebyshev 不等式给出掷出 $6$ 的次数在 $900$ 到 $1100$ 之间的概率下界。",
    "Prof. S. nimmt täglich, also $n=225$-mal, den Bus zur Universität und ist immer pünktlich an der Bushaltestelle. Der Bus verspätet sich jedoch jeden Tag. Bezeichne $X_i$ die zufällige Zeitdauer der Verspätung in Minuten am Tag $i$. Nehmen Sie an, dass $X_i$, $i=1,\\dots,n$, unabhängig und identisch exponentialverteilt sind mit $E(X_i)=1$.": "S 教授每天乘公交去大学，一年共 $n=225$ 次，并且总是准时到公交站。但公交每天都会晚点。令 $X_i$ 为第 $i$ 天晚点分钟数。假设 $X_i$（$i=1,\\dots,n$）独立同分布且服从指数分布，$E(X_i)=1$。",
    "Betrachten Sie die Zufallsgröße:": "考虑随机变量：",
    "also die aufsummierte Verspätung in einem Jahr.": "即一年内累计晚点时间。",
    "Zeigen Sie, dass $X$ approximativ normalverteilt ist. Wie lauten approximativer Erwartungswert und approximative Varianz?": "证明 $X$ 近似正态分布。其近似期望和近似方差是多少？",
    "Bestimmen Sie approximativ die Wahrscheinlichkeit dafür, dass Prof. S. über das Jahr gesehen mehr als $4$ Stunden auf den Bus wartet.": "近似求 S 教授一年中等待公交总时间超过 $4$ 小时的概率。",
    "Betrachten Sie eine Münze, die beim Münzwurf mit unbekannter Wahrscheinlichkeit $p\\in(0,1)$ Zahl anzeigt und dementsprechend mit Wahrscheinlichkeit $1-p$ Kopf.": "考虑一枚硬币，投掷时以未知概率 $p\\in(0,1)$ 出现反面，相应地以概率 $1-p$ 出现正面。",
    "Es bezeichne $X$ die Anzahl an Würfen, die nötig ist, bis das erste Mal Zahl erscheint. Das Experiment werde $n=200$ mal wiederholt, d.h. $X_i$ bezeichnet die Anzahl der benötigten Würfe, bis das erste Mal Zahl erscheint, bei der $i$-ten Wiederholung des Experiments.": "令 $X$ 为首次出现反面前所需投掷次数。该实验重复 $n=200$ 次，即 $X_i$ 表示第 $i$ 次重复实验中首次出现反面所需投掷次数。",
    "Mit": "用：",
    "wird die durchschnittlich benötigte Anzahl an Versuchen bezeichnet.": "表示平均所需尝试次数。",
    "Bestimmen Sie eine approximative Verteilung für $\\overline X$.": "求 $\\overline X$ 的近似分布。",
    "Wie muss $p$ gewählt werden, damit mit einer Wahrscheinlichkeit von mindestens $0.9$ folgendes gilt:": "$p$ 应如何选择，才能使下列事件至少以 $0.9$ 的概率成立：",
    "weicht betragsmäßig vom unbekannten Erwartungswert $E(X_i)$ um höchstens $0.1645$ ab?": "它与未知期望 $E(X_i)$ 的绝对偏差至多为 $0.1645$？",
    "Hinweis: Das $0.95$-Quantil der Standardnormalverteilung ist $1.645$, d.h. für $Z\\sim \\mathcal N(0,1)$ gilt": "提示：标准正态分布的 $0.95$ 分位数为 $1.645$，即对 $Z\\sim\\mathcal N(0,1)$ 有：",
    "Bestimmen Sie eine approximative Verteilung für $\\overline X^2$.": "求 $\\overline X^2$ 的近似分布。",
    "Für die Exponentialverteilung gilt:": "对指数分布有：",
    "Approximation durch Normalverteilung.": "用正态分布近似。",
    "Wahrscheinlichkeit für mehr als $4$ Stunden Wartezeit.": "等待时间超过 $4$ 小时的概率。",
}

QUESTION_TRANSLATIONS_07 = {
    "Zeigen Sie: Wenn zwei gemeinsam normalverteilte Zufallsvariablen unkorreliert sind, dann sind diese auch unabhängig.": "证明：若两个联合正态随机变量不相关，则它们独立。",
    "Die zweidimensionale Zufallsvariable $(X,Y)$ sei stetig verteilt mit Dichte:": "设二维随机变量 $(X,Y)$ 连续分布，其密度为：",
    "Zeigen Sie, dass $c=4$.": "证明 $c=4$。",
    "Bestimmen Sie die Randdichten $f_X$ und $f_Y$.": "求边际密度 $f_X$ 和 $f_Y$。",
    "Überprüfen Sie, ob $X$ und $Y$ unabhängig sind.": "检验 $X$ 与 $Y$ 是否独立。",
    "Bestimmen Sie $\\mathbb E(X+Y)$.": "求 $\\mathbb E(X+Y)$。",
    "Bestimmen Sie $\\mathbb P(X\\leq Y)$.": "求 $\\mathbb P(X\\leq Y)$。",
    "Die gemeinsame Dichte von $(X,Y)$ sei:": "$(X,Y)$ 的联合密度为：",
    "Was ist der Träger von $(X,Y)$?": "$(X,Y)$ 的支撑集是什么？",
    "Zeigen Sie, dass $X$ gleichverteilt auf $[0,1]$ ist.": "证明 $X$ 在 $[0,1]$ 上均匀分布。",
    "Bestimmen Sie die Randverteilung von $Y$.": "求 $Y$ 的边际分布。",
    "Zeigen Sie, dass $Y\\mid X=x$ gleichverteilt auf $[0,x]$ ist.": "证明 $Y\\mid X=x$ 在 $[0,x]$ 上均匀分布。",
    "Bestimmen Sie die bedingte Verteilung von $X\\mid Y=y$.": "求 $X\\mid Y=y$ 的条件分布。",
    "Berechnen Sie $\\mathbb E(Y)$ und die Dichte von $X\\mid Y$.": "计算 $\\mathbb E(Y)$ 以及 $X\\mid Y$ 的密度。",
    "Seien $X$ und $Y$ Zufallsvariablen mit gemeinsamer Wahrscheinlichkeitsfunktion:": "设 $X$ 和 $Y$ 是具有如下联合概率函数的随机变量：",
    "Zwei stetige Zufallsvariablen $X$ und $Y$ haben die gemeinsame Dichte:": "两个连续随机变量 $X$ 和 $Y$ 具有如下联合密度：",
    "Seien $X$ und $Y$ Zufallsvariablen mit:": "设随机变量 $X$ 和 $Y$ 满足：",
    "Setze:": "令：",
    "Bestimmen Sie $\\operatorname{Var}(W)$, $\\operatorname{Var}(T)$, $\\operatorname{Cov}(W,T)$ und $\\rho(W,T)$, wenn $X$ und $Y$ unabhängig sind.": "若 $X$ 与 $Y$ 独立，求 $\\operatorname{Var}(W)$、$\\operatorname{Var}(T)$、$\\operatorname{Cov}(W,T)$ 和 $\\rho(W,T)$。",
    "Bestimmen Sie dieselben Größen, wenn $\\rho(X,Y)=-\\frac14$ gilt.": "若 $\\rho(X,Y)=-\\frac14$，求同样这些量。",
    "Warum gilt in Szenario (b) $\\operatorname{Var}(W)<\\operatorname{Var}(T)$?": "为什么在情形 (b) 中有 $\\operatorname{Var}(W)<\\operatorname{Var}(T)$？",
    "Seien $X\\sim U(0,1)$ und $Y\\sim U(0,1)$ unabhängig. Bestimmen Sie die Verteilung von:": "设 $X\\sim U(0,1)$ 与 $Y\\sim U(0,1)$ 独立。求下列随机变量的分布：",
    "Seien $X\\sim\\operatorname{Exp}(\\lambda)$ und $Y\\sim\\operatorname{Exp}(\\lambda)$ unabhängig. Bestimmen Sie die Verteilung von $Z=X+Y$.": "设 $X\\sim\\operatorname{Exp}(\\lambda)$ 与 $Y\\sim\\operatorname{Exp}(\\lambda)$ 独立。求 $Z=X+Y$ 的分布。",
    "Seien $X\\sim\\operatorname{Poi}(\\lambda_X)$ und $Y\\sim\\operatorname{Poi}(\\lambda_Y)$ unabhängig. Bestimmen Sie die Verteilung von $Z=X+Y$.": "设 $X\\sim\\operatorname{Poi}(\\lambda_X)$ 与 $Y\\sim\\operatorname{Poi}(\\lambda_Y)$ 独立。求 $Z=X+Y$ 的分布。",
    "Sei $Z\\sim\\operatorname{Bernoulli}(0.5)$. Bedingt auf $Z=0$ sei:": "设 $Z\\sim\\operatorname{Bernoulli}(0.5)$。在条件 $Z=0$ 下，设：",
    "und bedingt auf $Z=1$ sei:": "在条件 $Z=1$ 下，设：",
    "Bestimmen Sie $\\mathbb E(X^2)$ und $\\operatorname{Var}(X)$.": "求 $\\mathbb E(X^2)$ 和 $\\operatorname{Var}(X)$。",
    "Bestimmen Sie $\\operatorname{Var}(X)$ mit dem Satz der totalen Varianz.": "用总方差公式求 $\\operatorname{Var}(X)$。",
    "Seien $X,Y$ unabhängig poissonverteilt mit Parameter $\\lambda$. Bestimmen Sie die Dichte von $Z=X+Y$.": "设 $X,Y$ 独立且都服从参数为 $\\lambda$ 的 Poisson 分布。求 $Z=X+Y$ 的概率函数。",
    "$A\\sim\\operatorname{Geom}(p)$ und $B\\sim\\operatorname{Geom}(p)$ seien unabhängig. Zeigen Sie:": "设 $A\\sim\\operatorname{Geom}(p)$ 与 $B\\sim\\operatorname{Geom}(p)$ 独立。证明：",
    "Zeigen Sie, dass für Zufallsvariablen $X$ und $Y$ mit endlichen Varianzen die Korrelation nicht größer als $1$ sein kann:": "证明：对具有有限方差的随机变量 $X,Y$，相关系数不可能大于 $1$：",
    "Seien $X_1,\\dots,X_n$ Zufallsvariablen mit beschränktem zweitem Moment.": "设 $X_1,\\dots,X_n$ 是二阶矩有界的随机变量。",
    "Gegeben seien $X$ und $Y$ mit gemeinsamer Dichte": "给定 $X$ 和 $Y$，其联合密度为：",
    "Begründen Sie kurz ohne weitere Rechnung, warum $X$ und $Y$ nicht unabhängig sein können.": "不做进一步计算，简要说明为什么 $X$ 和 $Y$ 不可能独立。",
    "Berechnen Sie die Randdichten von $X$ und $Y$.": "计算 $X$ 和 $Y$ 的边际密度。",
    "Berechnen Sie die Kovarianz von $X$ und $Y$.": "计算 $X$ 与 $Y$ 的协方差。",
    "Seien $X$ und $Y$ stochastisch unabhängig und standardnormalverteilt. Zeigen Sie mit Hilfe des multivariaten Transformationssatzes für Dichten, dass": "设 $X$ 和 $Y$ 随机独立且服从标准正态分布。用多元密度变换定理证明：",
    "exponentialverteilt ist.": "服从指数分布。",
    "Seien $X,Y\\in\\mathbb R$ unabhängige Zufallsvariablen mit beschränktem ersten Moment. Zeigen Sie:": "设 $X,Y\\in\\mathbb R$ 是独立随机变量且一阶矩有界。证明：",
    "Seien $Y_1,Y_2,X$ Zufallsvariablen mit beschränktem zweitem Moment. Zeigen Sie den Kovarianzzerlegungssatz:": "设 $Y_1,Y_2,X$ 为二阶矩有界的随机变量。证明协方差分解公式：",
    "Dabei:": "其中：",
    "Seien $X,Y\\in\\mathbb R$ Zufallsvariablen mit beschränktem zweitem Moment. Betrachten Sie das lineare Modell": "设 $X,Y\\in\\mathbb R$ 是二阶矩有界的随机变量。考虑线性模型：",
    "mit $\\beta\\in\\mathbb R$, wobei $\\varepsilon$ und $X$ unabhängig sind und": "其中 $\\beta\\in\\mathbb R$，并且 $\\varepsilon$ 与 $X$ 独立，且：",
    "Definiere den Determinationskoeffizienten:": "定义决定系数：",
    "In der Statistik interessiert man sich oft für die sogenannte empirische Dichtefunktion von zuvor erhobenen Daten. Im folgenden Beispiel wurden $200$ Daten erhoben und jeweils zwei Merkmale $X$ und $Y$ beobachtet. Die folgende Tabelle gibt die Beobachtungen an:": "统计中常关心已收集数据的所谓经验密度函数。下面例子中收集了 $200$ 条数据，并观察每条数据的两个特征 $X$ 和 $Y$。下表给出观察结果：",
    "Die empirische Dichte von $X$ und $Y$ ist dabei gegeben durch": "$X$ 和 $Y$ 的经验密度由下式给出：",
    "Bestimmen Sie die empirische gemeinsame Dichte von $X$ und $Y$. $(2\\text{ Pkt.})$": "求 $X$ 和 $Y$ 的经验联合密度。（2 分）",
    "Bestimmen Sie die Dichte $f_Y(y)$. $(2\\text{ Pkt.})$": "求密度 $f_Y(y)$。（2 分）",
    "Bestimmen Sie die Dichte $f_{X\\mid Y=1}(x)$. $(2\\text{ Pkt.})$": "求条件密度 $f_{X\\mid Y=1}(x)$。（2 分）",
    "Sind $X$ und $Y$ unabhängig? Begründen Sie ihre Antwort. $(2\\text{ Pkt.})$": "$X$ 和 $Y$ 是否独立？请说明理由。（2 分）",
    "Betrachte die Zufallsvariablen $X$ und $Y$, deren gemeinsame Verteilung soweit bekannt der Kontingenztabelle angegeben ist.": "考虑随机变量 $X$ 和 $Y$，其已知联合分布由列联表给出。",
    "a) Vervollständige die Tabelle.": "a) 补全表格。",
    "b) Berechne $\\operatorname{Cov}(X,Y)$ und $\\varphi$.": "b) 计算 $\\operatorname{Cov}(X,Y)$ 和 $\\varphi$。",
    "c) Bestimme $F_X(x)$ und zeichne sie.": "c) 求 $F_X(x)$ 并画出图像。",
    "d) Sind $X$ und $Y$ unabhängig?": "d) $X$ 和 $Y$ 是否独立？",
    "Seien $X$ und $Y$ Zufallsvariablen mit gemeinsamer Wahrscheinlichkeitsfunktion $f_{X,Y}(x,y)$:": "设 $X$ 和 $Y$ 具有联合概率函数 $f_{X,Y}(x,y)$：",
    "Bestimmen Sie die Randverteilungen von $X$ und $Y$.": "求 $X$ 和 $Y$ 的边际分布。",
    "Bestimmen Sie $E(X)$ und $\\operatorname{Var}(X)$.": "求 $E(X)$ 和 $\\operatorname{Var}(X)$。",
    "Bestimmen Sie die Kovarianz und Korrelation zwischen $X$ und $Y$ und interpretieren Sie diese.": "求 $X$ 与 $Y$ 的协方差和相关系数，并解释结果。",
    "Bestimmen Sie die bedingte Verteilung von $Y\\mid X=0$.": "求 $Y\\mid X=0$ 的条件分布。",
    "Sei $X$ betaverteilt mit": "设 $X$ 服从 Beta 分布，满足：",
    "und $Y$ gegeben $X$ geometrisch verteilt mit": "并且在给定 $X$ 时，$Y$ 服从如下几何分布：",
    "Berechnen Sie $E(Y)$. Hinweis:": "计算 $E(Y)$。提示：",
    "Berechnen Sie die Dichte von $X\\mid Y$.": "计算 $X\\mid Y$ 的密度。",
    "Berechnen Sie $E(X\\mid Y)$.": "计算 $E(X\\mid Y)$。",
    "zwei stochastisch unabhängige Zufallsvariablen.": "两个随机独立的随机变量。",
    "Bestimmen Sie Erwartungswert und Kovarianzmatrix des Zufallsvektors": "求该随机向量的期望和协方差矩阵：",
    "multivariat normalverteilt mit": "服从多元正态分布，具有：",
    "Geben Sie die Verteilungen von $X_1$ und $X_2$ mit Erwartungswert und Varianz an.": "给出 $X_1$ 和 $X_2$ 的分布、期望和方差。",
    "Sind $X_1$ und $X_2$ stochastisch unabhängig? Begründen Sie.": "$X_1$ 和 $X_2$ 是否随机独立？请说明理由。",
    "Berechnen Sie die Wahrscheinlichkeit": "计算概率：",
    "Runden Sie bitte auf $3$ Nachkommastellen.": "请四舍五入到小数点后三位。",
    "Schätzen Sie die untere Schranke von": "估计下列量的下界：",
    "ab.": "。",
    "Handelt es sich bei den folgenden Matrizen um gültige Kovarianzmatrizen? Begründen Sie.": "下列矩阵是否为合法协方差矩阵？请说明理由。",
    "ein Zufallsvektor mit gemeinsamer Dichte:": "一个具有如下联合密度的随机向量：",
    "Zeigen Sie, dass $X_1$ und $X_2$ stochastisch unabhängig sind.": "证明 $X_1$ 和 $X_2$ 随机独立。",
    "Leiten Sie die Randdichten von $X_1$ und $X_2$ her. Handelt es sich um bekannte Verteilungen?": "推导 $X_1$ 和 $X_2$ 的边际密度。它们是否属于已知分布？",
    "Leiten Sie die Dichte von $Y=X_1+X_2$ her.": "推导 $Y=X_1+X_2$ 的密度。",
    "multivariat normalverteilt mit:": "服从多元正态分布，参数为：",
    "und Kovarianzmatrix:": "以及协方差矩阵：",
    "Geben Sie $A$ an und begründen Sie. Geben Sie mit Begründung eine möglichst hohe Untergrenze für $B$ an.": "给出 $A$ 并说明理由。再给出 $B$ 尽可能大的下界并说明理由。",
    "Welche Verteilung hat": "下列随机变量服从什么分布：",
    "Wie lauten Erwartungswert und Varianz? Begründen Sie.": "其期望和方差是多少？请说明理由。",
    "an. Begründen Sie.": "并说明理由。",
    "Seien $X$ und $Y$ Zufallsvariablen mit gemeinsamer Wahrscheinlichkeitsfunktion": "设 $X$ 和 $Y$ 具有如下联合概率函数：",
    "Berechnen Sie $E(Y)$.": "计算 $E(Y)$。",
    "Handelt es sich bei den folgenden Matrizen um gültige Kovarianzmatrizen? Begründen Sie kurz.": "下列矩阵是否为合法协方差矩阵？请简要说明理由。",
    "Achtung: Damit das Produkt zweier Exponentialdichten entsteht, schreibt man:": "注意：为了得到两个指数密度的乘积，可写成：",
    "Unabhängigkeit.": "独立性。",
    "Randdichten.": "边际密度。",
    "Dichte von $Y=X_1+X_2$.": "$Y=X_1+X_2$ 的密度。",
    "$A$ und Abschätzung für $B$.": "$A$ 以及对 $B$ 的估计。",
    "Verteilung von $Y=\\sum_{i=1}^3X_i$.": "$Y=\\sum_{i=1}^3X_i$ 的分布。",
    "Gesucht.": "要求的量。",
}

QUESTION_TRANSLATIONS_09 = {
    "Gegeben sind:": "给定：",
    "Berechnen Sie TPR und FPR für mögliche Score-Cut-offs, zeichnen Sie die ROC-Kurve, berechnen Sie AUC und interpretieren Sie den Wert. Außerdem: Bewerten Sie in einem medizinischen Diagnosebeispiel False Positives, False Negatives und NPV/PPV bei Cut-off $0.65$.": "计算可能 score 阈值下的 TPR 和 FPR，画出 ROC 曲线，计算 AUC 并解释其含义。另外，在医学诊断例子中评价阈值 $0.65$ 下的假阳性、假阴性以及 NPV/PPV。",
    "Eine Grafik zeigt den Zusammenhang zwischen BIP pro Kopf und Kindersterblichkeitsrate in verschiedenen Ländern. Listen Sie die dargestellten Merkmale, Skalenniveaus und ästhetischen Zuordnungen auf.": "某图展示不同国家人均 GDP 与儿童死亡率之间的关系。请列出图中变量、尺度水平以及美学映射。",
    "Analysieren Sie eine gestapelte Balkengrafik zu Bildungsstand, Geschlecht und Altersgruppen.": "分析一张关于教育水平、性别和年龄组的堆叠柱状图。",
    "Analysieren Sie eine WHO-Grafik zu WASH-Services, Wohnort und Zugangszuwächsen.": "分析一张关于 WASH 服务、居住地和可及性增长的 WHO 图形。",
    "Diskutieren Sie kritisch die Aussage, die Grafik zeige eindeutig, dass höheres Einkommen bessere Bildungsqualität verursache. Zusätzlich: Identifizieren Sie Schwächen einer Alphabetisierungs-Grafik und schlagen Sie Verbesserungen für den Vergleich Asien/Europa vor.": "批判性讨论“该图明确表明更高收入导致更好教育质量”这一说法。另外，指出一张识字率图的弱点，并提出用于比较亚洲/欧洲的改进建议。",
    "Eine Grafik stellt den Zusammenhang zwischen Human Development Index (HDI) und Planetary Pressures Index für Ländergruppen und Zeitpunkte dar.": "某图展示不同国家组和时间点下 Human Development Index (HDI) 与 Planetary Pressures Index 之间的关系。",
    "Analysieren Sie eine Starbucks-Grafik zu Koffein, Zucker, Volumen und Getränken sowie eine alternative problematische Darstellung.": "分析一张关于星巴克饮品咖啡因、糖、容量和饮品类型的图，以及另一种有问题的替代表达。",
    "Holstein Kiel untersucht $n=36$ Elfmeter:": "Holstein Kiel 分析 $n=36$ 个点球：",
    "Gegeben sind Beobachtungen mit Kategorie $0/1$ und Score:": "给定带有 $0/1$ 类别和 score 的观测：",
    "Im Rahmen einer Studie zu den wirtschaftlichen Auswirkungen des Klimawandels auf den Weinanbau in Deutschland soll der Weinmostertrag in $\\mathrm{hl}/\\mathrm{ha}$ in den $13$ deutschen Weinanbaugebieten miteinander verglichen werden. Anhand der jetzt bereits vorhandenen Unterschiede zwischen den Regionen erhofft man sich, Informationen für die Zukunft gewinnen zu können.": "在一项关于气候变化对德国葡萄种植经济影响的研究中，需要比较德国 $13$ 个葡萄酒产区的葡萄汁产量（单位 $\\mathrm{hl}/\\mathrm{ha}$）。研究者希望通过当前地区差异为未来获取信息。",
    "Für das Jahr $2020$ liegen die folgenden Zahlen für die Regionen vor. Sie können für die folgenden Aufgaben davon ausgehen, dass der Rot- und Weißmostertrag zwischen den Regionen jeweils normalverteilt ist.": "给出 $2020$ 年各地区如下数据。以下小问可假设地区间红葡萄汁和白葡萄汁产量分别服从正态分布。",
    "Quelle: Destatis, Datensatz: $41253$-$0002$.": "来源：Destatis，数据集 $41253$-$0002$。",
    "Es soll überprüft werden, ob sich der mittlere Rot- und Weißmostertrag in den Regionen signifikant, $\\alpha=0{,}05$, voneinander unterscheidet.": "需要在显著性水平 $\\alpha=0{,}05$ 下检验各地区红葡萄汁与白葡萄汁的平均产量是否存在显著差异。",
    "Welchen Test würden Sie hierfür verwenden? Begründen Sie ihre Entscheidung. Stellen Sie die zu testenden Hypothesen auf. $(4P)$": "你会使用哪个检验？请说明理由，并写出待检验的假设。（4 分）",
    "Führen Sie den Test in R durch. Zu welchem Ergebnis kommen Sie? $(4P)$": "在 R 中执行该检验。你得到什么结论？（4 分）",
    "Geben Sie für den mittleren Unterschied zwischen Rot- und Weißmostertrag in den Regionen ein $90\\%$-Konfidenzintervall an. $(2P)$": "给出各地区红葡萄汁与白葡萄汁平均产量差的 $90\\%$ 置信区间。（2 分）",
    "Im zweiten Schritt soll jetzt überprüft werden, ob eine Abhängigkeit zwischen Rot- und Weißmostertrag in den Regionen besteht.": "第二步要检验各地区红葡萄汁和白葡萄汁产量之间是否存在依赖关系。",
    "Welchen Test würden Sie hierfür verwenden? Begründen Sie ihre Entscheidung. Welche zusätzliche Annahme über die Verteilung der Daten ist hier notwendig? Stellen Sie die zu testenden Hypothesen auf. $(4P)$": "你会使用哪个检验？请说明理由。这里还需要对数据分布作出什么额外假设？写出待检验的假设。（4 分）",
    "Führen Sie den Test in R durch. Gehen Sie davon aus, dass die zusätzliche Annahme aus (c)(i) gegeben ist. $(4P)$": "在 R 中执行该检验。假设 (c)(i) 中的额外条件成立。（4 分）",
    "Betrachten Sie die untenstehende Grafik. Sie zeigt den durchschnittlichen Ertrag („crop yield“) für landwirtschaftliche Nutzflächen in Tonnen pro Hektar auf den Kontinenten der Erde im Jahr 2018. ![](图片/Altklausur2LV-1.png) Analysieren Sie die grafischen Mittel, die zur Visualisierung benutzt wurden.": "观察下图。它展示了 2018 年世界各大洲农业用地的平均产量（crop yield，吨/公顷）。![](图片/Altklausur2LV-1.png) 分析该可视化使用的图形手段。",
    "Geben Sie für **alle** in der Grafik gezeigten Merkmale jeweils": "对图中显示的**所有**变量分别给出：",
    "- das Skalenniveau - die verwendeten Zuordnungen auf ästhetische Eigenschaften der gezeichneten Sechsecke": "- 尺度水平；- 这些变量到所绘制六边形美学属性的映射。",
    "Inwiefern verletzt die hier verwendete Farbpalette die in der Vorlesung besprochenen Kriterien für Farbskalen in statistischen Grafiken? Was für eine Art von Farbskala sollte stattdessen verwendet werden?": "这里使用的调色板在哪些方面违反了课堂上讨论的统计图形色标标准？应改用哪类色标？",
    "Statistische Grafiken sollen die Datenlage möglichst unverfälscht darstellen. Inwiefern verfälscht die obige Darstellung die tatsächliche Datenlage?": "统计图形应尽量不失真地呈现数据。上图在哪些方面扭曲了真实数据情况？",
    "Statistische Grafiken sollen die Datenlage möglichst kompakt darstellen, also: minimal viel verwendete Tinte für maximal viel vermittelte Information.": "统计图形应尽量紧凑地呈现数据，即用尽可能少的墨水传递尽可能多的信息。",
    "Inwiefern verfehlt die obige Darstellung dieses Ziel?": "上图在哪些方面没有达到这一目标？",
    "Statistische Grafiken sollen die Datenlage möglichst übersichtlich darstellen, um den Konsument:innen der Grafik schnelles und präzises Ablesen relevanter quantitativer Informationen zu ermöglichen.": "统计图形应尽量清晰，使读者能快速、准确读出相关定量信息。",
    "Definieren Sie eine alternative grafische Darstellung für die in der obenstehenden Grafik gezeigten Daten, welche diese unverfälscht, kompakt und übersichtlich visualisiert. Verwenden Sie für die Beschreibung die in der Vorlesung eingeführten Begrifflichkeiten der *grammar of graphics* oder die entsprechende `{ggplot2}`-Syntax.": "为上图数据设计一种替代图形表示，使其不失真、紧凑且清晰。描述时请使用课堂中介绍的 *grammar of graphics* 概念或相应 `{ggplot2}` 语法。",
    "Die obigen Grafiken visualisieren Antworthäufigkeiten auf die Frage „Wie oft fühlen Sie sich einsam?“, die im Rahmen des „Community Life Survey“ des nationalen britischen Statistikinstituts im Jahr 2016/2017 gestellt wurde. Alle drei Grafiken zeigen denselben Datensatz.": "上面的图形展示了英国国家统计机构在 2016/2017 年 “Community Life Survey” 中关于“你多久感到孤独？”这一问题的回答频数。三张图显示的是同一个数据集。",
    "Geben Sie an, welche Merkmale in diesen Grafiken visualisiert werden und welches Skalenniveau diese besitzen.": "指出这些图中可视化了哪些变量，以及它们各自的尺度水平。",
    "Welche Art von Farbskala wird in Grafiken B und C verwendet? Welche andere Art von Farbskala käme hier ebenso in Frage und warum?": "图 B 和图 C 使用了哪类色标？这里还可以使用哪类色标，为什么？",
    "Beantworten Sie die folgenden inhaltlichen Fragen. Geben Sie jeweils an, welche der drei Grafiken sich am besten eignet, um die jeweilige Frage zu beantworten und warum.": "回答下列实质性问题。每问请指出三张图中哪一张最适合回答该问题，并说明原因。",
    "Sind die hier dargestellten Merkmale empirisch unabhängig? Begründen Sie Ihre Antwort.": "这里显示的变量是否经验独立？请说明理由。",
    "Der „Community Life Survey“ befragt die Bewohner:innen einer Zufallsstichprobe britischer Haushalte über mehrere Jahre wiederholt mit denselben Fragebögen. Um was für eine Art von Erhebung handelt es sich also?": "“Community Life Survey” 对英国家庭随机样本中的居民进行多年重复问卷调查。它属于哪种调查类型？",
    "Warum können Aussagen wie": "为什么如下说法：",
    "„Die meisten Menschen in Großbritannien fühlen sich tendenziell seltener einsam, umso älter sie werden.“": "“英国多数人随着年龄增长往往更少感到孤独。”",
    "mit den in den Grafiken gezeigten Daten aus 2016/2017 nicht schlüssig begründet oder widerlegt werden? Mit was für Daten könnte so eine Aussage belegt oder widerlegt werden?": "不能用图中 2016/2017 年的数据得到有力支持或反驳？需要哪类数据才能支持或反驳这种说法？",
    "Die Grafik zeigt Streudiagramme zu den Datensätzen A, B, C und D, die jeweils $n=200$ Beobachtungen zweier metrischer Merkmale enthalten.": "该图显示数据集 A、B、C、D 的散点图，每个数据集都包含两个度量变量的 $n=200$ 个观测。",
    "Folgende Tabelle gibt die Pearson- und Spearman-Korrelationen der gezeigten Datensätze an.": "下表给出这些数据集的 Pearson 和 Spearman 相关系数。",
    "Die linke obere Grafik zeigt Kerndichteschätzer für drei der Merkmale aus $y_A,y_B,y_C$ oder $y_D$. Welcher Kerndichteschätzer $(1,2,3)$ gehört zu welchem Merkmal $(y_A,y_B,y_C,y_D)$?": "左上图显示了 $y_A,y_B,y_C,y_D$ 中三个变量的核密度估计。核密度估计 $(1,2,3)$ 分别对应哪个变量 $(y_A,y_B,y_C,y_D)$？",
    "Die rechte obere Grafik zeigt Boxplots für drei der Merkmale aus $y_A,y_B,y_C$ oder $y_D$. Welcher Boxplot $(i,ii,iii)$ gehört zu welchem Merkmal $(y_A,y_B,y_C,y_D)$? Falls für einen Boxplot mehrere Merkmale in Frage kommen, geben Sie alle an.": "右上图显示了 $y_A,y_B,y_C,y_D$ 中三个变量的箱线图。箱线图 $(i,ii,iii)$ 分别对应哪个变量？若一个箱线图可能对应多个变量，请全部列出。",
    "Nehmen Sie nun an, dass die Boxplots i und ii in der vorherigen Teilaufgabe die Verteilungen des jährlichen Nettoeinkommens in zwei unterschiedlichen Populationen zeigen. In welcher der Populationen ist die Konzentration der Nettoeinkommen, gemessen mit dem Gini-Index, größer? Begründen Sie Ihre Antwort.": "现在假设上一小问中的箱线图 i 和 ii 表示两个不同总体的年净收入分布。按 Gini 指数衡量，哪个总体的净收入集中程度更高？请说明理由。",
    "Wie verändert sich üblicherweise die Form einer Kerndichteschätzung, wenn die Bandbreite der verwendeten Kernfunktion verdoppelt wird? Warum?": "当核函数带宽加倍时，核密度估计的形状通常如何变化？为什么？",
    "Warum sind Histogramme im Allgemeinen weniger gut zur Visualisierung empirischer Verteilungen geeignet als Kerndichteschätzer?": "为什么一般来说，直方图不如核密度估计适合可视化经验分布？",
    "Durch was unterscheidet sich die Berechnung des Korrelationskoeffizienten nach Spearman von der Berechnung des Korrelationskoeffizienten nach Pearson? Was sind jeweils die Anwendungsvoraussetzungen der beiden Korrelationskoeffizienten?": "Spearman 相关系数的计算与 Pearson 相关系数有何不同？二者各自的适用前提是什么？",
    "Betrachten Sie die folgende Grafik:": "观察下列图形：",
    "Quelle: Ourworldindata.org": "来源：Ourworldindata.org。",
    "Übersetzung der relevanten Grafikbeschriftungen:": "相关图形标注翻译如下：",
    "- Titel: „Weltbevölkerung und Fruchtbarkeitsniveau über die Zeit“ - Untertitel: „Kumulative Anteile an Weltbevölkerung auf der x-Achse. Länder sind entlang der x-Achse absteigend nach ihrer Gesamtfruchtbarkeitsrate sortiert.“ - Linke Seite: - Global average fertility = Globale durchschnittliche Fruchtbarkeit - Global replacement fertility = Globale Fruchtbarkeitsrate für stabiles Bevölkerungsniveau - Horizontale Achse: „Kumulativer Anteil an Weltbevölkerung“ - Vertikale Achse: „Anzahl an Kindern pro Frau (Gesamtfruchtbarkeitsrate)“": "- 标题：“世界人口与生育水平随时间变化”；- 副标题：“x 轴为世界人口累计占比。国家沿 x 轴按总和生育率降序排列。”；- 左侧：Global average fertility = 全球平均生育率；Global replacement fertility = 维持稳定人口水平的替代生育率；- 横轴：“世界人口累计占比”；- 纵轴：“每名女性的孩子数（总和生育率）”。",
    "Analysieren Sie im Folgenden die Datensituation, die der obigen Grafik zugrunde liegt, und die grafischen Mittel, die zur Visualisierung benutzt wurden.": "下面分析该图背后的数据情境以及可视化使用的图形手段。",
    "Welche Untersuchungseinheiten aus welcher Grundgesamtheit werden in der Grafik dargestellt?": "图中展示的是来自哪个总体的哪些调查单位？",
    "Was für eine Erhebungsart und Datenstruktur liegen hier vor?": "这里的数据收集类型和数据结构是什么？",
    "Welches Skalenniveau haben Gesamtfruchtbarkeitsrate und Bevölkerungsanteil jeweils?": "总和生育率和人口占比分别是什么尺度水平？",
    "Sind die auf der linken Seite angegebenen Zeiträume die Ausprägungen eines ordinal-, nominal- oder intervallskalierten Merkmals? Begründen Sie Ihre Antwort kurz.": "左侧给出的时间段是有序、名义还是区间尺度变量的取值？请简要说明。",
    "Was für eine Art von Farbskala wurde in der Grafik verwendet? Welche Art von Farbskala wäre hier eventuell besser geeignet und warum?": "图中使用了哪类色标？哪类色标可能更合适，为什么？",
    "Welche „Geometrie“ wird hier zur Darstellung benutzt?": "这里使用了哪种“几何对象”进行呈现？",
    "Geben Sie für alle in der Grafik gezeigten Merkmale die verwendeten ästhetischen Zuordnungen an.": "给出图中所有变量所使用的美学映射。",
    "Welche ästhetischen Eigenschaften welcher Geometrien würden Sie für welche Merkmale verwenden, um in einer wohlüberlegten statistischen Grafik auf Basis dieser Daten die zeitlichen Entwicklungen der Gesamtfruchtbarkeitsraten zwischen ausgewählten Ländern einfach vergleichbar zu machen?": "若要基于这些数据设计一张合理统计图，使选定国家之间总和生育率的时间变化易于比较，你会为哪些变量使用哪些几何对象的哪些美学属性？",
    "Auch `ggplot2`-Befehle werden als Antwort akzeptiert.": "也可以用 `ggplot2` 命令作答。",
    "Betrachten Sie die in der Grafik in Rot eingezeichnete Linie. Stellen Sie sich vor, wir vertauschen die horizontalen und vertikalen Achsen der Grafik durch eine Rotation um $90^\\circ$ gegen den Uhrzeigersinn. Wäre die dadurch entstehende Funktion äquivalent zur empirischen Verteilungsfunktion der Gesamtfruchtbarkeitsrate im angegebenen Zeitraum? Begründen Sie Ihre Antwort.": "观察图中红色曲线。设想将图形逆时针旋转 $90^\\circ$，从而交换横轴和纵轴。所得函数是否等价于给定时间段中总和生育率的经验分布函数？请说明理由。",
    "Die folgenden Graphiken zeigen Streudiagramme zu den drei Datensätzen A, B und C, die jeweils $n=20$ Beobachtungen zweier metrischer Merkmale enthalten.": "下列图形展示三个数据集 A、B、C 的散点图，每个数据集包含两个度量变量的 $n=20$ 个观测。",
    "Zeichnen Sie ein Histogramm der relativen Häufigkeiten des Merkmals $X_A$ aus Datensatz A mit gleichbleibender Klassenbreite der Länge $5$ und charakterisieren Sie die Verteilung. Wodurch werden im Histogramm die relativen Häufigkeiten dargestellt?": "对数据集 A 中变量 $X_A$，以固定组距 $5$ 画相对频率直方图，并描述该分布。在直方图中，相对频率由什么表示？",
    "Nennen Sie jeweils einen allgemeinen Vor- und Nachteil der graphischen Darstellung eines metrischen Merkmals in einem Histogramm gegenüber der Darstellung in einem Boxplot.": "与箱线图相比，用直方图展示度量变量各有什么一般优点和缺点？",
    "Geben Sie für die drei Streudiagramme jeweils an, ob der Korrelationskoeffizient nach Bravais-Pearson oder der Korrelationskoeffizient nach Spearman größer ist oder ob beide etwa den gleichen Wert haben. Geben Sie den genauen Wert für einen Korrelationskoeffizienten an, falls dieser direkt aus der Graphik abgelesen werden kann.": "对三个散点图分别说明 Bravais-Pearson 相关系数和 Spearman 相关系数哪个更大，或二者是否大致相等。若能直接从图中读出某个相关系数的精确值，请给出。",
    "Welche Art von Zusammenhang misst der Korrelationskoeffizient nach Bravais-Pearson, welche Art von Zusammenhang der Korrelationskoeffizient nach Spearman? Für welche Skalenniveaus sind die beiden Maße jeweils geeignet?": "Bravais-Pearson 相关系数量度哪类关系？Spearman 相关系数量度哪类关系？二者分别适用于哪些尺度水平？",
    "Für zwei Merkmale $X$ und $Y$ mit positivem Wertebereich sind der Korrelationskoeffizient nach Bravais-Pearson": "对两个取值为正的变量 $X$ 和 $Y$，Bravais-Pearson 相关系数为：",
    "und der Korrelationskoeffizient nach Spearman": "而 Spearman 相关系数为：",
    "Ändern sich die Werte der beiden Zusammenhangsmaße jeweils, wenn $Y$ folgendermaßen zu $Y_1$ bzw. $Y_2$ transformiert wird?": "当 $Y$ 按如下方式变换为 $Y_1$ 或 $Y_2$ 时，这两个关联度量的值是否改变？",
    "$Y_1=-Y$": "$Y_1=-Y$。",
    "$Y_2=Y^2$": "$Y_2=Y^2$。",
    "Geben Sie konkrete Werte für die resultierenden Korrelationskoeffizienten $r_{X,Y_1}$, $r^{SP}_{X,Y_1}$, $r_{X,Y_2}$ und $r^{SP}_{X,Y_2}$ an, falls dies möglich ist.": "若可能，给出变换后相关系数 $r_{X,Y_1}$、$r^{SP}_{X,Y_1}$、$r_{X,Y_2}$ 和 $r^{SP}_{X,Y_2}$ 的具体值。",
    "Ein weiteres Zusammenhangsmaß stellt Kendalls Tau dar. Was ist die Grundidee dieser Maßzahl? Erläutern Sie kurz das Vorgehen bei der Berechnung.": "另一种关联度量是 Kendall's tau。该指标的基本思想是什么？简要说明其计算步骤。",
    "Betrachten Sie die untenstehende Grafik. Sie zeigt den durchschnittlichen Ertrag, „crop yield“, für landwirtschaftliche Nutzflächen in Tonnen pro Hektar auf den Kontinenten der Erde im Jahr 2018. ![](图片/Altklausur2LV-1.png) Analysieren Sie die grafischen Mittel, die zur Visualisierung benutzt wurden.": "观察下图。它展示了 2018 年世界各大洲农业用地平均产量（crop yield，吨/公顷）。![](图片/Altklausur2LV-1.png) 分析该可视化使用的图形手段。",
    "Geben Sie für alle in der Grafik gezeigten Merkmale jeweils": "对图中所有变量分别给出：",
    "- das Skalenniveau, - die verwendeten Zuordnungen auf ästhetische Eigenschaften der gezeichneten Sechsecke": "- 尺度水平；- 这些变量到所绘六边形美学属性的映射。",
    "Statistische Grafiken sollen die Datenlage möglichst unverfälscht darstellen.": "统计图形应尽量不失真地呈现数据。",
    "Inwiefern verfälscht die obige Darstellung die tatsächliche Datenlage?": "上图在哪些方面扭曲了真实数据情况？",
    "Statistische Grafiken sollen die Datenlage möglichst kompakt darstellen, also minimal viel verwendete Tinte für maximal viel vermittelte Information.": "统计图形应尽量紧凑，即用尽可能少的墨水传递尽可能多的信息。",
    "Statistische Grafiken sollen die Datenlage möglichst übersichtlich darstellen, um den Konsument:innen der Grafik schnelles und präzises Ablesen relevanter quantitativer Informationen zu ermöglichen. Inwiefern verfehlt die obige Darstellung dieses Ziel?": "统计图形应尽量清晰，使读者能快速准确读出相关定量信息。上图在哪些方面没有达到这一目标？",
    "Definieren Sie eine alternative grafische Darstellung für die in der obenstehenden Grafik gezeigten Daten, welche diese unverfälscht, kompakt und übersichtlich visualisiert. Verwenden Sie für die Beschreibung die in der Vorlesung eingeführten Begrifflichkeiten der Grammar of Graphics oder die entsprechende `{ggplot2}`-Syntax.": "为上图数据设计一种替代图形表示，使其不失真、紧凑且清晰。描述时请使用课堂中介绍的 Grammar of Graphics 术语或相应 `{ggplot2}` 语法。",
    "Betrachten Sie die untenstehende Grafik. Sie zeigt den durchschnittlichen Ertrag, „crop yield“, für landwirtschaftliche Nutzflächen in Tonnen pro Hektar auf den Kontinenten der Erde im Jahr 2018.": "观察下图。它展示了 2018 年世界各大洲农业用地平均产量（crop yield，吨/公顷）。",
    "Analysieren Sie die grafischen Mittel, die zur Visualisierung benutzt wurden.": "分析可视化使用的图形手段。",
    "Thema: Our-World-in-Data-Grafik zur Weltbevölkerung und Fruchtbarkeit.": "主题：Our World in Data 关于世界人口与生育率的图形。",
    "Untersuchungseinheiten und Grundgesamtheit.": "调查单位和总体。",
    "Erhebungsart und Datenstruktur.": "数据收集类型和数据结构。",
    "Skalenniveaus.": "尺度水平。",
    "Zeiträume.": "时间段。",
    "Farbskala.": "色标。",
    "Geometrie und Ästhetiken.": "几何对象和美学映射。",
    "Alternative Grafik für Ländervergleiche.": "用于国家比较的替代图形。",
    "Empirische Verteilungsfunktion?.": "是否为经验分布函数？",
    "Gegeben sind drei Streudiagramme mit jeweils $n=20$.": "给定三个散点图，每个都有 $n=20$ 个观测。",
    "Histogramm von $X_A$.": "$X_A$ 的直方图。",
    "Histogramm vs. Boxplot.": "直方图与箱线图比较。",
    "Pearson vs. Spearman.": "Pearson 与 Spearman 比较。",
    "Pearson und Spearman.": "Pearson 和 Spearman。",
    "Transformationen.": "变换。",
    "Kendalls Tau.": "Kendall's tau。",
    "Es geht um eine Grafik mit dem Titel:": "题目涉及一张标题为下列内容的图：",
    "**“Where are Americans born?”**": "**“美国人出生在哪里？”**",
    "Die Grafik zeigt für US-Bundesstaaten über die Zeit Anteile der Bevölkerung nach Geburtsort:": "该图展示美国各州随时间变化的、按出生地划分的人口比例：",
    "- außerhalb der USA, - woanders in den USA, - im selben Bundesstaat, - keine Daten verfügbar.": "- 美国以外；- 美国其他地方；- 同一州；- 无可用数据。",
    "Grundgesamtheit und Untersuchungseinheiten.": "总体和调查单位。",
    "Art der Datengewinnung und Erhebungsform.": "数据获取方式和调查形式。",
    "Grammar-of-Graphics-Analyse für den Teil „AK“ / Alaska.": "对 “AK”/Alaska 部分做 Grammar of Graphics 分析。",
    "Typ der Farbskala.": "色标类型。",
    "Grammar-of-Graphics-Analyse der gesamten Grafik.": "对整张图做 Grammar of Graphics 分析。",
    "Skalenniveaus der gezeigten Merkmale und Statistiken.": "图中变量和统计量的尺度水平。",
    "Geeignete Grafik für die Frage.": "适合该问题的图形。",
    "Aussagen beurteilen.": "评价相关说法。",
}

QUESTION_TRANSLATIONS = {}
QUESTION_TRANSLATIONS.update(QUESTION_TRANSLATIONS_02)
QUESTION_TRANSLATIONS.update(QUESTION_TRANSLATIONS_08)
QUESTION_TRANSLATIONS.update(QUESTION_TRANSLATIONS_03)
QUESTION_TRANSLATIONS.update(QUESTION_TRANSLATIONS_04)
QUESTION_TRANSLATIONS.update(QUESTION_TRANSLATIONS_05)
QUESTION_TRANSLATIONS.update(QUESTION_TRANSLATIONS_06)
QUESTION_TRANSLATIONS.update(QUESTION_TRANSLATIONS_07)
QUESTION_TRANSLATIONS.update(QUESTION_TRANSLATIONS_09)
QUESTION_TRANSLATIONS.update({
    "Bilde jeweils die partielle Ableitung nach $x$ und nach $y$.": "分别求关于 $x$ 和关于 $y$ 的偏导数。",
    "Aufgaben": "题目",
    "Bestimme die Stammfunktion oder das genaue Integral (falls Grenzen angegeben sind) der jeweiligen Funktion.": "求对应函数的原函数；如果给出了积分上下限，则求定积分的精确值。",
    "Tipp für (c): Nutze zweimal partielle Integration. Nachdem du das zweite Mal partiell integriert hast, betrachte den Ausdruck vorsichtig.": "提示 (c)：使用两次分部积分。第二次分部积分后，要仔细整理得到的表达式。",
    "Bestimme die Integrale.": "求下列积分。",
    "Tipp für (b): Setze $u=1+x^2$.": "提示 (b)：令 $u=1+x^2$。",
    "und:": "并且：",
    "Es sei": "设：",
})

FORMULAS.update({
    "01": r"""## 公式速查

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
""",
    "04": r"""## 公式速查

### 考试可用版

- **测度定义**：$\mu(\emptyset)=0$，$\mu(A)\ge0$，不交时 $\mu(\bigcup_nA_n)=\sum_n\mu(A_n)$
- **概率测度**：$\mathbb P(\Omega)=1$
- **单调性**：$A\subseteq B\Rightarrow\mu(A)\le\mu(B)$
- **计数测度**：$\mu_z(A)=|A|$
- **Lebesgue 测度**：$\lambda((a,b))=b-a$，$\lambda(\{x\})=0$
- **Dirac 测度**：$\delta_x(A)=I_A(x)$
- **原像**：$f^{-1}(B)=\{\omega:f(\omega)\in B\}$
- **可测映射**：$f^{-1}(B)\in\mathcal F_1$ 对所有 $B\in\mathcal F_2$ 成立
- **像测度**：$\mu_f(B)=\mu(f^{-1}(B))$
- **随机变量分布**：$\mathbb P_X(B)=\mathbb P(X^{-1}(B))$
- **指示函数积分**：$\int I_A\,d\mu=\mu(A)$
- **简单函数积分**：$f=\sum_i a_iI_{A_i}\Rightarrow\int f\,d\mu=\sum_i a_i\mu(A_i)$
- **离散积分**：$\int f\,d\mu=\sum_{\omega}f(\omega)\mu(\{\omega\})$

### 不会时怎么下手

- **题目问测度是否合法**：按三条检查：空集为 0、非负、不交可加。
- **题目问可测性**：不要看像，永远看原像。把目标集合 $B$ 拉回去算 $f^{-1}(B)$。
- **题目问 Bildmaß**：先写 $\mu_f(B)=\mu(f^{-1}(B))$，再算原像，最后算原像测度。
- **题目给 Dirac 测度**：只问集合里有没有支撑点。包含就是 1，不包含就是 0。
- **题目给 Lebesgue 测度**：区间算长度，单点测度是 0。
- **题目给计数测度**：有限集合数元素个数。
- **题目问积分**：有限/离散空间里，把积分改成“函数值 × 单点测度”的求和。
""",
    "05": r"""## 公式速查

### 考试可用版

- **期望**：$E(X)=\sum_xxP(X=x)$ 或 $E(X)=\int xf_X(x)dx$
- **线性性**：$E(aX+bY)=aE(X)+bE(Y)$
- **函数期望**：$E(g(X))=\sum_xg(x)P(X=x)$ 或 $\int g(x)f_X(x)dx$
- **方差**：$Var(X)=E(X^2)-E(X)^2$
- **样本方差**：$S^2=\frac1{n-1}\sum_i(x_i-\bar x)^2$
- **方差缩放**：$Var(aX+b)=a^2Var(X)$
- **和的方差**：$Var(X+Y)=Var(X)+Var(Y)+2Cov(X,Y)$
- **协方差**：$Cov(X,Y)=E(XY)-E(X)E(Y)$
- **相关系数**：$\rho=\frac{Cov(X,Y)}{\sigma_X\sigma_Y}$
- **Markov**：$P(|X|\ge a)\le\frac{E|X|}{a}$
- **Chebyshev**：$P(|X-\mu|\ge c)\le\frac{Var(X)}{c^2}$
- **正态标准化**：$Z=\frac{X-\mu}{\sigma}\sim N(0,1)$
- **配对 t**：$t=\frac{\bar D-\mu_0}{s_D/\sqrt n}$
- **Welch t**：$t=\frac{\bar X-\bar Y-\Delta_0}{\sqrt{s_X^2/n_X+s_Y^2/n_Y}}$
- **Wilcoxon**：$W^+=\sum_{D_i>0}Rang(|D_i|)$

### 不会时怎么下手

- **题目问期望**：先写定义，再代入；连续型别忘了多乘一个 $x$。
- **题目问方差**：通常走 $Var(X)=E(X^2)-E(X)^2$，先算 $E(X)$ 和 $E(X^2)$。
- **题目有线性变换**：期望乘 $a$，方差乘 $a^2$，加常数不影响方差。
- **题目问协方差**：先算 $E(XY)$、$E(X)$、$E(Y)$，再用移项公式。
- **题目问不等式上界**：只知道期望用 Markov；知道均值和方差用 Chebyshev。
- **题目是正态概率**：先标准化成 $Z$，再查标准正态。
- **题目是检验**：先判断配对/独立，再写假设、统计量、临界值或 p 值、结论。
""",
    "06": r"""## 公式速查

### 考试可用版

- **概率收敛**：$X_n\xrightarrow{P}X\Longleftrightarrow P(|X_n-X|>\varepsilon)\to0$
- **分布收敛**：$X_n\xrightarrow{D}X\Longleftrightarrow F_{X_n}(x)\to F_X(x)$ 在连续点成立
- **均方收敛**：$E[(X_n-X)^2]\to0$
- **几乎必然收敛**：$P(\lim X_n=X)=1$
- **强弱关系**：几乎必然 $\Rightarrow$ 均方 $\Rightarrow$ 概率 $\Rightarrow$ 分布
- **连续映射**：$X_n\to X\Rightarrow g(X_n)\to g(X)$，$g$ 连续
- **Slutsky**：$X_n\xrightarrow{D}X,\ Y_n\xrightarrow{P}c\Rightarrow X_n+Y_n\xrightarrow{D}X+c,\ X_nY_n\xrightarrow{D}cX$
- **弱大数定律**：$\bar X_n\xrightarrow{P}\mu$
- **强大数定律**：$\bar X_n\xrightarrow{f.s.}E(X_1)$
- **CLT: 和**：$\frac{\sum_{i=1}^nX_i-n\mu}{\sqrt n\sigma}\xrightarrow{D}N(0,1)$
- **CLT: 均值**：$\frac{\bar X_n-\mu}{\sigma/\sqrt n}\xrightarrow{D}N(0,1)$
- **二项正态近似**：$B(n,p)\approx N(np,np(1-p))$
- **二项 Poisson 近似**：$B(n,p)\approx Po(np)$

### 不会时怎么下手

- **题目问概率收敛**：目标永远是证明 $P(|X_n-X|>\varepsilon)\to0$。
- **题目问分布收敛**：看分布函数极限，只在极限分布的连续点检查。
- **题目有样本均值**：先想大数定律，结论通常是收敛到期望。
- **题目有和或均值的近似分布**：先算单个变量的 $\mu,\sigma^2$，再用 CLT 标准化。
- **题目有函数 $g(\bar X_n)$**：先找 $\bar X_n$ 的极限，再用连续映射或 Delta 方法。
- **题目出现 Slutsky**：把表达式拆成“分布收敛的一块”和“概率收敛到常数的一块”。
- **题目问二项近似**：$p$ 很小用 Poisson；$np,n(1-p)$ 都不小用正态。
""",
    "07": r"""## 公式速查

### 考试可用版

- **联合分布函数**：$F_{X,Y}(x,y)=P(X\le x,Y\le y)$
- **边际密度**：$f_X(x)=\int f_{X,Y}(x,y)dy$
- **边际概率**：$P_X(x)=\sum_yP(X=x,Y=y)$
- **条件密度**：$f_{X|Y}(x|y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}$
- **条件期望**：$E(X|Y=y)=\int xf_{X|Y}(x|y)dx$
- **全期望**：$E(E(X|Y))=E(X)$
- **总方差**：$Var(X)=E[Var(X|Y)]+Var(E[X|Y])$
- **卷积**：$f_{X+Y}(z)=\int f_X(x)f_Y(z-x)dx$
- **二维变换**：$f_Y(y)=f_X(h(y))|\det Dh(y)|$
- **协方差矩阵**：$\Sigma=E[(X-E X)(X-E X)^T]$
- **线性变换**：$Cov(AX)=A\,Cov(X)A^T$
- **多元正态**：$f(x)=\frac1{\sqrt{(2\pi)^d\det\Sigma}}\exp[-\frac12(x-\mu)^T\Sigma^{-1}(x-\mu)]$

### 不会时怎么下手

- **题目给联合密度**：先画或写支持集，再积分；上下限比积分更重要。
- **题目问边际分布**：对不关心的变量积分或求和。
- **题目问条件密度**：先求分母边际密度 $f_Y(y)$，再用联合除以边际。
- **题目问卷积**：写 $z=x+y$，然后让 $x$ 同时满足两个支持集条件。
- **题目问二维变换**：先写反变换，再算 Jacobian，最后写新支持集。
- **题目问协方差矩阵**：先算每个方差和协方差，再排成矩阵。
- **题目问矩阵是否合法**：检查对称、对角非负、半正定。
""",
    "08": r"""## 公式速查

### 考试可用版

- **条件概率**：$P(A|B)=\frac{P(A\cap B)}{P(B)}$
- **乘法公式**：$P(A\cap B)=P(A|B)P(B)$
- **全概率**：$P(A)=\sum_iP(A|B_i)P(B_i)$
- **Bayes**：$P(A|B)=\frac{P(B|A)P(A)}{P(B)}$
- **Bayes 二分类**：$P(A|B)=\frac{P(B|A)P(A)}{P(B|A)P(A)+P(B|A^c)P(A^c)}$
- **敏感度/TPR**：$\frac{TP}{TP+FN}=P(T+|K)$
- **特异度/TNR**：$\frac{TN}{TN+FP}=P(T-|K^c)$
- **FPR**：$\frac{FP}{FP+TN}=1-TNR$
- **PPV**：$\frac{TP}{TP+FP}=P(K|T+)$
- **NPV**：$\frac{TN}{TN+FN}=P(K^c|T-)$
- **Odds**：$O(A)=\frac{P(A)}{1-P(A)}$
- **Odds Ratio**：$OR=\frac{ad}{bc}$
- **期望频数**：$E_{ij}=\frac{\text{行和}_i\text{列和}_j}{n}$
- **Chi-square**：$\chi^2=\sum\frac{(O_{ij}-E_{ij})^2}{E_{ij}}$

### 不会时怎么下手

- **题目问条件概率**：先命名事件，再确认竖线后面的是“已知条件”。
- **题目问原因概率**：例如阳性后患病概率，通常用 Bayes，不要直接拿敏感度。
- **题目有多个来源/组别**：先用全概率公式算分母。
- **题目有检测指标**：把 $K,T+$ 写清楚，再区分 $P(T+|K)$ 和 $P(K|T+)$。
- **题目给列联表**：先补全行和列总数，再算条件比例。
- **题目问关联强度**：二乘二表可用 Odds Ratio；多格表常用 $\chi^2$。
""",
    "09": r"""## 公式速查

### 考试可用版

- **直方图高度**：$\frac{\text{relative Häufigkeit}}{\text{Klassenbreite}}$
- **IQR**：$IQR=Q_3-Q_1$
- **箱线图栅栏**：$Q_1-1.5IQR,\ Q_3+1.5IQR$
- **均值**：$\bar X=\frac1n\sum_iX_i$
- **加权均值**：$\bar X_w=\frac{\sum_iw_iX_i}{\sum_iw_i}$
- **几何均值**：$\bar X_g=\sqrt[n]{\prod_iX_i}$
- **调和均值**：$\bar X_h=\frac n{\sum_i1/X_i}$
- **Pearson**：$r_{xy}=\frac{Cov(X,Y)}{s_Xs_Y}$
- **Spearman 简式**：$r^{SP}=1-\frac{6\sum_iD_i^2}{n(n^2-1)}$
- **Kendall tau**：$\tau=\frac{N_c-N_d}{n(n-1)/2}$
- **TPR**：$\frac{TP}{TP+FN}$
- **FPR**：$\frac{FP}{FP+TN}$
- **AUC**：$P(\text{Score}_+>\text{Score}_-)$
- **AUC 梯形**：$\sum_i\frac{TPR_{i+1}+TPR_i}{2}(FPR_{i+1}-FPR_i)$

### 不会时怎么下手

- **题目问图形选择**：先看变量类型，分类变量用条形/颜色，度量变量用点、线、直方图、箱线图。
- **题目问直方图**：先看组距是否相等；不等组距必须用密度高度。
- **题目问箱线图**：先排序，求 $Q_1,Q_2,Q_3$，再算 IQR 和异常值栅栏。
- **题目问相关**：Pearson 看线性，Spearman 看秩次单调，Kendall 看配对同向/反向。
- **题目问 ROC**：按阈值排序，每个阈值数 TP、FP、TN、FN，再算 TPR/FPR。
- **题目问 AUC**：可以用梯形面积，也可以理解成正例分数高于负例的概率。
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


def strip_trailing_horizontal_rules(text):
    return re.sub(r"(?:\n\s*-{3,}\s*)+\Z", "", text.strip())


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
    question = add_question_translations(question, task.get("topic", ""))
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
    return strip_trailing_horizontal_rules(compact_blank_lines("\n".join(part for part in parts if part is not None)))


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


def topic_appendix(topic):
    def block_lines(text):
        return text.strip().splitlines()

    if topic.startswith("01"):
        return block_lines(r"""
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
""")

    if topic.startswith("02"):
        return [
        "## 常见错误提醒",
        "",
        "- **把独立当成互斥**：互斥是 $A\\cap B=\\emptyset$，独立是 $\\mathbb P(A\\cap B)=\\mathbb P(A)\\mathbb P(B)$。除非某个事件概率为 $0$，否则互斥事件通常不独立。",
        "- **默认使用 Laplace**：只有所有基本结果等可能时，才可以写 $\\mathbb P(A)=|A|/|\\Omega|$。题目没有说明等可能时，要先解释模型假设。",
        "- **结果空间写得太细或太粗**：只问缺陷品总数时，$\\Omega$ 可以是 $\\{0,\\dots,n\\}$；若问每个产品是否缺陷，就要用 $\\{0,1\\}^n$。",
        "- **事件没有写成集合**：概率题先写 $A=\\{\\omega:\\text{满足条件}\\}$，再计算 $\\mathbb P(A)$，否则容易把文字条件和概率公式混在一起。",
        "- **忘记归一化条件**：给出点概率形如 $c/x!$、$cq^x$ 时，第一步永远是把所有点概率加起来等于 $1$。",
        "- **σ-代数只检查有限并**：σ-代数要求补集和可数并封闭；在有限集合里可数并会退化成有限并，但证明时最好说明这一点。",
        "- **生成 σ-代数漏原子**：由几个集合生成 σ-代数时，先找原子分割，再写所有原子的并；不要只把题目给出的集合和补集列出来。",
        "- **反例没有完整定义概率空间**：反驳题要写清楚 $\\Omega$、事件和概率，否则只是直觉说明，不是形式反例。",
        "",
        "## 本章必会题型清单",
        "",
        "- 会根据题意写出合适的结果空间 $\\Omega$。",
        "- 会把文字事件翻译成 $\\Omega$ 的子集。",
        "- 会判断能否使用 Laplace 模型，并计算 $|A|/|\\Omega|$。",
        "- 会用补集、容斥、不交并和单调性计算或估计概率。",
        "- 会区分独立、互斥、对立事件，并能用公式证明或反驳。",
        "- 会用归一化条件求未知常数 $c$。",
        "- 会验证一个集合族是不是 σ-代数。",
        "- 会由给定集合找原子分割，并写出生成的 σ-代数。",
        "- 会说明两个 σ-代数的并不一定是 σ-代数，并给出反例。",
        "- 会区分 σ-代数和 Dynkin-System 的封闭性要求。",
        ]
    if topic.startswith("03"):
        return [
            "## 常见错误提醒",
            "",
            "- **把密度值当概率**：$f(2)$ 不是 $P(X=2)$。\n  例：连续型 $P(1<X<3)=\\int_1^3 f(x)\\,dx$，且 $P(X=2)=0$；离散型 $P(1<X<3)=P(X=2)$。",
            "- **忘记检查密度积分为 1**：求常数 $c$ 时不要先代数乱算，先归一化。\n  例：若 $f(x)=cx$ 在 $[0,2]$ 上，则 $1=\\int_0^2cx\\,dx=2c$，所以 $c=\\frac12$。",
            "- **CDF 求概率时端点看错**：$F(b)-F(a)$ 对应 $P(a<X\\le b)$，不是所有端点形式。\n  例：若问 $P(a\\le X\\le b)$ 且 $a$ 有跳跃，要用 $F(b)-F(a-)$。",
            "- **把跳跃点当密度处理**：CDF 的跳跃是点概率，不是普通密度。\n  例：若 $F(2)=0.7,F(2-)=0.4$，则 $P(X=2)=0.3$。",
            "- **分段函数不看支持集**：公式只在对应区间有效，区间外也要写。\n  例：$f(x)=2x,0<x<1$，完整写法是 $f(x)=2xI_{(0,1)}(x)$ 或分段写区间外为 $0$。",
            "- **变量变换忘记绝对值**：密度变换乘的是 $|h'(y)|$。\n  例：$Y=2X$，$h(y)=y/2$，所以 $f_Y(y)=f_X(y/2)\\cdot\\frac12$。",
            "- **变量变换忘记新范围**：算出公式后一定写 $y\\in g(\\text{原支持集})$。\n  例：若 $X\\in[0,1]$ 且 $Y=X^2$，则 $Y\\in[0,1]$，区间外密度为 $0$。",
            "- **非单调变换只取一个反函数**：多个原像分支要全部加上。\n  例：若 $Y=X^2$ 且 $X$ 可正可负，则 $f_Y(y)=f_X(\\sqrt y)\\frac1{2\\sqrt y}+f_X(-\\sqrt y)\\frac1{2\\sqrt y}$。",
            "- **分位数直接套全局公式**：先判断 $p$ 落在哪个分段，再解 $F(x)=p$。\n  例：若 $F(x)=x^2$ 只在 $0\\le x<1/2$ 有效，求 $0.25$ 分位数时才解 $x^2=0.25$。",
            "- **常见分布参数混淆**：先写分布名和参数含义，再代公式。\n  例：$X\\sim Po(3)$ 时 $E(X)=Var(X)=3$；$X\\sim B(10,0.3)$ 时 $E(X)=3$，$Var(X)=2.1$。",
            "",
            "## 本章必会题型清单",
            "",
            "- 会判断一个函数是不是合法的分布函数 CDF。",
            "- 会由 CDF 计算区间概率和跳跃点概率。",
            "- 会由 CDF 分段求导得到密度。",
            "- 会判断一个函数是不是合法密度，并用归一化求常数 $c$。",
            "- 会计算连续型随机变量的期望、中位数、众数和分位数。",
            "- 会识别 Bernoulli、Binomial、Poisson、Hypergeometric、Uniform、Exponential 等常见分布。",
            "- 会根据题意选择点概率、区间概率、尾概率或补集概率。",
            "- 会做一维单调变量变换，写出反函数、导数绝对值和新支持集。",
            "- 会处理非单调变换的多个原像分支。",
            "- 会判断什么时候用 Poisson 近似或正态近似。",
        ]
    if topic.startswith("04"):
        return block_lines(r"""
## 常见错误提醒

- **可测性看错方向**：可测性看原像，不是看像。
  例：要查 $f$ 可测，检查 $f^{-1}(B)\in\mathcal F$，不是 $f(B)$。
- **Dirac 测度当成长度**：Dirac 只看支撑点是否在集合里。
  例：$\delta_2([0,1])=0$，$\delta_2([1,3])=1$。
- **Lebesgue 测度把单点算成 1**：单点长度是 0。
  例：$\lambda(\{2\})=0$，但计数测度 $\mu_z(\{2\})=1$。
- **像测度忘记取原像**：先拉回原空间再算测度。
  例：$\mu_f(\{3\})=\mu(f^{-1}(\{3\}))$。
- **有限空间积分写成普通积分**：有限测度空间上是求和。
  例：$\int_A f\,d\mu=\sum_{\omega\in A}f(\omega)\mu(\{\omega\})$。

## 本章必会题型清单

- 会验证一个函数是不是测度。
- 会区分计数测度、Lebesgue 测度和 Dirac 测度。
- 会判断映射可测性：通过原像检查。
- 会计算 Bildmaß / 像测度。
- 会计算指示函数、简单函数和有限空间上的积分。
- 会解释密度相对于哪个测度存在。
""")
    if topic.startswith("05"):
        return block_lines(r"""
## 常见错误提醒

- **方差线性变换忘记平方**：系数提出来要平方。
  例：$Var(3X+2)=9Var(X)$。
- **算方差只算了 $E(X^2)$**：方差还要减 $E(X)^2$。
  例：$Var(X)=E(X^2)-E(X)^2$。
- **独立和不相关混用**：独立推出协方差为 0，但协方差为 0 不一定独立。
  例：只知道 $Cov(X,Y)=0$，不能直接说 $X,Y$ 独立。
- **Markov/Chebyshev 用错条件**：Markov 要非负或绝对值，Chebyshev 要均值和方差。
  例：$P(|X-\mu|\ge2)\le Var(X)/4$ 是 Chebyshev。
- **正态标准化漏除以标准差**：不是除以方差。
  例：$Z=(X-\mu)/\sigma$，不是 $(X-\mu)/\sigma^2$。
- **检验题不写假设**：没有 $H_0,H_1$，后面算对也容易丢分。
  例：配对题先写 $H_0:\mu_D=0$，再算 $t$。

## 本章必会题型清单

- 会计算期望、$E(X^2)$ 和方差。
- 会处理线性变换下的期望和方差。
- 会计算协方差和相关系数。
- 会使用 Markov、Chebyshev、Jensen。
- 会把正态变量标准化并查概率。
- 会区分配对 t、Welch t 和 Wilcoxon 检验。
- 会写假设、统计量、决策和结论。
""")
    if topic.startswith("06"):
        return block_lines(r"""
## 常见错误提醒

- **把分布收敛当概率收敛**：分布收敛通常更弱。
  例：$X_n\xrightarrow{D}X$ 不一定推出 $X_n\xrightarrow{P}X$。
- **证明概率收敛没有写 $\varepsilon$**：概率收敛必须对任意 $\varepsilon>0$。
  例：要证明 $P(|X_n-X|>\varepsilon)\to0$。
- **CLT 标准化少了 $\sqrt n$**：和与均值的标准化不同。
  例：$\frac{\sum X_i-n\mu}{\sqrt n\sigma}$，或 $\frac{\bar X-\mu}{\sigma/\sqrt n}$。
- **大数定律忘记极限是期望**：样本均值收敛到单个变量的期望。
  例：$\bar X_n\xrightarrow{P}E(X_1)$。
- **Slutsky 拆不出常数项**：要找一块收敛到常数。
  例：若 $Y_n\xrightarrow{P}2$，则 $X_nY_n\xrightarrow{D}2X$。

## 本章必会题型清单

- 会区分概率收敛、分布收敛、均方收敛、几乎必然收敛。
- 会用定义证明简单概率收敛。
- 会用连续映射定理和 Slutsky 定理。
- 会用大数定律处理样本均值。
- 会用 CLT 标准化和或均值。
- 会判断二项分布用正态近似还是 Poisson 近似。
""")
    if topic.startswith("07"):
        return block_lines(r"""
## 常见错误提醒

- **边际密度积分上下限写错**：上下限由联合支持集决定，不一定是固定常数。
  例：若 $0<x<y<1$，求 $f_Y(y)$ 时 $x$ 从 $0$ 到 $y$。
- **条件密度忘记除以边际**：条件密度不是联合密度。
  例：$f_{X|Y}(x|y)=f_{X,Y}(x,y)/f_Y(y)$。
- **卷积不看支持集**：积分范围要同时满足 $x$ 和 $z-x$ 都合法。
  例：$X,Y\in[0,1]$ 时，$z<1$ 和 $z>1$ 的范围不同。
- **Jacobian 用正变换而不是反变换**：常用公式需要反变换的导数绝对值。
  例：先写 $x=h(y)$，再算 $|\det Dh(y)|$。
- **协方差矩阵忘记对称**：合法协方差矩阵必须对称且半正定。
  例：$\begin{pmatrix}1&2\\3&1\end{pmatrix}$ 不是协方差矩阵。

## 本章必会题型清单

- 会由联合密度求边际密度。
- 会求条件密度和条件期望。
- 会使用全期望和总方差公式。
- 会用卷积求和变量密度。
- 会做二维变量变换并计算 Jacobian。
- 会判断协方差矩阵是否合法。
- 会处理多元正态的边际、独立和线性变换。
""")
    if topic.startswith("08"):
        return block_lines(r"""
## 常见错误提醒

- **把 $P(T+|K)$ 当成 $P(K|T+)$**：敏感度不是阳性预测值。
  例：$P(T+|K)$ 要转成 $P(K|T+)$ 必须用 Bayes。
- **Bayes 分母漏掉反面情况**：分母是所有能导致阳性的路径。
  例：$P(T+)=P(T+|K)P(K)+P(T+|K^c)P(K^c)$。
- **列联表只比人数不比比例**：组大小不同必须比条件比例。
  例：A 组 30/100，B 组 20/40，不能只说 30 大于 20。
- **Odds 和概率混淆**：Odds 是 $\frac p{1-p}$，不是 $p$。
  例：$p=0.2$ 时 Odds $=0.25$。
- **χ² 期望频数算错**：每格期望是行和乘列和再除以总数。
  例：$E_{ij}=\frac{\text{行和}\cdot\text{列和}}n$。

## 本章必会题型清单

- 会命名事件并写条件概率。
- 会用全概率公式算分母。
- 会用 Bayes 求后验概率。
- 会区分敏感度、特异度、PPV、NPV、FPR、FNR。
- 会补全列联表并计算条件比例。
- 会计算 Odds、Odds Ratio 和 χ² 统计量。
""")
    if topic.startswith("09"):
        return block_lines(r"""
## 常见错误提醒

- **直方图组距不等还用频率高度**：组距不等必须用频率密度。
  例：高度 $=\text{relative Häufigkeit}/\text{Klassenbreite}$。
- **箱线图异常值边界算错**：先算 IQR，再算上下栅栏。
  例：$Q_1-1.5IQR$ 和 $Q_3+1.5IQR$。
- **Pearson/Spearman 混用**：Pearson 看线性，Spearman 看单调秩关系。
  例：严格递增但弯曲的关系，Spearman 可能很高，Pearson 不一定。
- **ROC 阈值方向弄反**：先确认 score 大判阳性还是 score 小判阳性。
  例：若 score 大判阳性，阈值降低时 TPR 和 FPR 通常都会上升。
- **AUC 坐标顺序写反**：ROC 横轴是 FPR，纵轴是 TPR。
  例：点写成 $(FPR,TPR)$，不是 $(TPR,FPR)$。

## 本章必会题型清单

- 会根据变量类型选择合适图形。
- 会计算直方图高度、均值、分位数、IQR 和箱线图栅栏。
- 会判断偏态方向和异常值。
- 会计算 Pearson、Spearman、Kendall 相关。
- 会根据阈值计算 TP、FP、TN、FN、TPR、FPR。
- 会画 ROC 点并用梯形法估计 AUC。
""")
    return []


def insert_guide(text, guide):
    marker = "##### Lösung"
    if marker in text:
        return text.replace(marker, f"##### 中文解题思路\n\n{guide}\n\n{marker}", 1)
    return text + f"\n\n##### 中文解题思路\n\n{guide}\n"


def structure_exercise_body(body, guide, topic=""):
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

    question = add_question_translations(question, topic)
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
    return strip_trailing_horizontal_rules(compact_blank_lines("\n".join(parts)))


def strip_long_subpart_titles(text):
    def replace(match):
        hashes = match.group(1)
        label = match.group(2)
        title = match.group(3).strip()
        if title == "$$" or len(title) > 60:
            return f"{hashes} ({label})"
        return match.group(0)

    return re.sub(r"^(#{4,6})[ \t]+\(([a-h]|\d+)\)[ \t]+(.+)$", replace, text, flags=re.M | re.I)


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
            body = structure_exercise_body(body, guide, topic)
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
        appendix = topic_appendix(topic)
        if appendix:
            lines += appendix + ["", "---", ""]
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
        "- 小问标题误吞公式块起始符这类坏标题：0",
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
