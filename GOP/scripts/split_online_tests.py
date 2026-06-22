from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "在线测试.md"

TEST_NAMES = {
    "一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7,
    "八": 8, "九": 9, "十": 10, "十一": 11, "十二": 12, "十三": 13, "十四": 14,
}

CN_DIGITS = {v: k for k, v in TEST_NAMES.items()}


def normalize_latex(text: str) -> str:
    text = text.replace("\\(", "$").replace("\\)", "$")
    text = text.replace("\\[", "$$").replace("\\]", "$$")
    return text


OPTION_NUMBERS = {chr(ord("a") + i): str(i + 1) for i in range(26)}


def normalize_options(text: str) -> str:
    def heading_repl(match: re.Match[str]) -> str:
        return f"- [ ] **{OPTION_NUMBERS[match.group(1)]}.**"

    def bullet_repl(match: re.Match[str]) -> str:
        return f"{match.group(1)}- [ ] **{OPTION_NUMBERS[match.group(2)]}.**"

    text = re.sub(r"^### ([a-z])\.\s*$", heading_repl, text, flags=re.M)
    text = re.sub(r"^(\s*)- (?:\[ \] )?\*\*([a-z])\.\*\*", bullet_repl, text, flags=re.M)
    return compact_option_headings(text)


def demote_content_headings(text: str) -> str:
    text = re.sub(r"^### ", "#### ", text, flags=re.M)
    text = re.sub(r"^## ", "### ", text, flags=re.M)
    return text


