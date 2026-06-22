# 描述性统计分章节中文讲义处理计划

> 范围：正式章节 `01` 到 `12`。`00_前置页.pdf` 作为前置材料，不计入 12 个正式章节。  
> 输出原则：每章一个独立目录，目录内包含中文 Markdown 与 `assets/` 图片目录。  
> 质量底线：不以批量整页截图冒充精准裁图；图表页必须保留理解所需的标题、坐标轴、图例、表格或图注。

## 统一目录结构

```text
分章节讲义/
  中文讲义/
    manifest.json
    README_处理计划.md
    01_Einfuehrung/
      assets/
      01_Einfuehrung_中文讲义.md
    ...
    12_Korrelation_Kausalitaet/
      assets/
      12_Korrelation_Kausalitaet_中文讲义.md
```

## 每章完成标准

- Markdown 按原 PDF 页码逐页覆盖，不跳页。
- 中文翻译保留德语关键词，关键词后紧跟括号内德语原词。
- 对公式不照搬抽取碎片，而是重新排成可读 LaTeX。
- 图片统一放入本章 `assets/`，Markdown 使用相对链接 `assets/...png`。
- 图表裁切必须通过人工视觉抽查；必要时保留整块图表上下文，而不是只裁曲线。
- 每章末尾必须有：逻辑梳理、关键考核点、小测验、德语词汇表、C1 级德语句式。
- 质检必须检查：页码覆盖、图片链接存在、图片裁切没有切字/切轴/切图例。

## 章节任务看板

| 章节 | PDF | 页数 | 文本字符 | 图片/绘图风险 | 状态 |
|---|---|---:|---:|---|---|
| 01 | `01_Einführung.pdf` | 58 | 33803 | 中：有 11 页嵌入图片 | 已完成，质检通过 |
| 02 | `02_Datenerhebung & Messung.pdf` | 31 | 11397 | 低：1 页嵌入图片 | 已完成，质检通过 |
| 03 | `03_Wahrscheinlichkeit_ Grundlagen & Definitionen.pdf` | 52 | 20253 | 低：少量绘图页 | 已完成，质检通过 |
| 04 | `04_Zusammenhangsmaße für diskrete Merkmale.pdf` | 57 | 21526 | 低：少量绘图页 | 已完成，质检通过 |
| 05 | `05_Zufallsvariablen, Verteilungen & Häufigkeiten.pdf` | 37 | 13678 | 中：1 页图片，4 页绘图 | 已完成，质检通过 |
| 06 | `06_Statistische Grafiken.pdf` | 91 | 27360 | 极高：24 页图片，40 页绘图 | 已完成，质检通过 |
| 07 | `07_Kennwerte & Verteilungseigenschaften.pdf` | 84 | 31020 | 高：图片和绘图混合 | 已完成，待最终总复核 |
| 08 | `08_Wichtige parametrische Verteilungen.pdf` | 56 | 19191 | 高：21 页绘图 | 已完成，质检通过 |
| 09 | `09_Zufallsvektoren & multivariate Verteilungen.pdf` | 43 | 17121 | 中：3 页图片，4 页绘图 | 已完成，质检通过 |
| 10 | `10_Schätzung & Grenzwertsätze.pdf` | 28 | 12019 | 中：1 页图片，8 页绘图 | 已完成，质检通过 |
| 11 | `11_Zusammenhangsmaße für metrische Merkmale.pdf` | 72 | 29199 | 高：2 页图片，28 页绘图 | 已完成，质检通过 |
| 12 | `12_Korrelation & Kausalität.pdf` | 38 | 11846 | 高：3 页图片，16 页绘图 | 已完成，质检通过 |

## 批次安排

1. **批次 A：结构较轻章节**  
   02、03、04、05、10。目标是先稳定翻译模板、公式重排和词汇表风格。

2. **批次 B：图形密集章节**  
   06、08、11、12。目标是重点处理图表裁切，先做图片总览，再逐页决定是否裁图。

3. **批次 C：导论与综合章节**  
   01、09。目标是统一前置概念、随机向量与多变量分布的术语。

4. **批次 D：全局复核**  
   全部 Markdown 做页码覆盖、图片链接、术语一致性、德语句式质量复查。

## 当前文件与脚本

- 预处理脚本：`scripts/prepare_lecture_chapters.py`
- 第 7 章裁图脚本：`scripts/crop_ch07_pdf_figures.py`
- 临时渲染与文本抽取目录：`.codex-tmp/lecture_chapters/`

## 风险记录

- Poppler 渲染会输出字体替代警告，但页面 PNG 已生成；后续以视觉抽查为准。
- PDF 文本层中的公式顺序会碎裂，正式 Markdown 中必须人工重排公式。
- 图表密集章节不能只依赖对象统计，必须查看 contact sheet 和关键页原图。
