from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def replace_section(text: str, number: int, title: str, content: str) -> str:
    pattern = rf"## {number}\. {re.escape(title)}\n.*?(?=\n## {number + 1}\. )"
    replacement = f"## {number}. {title}\n{content.strip()}\n\n"
    return re.sub(pattern, lambda _m: replacement, text, flags=re.S)


def apply(path: Path, parts: dict[str, str]) -> None:
    text = path.read_text(encoding="utf-8")
    text = replace_section(text, 5, "德文练习题目", parts["de_q"])
    text = replace_section(text, 6, "中文练习题目", parts["zh_q"])
    text = replace_section(text, 7, "德文练习解答", parts["de_a"])
    text = replace_section(text, 8, "中文练习解答", parts["zh_a"])
    path.write_text(text, encoding="utf-8")


EX = {
    "二": {
        "de_q": r"""
### Übung A: Laplace-Wahrscheinlichkeit in einer Bäckerei

In einer Bäckerei gibt es 5 Backbleche. Drei ungebackene Brote werden unabhängig und völlig zufällig auf die 5 Bleche verteilt. Ein Brot verbrennt, wenn es alleine auf seinem Blech liegt. Sei $B$ das Ereignis: „mindestens ein Brot verbrennt“.

1. Bestimmen Sie den Ergebnisraum und seine Größe.
2. Berechnen Sie $P(B)$.
3. Erklären Sie, warum hier eine Laplace-Rechnung möglich ist.

### Übung B: Spezialbrote auf zwei Filialen verteilen

Es gibt 8 verschiedene Spezialbrote. Sie werden auf zwei Filialen verteilt. Jede Filiale darf höchstens 7 Brote bekommen, also darf keine Filiale alle 8 Brote erhalten.

1. Wie viele verschiedene Zuteilungen sind möglich?
2. Unter den 8 Broten sind genau 3 glutenfreie Brote. Alle zulässigen Zuteilungen seien gleich wahrscheinlich. Berechnen Sie die Wahrscheinlichkeit, dass alle drei glutenfreien Brote in derselben Filiale landen.

### Übung C: Kartenziehen mit Zurücklegen

Aus einem Skatspiel mit 32 Karten werden dreimal hintereinander Karten mit Zurücklegen gezogen. Es gibt 4 Buben und 8 Herzkarten; der Herz-Bube zählt zu beiden Gruppen.

Berechnen Sie die Wahrscheinlichkeiten für:

1. höchstens einen Buben,
2. nur Herz,
3. weder Herz noch Bube.

### Übung D: Siebformel und Wahrscheinlichkeitsgrenzen

Seien $A$ und $B$ Ereignisse mit $P(A)=3/4$ und $P(B)=1/3$.

1. Zeigen Sie, dass $1/12 \le P(A\cap B)\le 1/3$ gilt.
2. Leiten Sie daraus Schranken für $P(A\cup B)$ ab.
""",
        "zh_q": r"""
### 练习 A：面包店中的拉普拉斯概率

一家面包店有 5 个烤盘。3 个未烤的面包彼此独立、完全随机地放到 5 个烤盘上。若某个面包独自位于一个烤盘上，则该面包会烤焦。设事件 $B$ 为：“至少有一个面包烤焦”。

1. 写出样本空间思想并给出样本空间大小。
2. 计算 $P(B)$。
3. 说明为什么这里可以使用拉普拉斯概率。

### 练习 B：特殊面包分配给两家分店

有 8 个互不相同的特殊面包，要分配给两家分店。每家分店最多只能拿 7 个，因此不能出现某一家拿走全部 8 个的情况。

1. 一共有多少种不同分配？
2. 其中恰好 3 个是无麸质面包。假设所有合法分配等可能，求“三个无麸质面包都落在同一家分店”的概率。

### 练习 C：有放回抽牌

从 32 张 Skat 牌中连续抽 3 次，每次抽完放回。牌中有 4 张 J，8 张红桃；红桃 J 同时属于红桃和 J。

计算：

1. 至多抽到一张 J 的概率；
2. 三张全是红桃的概率；
3. 三张都既不是红桃也不是 J 的概率。

### 练习 D：容斥公式和概率界限

设事件 $A,B$ 满足 $P(A)=3/4$、$P(B)=1/3$。

1. 证明 $1/12 \le P(A\cap B)\le 1/3$。
2. 由此推出 $P(A\cup B)$ 的上下界。
""",
        "de_a": r"""
### Lösung A

Die drei Brote können als unterscheidbare Platzierungen betrachtet werden. Jedes Brot hat 5 mögliche Bleche, also gibt es $5^3=125$ gleich wahrscheinliche Elementarereignisse.

Am einfachsten rechnen wir über das Gegenereignis $B^c$: Kein Brot verbrennt. Bei nur 3 Broten bedeutet das: Es darf kein Blech mit genau einem Brot geben. Das ist nur möglich, wenn alle 3 Brote auf demselben Blech liegen. Dafür gibt es 5 Möglichkeiten. Also

$$P(B^c)=\frac{5}{125}=\frac1{25},\qquad P(B)=1-\frac1{25}=\frac{24}{25}=0.96.$$

Laplace ist erlaubt, weil jede vollständige Zuordnung der drei Brote zu den fünf Blechen gleich wahrscheinlich ist.

### Lösung B

Eine Zuteilung ist durch die Teilmenge der Brote bestimmt, die an Filiale 1 geht. Ohne Einschränkung gäbe es $2^8=256$ Teilmengen. Verboten sind nur: Filiale 1 bekommt kein Brot und Filiale 1 bekommt alle 8 Brote. Also bleiben

$$256-2=254$$

zulässige Zuteilungen.

Für das Ereignis $S$ „alle drei glutenfreien Brote in derselben Filiale“ zählen wir günstig. Wenn alle drei glutenfreien Brote in Filiale 1 liegen, kann Filiale 1 zusätzlich beliebige der 5 normalen Brote bekommen, aber nicht alle 5, sonst bekäme Filiale 2 gar nichts. Das sind $2^5-1=31$ Möglichkeiten. Symmetrisch gibt es 31 Möglichkeiten für „alle glutenfreien Brote in Filiale 2“. Also:

$$P(S)=\frac{31+31}{254}=\frac{62}{254}=\frac{31}{127}\approx 0.24.$$

### Lösung C

Bei Ziehen mit Zurücklegen bleiben die Wahrscheinlichkeiten in jedem Zug gleich.

1. Die Wahrscheinlichkeit für einen Buben ist $4/32=1/8$. Höchstens ein Bube bedeutet 0 oder 1 Bube:

$$P=\left(\frac78\right)^3+3\cdot \frac18\left(\frac78\right)^2=\frac{343}{512}+\frac{147}{512}=\frac{245}{256}.$$

2. Herz hat Wahrscheinlichkeit $8/32=1/4$. Nur Herz in allen drei Zügen:

$$P=\left(\frac14\right)^3=\frac1{64}.$$

3. Weder Herz noch Bube: Es gibt $32-8-4+1=21$ solche Karten, weil der Herz-Bube doppelt abgezogen wurde. Also:

$$P=\left(\frac{21}{32}\right)^3.$$

### Lösung D

Immer gilt $P(A\cap B)\le P(B)=1/3$ und auch $P(A\cap B)\le P(A)$. Für die untere Schranke verwenden wir

$$P(A\cup B)=P(A)+P(B)-P(A\cap B)\le 1.$$

Daraus folgt

$$P(A\cap B)\ge P(A)+P(B)-1=\frac34+\frac13-1=\frac1{12}.$$

Also $1/12\le P(A\cap B)\le 1/3$.

Für die Vereinigung:

$$P(A\cup B)=\frac34+\frac13-P(A\cap B)=\frac{13}{12}-P(A\cap B).$$

Wenn $P(A\cap B)$ maximal $1/3$ ist, ist die Vereinigung minimal: $13/12-1/3=3/4$. Wenn $P(A\cap B)$ minimal $1/12$ ist, ist die Vereinigung maximal: $13/12-1/12=1$. Also

$$\frac34\le P(A\cup B)\le 1.$$
""",
        "zh_a": r"""
### 解答 A

把 3 个面包看成可区分的放置结果。每个面包都有 5 个烤盘可选，所以样本空间大小是 $5^3=125$。

直接算“至少一个烤焦”有点绕，改算补事件 $B^c$：没有任何面包烤焦。因为总共只有 3 个面包，如果没有烤盘上恰好只有 1 个面包，那只能是 3 个面包全在同一个烤盘上。这样的结果有 5 种。因此

$$P(B^c)=\frac{5}{125}=\frac1{25},\qquad P(B)=1-\frac1{25}=\frac{24}{25}=0.96.$$

这里能用拉普拉斯概率，是因为每一种“3 个面包分别放到哪个烤盘”的完整结果都是等可能的。

### 解答 B

一次分配可以由“哪些面包给分店 1”这个子集决定。若没有限制，共有 $2^8=256$ 个子集。题目禁止某一家拿走全部 8 个，所以要去掉“分店 1 一个都没有”和“分店 1 拿走全部 8 个”两种情况：

$$256-2=254.$$

现在算三个无麸质面包都在同一家分店。若它们都在分店 1，分店 1 还可以从 5 个普通面包中任选一些，但不能 5 个都选，否则分店 2 没有面包。因此有 $2^5-1=31$ 种。它们都在分店 2 也同理有 31 种。所以

$$P(S)=\frac{31+31}{254}=\frac{31}{127}\approx 0.24.$$

### 解答 C

有放回抽牌意味着每次抽牌概率不变。

1. 抽到 J 的概率是 $4/32=1/8$。至多一张 J = 0 张 J 或 1 张 J：

$$P=\left(\frac78\right)^3+3\cdot \frac18\left(\frac78\right)^2=\frac{245}{256}.$$

2. 抽到红桃的概率是 $8/32=1/4$，三次都是红桃：

$$P=\left(\frac14\right)^3=\frac1{64}.$$

3. 既不是红桃也不是 J 的牌数为 $32-8-4+1=21$，因为红桃 J 被重复减了一次要加回来。因此：

$$P=\left(\frac{21}{32}\right)^3.$$

### 解答 D

交集不可能比任一事件更大，所以

$$P(A\cap B)\le P(B)=1/3.$$

下界用容斥公式：

$$P(A\cup B)=P(A)+P(B)-P(A\cap B)\le 1.$$

因此

$$P(A\cap B)\ge P(A)+P(B)-1=\frac34+\frac13-1=\frac1{12}.$$

所以 $1/12\le P(A\cap B)\le 1/3$。

再由

$$P(A\cup B)=\frac34+\frac13-P(A\cap B)=\frac{13}{12}-P(A\cap B),$$

可得交集越大，并集越小。于是

$$\frac34\le P(A\cup B)\le 1.$$
""",
    },
    "三": {
        "de_q": r"""
### Übung A: Qualitätskontrolle und Bayes

Eine Fabrik produziert Smartphone-Chips mit drei Maschinen. Maschine A produziert 30%, Maschine B 45% und Maschine C 25% der Gesamtproduktion. Die Defektraten betragen: A: 1%, B: 2%, C: 3%. Sei $D$ das Ereignis „Chip ist defekt“.

1. Berechnen Sie $P(D)$.
2. Ein Chip ist defekt. Berechnen Sie $P(C\mid D)$.
3. Prüfen Sie, ob $C$ und $D$ unabhängig sind.

### Übung B: Bedingte Wahrscheinlichkeit und Vereinigung

Gegeben sind $P(A)=P(B)=1/2$ und $P(B\mid A)=1/2$.

1. Sind $A$ und $B$ unabhängig?
2. Berechnen Sie $P(A\cup B)$.

### Übung C: Alarmanlage

Eine Alarmanlage löst bei Dieben mit Wahrscheinlichkeit 0.995 Alarm aus. Bei harmlosen Kundinnen und Kunden löst sie fälschlich mit Wahrscheinlichkeit 0.006 Alarm aus. Unter 1000 Personen befinden sich im Mittel 2 Diebe.

1. Berechnen Sie die Wahrscheinlichkeit, dass ein Alarm zu Recht ausgelöst wird.
2. Berechnen Sie die Wahrscheinlichkeit, dass harmlose Personen erschreckt werden.
3. Berechnen Sie die Wahrscheinlichkeit, dass bei Alarm tatsächlich ein Diebstahl vorliegt.
""",
        "zh_q": r"""
### 练习 A：质量控制与贝叶斯公式

某工厂用三台机器生产手机芯片。机器 A 生产 30%，机器 B 生产 45%，机器 C 生产 25%。缺陷率分别为：A 为 1%，B 为 2%，C 为 3%。设 $D$ 表示“芯片有缺陷”。

1. 计算 $P(D)$。
2. 已知一个芯片有缺陷，计算它来自机器 C 的概率 $P(C\mid D)$。
3. 判断事件 $C$ 和 $D$ 是否独立。

### 练习 B：条件概率与并集

已知 $P(A)=P(B)=1/2$，且 $P(B\mid A)=1/2$。

1. 判断 $A$ 和 $B$ 是否独立。
2. 计算 $P(A\cup B)$。

### 练习 C：报警器

报警器在小偷经过时以 0.995 的概率报警；普通顾客经过时以 0.006 的概率误报。每 1000 人中平均有 2 个小偷。

1. 计算报警器“正确报警”的概率。
2. 计算“无辜顾客被吓到”的概率。
3. 已知报警，计算真的有小偷的概率。
""",
        "de_a": r"""
### Lösung A

Mit dem Satz der totalen Wahrscheinlichkeit:

$$P(D)=0.30\cdot0.01+0.45\cdot0.02+0.25\cdot0.03=0.003+0.009+0.0075=0.0195.$$

Also sind 1.95% aller Chips defekt.

Bayes:

$$P(C\mid D)=\frac{P(D\mid C)P(C)}{P(D)}=\frac{0.03\cdot0.25}{0.0195}=\frac{0.0075}{0.0195}\approx0.3846.$$

Also stammt ein defekter Chip mit etwa 38.46% Wahrscheinlichkeit von Maschine C.

Unabhängigkeit würde $P(D\mid C)=P(D)$ verlangen. Hier ist $P(D\mid C)=0.03$, aber $P(D)=0.0195$. Daher sind $C$ und $D$ nicht unabhängig.

### Lösung B

Aus $P(B\mid A)=P(A\cap B)/P(A)$ folgt:

$$P(A\cap B)=P(B\mid A)P(A)=\frac12\cdot\frac12=\frac14.$$

Da $P(A)P(B)=1/2\cdot1/2=1/4$, sind $A$ und $B$ unabhängig.

Für die Vereinigung:

$$P(A\cup B)=P(A)+P(B)-P(A\cap B)=\frac12+\frac12-\frac14=\frac34.$$

### Lösung C

Die Prävalenz ist $P(T)=2/1000=0.002$, also $P(\bar T)=0.998$. Alarm sei $A$.

Korrekt alarmiert:

$$P(A\cap T)=P(A\mid T)P(T)=0.995\cdot0.002=0.00199.$$

Harmlose erschreckt:

$$P(A\cap\bar T)=P(A\mid\bar T)P(\bar T)=0.006\cdot0.998=0.005988.$$

Gesamtwahrscheinlichkeit für Alarm:

$$P(A)=0.00199+0.005988=0.007978.$$

Gesucht ist der positive Vorhersagewert:

$$P(T\mid A)=\frac{0.00199}{0.007978}\approx0.2494.$$

Nur etwa 24.94% der Alarme betreffen tatsächlich Diebe. Der Grund ist die sehr niedrige Grundrate: Es gibt viel mehr harmlose Personen als Diebe, daher erzeugt selbst eine kleine Fehlalarmrate viele falsche Alarme.
""",
        "zh_a": r"""
### 解答 A

用全概率公式：

$$P(D)=0.30\cdot0.01+0.45\cdot0.02+0.25\cdot0.03=0.0195.$$

所以总缺陷率为 1.95%。

用贝叶斯公式：

$$P(C\mid D)=\frac{P(D\mid C)P(C)}{P(D)}=\frac{0.03\cdot0.25}{0.0195}\approx0.3846.$$

因此，已知芯片有缺陷，它来自机器 C 的概率约为 38.46%。

若 $C$ 和 $D$ 独立，应有 $P(D\mid C)=P(D)$。但这里 $P(D\mid C)=0.03$，而 $P(D)=0.0195$，不相等，所以不独立。

### 解答 B

由条件概率公式：

$$P(A\cap B)=P(B\mid A)P(A)=\frac12\cdot\frac12=\frac14.$$

又因为 $P(A)P(B)=1/4$，所以 $A$ 和 $B$ 独立。

并集：

$$P(A\cup B)=P(A)+P(B)-P(A\cap B)=\frac12+\frac12-\frac14=\frac34.$$

### 解答 C

设 $T$ 表示“小偷”，$A$ 表示“报警”。患病率/基率类似地是

$$P(T)=2/1000=0.002,\qquad P(\bar T)=0.998.$$

正确报警：

$$P(A\cap T)=0.995\cdot0.002=0.00199.$$

误报吓到普通顾客：

$$P(A\cap\bar T)=0.006\cdot0.998=0.005988.$$

报警总概率：

$$P(A)=0.00199+0.005988=0.007978.$$

已知报警，真的有小偷的概率：

$$P(T\mid A)=\frac{0.00199}{0.007978}\approx0.2494.$$

所以只有约 24.94% 的报警是真的。原因不是报警器很差，而是小偷基率太低，普通顾客数量巨大，小误报率也会产生很多误报。
""",
    },
}