def compact_option_headings(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    option_only = re.compile(r"^- \[ \] \*\*(\d+)\.\*\*$")
    while i < len(lines):
        line = lines[i]
        if option_only.match(line) and i + 1 < len(lines):
            offset = 2 if i + 2 < len(lines) and not lines[i + 1].strip() else 1
            if i + offset < len(lines):
                next_line = lines[i + offset].strip()
            else:
                next_line = ""
            if (
                next_line
                and not next_line.startswith("---")
                and not next_line.startswith("![[")
                and not next_line.startswith("|")
                and not next_line.startswith("- [ ]")
            ):
                out.append(f"{line} {next_line}")
                i += offset + 1
                continue
        out.append(line)
        i += 1
    return "\n".join(out)


def has_cjk(s: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", s))


def is_shared_line(s: str) -> bool:
    t = s.strip()
    if not t:
        return True
    if t.startswith("![[") or t.startswith("!["):
        return True
    if t.startswith("|") or re.fullmatch(r"[-|: ]+", t):
        return True
    if t.startswith("---"):
        return True
    if t.startswith("### ") and re.fullmatch(r"### [a-z]\.", t):
        return True
    if re.fullmatch(r"\$.*\$", t) or t.startswith("$$"):
        return True
    return False


def clean_label(line: str, lang: str) -> str | None:
    stripped = line.strip()
    if stripped.startswith("**DE:**"):
        return line.replace("**DE:**", "", 1).strip() if lang == "de" else None
    if stripped.startswith("**中:**") or stripped.startswith("**中：**") or stripped.startswith("**中**"):
        if lang == "zh":
            return re.sub(r"^\*\*中(?::|：)?\*\*", "", line).strip()
        return None
    return line


def filter_lang(block: str, lang: str) -> str:
    out: list[str] = []
    for raw in normalize_latex(block).splitlines():
        raw_stripped = raw.strip()
        raw_is_de = raw_stripped.startswith("**DE:**")
        raw_is_zh = raw_stripped.startswith("**中:**") or raw_stripped.startswith("**中：**") or raw_stripped.startswith("**中**")
        if lang == "de" and raw_is_zh:
            images = re.findall(r"!\[\[[^\]]+\]\]", raw)
            if images:
                out.extend(images)
            continue
        line = clean_label(raw, lang)
        if line is None:
            continue
        stripped = line.strip()
        if stripped.startswith("# 测试"):
            continue
        if lang == "de":
            if raw_is_de:
                out.append(line)
                continue
            if has_cjk(line) and not is_shared_line(line):
                images = re.findall(r"!\[\[[^\]]+\]\]", line)
                out.extend(images)
                continue
            if stripped.startswith("## ") and has_cjk(line):
                continue
            out.append(line)
        else:
            if raw_is_zh:
                out.append(line)
                continue
            if stripped.startswith("## ") and not has_cjk(line):
                continue
            if has_cjk(line) or is_shared_line(line):
                out.append(line)
    # Compact excessive blank lines but keep Markdown spacing readable.
    text = "\n".join(out)
    text = re.sub(r"\n{4,}", "\n\n\n", text).strip()
    return demote_content_headings(normalize_options(text))


def split_tests(text: str) -> dict[int, str]:
    pattern = re.compile(r"^# 测试([一二三四五六七八九十]+)\s*$", re.M)
    matches = list(pattern.finditer(text))
    blocks = {}
    for idx, match in enumerate(matches):
        name = match.group(1)
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        blocks[TEST_NAMES[name]] = text[start:end].strip()
    return blocks


ANSWER_NOTES_ZH = {
2: """### 概率概念章节

**正确答案：a, b, e**

- **a 正确。** 这是概率的主观解释：概率表达观察者对事件发生的信念强度。
- **b 正确。** 这是频率主义解释：在可重复随机过程中，概率可理解为长期相对频率。
- **c 错误。** $P(A)=0$ 不一定表示事件绝对不可能发生；连续分布中单点事件概率为 $0$，但该点仍可能作为结果出现。
- **d 错误。** 必然事件概率是 $1$，不是 $\\infty$。
- **e 正确。** 概率在数学上由公理定义，但可有主观、频率、贝叶斯等解释。

### 拉普拉斯概率章节

**正确答案：a, d, f**

- **a 正确。** 拉普拉斯情形的核心是所有基本事件等可能，所以事件概率与其包含的基本事件个数成正比。
- **b 错误。** 投两次硬币的等可能样本空间应包含 $(Z,K)$ 和 $(K,Z)$ 两种顺序，不能合并。
- **c 错误。** “一次字面一次头像”包含两个基本事件，概率为 $1/2$；“两次头像”概率为 $1/4$。
- **d 正确。** “先字面后头像”和“两次头像”各包含一个等可能基本事件，概率相同。
- **e 错误。** 基本事件不总是等可能；等可能只是拉普拉斯模型的特殊条件。
- **f 正确。** 在有限或离散样本空间里，事件就是 $\\Omega$ 的子集，所有事件构成幂集。

### 概率空间章节

**正确答案：a, c**

- **a 正确。** 样本空间 $\\Omega$ 是所有基本事件 $\\omega$ 的集合。
- **b 错误。** 一次随机试验中基本事件互斥，只会发生一个基本事件；多个普通事件可以同时发生。
- **c 正确。** 事件 $A$ 在形式上就是 $\\Omega$ 的子集。
- **d 错误。** 概率空间可以有无限甚至不可数多个基本事件，例如连续型随机变量。

### 柯尔莫哥洛夫公理章节

**正确答案：d**

- **a 错误。** 公理化概率不只适用于频率主义解释。
- **b 错误。** 概率允许等于 $0$，即 $P(A)\\ge 0$。
- **c 错误。** 互斥事件满足 $P(A\\cup B)=P(A)+P(B)$，不是取较小值。
- **d 正确。** “$B$ 总是只能和 $A$ 一起发生”表示 $B\\subseteq A$，因此 $A\\cup B=A$，且 $P(A)\\ge P(B)$，所以 $P(A\\cup B)=P(A)=\\max(P(A),P(B))$。""",
3: """### 条件概率与全概率

**Question 1 正确答案：a, d, k, m, n**

- 条件概率应理解为“在 $B$ 已发生的条件下 $A$ 发生的概率”，公式是 $P(A\\mid B)=P(A\\cap B)/P(B)$，前提是 $P(B)>0$。
- **a、d 正确。** 固定条件后，相当于在满足条件的子空间上重新归一化概率。
- **k 正确。** 因为 $P(A\\mid B)=P(A\\cap B)/P(B)$，且 $P(B)\\le 1$，所以 $P(A\\mid B)\\ge P(A\\cap B)$。
- **m 正确。** 全概率公式用条件概率和条件事件本身的概率加权求无条件概率。
- **n 正确。** 单个基本事件构成的集合彼此不相交，并覆盖整个样本空间。

**Question 2 正确答案：c, d, e**

- **c 正确。** $P(A\\mid\\Omega)=P(A)$。
- **d 正确。** 若 $A\\subseteq B$，则在 $A$ 发生时 $B$ 必然发生，所以 $P(B\\mid A)=1$。
- **e 正确。** 不相交划分意味着 $B_1\\cap B_2=\\varnothing$，所以 $P(B_1\\mid B_2)=0$。

**$P(A\\mid A)$：** 若 $P(A)>0$，则 $P(A\\mid A)=1$；若 $P(A)=0$，条件概率未定义。考试若默认条件事件概率为正，应选 $1$。

### 啤酒帐篷题

**正确答案：a, b, c, f, g, h, i, l, m, n**

- 已知 $P(X)=0.15$，$P(Z)=0.25$，$P(Z\\mid X)=0.96\\overline{6}$，$P(X\\mid Z)=0.58$。
- 交集可由两边算出：$P(X\\cap Z)=P(Z\\mid X)P(X)=0.96\\overline{6}\\cdot0.15=0.145$，也等于 $0.58\\cdot0.25=0.145$。
- $P(X\\cap Z)$ 一定不大于 $P(X)$ 和 $P(Z)$。
- $P(Z\\cap\\overline X)$ 表示 Xaver 没倒、Zenzi 倒；$P(Z\\mid\\overline X)$ 表示在 Xaver 没倒的条件下 Zenzi 倒。
- $P(Z\\mid\\overline X)=\\frac{P(Z)-P(X\\cap Z)}{P(\\overline X)}=\\frac{0.25-0.145}{0.85}\\approx0.124$。

### 随机独立性

**正确答案：a, c**

- **a 正确。** 若 $P(A\\mid B)=P(A)$，则 $P(A\\cap B)=P(A)P(B)$，在概率为正时也推出 $P(B\\mid A)=P(B)$。
- **b 错误。** 条件独立不推出无条件独立，辛普森悖论就是典型提醒。
- **c 正确。** 多个事件的相互独立要求任意子组合都满足乘法关系；用条件概率表述就是知道其他事件不改变某个事件概率。

### 贝叶斯公式

**正确答案：a, c**

- **a 正确。** $P(B\\mid A)=\\frac{P(A\\mid B)P(B)}{P(A)}$。
- **b 错误。** 观测前的是先验概率；结合观测后的才是后验概率。
- **c 正确。** 诊断测试的预测值不仅取决于灵敏度、特异度，也强烈取决于患病率。
- **d 错误。** 赔率形式仍需要先验赔率，只是更新写成“先验赔率 $\\times$ 似然比”。

### PCR 检测题

**正确答案：a, f, i, j**

- 灵敏度至少 $70\\%$，所以假阴性率最多 $30\\%$，**a 正确**。
- 特异度 $95\\%$，所以健康者假阳性概率 $5\\%$，阳性赔率为 $0.05:0.95=1:19$，**f 正确**。
- 阳性似然比至少 $0.70/0.05=14$，**i 正确**。
- 阴性支持“未感染”的似然比为 $0.95/0.30\\approx3.17$，约为 $3$，**j 正确**。
- **k 错误。** 检测前未感染概率 $95\\%$，阴性后 $P(\\overline K\\mid\\overline T)=\\frac{0.95\\cdot0.95}{0.95\\cdot0.95+0.30\\cdot0.05}\\approx98.37\\%$，不到 $99\\%$。""",
4: """### 复习解答

- **列联表与条件频率：正确选项 a, c。** 列联表内部是联合频数，边缘位置才是边际频数；条件频率要固定一个条件类别后在该行或列内归一化。
- **经验独立性与列联系数：正确选项 a, b, c, e。** 经验独立意味着条件分布相同；列联系数衡量类别变量之间偏离独立的程度，但它不是方向性因果量。
- **Odds 与 Odds Ratio：** 原文中已有数值答案：样本量 $560$，有胡萝卜鼻 $383$，条件相对频率约 $0,9$ 与 $0,6$，条件 odds 约 $1,6$，无胡萝卜鼻 odds 约 $0,5$，两个 odds ratio 都约 $7,5$。这说明“胡萝卜鼻”和“羊毛围巾”关联强，但不能直接解释为风险因果。
- **马赛克图：正确选项 b。** 马赛克图主要展示两个或多个类别变量的联合分布；经验独立时，相应条件切分比例应一致。
- **多维马赛克图：待图片确认。** 当前目录没有 `Pasted image 20260620021915.png`，所以不能可靠判断 Grafik A-D 的切分顺序。复习时重点看：最先切分的变量决定大块宽度/高度，后续变量决定条件分布是否容易读取。""",
5: """### 复习解答

**Question 1：建议答案 a, b, c, d, e, f, i**

- 随机变量是函数 $X:\\Omega\\to T\\subseteq\\mathbb R$，所以每个基本事件被分配**恰好一个**数值；因此“至少一个”“至多一个”在逻辑上也成立，但最精确的是“恰好一个”。
- 支撑集中的值按定义应至少有某个基本事件映射到它。
- $P(X=x)$ 不是 $P(X\\le x)$；后者是分布函数 $F_X(x)$。
- 连续变量区间概率用积分 $\\int_a^b f_X(x)dx$，不是求和，且通常 $P(X=x)=0$。

**Question 2：正确答案 a, b**

- 连续随机变量的分布函数 $F$ 连续，且 $\\lim_{x\\to\\infty}F(x)=1$。
- 若密度存在，则通常在可导点 $F'(x)=f(x)$，不是 $F'(x)<f(x)$。

**Question 3：正确答案 b**

- $[1,1.1]$ 和角度区间都是连续取值集合；有理数 $\\mathbb Q$ 可数，因此可作为离散型取值集合。

**Question 4：正确答案 a, b, e, j**

- 频数表最适合取值种类远少于样本量的变量。
- 相对频率必须非负、总和为 $1$，且在样本量 $n=10$ 时通常应是 $0.1$ 的倍数；所以 $0.15$ 不可能。
- $h_j$ 是绝对频数，$f_j$ 是相对频率；若 $f_1=0.5$，剩余频率总和也只有 $0.5$，所以每个剩余 $f_j\\le0.5$。

**Question 5：正确答案 c**

- 经验分布函数是阶梯函数，单调不减，但不严格单调，也不连续。
- 它给出样本中 $x_i\\le z$ 的比例或频率。
- 图中样本量、阶梯数量等读图题需结合图片确认。

**Question 6-7：待图片确认**

- 当前缺少两张 ECDF 图片，不能可靠读出中位数、90% 分位数或赌约胜率。
- 复习方法：$F_A(x)$ 给出 $A\\le x$ 的比例；“50% 在该值以上”对应 $A$ 的中位数附近；比较随机抽取的 $a_i$ 与独立抽取的 $b_{i'}$ 时，可以由两个边缘分布估计；若比较同一个调查单位的 $a_i,b_i$，只看边缘分布不够，还需要联合分布。""",
6: """### 复习解答

**正确答案：a, d, g, k, n**

- 调查单位是“某州在某一年”的观测，而不只是州本身，因为每个州跨年份重复出现。
- 映射到图形美学的变量有州名、年份、感染率：水平位置对应年份，垂直位置对应州，颜色对应感染率。
- 几何对象是小矩形格子；颜色不是几何对象，而是美学属性。
- 这种热图很适合看各州随时间变化的模式和差异，但不适合精确读取具体感染率数值。""",
7: """### 复习解答

**Question 1：建议答案 c**

- 感染率是从低到高的有序数量，适合顺序型色阶；它不是类别型色阶，也不是围绕中心值正负分叉的发散色阶。
- 是否感知均匀、是否无障碍，需要实际图片和配色才能严格确认；当前缺少图片文件，所以不强行判断。

**Question 2：建议答案 b, c, e, g**

- 图展示的是各党派内部的赞同比例，不是“赞成票来源构成”，所以“62% 的赞成票来自民主党”是误读。
- 颜色若对应党派身份，可以帮助识别类别；百分比标注能弥补坐标轴或柱长读取不精确。
- 横纵轴标签需要清楚说明类别和百分比含义。
- 100% 堆叠条形图在这里只有一个比例，没有额外组成部分，信息增益有限。

**Question 3：待图片确认**

- 缺少三张图 A-C 的原图，无法可靠判断哪张最适合比较总数、比例或性别分组。
- 复习时记住：比较总量通常看共同基线的长度；比较比例常用 100% 堆叠或并列比例；比较分组绝对数常用并列条形。

**Question 4：正确答案 b**

- 图形设计首先服务于信息和问题；面积、体积通常不如位置和长度精确，饼图也不擅长多组比例比较。

**Question 5：正确答案 a, c**

- KDE 是对各观测点核函数贡献的平滑平均；高斯核在任意位置都有非零贡献，所以所有观测都会参与估计。
- 带宽通常比核函数选择更关键；KDE 也不是永远优于直方图。

**Question 6：正确答案 c**

- 散点图用于展示两个度量型变量之间的关系。

**Question 7：正确答案 a**

- 经典 `speed` 与 `dist` 散点图呈正相关：速度越高，刹车距离通常越长。""",
8: """### 复习解答

**Frage 1：建议答案 e, g, i, m, n, o, p**

- 众数是出现最频繁的取值，不是最大频数本身；中位数不是最小值和最大值的中点。
- 等宽直方图中，众数可近似位于最高柱附近；经验分布函数中最大跳跃对应最高频取值。
- 几何平均数可写为 $\\exp(\\overline{\\log x})$，适合乘法增长因子。
- 奇数样本下按 $\\alpha=\\frac{n-1}{2n}$ 修剪后只剩中间值，即中位数。
- 下方大离群值会把算术平均数往下拉，常使均值低于中位数。

**Frage 2：数值答案**

- 数据：$(1,4,3,2,4,2,2,2,4,0,3,3,3)$，排序为 $0,1,2,2,2,2,3,3,3,3,4,4,4$。
- 算术平均数：$33/13\\approx2.54$。
- $F_E(2.4)=P(E\\le2.4)=6/13\\approx0.46$。
- 中位数：第 7 个值，为 $3$。
- 标准差：若使用样本标准差（R 的 `sd`），约 $1.20$；若用 $1/n$ 的描述性标准差，约 $1.15$。
- IQR：按 R 默认分位数为 $3-2=1.00$。
- 极差：$4-0=4.00$。
- 加入 $17$ 后，R 默认 IQR 约 $1.75$；样本标准差约 $4.03$。离群值对标准差影响非常大，对 IQR 影响较小。

**Frage 3：正确答案 a, b**

- 排序后为 $1,1,1,2,2,3,3,3,3,4$，中位数是 $(2+3)/2=2.5$，众数是 $3$。

**Frage 4：待图片确认**

- 缺少直方图、ECDF、箱线图原图，不能可靠配对。复习时用三点配对：范围和离群点、四分位数位置、ECDF 跳跃密集区域。

**Frage 5：数值答案**

- 情景 I 是按群体加权平均：$0.25\\cdot1.1+0.25\\cdot1.02+0.5\\cdot3=2.03$。
- 情景 II 是分阶段连续传播，适合用几何平均：$(1.1\\cdot e\\cdot1.02)^{1/3}\\approx1.45$。若课程按普通阶段算术平均，则为 $1.61$；从“繁殖率跨阶段相乘”的语境看，几何平均更有复习价值。

**Frage 6：正确答案 a**

- 均值 $7.20$ 与中位数 $7.00$ 接近，符合两个骰子和大致对称的分布。
- 方差单位是平方单位，平均偏离程度应看标准差 $2.36$，不是方差 $5.55$。
- 两个骰子和的期望可由单个骰子期望相加得到。""",
9: """### 复习解答

**Question 1：正确答案 b, c**

- 正态分布对称且单峰，所以众数、期望值、中位数相同。
- 期望具有线性性，$E(X+Y)=E(X)+E(Y)$ 总成立。
- 方差相加还需要独立或零协方差；一般有 $Var(X+Y)=Var(X)+Var(Y)+2Cov(X,Y)$。

**Question 2：正确答案 a, d**

- 期望可线性拆分；$E(4X)=4E(X)$。
- 方差满足 $Var(aX)=a^2Var(X)$，所以 $Var(-2X)=4Var(X)$。
- 不是所有分布都有有限期望和方差，例如柯西分布。

**Question 3：正确答案 c**

- $Var(aX)=a^2Var(X)=a^2c$。若 $Var(aX)=Var(bX)$，只能推出 $|a|=|b|$；当 $a,b>0$ 时才必然推出 $a=b$。

**Question 4：待图片确认**

- 缺少变量 T/G/R/N/B 的图，不能可靠读出 IQR、偏度、峰度。复习时：IQR 看箱体宽度；分位偏度看中位数在箱体中的位置；超额峰度看尖峰和尾部极端值。

**Question 5：建议答案 a, d, e**

- 样本 $(11,14,55,54,27)$ 右尾较长，矩偏度为正；德语中常称为 `linksteil/rechtsschief`。
- 负超额峰度表示比正态更平坦或尾部较轻，不是 leptokurtisch。
- 分位数偏度系数 $g_p$ 的范围在 $[-1,1]$。

**Question 6：建议答案 c, d, e, g, i, k, o, q**

- 多峰分布中均值/中位数可能落在低密度区域，解释性变差。
- 左偏分布的主体常在高值端；右偏分布通常 $Modus<Median<Mittelwert$。
- 对称双峰分布的两个峰到中心距离相等；单峰对称分布中众数约等于中位数。
- 强偏态或厚尾通常伴随正超额峰度；此时算术平均数容易被极端值影响。

**Question 7：正确答案 a, b, d, e, f**

- Lorenz 曲线描述“按变量值从小到大排序后，前 $p$ 比例单位占有总量的比例”。
- 它通常连续、单调递增且凸，斜率单调不减。
- 它位于完全平等线下方；集中度越大，曲线离对角线越远，Gini 越大。

**Question 8-9：待图片确认**

- 缺少 Lorenz 曲线图片，不能可靠判定曲线编号。
- 复习判断：离对角线越远，收入集中越强；曲线越贴近对角线，越平等。

**Question 10：正确答案：无**

- 原始蛋糕份额的 Gini 约 $0.228$，不是 $0.29$。
- 每人都减去 $5^\\circ$ 不是比例缩放，会改变集中度，Gini 约升至 $0.245$。
- 把每个观测一分为二并复制为两个相同相对份额，本质上不改变相对不平等，Gini 不下降。""",
10: """### 复习解答

**Question 1：正确答案 a, c, g**

- 二项分布和几何分布都基于独立同分布伯努利试验。
- 伯努利分布是二项分布在 $n=1$ 时的特殊情形，不是反过来。
- 二项分布数固定次数内成功次数；几何分布通常描述首次成功所需试验次数或失败次数。
- 超几何分布对应无放回抽样；泊松分布是离散分布，参数表示区间内平均发生次数。

**Question 2：正确答案 a, c, d, e, j**

- 连续密度通常有归一化常数；Gamma 支撑在正实数，$\\alpha=1$ 时为指数分布；正态支撑为全体实数。
- 正态分布只有位置和尺度两个自由参数，高度由归一化条件决定。
- 标准正态密度缺少系数 $1/\\sqrt{2\\pi}$ 时不完整。
- Beta 分布通常支撑在 $[0,1]$；Cauchy 分布有位置和尺度参数，但适合描述极端离群值较多的情形。

**Question 3：正确答案 b**

- 泊松分布满足 $E(X)=Var(X)=\\lambda$。正态分布一般为 $E=\\mu,Var=\\sigma^2$；卡方分布 $E=k,Var=2k$。

**Question 4：建议答案 a, b, d, e**

- 对随机变量作确定性变换仍得到随机变量。
- 指数分布支撑为正数，$Y=X^2$ 在支撑上单调，可直接用密度变换。
- $\\sin(2\\pi X)$ 非单调，简单单调版密度变换不能直接套用，需要分段/多原像处理。
- 密度变换的直觉是：原区间被拉长时，单位长度上的概率质量变稀，密度下降。""",
11: """### 复习解答

**Question 1：正确答案 a, c**

- $P(A\\mid B)=P(A)$ 表示 $B$ 不改变 $A$ 的概率，在概率为正时等价于相互独立，因此也有 $P(B\\mid A)=P(B)$。
- 条件独立不推出无条件独立。
- 多事件相互独立要求任意子集都满足相应乘法关系。

**Question 2：正确答案 a, b, c, f**

- 离散联合“密度”就是联合概率质量。
- 连续联合密度在矩形区域上积分得到该区域概率。
- 对联合密度把另一个变量积分掉，可得边缘分布/边缘密度；题中 $F_X(x)$ 的积分顺序表达了这一点。
- 联合分布包含依赖结构，边缘分布本身不够。
- $f_{X,Y}=f_Xf_Y$ 只在独立时成立，不是总成立；它与联合分布函数乘积分解等价。

**Question 3：正确答案 b**

- 只存在某一个 $y$ 使条件分布等于边缘分布，不足以说明独立；独立要求所有相关 $y$ 都成立。
- 联合表中同一行/列存在正概率边缘时出现一个内部零格，通常破坏乘积分解，因此可推出相依。
- 离散和连续变量可以组成混合分布，一般规则并非失效，只是记号更细。

**Question 4：正确答案 d, e**

- $f_{X,Y}(x,y)=f_{Y,X}(y,x)$ 只是变量顺序交换。
- $P(|X-Y|<3)$ 对应区域 $y\\in(x-3,x+3)$ 的联合密度积分。
- 条件密度一般不对称；边缘分布不能唯一决定联合分布。

**Question 5：待图片确认**

- 缺少等高线与条件密度图，a-c 不能可靠判断。
- **d 错误。** 一般应为 $f_X(x)=\\int f_{X,Y}(x,y)dy=\\int f_{X\\mid Y=y}(x)f_Y(y)dy$，不能漏掉权重 $f_Y(y)$。""",
12: """### 复习解答

原文写的是“同测试十一”，所以本文件的复习解答同测试十一。建议直接对照 [测试十一.md]：重点掌握事件独立、随机变量独立、联合分布、边缘分布、条件密度之间的关系。""",
13: """### 复习解答

**Question 1：正确答案 c, d**

- 协方差 $35.89$ 的正号说明同向变化倾向，但数值大小受量纲影响，单独不能判断“强不强”。
- 若要比较强度，应计算标准化后的相关系数。

**Question 2：正确答案 b**

- 气温越高通常穿得越少，是负相关或反向关系。

**Question 3：正确答案 e**

- $Cov(X,X)=Var(X)$，不是平方根。
- 协方差会随线性缩放改变；相关系数对正比例缩放不变，但负比例缩放会改变符号。
- 零相关不等于独立；$|\\rho|=1$ 表示完全线性关系。

**Question 4：正确答案 a, d, e**

- Spearman 相关就是对秩计算 Pearson 相关。
- 秩相关比 Pearson 对离群值稳健。
- 单调关系会让秩之间呈线性关系；但相关为 $0$ 不代表经验独立。

**Question 5：正确答案 c, e**

- 一致对看的是两个对象在两个变量上的排序方向是否一致，不是是否高于均值。
- 距离相关利用所有观测两两距离；Pearson 完全线性相关会推出 Spearman 也达到绝对值 $1$。
- Spearman 为 $1$ 只说明严格单调，不一定 Pearson 为 $1$；距离相关非负，不会取 $-1$。

**Question 6：正确答案 a**

- $r=-0.93$ 表示强负线性相关：降水越多，售票越少的线性趋势越明显。

**Question 7：部分待图片确认**

- 缺少季节散点图，前四个读图问题不能可靠判断。
- 加入“夏季无雨且高售票”的点会如何改变相关，要看原夏季云图位置；一般这是高杠杆点。
- 最后一问可确定：漏记每第 10 张票，相当于把售票数乘以正常数修正，Pearson 相关系数不变，所以答案是 `0`。""",
14: """### 复习解答

**Question 1：正确答案 d**

- 假阳性多意味着健康者被判阳性多，即特异度低。灵敏度主要控制患病者中被检出的比例。

**Question 2：正确答案 a**

- 高灵敏度表示实际患病者中测试阳性的比例高，也就是真阳性多、假阴性少。

**Question 3：正确答案 b**

- 特异度 $=P(\\text{Test negativ}\\mid\\text{tatsächlich gesund})$，即实际健康者中测为阴性的比例。

**Question 4：建议答案 a, c**

- 只改变患病者评分分布的方差，健康者分布不变，所以特异度保持不变。
- 若阳性判定阈值位于患病者均值下方，患病者方差增大会让更多患病者落到阈值以下，灵敏度下降；ppV/npV 通常也会随之变化。

**Question 5：ROC 与阈值题**

- 由数据看，舌重越大总体越像患病，AUC 约为 $7/8=0.875$，说明关联较强；**a、b、c 正确**。
- 阈值题要特别注意课程约定是 $G\\ge c$ 还是 $G>c$ 判阳性；不同约定会影响等于阈值的患者。
- 若按 $G\\ge106$ 判阳性，则阴性预测值为 $TN/(TN+FN)=2/(2+1)\\approx67\\%$，h 正确。
- 若按 $G>76$ 判阳性，则阳性预测值为 $3/(3+0)=100\\%$，i 正确。
- 这题适合复习：严重漏诊成本高时偏向低阈值提高灵敏度；过度治疗成本高时偏向高阈值提高特异度。

**Question 6：数值答案**

- 总人数 $100000000$，被通缉 $2000$，未被通缉 $99998000$。
- 灵敏度 $99.9\\%$：$A=1998$，$D=2$。
- 特异度 $99.5\\%$：$E=99498010$，$B=499990$。
- $C=A+B=501988$，$F=D+E=99498012$。
- $npV=E/(D+E)\\approx0.99999998$，按三位小数为 `1,000`。
- $ppV=A/(A+B)\\approx0.00398$，按三位小数为 `0,004`。这就是低基率问题：即使灵敏度和特异度很高，阳性警报里真阳性的比例仍可能很低。""",
}


ANSWER_NOTES_DE = {
2: """### Wahrscheinlichkeitsbegriff

**Richtige Antworten: 1, 2, 5**

- **1 ist richtig.** Das ist die subjektive Interpretation von Wahrscheinlichkeit: Sie beschreibt den Grad persönlicher Unsicherheit.
- **2 ist richtig.** Das ist die frequentistische Interpretation: Bei vielen Wiederholungen nähert sich die relative Häufigkeit der Wahrscheinlichkeit.
- **3 ist falsch.** $P(A)=0$ bedeutet nicht immer, dass $A$ unmöglich ist; bei stetigen Verteilungen haben einzelne Werte Wahrscheinlichkeit $0$.
- **4 ist falsch.** Ein sicheres Ereignis hat Wahrscheinlichkeit $1$, nicht $\\infty$.
- **5 ist richtig.** Wahrscheinlichkeit ist mathematisch axiomatisch definiert, kann aber unterschiedlich interpretiert werden.

### Laplacewahrscheinlichkeiten

**Richtige Antworten: 1, 4, 6**

- Bei Laplace-Modellen sind die Elementarereignisse gleich wahrscheinlich.
- Beim zweimaligen Münzwurf gehören $(Z,K)$ und $(K,Z)$ getrennt in den Ergebnisraum.
- „Einmal Zahl, einmal Kopf“ hat Wahrscheinlichkeit $1/2$, „zweimal Kopf“ nur $1/4$.
- „Zuerst Zahl, dann Kopf“ und „zweimal Kopf“ bestehen jeweils aus einem gleich wahrscheinlichen Elementarereignis.
- Die Potenzmenge von $\\Omega$ enthält alle Ereignisse.

### Wahrscheinlichkeitsräume

**Richtige Antworten: 1, 3**

- $\\Omega$ ist die Menge der Elementarereignisse.
- Ein Ereignis ist formal eine Teilmenge von $\\Omega$.
- Elementarereignisse schließen sich in einem einzelnen Zufallsexperiment gegenseitig aus.
- Wahrscheinlichkeitsräume können unendlich oder sogar überabzählbar viele Elementarereignisse enthalten.

### Axiome von Kolmogorow

**Richtige Antwort: 4**

- Kolmogorow-Axiome gelten unabhängig von der Interpretation der Wahrscheinlichkeit.
- Wahrscheinlichkeiten dürfen $0$ sein.
- Für disjunkte Ereignisse gilt $P(A\\cup B)=P(A)+P(B)$.
- Wenn $B\\subseteq A$, dann ist $A\\cup B=A$ und damit $P(A\\cup B)=\\max(P(A),P(B))$.""",
3: """### Bedingte Wahrscheinlichkeit und totale Wahrscheinlichkeit

**Question 1: richtige Antworten 1, 4, 11, 13, 14**

- Bedingte Wahrscheinlichkeit bedeutet: Wahrscheinlichkeit von $A$ unter der Annahme, dass $B$ eingetreten ist.
- Die Formel lautet $P(A\\mid B)=P(A\\cap B)/P(B)$ für $P(B)>0$.
- Daraus folgt $P(A\\mid B)\\ge P(A\\cap B)$, weil durch $P(B)\\le1$ geteilt wird.
- Der Satz der totalen Wahrscheinlichkeit setzt unbedingte Wahrscheinlichkeiten aus bedingten Wahrscheinlichkeiten zusammen.
- Die einzelnen Elementarereignisse bilden eine disjunkte Zerlegung von $\\Omega$.

**Question 2: richtige Antworten 3, 4, 5**

- $P(A\\mid\\Omega)=P(A)$.
- Wenn $A\\subseteq B$, dann gilt $P(B\\mid A)=1$.
- Wenn $B_1$ und $B_2$ disjunkt sind, ist $P(B_1\\mid B_2)=0$.

**$P(A\\mid A)$:** Für $P(A)>0$ gilt $P(A\\mid A)=1$; bei $P(A)=0$ ist die bedingte Wahrscheinlichkeit nicht definiert.

### Bierzelt-Aufgabe

**Richtige Antworten: 1, 2, 3, 6, 7, 8, 9, 12, 13, 14**

- Gegeben sind $P(X)=0.15$, $P(Z)=0.25$, $P(Z\\mid X)=0.96\\overline6$ und $P(X\\mid Z)=0.58$.
- $P(X\\cap Z)=P(Z\\mid X)P(X)=0.96\\overline6\\cdot0.15=0.145$.
- Ein Schnitt kann nie wahrscheinlicher sein als eines der beteiligten Ereignisse.
- $P(Z\\cap\\overline X)$ beschreibt: Xaver schüttet nicht, Zenzi aber schon.
- $P(Z\\mid\\overline X)=\\frac{0.25-0.145}{0.85}\\approx0.124$.

### Stochastische Unabhängigkeit

**Richtige Antworten: 1, 3**

- $P(A\\mid B)=P(A)$ ist bei positiven Wahrscheinlichkeiten äquivalent zu $P(A\\cap B)=P(A)P(B)$ und damit auch zu $P(B\\mid A)=P(B)$.
- Bedingte Unabhängigkeit impliziert nicht automatisch unbedingte Unabhängigkeit.
- Für mehrere Ereignisse muss Unabhängigkeit für alle relevanten Teilkombinationen gelten.

### Satz von Bayes

**Richtige Antworten: 1, 3**

- Bayes: $P(B\\mid A)=\\frac{P(A\\mid B)P(B)}{P(A)}$.
- A-priori-Wahrscheinlichkeiten gelten vor der Beobachtung; nach der Beobachtung spricht man von posterioren Wahrscheinlichkeiten.
- Bei diagnostischen Tests hängt die Aussagekraft stark von der Grundrate ab.

### PCR-Test

**Richtige Antworten: 1, 6, 9, 10**

- Sensitivität mindestens $70\\%$ bedeutet: höchstens $30\\%$ der Infizierten werden übersehen.
- Spezifität $95\\%$ bedeutet: bei Nichtinfizierten ist $P(T\\mid\\overline K)=0.05$, Odds also $0.05:0.95=1:19$.
- Positive Likelihood Ratio: mindestens $0.70/0.05=14$.
- Negative Likelihood Ratio zugunsten von „nicht infiziert“: $0.95/0.30\\approx3.17$.
- Quirin erreicht nach negativem Test nur etwa $98.37\\%$ Sicherheit, also nicht $99\\%$.""",
4: """### Lösung und Wiederholung

- **Kontingenztafeln und bedingte Häufigkeit: richtige Optionen 1, 3.** Innere Tabellenzellen sind gemeinsame Häufigkeiten; Randhäufigkeiten stehen am Tabellenrand. Bedingte Häufigkeiten erhält man durch Normierung innerhalb einer Zeile oder Spalte.
- **Empirische Unabhängigkeit und Kontingenzkoeffizient: richtige Optionen 1, 2, 3, 5.** Empirische Unabhängigkeit bedeutet gleiche bedingte Verteilungen. Kontingenzkoeffizienten messen Abweichung von Unabhängigkeit, aber keine Kausalität.
- **Odds und Odds Ratio:** Die im Ausgangstext enthaltenen Antworten sind $n=560$, Rübennase $383$, bedingte relative Häufigkeiten etwa $0,9$ und $0,6$, bedingte Odds etwa $1,6$, Odds für keine Rübennase etwa $0,5$, beide Odds Ratios etwa $7,5$. Ein großes Odds Ratio zeigt starken Zusammenhang, aber nicht automatisch einen kausalen Risikofaktor.
- **Mosaikplots: richtige Option 2.** Mosaikplots visualisieren gemeinsame Verteilungen kategorialer Merkmale. Bei empirischer Unabhängigkeit bleiben die bedingten Proportionen gleich.
- **Multidimensionale Mosaikplots: bildabhängig.** Ohne `Pasted image 20260620021915.png` lässt sich die Reihenfolge der Aufteilungen in Grafik A-D nicht sicher beurteilen.""",
5: """### Lösung und Wiederholung

**Question 1: empfohlene Antworten 1, 2, 3, 4, 5, 6, 9**

- Eine Zufallsvariable ist eine Abbildung $X:\\Omega\\to T\\subseteq\\mathbb R$.
- Jedes Elementarereignis bekommt genau einen Wert; daher sind „mindestens“, „höchstens“ und „genau“ logisch zu beachten, am präzisesten ist „genau“.
- Werte im Träger sollten tatsächlich von mindestens einem Elementarereignis erreicht werden.
- $P(X=x)$ ist nicht $P(X\\le x)$; letzteres ist die Verteilungsfunktion.
- Für stetige Variablen werden Intervallwahrscheinlichkeiten integriert, nicht summiert.

**Question 2: richtige Antworten 1, 2**

- Die Verteilungsfunktion einer stetigen Zufallsvariable ist stetig.
- Außerdem gilt $\\lim_{x\\to\\infty}F(x)=1$.
- An differenzierbaren Stellen gilt $F'(x)=f(x)$, nicht $F'(x)<f(x)$.

**Question 3: richtige Antwort 2**

- $[1,1.1]$ und Winkelintervalle sind kontinuierlich. $\\mathbb Q$ ist abzählbar und kann daher als diskreter Träger verwendet werden.

**Question 4: richtige Antworten 1, 2, 5, 10**

- Häufigkeitstabellen sind sinnvoll, wenn deutlich weniger Ausprägungen als Beobachtungen vorliegen.
- Relative Häufigkeiten müssen nicht nur zu $1$ summieren, sondern bei $n=10$ auch in Zehntelschritten auftreten.
- $h_j$ ist absolute, $f_j$ relative Häufigkeit.
- Wenn $f_1=0.5$, kann kein anderer einzelner Anteil größer als $0.5$ sein.

**Question 5: richtige Antwort 3**

- Empirische Verteilungsfunktionen sind monoton nicht fallend, aber nicht streng monoton und nicht stetig.
- Sie geben den Anteil der Beobachtungen mit $x_i\\le z$ an.

**Question 6-7: bildabhängig.** Ohne die ECDF-Grafiken können Median, Quantile und Wettwahrscheinlichkeiten nicht sicher abgelesen werden. Wichtig: Für Vergleiche derselben Untersuchungseinheit braucht man die gemeinsame Verteilung, nicht nur die Randverteilungen.""",
6: """### Lösung und Wiederholung

**Richtige Antworten: 1, 4, 7, 11, 14**

- Untersuchungseinheiten sind Bundesstaat-Jahr-Kombinationen, weil jeder Staat über viele Jahre beobachtet wird.
- Visualisierte Merkmale sind Bundesstaat, Jahr und Infektionsrate.
- Die Geometrie sind Rechtecke bzw. Kacheln.
- Die ästhetische Zuordnung ist: horizontale Position $\\leftrightarrow$ Jahr, vertikale Position $\\leftrightarrow$ Bundesstaat, Farbe $\\leftrightarrow$ Infektionsrate.
- Die Grafik eignet sich gut zum Erkennen von Verlaufsmustern, aber nicht für präzise quantitative Vergleiche einzelner Infektionsraten.""",
7: """### Lösung und Wiederholung

**Question 1: empfohlene Antwort 3**

- Infektionsraten sind geordnete quantitative Werte; dafür passt eine sequentielle Farbskala.
- Qualitative Skalen sind für ungeordnete Kategorien, divergierende Skalen für Werte um einen sinnvollen Mittelpunkt.
- Wahrnehmungseinheitlichkeit und Barrierefreiheit sind ohne Originalbild nur eingeschränkt beurteilbar.

**Question 2: empfohlene Antworten 2, 3, 5, 7**

- Die Grafik zeigt Zustimmungsanteile innerhalb der Parteien, nicht die Herkunft aller Zustimmungen.
- Farben können Parteikategorien unterstützen; Prozentwerte über den Balken helfen beim exakten Lesen.
- Achsenbeschriftungen sollten klar angeben, welche Kategorien und Prozentwerte dargestellt werden.
- Ein 100%-Stapeldiagramm bringt hier kaum Zusatzinformation.

**Question 3: bildabhängig.** Ohne Grafik A-C kann die Eignung der Darstellungen nicht sicher verglichen werden. Regel: gemeinsame Basislinien helfen bei absoluten Vergleichen; 100%-Darstellungen helfen bei Anteilen.

**Question 4: richtige Antwort 2**

- Grafiken sollten zuerst nach Fragestellung, Botschaft und Informationsgehalt konstruiert werden.
- Flächen, Volumina und Kreisdiagramme sind für präzise Vergleiche oft schwächer als Positionen und Längen.

**Question 5: richtige Antworten 1, 3**

- KDE mittelt Kernbeiträge über Beobachtungen.
- Beim Gauß-Kern tragen alle Beobachtungen überall bei.
- Die Bandbreite ist meist wichtiger als die Wahl des Kerns.

**Question 6: richtige Antwort 3.** Ein Streudiagramm zeigt den Zusammenhang zweier metrischer Merkmale.

**Question 7: richtige Antwort 1.** Beim klassischen `speed`/`dist`-Datensatz steigt die Bremsdistanz tendenziell mit der Geschwindigkeit.""",
8: """### Lösung und Wiederholung

**Frage 1: empfohlene Antworten 5, 7, 9, 13, 14, 15, 16**

- Der Modus ist der häufigste Wert, nicht die Häufigkeit selbst.
- Der Median ist nicht die Mitte zwischen Minimum und Maximum.
- Bei gleich breiten Histogrammklassen liegt der Modus ungefähr in der höchsten Säule.
- In der ECDF entspricht der größte Sprung dem häufigsten Wert.
- Das geometrische Mittel ist $\\exp(\\overline{\\log x})$.
- Bei ungeradem $n$ und starkem Trimmen bis auf den mittleren Wert ergibt sich der Median.
- Untere Ausreißer ziehen das arithmetische Mittel nach unten.

**Frage 2: numerische Antworten**

- Mittelwert: $33/13\\approx2.54$.
- $F_E(2.4)=6/13\\approx0.46$.
- Median: $3$.
- Standardabweichung: als Stichprobenstandardabweichung etwa $1.20$; mit $1/n$ etwa $1.15$.
- IQR nach R-Standardquantilen: $1.00$.
- Spannweite: $4.00$.
- Mit zusätzlichem Wert $17$: IQR etwa $1.75$, Stichprobenstandardabweichung etwa $4.03$.

**Frage 3: richtige Antworten 1, 2**

- Sortiert: $1,1,1,2,2,3,3,3,3,4$.
- Median $=(2+3)/2=2.5$, Modus $3$.

**Frage 4: bildabhängig.** Ohne Histogramm/ECDF/Boxplot-Grafik kann die Zuordnung nicht sicher bestimmt werden.

**Frage 5: numerische Antworten**

- Szenario I: $0.25\\cdot1.1+0.25\\cdot1.02+0.5\\cdot3=2.03$.
- Szenario II als phasenweises Wachstum: geometrischer Mittelwert $(1.1\\cdot e\\cdot1.02)^{1/3}\\approx1.45$. Falls nur arithmetisch gemittelt wird: $1.61$.

**Frage 6: richtige Antwort 1**

- Mittelwert $7.20$ und Median $7.00$ liegen nahe beieinander, was zu ungefährer Symmetrie passt.
- Die Varianz ist quadratisch skaliert; durchschnittliche Abweichung interpretiert man eher über die Standardabweichung.""",
9: """### Lösung und Wiederholung

**Question 1: richtige Antworten 2, 3**

- Bei der Normalverteilung fallen Modus, Erwartungswert und Median zusammen.
- Erwartungswerte sind linear: $E(X+Y)=E(X)+E(Y)$.
- Varianzen addieren sich nur bei Unabhängigkeit bzw. Nullkovarianz.

**Question 2: richtige Antworten 1, 4**

- $E[\\sum X_i]=\\sum E[X_i]$.
- $E[4X]=4E[X]$, nicht $16E[X]$.
- $Var[-2X]=(-2)^2Var(X)=4Var(X)$.
- Nicht jede Verteilung besitzt endlichen Erwartungswert und endliche Varianz.

**Question 3: richtige Antwort 3**

- Aus $Var[aX]=Var[bX]$ folgt $a^2c=b^2c$, also $|a|=|b|$.
- Wenn $a,b>0$, folgt daraus $a=b$.

**Question 4: bildabhängig.** IQR liest man aus der Boxbreite, Schiefe aus der Lage des Medians innerhalb der Box, Kurtosis aus Spitzen und Ausreißern.

**Question 5: empfohlene Antworten 1, 4, 5**

- Die Daten haben eine längere rechte Seite; der Momentenschiefekoeffizient ist positiv.
- Negative Exzess-Kurtosis bedeutet nicht leptokurtisch.
- Der Quantilskoeffizient der Schiefe liegt zwischen $-1$ und $1$.

**Question 6: empfohlene Antworten 3, 4, 5, 7, 9, 11, 15, 17**

- Multimodalität kann Mittelwert und Median schwer interpretierbar machen.
- Bei Rechtsschiefe gilt typischerweise Modus < Median < Mittelwert.
- Bei symmetrischer bimodaler Verteilung liegen die beiden Modi gleich weit vom Median entfernt.
- Starke Schiefe oder starke positive Exzesskurtosis macht den Mittelwert oft instabil.

**Question 7: richtige Antworten 1, 2, 4, 5, 6**

- Lorenzkurven zeigen, welchen Anteil an der Gesamtsumme die unteren $p$-Anteile der Einheiten besitzen.
- Sie sind monoton steigend und typischerweise konvex.
- Je weiter unter der Gleichverteilungslinie, desto stärker die Konzentration.

**Question 8-9: bildabhängig.** Ohne Lorenzkurven-Grafik können die Kurvennummern nicht sicher zugeordnet werden.

**Question 10: richtige Antwort: keine**

- Gini der ursprünglichen Kuchenanteile etwa $0.228$, nicht $0.29$.
- Allen $5^\\circ$ abzuziehen ist keine proportionale Skalierung und verändert Gini.
- Das Aufteilen jeder Person in zwei gleiche Teile ändert relative Ungleichheit nicht.""",
10: """### Lösung und Wiederholung

**Question 1: richtige Antworten 1, 3, 7**

- Binomial- und geometrische Verteilung basieren auf Bernoulli-Experimenten.
- Bernoulli ist der Spezialfall der Binomialverteilung mit $n=1$.
- Die Binomialverteilung zählt Erfolge in fester Versuchszahl.
- Die hypergeometrische Verteilung entsteht beim Ziehen ohne Zurücklegen.
- Die Poisson-Verteilung ist diskret; ihre Rate ist die mittlere Ereigniszahl im Intervall.

**Question 2: richtige Antworten 1, 3, 4, 5, 10**

- Dichten enthalten eine Normierungskonstante.
- Exponential- und Gamma-Verteilungen leben auf positiven reellen Zahlen; Gamma mit $\\alpha=1$ ist exponential.
- Die Normalverteilung hat Träger $\\mathbb R$ und nur zwei freie Parameter.
- Die Standardnormaldichte braucht den Faktor $1/\\sqrt{2\\pi}$.
- Beta liegt standardmäßig auf $[0,1]$.
- Cauchy hat Parameter, eignet sich aber für extreme Ausreißer.

**Question 3: richtige Antwort 2**

- Für Poisson gilt $E(X)=Var(X)=\\lambda$.

**Question 4: empfohlene Antworten 1, 2, 4, 5**

- Deterministische Transformationen von Zufallsvariablen sind wieder Zufallsvariablen.
- $Y=X^2$ bei $X>0$ ist monoton transformierbar.
- $\\sin(2\\pi X)$ ist nicht global monoton und braucht eine Mehr-Urbild- oder Stückelungsbehandlung.
- Der Dichtetransformationssatz multipliziert die alte Dichte am Urbild mit dem Betrag der Ableitung der Umkehrfunktion.
- Wird ein kurzes Intervall auf ein langes gestreckt, sinkt die Dichte.""",
11: """### Lösung und Wiederholung

**Question 1: richtige Antworten 1, 3**

- $P(A\\mid B)=P(A)$ bedeutet bei positiven Wahrscheinlichkeiten Unabhängigkeit.
- Bedingte Unabhängigkeit impliziert keine unbedingte Unabhängigkeit.
- Mehrere Ereignisse sind nur dann unabhängig, wenn alle relevanten Teilkombinationen die Unabhängigkeitsbedingungen erfüllen.

**Question 2: richtige Antworten 1, 2, 3, 6**

- Bei diskreten Variablen ist die gemeinsame Masse $P(X=x,Y=y)$.
- Bei stetigen Variablen liefert Integration über einen Bereich dessen Wahrscheinlichkeit.
- Randverteilungen entstehen durch Ausintegrieren der anderen Variable.
- Die gemeinsame Verteilung enthält Abhängigkeitsinformation, die Randverteilungen allein nicht enthalten.
- Produktzerlegung von Dichte oder Verteilungsfunktion ist ein Kriterium für Unabhängigkeit, nicht allgemein wahr.

**Question 3: richtige Antwort 2**

- Ein einziges $y$ mit $f_{X\\mid Y}(x\\mid y)=f_X(x)$ reicht nicht für Unabhängigkeit.
- Ein Nullfeld im Inneren einer ansonsten positiven gemeinsamen Tabelle kann Multiplikationszerlegung unmöglich machen.
- Diskrete und stetige Variablen können gemeinsam modelliert werden; man muss nur die passende Maßnotation verwenden.

**Question 4: richtige Antworten 4, 5**

- $f_{X,Y}(x,y)=f_{Y,X}(y,x)$ ist nur ein Vertauschen der Argumentreihenfolge.
- $P(|X-Y|<3)$ entspricht dem Integral über $y\\in(x-3,x+3)$.
- Randverteilungen bestimmen die gemeinsame Verteilung nicht eindeutig.

**Question 5: bildabhängig**

- Ohne Kontur- und bedingte Dichtegrafik sind 1-3 nicht sicher.
- Aussage 4 ist falsch: korrekt ist $f_X(x)=\\int f_{X\\mid Y=y}(x)f_Y(y)dy$; die Gewichtung mit $f_Y(y)$ darf nicht fehlen.""",
12: """### Lösung und Wiederholung

Der Ausgangstext sagt „wie Test 11“. Daher gelten dieselben Lösungen wie in Test 11: Ereignisunabhängigkeit, Unabhängigkeit von Zufallsvariablen, gemeinsame Verteilung, Randverteilung und bedingte Dichten sind die zentralen Punkte.""",
13: """### Lösung und Wiederholung

**Question 1: richtige Antworten 3, 4**

- Eine positive Kovarianz zeigt gleichsinnige Tendenz.
- Die Größe $35.89$ ist wegen der Einheiten allein schwer interpretierbar; für Stärke braucht man Korrelation.

**Question 2: richtige Antwort 2**

- Je wärmer es ist, desto weniger Kleidungsschichten trägt man typischerweise: negativer Zusammenhang.

**Question 3: richtige Antwort 5**

- $Cov(X,X)=Var(X)$.
- Kovarianz ändert sich bei Skalierung; Korrelation ist standardisiert, kann aber bei negativer Skalierung das Vorzeichen wechseln.
- Nullkorrelation bedeutet nicht Unabhängigkeit.
- $|\\rho|=1$ bedeutet perfekte lineare Beziehung.

**Question 4: richtige Antworten 1, 4, 5**

- Spearman ist Pearson-Korrelation der Ränge.
- Rangkorrelationen sind robuster gegenüber Ausreißern.
- Monotone Zusammenhänge werden durch Ränge linearisiert.
- Korrelationswert $0$ bedeutet nicht empirische Unabhängigkeit.

**Question 5: richtige Antworten 3, 5**

- Distanzkorrelation nutzt paarweise Distanzen aller Beobachtungen.
- Perfekte Pearson-Korrelation impliziert perfekte Spearman-Korrelation.
- Perfekte Spearman-Korrelation impliziert nicht zwingend perfekte Pearson-Korrelation.
- Distanzkorrelation ist nicht negativ.

**Question 6: richtige Antwort 1**

- $r=-0.93$ zeigt einen starken negativen linearen Zusammenhang.

**Question 7: teilweise bildabhängig**

- Die ersten vier Teilfragen brauchen die Jahreszeiten-Streudiagramme.
- Die Korrektur „jedes 10. Ticket fehlt“ ist eine positive lineare Skalierung der Ticketzahlen; Pearson-Korrelation bleibt daher unverändert. Antwort für diese Teilfrage: `0`.""",
14: """### Lösung und Wiederholung

**Question 1: richtige Antwort 4**

- Viele falsch-positive Ergebnisse entstehen bei niedriger Spezifität.

**Question 2: richtige Antwort 1**

- Hohe Sensitivität bedeutet viele wahr-positive und wenige falsch-negative Ergebnisse.

**Question 3: richtige Antwort 2**

- Spezifität ist $P(\\text{Test negativ}\\mid\\text{tatsächlich gesund})$.

**Question 4: empfohlene Antworten 1, 3**

- Wenn nur die Krankenverteilung breiter wird, bleibt die Gesundenverteilung und damit die Spezifität unverändert.
- Bei einem festen Schwellenwert kann eine größere Varianz der Krankenverteilung mehr Kranke unter den Cutoff schieben; Sensitivität sinkt.

**Question 5: ROC und Cutoffs**

- Aus den Daten ergibt sich ungefähr AUC $=7/8=0.875$, also ein starker Zusammenhang zwischen Zungengewicht und Krankheit.
- Eine ROC-Kurve nahe der Diagonalen bedeutet schwache Trennschärfe; nahe am linken oberen bzw. oberen Rand bedeutet gute Trennschärfe.
- Cutoff-Entscheidungen hängen von den Kosten falsch-negativer und falsch-positiver Diagnosen ab.
- Bei $G\\ge106$ als positiv ist $npV=2/(2+1)\\approx67\\%$.
- Bei $G>76$ als positiv ist $ppV=3/(3+0)=100\\%$.

**Question 6: numerische Antworten**

- Gesucht: $2000$, nicht gesucht: $99998000$.
- Sensitivität $99.9\\%$: $A=1998$, $D=2$.
- Spezifität $99.5\\%$: $E=99498010$, $B=499990$.
- $C=A+B=501988$, $F=D+E=99498012$.
- $npV=E/(D+E)\\approx1.000$.
- $ppV=A/(A+B)\\approx0.004$.
- Das zeigt das Grundratenproblem: Bei sehr seltener Zielgruppe sind trotz hoher Testgüte die meisten positiven Alarme falsch.""",
}


def german_from_zh(num: int, zh: str) -> str:
    return ANSWER_NOTES_DE.get(num, "### Lösung\n\nNoch keine deutsche Lösung hinterlegt.\n")


def image_note(block: str) -> str:
    images = re.findall(r"!\[\[([^\]]+)\]\]", block)
    if not images:
        return ""
    names = ", ".join(f"`{name}`" for name in images)
    return (
        "\n\n> 图片处理说明：原文引用了图片 "
        f"{names}。当前目录没有对应图片文件，因此这里保留 Obsidian 图片引用；"
        "需要读图才能确定的解答已标注为“待图片确认”。\n"
    )


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    blocks = split_tests(text)
    for num in range(2, 15):
        block = blocks[num]
        zh_answers = ANSWER_NOTES_ZH[num]
        de_questions = filter_lang(block, "de")
        zh_questions = filter_lang(block, "zh")
        img_note = image_note(block)
        img_note_block = f"{img_note.strip()}\n\n" if img_note.strip() else ""
        content = (
            "## 德文题目\n\n"
            f"{img_note_block}"
            f"{de_questions}\n\n"
            "## 中文题目\n\n"
            f"{zh_questions}\n\n"
            "## 德文解答\n\n"
            f"{german_from_zh(num, zh_answers)}\n\n"
            "## 中文解答\n\n"
            f"{zh_answers.strip()}\n"
        )
        (ROOT / f"测试{CN_DIGITS[num]}.md").write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