EX.update({
    "十一": {
        "de_q": r"""
### Übung A: Gemeinsame Tabelle

Für zwei Zufallsvariablen $X,Y\in\{0,1\}$ sei die gemeinsame Verteilung:

| $X\backslash Y$ | 0 | 1 |
|---|---:|---:|
| 0 | 0.1 | 0.2 |
| 1 | 0.3 | 0.4 |

1. Bestimmen Sie die Randverteilungen von $X$ und $Y$.
2. Berechnen Sie $P(X=1\mid Y=1)$.
3. Prüfen Sie, ob $X$ und $Y$ unabhängig sind.
""",
        "zh_q": r"""
### 练习 A：联合分布表

两个随机变量 $X,Y\in\{0,1\}$ 的联合分布为：

| $X\backslash Y$ | 0 | 1 |
|---|---:|---:|
| 0 | 0.1 | 0.2 |
| 1 | 0.3 | 0.4 |

1. 求 $X$ 和 $Y$ 的边缘分布。
2. 计算 $P(X=1\mid Y=1)$。
3. 判断 $X$ 和 $Y$ 是否独立。
""",
        "de_a": r"""
### Lösung A

Randverteilung von $X$ über Zeilensummen:

$$P(X=0)=0.1+0.2=0.3,\qquad P(X=1)=0.3+0.4=0.7.$$

Randverteilung von $Y$ über Spaltensummen:

$$P(Y=0)=0.1+0.3=0.4,\qquad P(Y=1)=0.2+0.4=0.6.$$

Bedingte Wahrscheinlichkeit:

$$P(X=1\mid Y=1)=\frac{P(X=1,Y=1)}{P(Y=1)}=\frac{0.4}{0.6}=\frac23.$$

Für Unabhängigkeit müsste z.B. gelten:

$$P(X=1,Y=1)=P(X=1)P(Y=1)=0.7\cdot0.6=0.42.$$

Tatsächlich ist $P(X=1,Y=1)=0.4$. Also sind $X$ und $Y$ nicht unabhängig.
""",
        "zh_a": r"""
### 解答 A

对行求和得到 $X$ 的边缘分布：

$$P(X=0)=0.1+0.2=0.3,\qquad P(X=1)=0.3+0.4=0.7.$$

对列求和得到 $Y$ 的边缘分布：

$$P(Y=0)=0.1+0.3=0.4,\qquad P(Y=1)=0.2+0.4=0.6.$$

条件概率：

$$P(X=1\mid Y=1)=\frac{P(X=1,Y=1)}{P(Y=1)}=\frac{0.4}{0.6}=\frac23.$$

若独立，应有

$$P(X=1,Y=1)=P(X=1)P(Y=1)=0.7\cdot0.6=0.42.$$

但实际联合概率是 $0.4$，不相等，所以不独立。
""",
    },
    "十二": {
        "de_q": r"""
### Übung A: Gemeinsame Dichte auf einem Dreieck

Die gemeinsame Dichte von $(X,Y)$ sei $f(x,y)=2$ für $0<x<y<1$ und sonst 0.

1. Prüfen Sie, dass dies eine Dichte ist.
2. Bestimmen Sie $f_X(x)$ und $f_Y(y)$.
3. Bestimmen Sie $f_{X\mid Y=y}(x)$.

### Übung B: Summe zweier Bernoulli-Variablen

Seien $X,Y$ unabhängig mit $P(X=1)=p$ und $P(Y=1)=q$.

Bestimmen Sie die Verteilung von $S=X+Y$.
""",
        "zh_q": r"""
### 练习 A：三角区域上的联合密度

$(X,Y)$ 的联合密度为：当 $0<x<y<1$ 时 $f(x,y)=2$，其他地方为 0。

1. 检查这是合法密度。
2. 求 $f_X(x)$ 和 $f_Y(y)$。
3. 求条件密度 $f_{X\mid Y=y}(x)$。

### 练习 B：两个 Bernoulli 变量之和

设 $X,Y$ 独立，且 $P(X=1)=p$、$P(Y=1)=q$。

求 $S=X+Y$ 的分布。
""",
        "de_a": r"""
### Lösung A

Nichtnegativität ist klar. Normierung:

$$\int_0^1\int_0^y 2\,dx\,dy=\int_0^1 2y\,dy=1.$$

Also ist $f$ eine Dichte.

Für $X=x$ gilt wegen $x<y<1$:

$$f_X(x)=\int_x^1 2\,dy=2(1-x),\quad 0<x<1.$$

Für $Y=y$ gilt $0<x<y$:

$$f_Y(y)=\int_0^y 2\,dx=2y,\quad 0<y<1.$$

Die bedingte Dichte ist

$$f_{X\mid Y=y}(x)=\frac{f(x,y)}{f_Y(y)}=\frac{2}{2y}=\frac1y,\quad 0<x<y.$$

### Lösung B

$S$ kann die Werte 0, 1, 2 annehmen.

$$P(S=0)=P(X=0,Y=0)=(1-p)(1-q).$$

$$P(S=1)=P(X=1,Y=0)+P(X=0,Y=1)=p(1-q)+(1-p)q.$$

$$P(S=2)=P(X=1,Y=1)=pq.$$

Das ist die Faltung zweier unabhängiger Bernoulli-Verteilungen.
""",
        "zh_a": r"""
### 解答 A

非负性显然成立。归一化：

$$\int_0^1\int_0^y 2\,dx\,dy=\int_0^1 2y\,dy=1.$$

所以这是合法密度。

对 $X=x$，因为 $x<y<1$：

$$f_X(x)=\int_x^1 2\,dy=2(1-x),\quad 0<x<1.$$

对 $Y=y$，因为 $0<x<y$：

$$f_Y(y)=\int_0^y 2\,dx=2y,\quad 0<y<1.$$

条件密度为

$$f_{X\mid Y=y}(x)=\frac{f(x,y)}{f_Y(y)}=\frac{2}{2y}=\frac1y,\quad 0<x<y.$$

### 解答 B

$S=X+Y$ 可取 $0,1,2$。

$$P(S=0)=(1-p)(1-q).$$

$$P(S=1)=p(1-q)+(1-p)q.$$

$$P(S=2)=pq.$$

这就是两个独立 Bernoulli 分布求和的卷积。
""",
    },
    "十四": {
        "de_q": r"""
### Übung A: Diagnostischer Score und Cutoffs

Sechs Personen haben folgenden Score und Krankheitsstatus:

| Person | Score | Status |
|---|---:|---|
| 1 | 90 | krank |
| 2 | 80 | krank |
| 3 | 70 | gesund |
| 4 | 60 | krank |
| 5 | 40 | gesund |
| 6 | 20 | gesund |

Ein Test ist positiv, wenn der Score mindestens $c$ beträgt.

1. Berechnen Sie Sensitivität und Spezifität für $c=80$.
2. Berechnen Sie Sensitivität und Spezifität für $c=70$.
3. Berechnen Sie Sensitivität und Spezifität für $c=60$.
4. Welcher Cutoff wäre sinnvoll, wenn falsch negative Fälle besonders gefährlich sind?

### Übung B: Kausalität

In einer Befragung zeigt sich: Personen, die Kopfschmerztabletten genommen haben, berichten häufiger Kopfschmerzen am Abend.

1. Darf man daraus schließen, dass die Tabletten Kopfschmerzen verursachen?
2. Nennen Sie eine plausible alternative Erklärung.
""",
        "zh_q": r"""
### 练习 A：诊断评分和阈值

六个人的评分和真实状态如下：

| 人 | 评分 | 状态 |
|---|---:|---|
| 1 | 90 | 有病 |
| 2 | 80 | 有病 |
| 3 | 70 | 健康 |
| 4 | 60 | 有病 |
| 5 | 40 | 健康 |
| 6 | 20 | 健康 |

若评分至少为 $c$，测试判为阳性。

1. 计算 $c=80$ 时的灵敏度和特异度。
2. 计算 $c=70$ 时的灵敏度和特异度。
3. 计算 $c=60$ 时的灵敏度和特异度。
4. 如果假阴性特别危险，哪个阈值更合理？

### 练习 B：因果判断

某调查发现：服用头痛药的人，晚上报告头痛的比例更高。

1. 能否直接得出“头痛药导致头痛”？
2. 给出一个合理的替代解释。
""",
        "de_a": r"""
### Lösung A

Es gibt 3 Kranke und 3 Gesunde.

Bei $c=80$ sind Personen 1 und 2 positiv. Beide sind krank. Person 4 ist krank, aber negativ. Also $TP=2$, $FN=1$, $FP=0$, $TN=3$.

$$Sensitivität=2/3,\qquad Spezifität=3/3=1.$$

Bei $c=70$ sind Personen 1,2,3 positiv. Davon sind 1 und 2 krank, 3 ist gesund. Person 4 ist krank, aber negativ. Also $TP=2$, $FN=1$, $FP=1$, $TN=2$.

$$Sensitivität=2/3,\qquad Spezifität=2/3.$$

Bei $c=60$ sind Personen 1,2,3,4 positiv. Alle Kranken werden erkannt, aber Person 3 ist falsch positiv. Also $TP=3$, $FN=0$, $FP=1$, $TN=2$.

$$Sensitivität=1,\qquad Spezifität=2/3.$$

Wenn falsch negative Fälle besonders gefährlich sind, ist $c=60$ sinnvoller, weil die Sensitivität 1 ist und niemand Krankes übersehen wird.

### Lösung B

Nein. Die beobachtete Assoziation beweist keine Kausalität. Eine plausible alternative Erklärung ist Confounding durch ursprüngliche Beschwerden: Menschen nehmen Kopfschmerztabletten gerade deshalb, weil sie bereits Kopfschmerzen haben oder dazu neigen. Dann verursacht nicht die Tablette den Kopfschmerz, sondern der ursprüngliche Kopfschmerz erklärt sowohl Tabletteneinnahme als auch spätere Beschwerden.
""",
        "zh_a": r"""
### 解答 A

共有 3 个有病者和 3 个健康者。

$c=80$ 时，1 和 2 判阳性，二者都有病；4 有病但被判阴性。所以 $TP=2$，$FN=1$，$FP=0$，$TN=3$。

$$灵敏度=2/3,\qquad 特异度=1.$$

$c=70$ 时，1、2、3 判阳性，其中 1、2 有病，3 健康；4 有病但阴性。所以 $TP=2$，$FN=1$，$FP=1$，$TN=2$。

$$灵敏度=2/3,\qquad 特异度=2/3.$$

$c=60$ 时，1、2、3、4 判阳性，所有病人都被识别，但 3 是假阳性。所以 $TP=3$，$FN=0$，$FP=1$，$TN=2$。

$$灵敏度=1,\qquad 特异度=2/3.$$

如果假阴性特别危险，应更倾向 $c=60$，因为它没有漏诊，灵敏度为 1。

### 解答 B

不能直接说头痛药导致头痛。这里可能有混杂或反向因果：人们正是因为已经头痛或容易头痛，才会吃头痛药。因此原本的头痛倾向同时解释了“吃药”和“晚上仍报告头痛”，不能把观察到的关联直接解释成药物导致头痛。
""",
    },
})
EX.update({
    "六": {
        "de_q": r"""
### Übung A: Grammar of Graphics an einer Heatmap

Eine Grafik zeigt für 50 Bundesstaaten und die Jahre 1930 bis 2000 die Masern-Inzidenz. Jede Zelle ist ein Bundesstaat-Jahr-Paar. Die x-Achse zeigt Jahre, die y-Achse Bundesstaaten, die Farbe zeigt die Inzidenz.

1. Was ist die Untersuchungseinheit?
2. Welche Merkmale werden dargestellt?
3. Welche Geometrie wird verwendet?
4. Welche ästhetischen Mappings liegen vor?
5. Was kann man gut und was schlecht aus dieser Grafik ablesen?
""",
        "zh_q": r"""
### 练习 A：用图形语法分析热图

某图展示 50 个州在 1930 到 2000 年间的麻疹发病率。每个小格代表一个“州-年份”组合。横轴是年份，纵轴是州，颜色表示发病率。

1. 研究单位是什么？
2. 展示了哪些变量？
3. 使用了什么几何对象？
4. 有哪些美学映射？
5. 这张图适合读出什么，不适合读出什么？
""",
        "de_a": r"""
### Lösung A

Die Untersuchungseinheit ist ein Bundesstaat in einem bestimmten Jahr. Es geht also nicht nur um Bundesstaaten und nicht nur um Jahre, sondern um Paare aus Bundesstaat und Jahr.

Dargestellte Merkmale sind: Jahr, Bundesstaat und Masern-Inzidenz. Jahr wird auf die x-Position gemappt, Bundesstaat auf die y-Position, Inzidenz auf Farbe. Die Geometrie besteht aus Rechtecken bzw. Kacheln.

Gut erkennbar sind Muster über die Zeit, Unterschiede zwischen Bundesstaaten und abrupte Veränderungen, etwa nach Einführung einer Impfung. Schlecht ablesbar sind exakte Zahlenwerte, weil Farbe weniger präzise ist als Position oder Länge. Dafür bräuchte man Tabellen, Labels oder interaktive Abfrage.
""",
        "zh_a": r"""
### 解答 A

研究单位是“某个州在某一年”这个组合，而不是单独一个州，也不是单独一年。

展示的变量有：年份、州、麻疹发病率。年份映射到横轴位置，州映射到纵轴位置，发病率映射到颜色。几何对象是一个个矩形小格。

这张图适合看时间趋势、州之间差异、以及例如疫苗引入后是否出现明显下降。不适合精确读出某个格子的具体数值，因为颜色不如位置或长度精确。若要精确值，需要表格、标签或交互查看。
""",
    },
    "七": {
        "de_q": r"""
### Übung A: Farbskalen auswählen

Wählen Sie eine passende Farbskala und begründen Sie kurz:

1. Parteizugehörigkeit: A, B, C, D.
2. Einkommen von niedrig bis hoch.
3. Temperaturabweichung vom langjährigen Mittel: negativ, null, positiv.

### Übung B: Diagrammwahl

Für jede Fragestellung wählen Sie einen geeigneten Grafiktyp:

1. Häufigkeit der Verkehrsmittel von Studierenden.
2. Verteilung von Körpergrößen.
3. Zusammenhang zwischen Lernzeit und Klausurpunktzahl.

### Übung C: KDE und Bandbreite

Erklären Sie, was bei einer Kerndichteschätzung passiert, wenn die Bandbreite zu klein oder zu groß gewählt wird.
""",
        "zh_q": r"""
### 练习 A：选择色阶

为以下变量选择合适色阶并简要说明：

1. 政党类别：A、B、C、D。
2. 收入从低到高。
3. 气温相对长期平均值的偏差：负、零、正。

### 练习 B：选择图形

为每个问题选择合适图形：

1. 学生上学交通方式的频数。
2. 身高分布。
3. 学习时间和考试分数之间的关系。

### 练习 C：核密度估计和带宽

解释核密度估计中带宽过小或过大分别会发生什么。
""",
        "de_a": r"""
### Lösung A

Parteizugehörigkeit ist nominal ohne natürliche Ordnung, also qualitative Farbskala. Einkommen hat eine Richtung von niedrig nach hoch, also sequentielle Farbskala. Temperaturabweichung hat einen sinnvollen Mittelpunkt 0; negative und positive Abweichungen sollen unterscheidbar sein, also divergierende Farbskala.

### Lösung B

Verkehrsmittel sind kategoriale Häufigkeiten, daher Balkendiagramm. Körpergröße ist metrisch, daher Histogramm, Boxplot oder Dichteplot. Lernzeit und Klausurpunktzahl sind zwei metrische Variablen, daher Streudiagramm.

### Lösung C

Bei zu kleiner Bandbreite wird die Dichte zu zackig: Zufälliges Rauschen wirkt wie echte Struktur. Bei zu großer Bandbreite wird zu stark geglättet: echte Gipfel, Schiefe oder Gruppen können verschwinden. Eine gute Bandbreite zeigt die grobe Form, ohne jedes einzelne Datenrauschen zu überbetonen.
""",
        "zh_a": r"""
### 解答 A

政党类别是无顺序类别，用定性色阶。收入有从低到高的方向，用顺序色阶。气温偏差围绕 0，有正负两边，用发散色阶。

### 解答 B

交通方式是类别频数，适合条形图。身高是度量变量，适合直方图、箱线图或密度图。学习时间和考试分数是两个度量变量，适合散点图。

### 解答 C

带宽太小，密度曲线会很抖，把随机噪声看成真实结构。带宽太大，曲线会过度平滑，真实峰值、偏态或分组可能被抹掉。合适带宽应保留主要形状，同时不过分追随每个数据点。
""",
    },
    "九": {
        "de_q": r"""
### Übung A: Erwartungswert und Varianz

Eine Zufallsvariable $X$ nimmt die Werte $0,1,2$ mit Wahrscheinlichkeiten $0.2,0.5,0.3$ an.

1. Berechnen Sie $E(X)$.
2. Berechnen Sie $E(X^2)$ und $Var(X)$.
3. Berechnen Sie $Var(3X+2)$.

### Übung B: Lorenzkurve

Vier Personen haben Einkommen $1,1,2,6$.

1. Berechnen Sie die kumulierten Bevölkerungsanteile.
2. Berechnen Sie die kumulierten Einkommensanteile.
3. Interpretieren Sie die Lorenzkurve qualitativ.
""",
        "zh_q": r"""
### 练习 A：期望和方差

随机变量 $X$ 取值 $0,1,2$，概率分别为 $0.2,0.5,0.3$。

1. 计算 $E(X)$。
2. 计算 $E(X^2)$ 和 $Var(X)$。
3. 计算 $Var(3X+2)$。

### 练习 B：洛伦兹曲线

四个人的收入为 $1,1,2,6$。

1. 计算累计人口比例。
2. 计算累计收入比例。
3. 定性解释洛伦兹曲线。
""",
        "de_a": r"""
### Lösung A

$$E(X)=0\cdot0.2+1\cdot0.5+2\cdot0.3=1.1.$$

$$E(X^2)=0^2\cdot0.2+1^2\cdot0.5+2^2\cdot0.3=1.7.$$

Also

$$Var(X)=E(X^2)-E(X)^2=1.7-1.1^2=0.49.$$

Für lineare Transformationen gilt:

$$Var(3X+2)=3^2Var(X)=9\cdot0.49=4.41.$$

### Lösung B

Die Einkommen sind schon sortiert. Gesamtbetrag: $1+1+2+6=10$. Kumulierte Bevölkerungsanteile:

$$0,\;1/4,\;2/4,\;3/4,\;1.$$

Kumulierte Einkommensanteile:

$$0,\;1/10,\;2/10,\;4/10,\;1.$$

Die unteren 75% der Personen besitzen nur 40% des Einkommens; die oberste Person besitzt 60%. Die Lorenzkurve liegt daher deutlich unter der Gleichverteilungslinie: Es gibt spürbare Konzentration.
""",
        "zh_a": r"""
### 解答 A

$$E(X)=0\cdot0.2+1\cdot0.5+2\cdot0.3=1.1.$$

$$E(X^2)=0^2\cdot0.2+1^2\cdot0.5+2^2\cdot0.3=1.7.$$

所以

$$Var(X)=E(X^2)-E(X)^2=1.7-1.1^2=0.49.$$

线性变换下方差只受乘数影响：

$$Var(3X+2)=3^2Var(X)=4.41.$$

### 解答 B

收入已经排序，总收入为 10。累计人口比例为

$$0,\;1/4,\;2/4,\;3/4,\;1.$$

累计收入比例为

$$0,\;1/10,\;2/10,\;4/10,\;1.$$

最下面 75% 的人只拥有 40% 收入，最高收入者拥有 60%。所以洛伦兹曲线明显低于完全平等线，说明收入集中度较高。
""",
    },
})
EX.update({
    "四": {
        "de_q": r"""
### Übung A: Kontingenztafel vollständig auswerten

In einer Kundenbefragung werden Alter $X$ und Zufriedenheit $Y$ erhoben. Die absolute Häufigkeitstabelle lautet:

| Alter | zufrieden | unzufrieden | Summe |
|---|---:|---:|---:|
| unter 30 | 42 | 18 | 60 |
| 30 bis 50 | 70 | 30 | 100 |
| über 50 | 63 | 27 | 90 |
| Summe | 175 | 75 | 250 |

1. Berechnen Sie $h_{21}$, $f_{2\bullet}$ und $f(Y=\text{unzufrieden}\mid X=\text{30 bis 50})$.
2. Berechnen Sie die Odds „zufrieden statt unzufrieden“ für unter 30-Jährige.
3. Berechnen Sie das Odds Ratio für „unzufrieden statt zufrieden“ zwischen unter 30 und 30 bis 50.
4. Prüfen Sie, ob Alter und Zufriedenheit empirisch unabhängig wirken.
""",
        "zh_q": r"""
### 练习 A：完整分析列联表

一次客户调查记录年龄 $X$ 和满意度 $Y$。绝对频数表如下：

| 年龄 | 满意 | 不满意 | 合计 |
|---|---:|---:|---:|
| 30 岁以下 | 42 | 18 | 60 |
| 30 到 50 岁 | 70 | 30 | 100 |
| 50 岁以上 | 63 | 27 | 90 |
| 合计 | 175 | 75 | 250 |

1. 计算 $h_{21}$、$f_{2\bullet}$ 和 $f(Y=\text{不满意}\mid X=\text{30 到 50 岁})$。
2. 计算 30 岁以下人群“满意相对于不满意”的赔率。
3. 计算 30 岁以下与 30 到 50 岁人群之间“不满意相对于满意”的赔率比。
4. 判断年龄和满意度是否表现为经验独立。
""",
        "de_a": r"""
### Lösung A

$h_{21}$ ist die absolute Häufigkeit in Zeile 2, Spalte 1, also $70$. Die relative Zeilensumme der zweiten Zeile ist

$$f_{2\bullet}=\frac{100}{250}=0.4.$$

Die bedingte relative Häufigkeit für Unzufriedenheit innerhalb der Gruppe 30 bis 50 ist

$$f(Y=\text{unzufrieden}\mid X=\text{30 bis 50})=\frac{30}{100}=0.3.$$

Odds „zufrieden statt unzufrieden“ für unter 30:

$$\frac{42}{18}=\frac73\approx2.33.$$

Das heißt: In dieser Gruppe kommen auf eine unzufriedene Person etwa 2.33 zufriedene Personen.

Odds „unzufrieden statt zufrieden“: unter 30 ist $18/42=3/7$, bei 30 bis 50 ist $30/70=3/7$. Das Odds Ratio ist

$$\frac{18/42}{30/70}=1.$$

Die Gruppen haben in diesem Beispiel dieselben Zufriedenheitsanteile: $42/60=70/100=63/90=0.7$. Daher wirken Alter und Zufriedenheit empirisch unabhängig.
""",
        "zh_a": r"""
### 解答 A

$h_{21}$ 是第 2 行第 1 列的绝对频数，即 $70$。第 2 行的相对边际频率为

$$f_{2\bullet}=\frac{100}{250}=0.4.$$

30 到 50 岁组内部不满意比例为

$$f(Y=\text{不满意}\mid X=\text{30 到 50 岁})=\frac{30}{100}=0.3.$$

30 岁以下“满意相对于不满意”的赔率为

$$\frac{42}{18}=\frac73\approx2.33.$$

含义：在 30 岁以下人群中，每 1 个不满意者大约对应 2.33 个满意者。

“不满意相对于满意”的赔率：30 岁以下为 $18/42=3/7$，30 到 50 岁为 $30/70=3/7$。赔率比为

$$\frac{18/42}{30/70}=1.$$

各年龄组满意比例都是 $0.7$，不满意比例都是 $0.3$，所以这个例子中年龄和满意度表现为经验独立。
""",
    },
    "五": {
        "de_q": r"""
### Übung A: Diskrete Zufallsvariable

Eine Zufallsvariable $X$ nimmt die Werte $0,1,2$ mit $P(X=0)=0.2$, $P(X=1)=0.5$, $P(X=2)=0.3$ an.

1. Prüfen Sie, ob dies eine Wahrscheinlichkeitsfunktion ist.
2. Bestimmen Sie die Verteilungsfunktion $F_X(x)$.
3. Berechnen Sie $P(0<X\le2)$.

### Übung B: Empirische Verteilungsfunktion

Gegeben sind die Daten $3,1,4,1,5$.

1. Sortieren Sie die Daten.
2. Bestimmen Sie die empirische Verteilungsfunktion bei $z=1$, $z=3$ und $z=4.5$.
""",
        "zh_q": r"""
### 练习 A：离散随机变量

随机变量 $X$ 取值 $0,1,2$，且 $P(X=0)=0.2$，$P(X=1)=0.5$，$P(X=2)=0.3$。

1. 检查这是否是合法概率函数。
2. 写出分布函数 $F_X(x)$。
3. 计算 $P(0<X\le2)$。

### 练习 B：经验分布函数

给定数据 $3,1,4,1,5$。

1. 将数据排序。
2. 计算经验分布函数在 $z=1$、$z=3$ 和 $z=4.5$ 处的值。
""",
        "de_a": r"""
### Lösung A

Alle Wahrscheinlichkeiten sind nichtnegativ und

$$0.2+0.5+0.3=1.$$

Also ist die Wahrscheinlichkeitsfunktion gültig.

Die Verteilungsfunktion lautet:

$$F_X(x)=\begin{cases}
0,&x<0,\\
0.2,&0\le x<1,\\
0.7,&1\le x<2,\\
1,&x\ge2.
\end{cases}$$

Weiter:

$$P(0<X\le2)=P(X=1)+P(X=2)=0.5+0.3=0.8.$$

### Lösung B

Sortiert: $1,1,3,4,5$. Die empirische Verteilungsfunktion ist der Anteil der Beobachtungen mit $x_i\le z$.

Bei $z=1$: zwei von fünf Beobachtungen sind $\le1$, also $\hat F(1)=2/5=0.4$.

Bei $z=3$: drei von fünf Beobachtungen sind $\le3$, also $\hat F(3)=3/5=0.6$.

Bei $z=4.5$: vier von fünf Beobachtungen sind $\le4.5$, also $\hat F(4.5)=4/5=0.8$.
""",
        "zh_a": r"""
### 解答 A

三个概率都非负，并且

$$0.2+0.5+0.3=1.$$

所以这是合法概率函数。

分布函数为

$$F_X(x)=\begin{cases}
0,&x<0,\\
0.2,&0\le x<1,\\
0.7,&1\le x<2,\\
1,&x\ge2.
\end{cases}$$

并且

$$P(0<X\le2)=P(X=1)+P(X=2)=0.8.$$

### 解答 B

排序后：$1,1,3,4,5$。经验分布函数就是“不超过 $z$ 的样本比例”。

$z=1$ 时，有 2 个观测不超过 1，所以 $\hat F(1)=2/5=0.4$。

$z=3$ 时，有 3 个观测不超过 3，所以 $\hat F(3)=3/5=0.6$。

$z=4.5$ 时，有 4 个观测不超过 4.5，所以 $\hat F(4.5)=4/5=0.8$。
""",
    },
    "十三": {
        "de_q": r"""
### Übung A: Kovarianz und Pearson-Korrelation

Gegeben sind vier Beobachtungspaare: $(1,1),(2,2),(3,2),(4,5)$.

1. Berechnen Sie die Mittelwerte von $X$ und $Y$.
2. Berechnen Sie die empirische Kovarianz mit Nenner $n$.
3. Berechnen Sie Pearson-$r$.

### Übung B: Rangkorrelation

Verwenden Sie dieselben Daten. Die Ränge von $X$ sind $1,2,3,4$. Für $Y=(1,2,2,5)$ verwenden Sie die Midranks $1,2.5,2.5,4$.

1. Berechnen Sie Spearman-$r$ als Pearson-Korrelation der Ränge.
2. Erklären Sie, warum Spearman hier höher als Pearson sein kann.
""",
        "zh_q": r"""
### 练习 A：协方差和 Pearson 相关

给定四个观测对：$(1,1),(2,2),(3,2),(4,5)$。

1. 计算 $X$ 和 $Y$ 的均值。
2. 用分母 $n$ 计算经验协方差。
3. 计算 Pearson 相关系数 $r$。

### 练习 B：秩相关

使用同一组数据。$X$ 的秩为 $1,2,3,4$。对 $Y=(1,2,2,5)$ 使用平均秩 $1,2.5,2.5,4$。

1. 把 Spearman 相关看成秩的 Pearson 相关来计算。
2. 解释为什么 Spearman 可能高于 Pearson。
""",
        "de_a": r"""
### Lösung A

Mittelwerte:

$$\bar x=(1+2+3+4)/4=2.5,\qquad \bar y=(1+2+2+5)/4=2.5.$$

Zentrierte Werte: $X-\bar x=(-1.5,-0.5,0.5,1.5)$ und $Y-\bar y=(-1.5,-0.5,-0.5,2.5)$. Produkte:

$$2.25,\;0.25,\;-0.25,\;3.75.$$

Summe $=6$, also Kovarianz mit Nenner $n$:

$$cov_n(X,Y)=6/4=1.5.$$

Varianzen:

$$Var_n(X)=1.25,\qquad Var_n(Y)=2.25.$$

Damit

$$r=\frac{1.5}{\sqrt{1.25}\sqrt{2.25}}\approx0.89.$$

### Lösung B

Ränge: $R_X=(1,2,3,4)$, $R_Y=(1,2.5,2.5,4)$. Beide Rangmittelwerte sind $2.5$. Die Rangkovarianz ist

$$\frac{2.25+0+0+2.25}{4}=1.125.$$

Die Rangvarianzen sind $1.25$ und $1.125$. Also

$$r_S=\frac{1.125}{\sqrt{1.25}\sqrt{1.125}}\approx0.95.$$

Spearman kann höher sein, weil die Beziehung fast monoton ist: Größere $X$-Werte gehen im Allgemeinen mit größeren $Y$-Rängen einher. Pearson wird stärker von der konkreten metrischen Form und vom Sprung auf $Y=5$ beeinflusst.
""",
        "zh_a": r"""
### 解答 A

均值：

$$\bar x=2.5,\qquad \bar y=2.5.$$

中心化后：

$$X-\bar x=(-1.5,-0.5,0.5,1.5),$$

$$Y-\bar y=(-1.5,-0.5,-0.5,2.5).$$

乘积为 $2.25,0.25,-0.25,3.75$，和为 6，所以

$$cov_n(X,Y)=6/4=1.5.$$

方差为

$$Var_n(X)=1.25,\qquad Var_n(Y)=2.25.$$

因此

$$r=\frac{1.5}{\sqrt{1.25}\sqrt{2.25}}\approx0.89.$$

### 解答 B

秩为 $R_X=(1,2,3,4)$，$R_Y=(1,2.5,2.5,4)$。两个秩均值都是 $2.5$。秩协方差为

$$\frac{2.25+0+0+2.25}{4}=1.125.$$

秩方差分别为 $1.25$ 和 $1.125$，所以

$$r_S=\frac{1.125}{\sqrt{1.25}\sqrt{1.125}}\approx0.95.$$

Spearman 更高，是因为这组数据整体几乎单调上升。Pearson 更受具体数值距离影响，尤其受 $Y=5$ 这个跳跃影响。
""",
    },
})
EX.update({
    "八": {
        "de_q": r"""
### Übung A: Lage und Streuung vollständig berechnen

Gegeben sind die fünf Beobachtungen $2,4,4,6,9$.

1. Berechnen Sie arithmetisches Mittel, Median und Modus.
2. Berechnen Sie Spannweite, empirische Varianz mit Nenner $n$ und Standardabweichung.
3. Erklären Sie, warum der Mittelwert größer als der Median ist.

### Übung B: Geometrisches Mittel

Ein Umsatz wächst in drei Jahren mit den Faktoren $1.10$, $0.80$ und $1.25$.

1. Berechnen Sie den gesamten Wachstumsfaktor.
2. Berechnen Sie den konstanten jährlichen Wachstumsfaktor, der denselben Gesamteffekt hätte.
""",
        "zh_q": r"""
### 练习 A：完整计算位置和离散程度

给定五个观测值 $2,4,4,6,9$。

1. 计算算术平均数、中位数和众数。
2. 计算极差、以 $n$ 为分母的经验方差和标准差。
3. 解释为什么均值大于中位数。

### 练习 B：几何平均

某营业额三年的增长因子分别为 $1.10$、$0.80$ 和 $1.25$。

1. 计算总增长因子。
2. 计算每年都使用同一个增长因子时，能产生同样总效果的那个因子。
""",
        "de_a": r"""
### Lösung A

Sortiert: $2,4,4,6,9$. Mittelwert:

$$\bar x=\frac{2+4+4+6+9}{5}=5.$$

Median ist der mittlere Wert, also $4$. Der Modus ist ebenfalls $4$, weil dieser Wert am häufigsten vorkommt.

Spannweite:

$$9-2=7.$$

Abweichungen vom Mittelwert $5$: $-3,-1,-1,1,4$. Quadrate: $9,1,1,1,16$, Summe $28$. Mit Nenner $n=5$:

$$s_n^2=\frac{28}{5}=5.6,\qquad s_n=\sqrt{5.6}\approx2.37.$$

Der Mittelwert ist größer als der Median, weil der hohe Wert 9 den Mittelwert nach rechts zieht. Der Median reagiert viel schwächer auf diesen rechten Randwert.

### Lösung B

Gesamter Faktor:

$$1.10\cdot0.80\cdot1.25=1.10.$$

Der konstante jährliche Faktor $g$ erfüllt $g^3=1.10$, also

$$g=\sqrt[3]{1.10}\approx1.0323.$$

Das entspricht etwa 3.23% durchschnittlichem Wachstum pro Jahr. Hier ist das geometrische Mittel richtig, weil Wachstumsfaktoren multiplikativ wirken.
""",
        "zh_a": r"""
### 解答 A

排序后为 $2,4,4,6,9$。均值：

$$\bar x=\frac{2+4+4+6+9}{5}=5.$$

中位数是中间的值，即 $4$。众数也是 $4$，因为它出现次数最多。

极差：

$$9-2=7.$$

相对均值 5 的偏差为 $-3,-1,-1,1,4$，平方为 $9,1,1,1,16$，平方和为 28。因此

$$s_n^2=\frac{28}{5}=5.6,\qquad s_n=\sqrt{5.6}\approx2.37.$$

均值大于中位数，是因为右侧较大的值 9 把均值向右拉。中位数只看排序中的中间位置，所以受这个极端值影响较小。

### 解答 B

总增长因子：

$$1.10\cdot0.80\cdot1.25=1.10.$$

设每年固定增长因子为 $g$，则 $g^3=1.10$，所以

$$g=\sqrt[3]{1.10}\approx1.0323.$$

这表示平均每年约增长 3.23%。这里必须用几何平均，因为增长因子是相乘的，不是相加的。
""",
    },
    "十": {
        "de_q": r"""
### Übung A: Gleichverteilung und Transformation

Sei $U\sim U[a,b]$ stetig gleichverteilt.

1. Leiten Sie $E(U)$ und $Var(U)$ her.
2. Sei $Z=cU+d$ mit $c>0$. Bestimmen Sie Träger und Dichte von $Z$.

### Übung B: Normalverteilung linear transformieren

Sei $X\sim N(2.5,2)$ und $Y=1+3X$.

1. Bestimmen Sie Verteilung, Erwartungswert und Varianz von $Y$.
2. Berechnen Sie $E(X^2)$ ohne Integration.

### Übung C: Exponentialverteilung

Sei $X\sim Exp(\lambda)$ mit Dichte $f(x)=\lambda e^{-\lambda x}$ für $x\ge0$.

1. Leiten Sie die Verteilungsfunktion her.
2. Interpretieren Sie $P(X>t)$ als Wartezeitwahrscheinlichkeit.
""",
        "zh_q": r"""
### 练习 A：均匀分布与线性变换

设 $U\sim U[a,b]$ 为连续均匀分布。

1. 推导 $E(U)$ 和 $Var(U)$。
2. 设 $Z=cU+d$，其中 $c>0$。求 $Z$ 的支撑集和密度。

### 练习 B：正态分布的线性变换

设 $X\sim N(2.5,2)$，且 $Y=1+3X$。

1. 求 $Y$ 的分布、期望和方差。
2. 不积分，计算 $E(X^2)$。

### 练习 C：指数分布

设 $X\sim Exp(\lambda)$，密度为 $f(x)=\lambda e^{-\lambda x}$，$x\ge0$。

1. 推导分布函数。
2. 解释 $P(X>t)$ 的等待时间含义。
""",
        "de_a": r"""
### Lösung A

Für $U\sim U[a,b]$ gilt $f_U(u)=1/(b-a)$ auf $[a,b]$.

$$E(U)=\int_a^b u\frac1{b-a}\,du=\frac{b^2-a^2}{2(b-a)}=\frac{a+b}{2}.$$

Weiter

$$E(U^2)=\int_a^b u^2\frac1{b-a}\,du=\frac{b^3-a^3}{3(b-a)}=\frac{a^2+ab+b^2}{3}.$$

Also

$$Var(U)=E(U^2)-E(U)^2=\frac{(b-a)^2}{12}.$$

Für $Z=cU+d$ ist der Träger $[ca+d,cb+d]$. Die Umkehrfunktion ist $u=(z-d)/c$, Ableitung $1/c$. Daher

$$f_Z(z)=\frac1{b-a}\cdot\frac1c=\frac1{c(b-a)}$$

für $z\in[ca+d,cb+d]$.

### Lösung B

Lineare Transformationen normalverteilter Zufallsvariablen sind wieder normalverteilt:

$$Y=1+3X\sim N(1+3\cdot2.5,\;3^2\cdot2)=N(8.5,18).$$

Also $E(Y)=8.5$ und $Var(Y)=18$.

Für $E(X^2)$ verwenden wir $Var(X)=E(X^2)-E(X)^2$:

$$E(X^2)=Var(X)+E(X)^2=2+2.5^2=8.25.$$

### Lösung C

Für $x<0$ ist $F(x)=0$. Für $x\ge0$:

$$F(x)=\int_0^x \lambda e^{-\lambda u}\,du=1-e^{-\lambda x}.$$

Damit

$$P(X>t)=1-F(t)=e^{-\lambda t}.$$

In Worten: Wenn $X$ die Wartezeit bis zum nächsten Ereignis ist, dann ist $P(X>t)$ die Wahrscheinlichkeit, länger als $t$ Zeiteinheiten warten zu müssen.
""",
        "zh_a": r"""
### 解答 A

连续均匀分布在 $[a,b]$ 上的密度为 $f_U(u)=1/(b-a)$。

$$E(U)=\int_a^b u\frac1{b-a}\,du=\frac{a+b}{2}.$$

再算二阶矩：

$$E(U^2)=\int_a^b u^2\frac1{b-a}\,du=\frac{a^2+ab+b^2}{3}.$$

所以

$$Var(U)=E(U^2)-E(U)^2=\frac{(b-a)^2}{12}.$$

若 $Z=cU+d$ 且 $c>0$，则支撑集从 $[a,b]$ 变成 $[ca+d,cb+d]$。反函数为 $u=(z-d)/c$，导数为 $1/c$，因此

$$f_Z(z)=\frac1{b-a}\cdot\frac1c=\frac1{c(b-a)}.$$

### 解答 B

正态分布的线性变换仍为正态分布：

$$Y=1+3X\sim N(1+3\cdot2.5,\;3^2\cdot2)=N(8.5,18).$$

所以 $E(Y)=8.5$，$Var(Y)=18$。

利用 $Var(X)=E(X^2)-E(X)^2$：

$$E(X^2)=Var(X)+E(X)^2=2+2.5^2=8.25.$$

### 解答 C

当 $x<0$ 时，$F(x)=0$。当 $x\ge0$：

$$F(x)=\int_0^x \lambda e^{-\lambda u}\,du=1-e^{-\lambda x}.$$

所以

$$P(X>t)=1-F(t)=e^{-\lambda t}.$$

如果 $X$ 表示等待下一个事件发生的时间，那么 $P(X>t)$ 就是“等待时间超过 $t$”的概率。
""",
    },
})

GENERIC = {}


def main() -> None:
    for num, parts in EX.items():
        apply(ROOT / f"测试{num}.md", parts)
    for num, parts in GENERIC.items():
        apply(ROOT / f"测试{num}.md", parts)


if __name__ == "__main__":
    main()
