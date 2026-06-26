# AUDIT

生成目录：`考前辅导25_题解Markdown`

## 总体核对

| 项目 | 数量 |
|---|---:|
| 原始 PDF 文件 | 30 |
| 输出 Markdown 题解文件 | 30 |
| 题解 Markdown 额外索引文件 | 3 |
| 输出 `## Aufgabe` 题目数 | 174 |
| 残留 OCR 页标记/乱码检查 | 0 命中 |

说明：`Tag00Aufgaben.pdf` 与 `Tag06_Losungen.pdf` 原先因为没有标准 `Aufgabe` OCR 标题被误计为 0；本次按 PDF 中实际编号练习整理为正式 `## Aufgabe` 标题，因此计入 4 题和 5 题。

## 逐文件题数

| Markdown 文件 | 题数 | 状态 |
|---|---:|---|
| HU2.md | 2 | OK |
| HU4.md | 2 | OK |
| HU7.md | 2 | OK |
| Statistik_Tag2_Aufgaben.md | 13 | OK |
| Statistik2_Tag1_Aufgaben.md | 8 | OK |
| Statistik2_Tag3_Aufgaben.md | 18 | OK |
| Statistik2_Woche_2_Tag3_Aufgaben.md | 14 | OK |
| Statistik2_Woche2_Tag1_Aufgaben.md | 6 | OK |
| Statistik2_Woche2_Tag2_Aufgaben.md | 10 | OK |
| Tag00Aufgaben.md | 4 | OK |
| Tag02Aufgaben_Losungen.md | 3 | OK |
| Tag03Aufgaben_Losung.md | 7 | OK |
| Tag04_Losungen.md | 7 | OK |
| Tag05_Losungen.md | 6 | OK |
| Tag06_Losungen.md | 5 | OK |
| tutorium_tag5_aufgaben.md | 6 | OK |
| woche3.md | 4 | OK |
| woche3_2.md | 5 | OK |
| WTG_Blatt_1.md | 6 | OK |
| WTG_Blatt_10-2.md | 4 | OK |
| WTG_Blatt_11.md | 4 | OK |
| WTG_Blatt_12.md | 3 | OK |
| WTG_Blatt_2.md | 5 | OK |
| WTG_Blatt_3.md | 4 | OK |
| WTG_Blatt_4.md | 4 | OK |
| WTG_Blatt_5.md | 4 | OK |
| WTG_Blatt_6_Losung.md | 4 | OK |
| WTG_Blatt_7.md | 5 | OK |
| WTG_Blatt_8.md | 4 | OK |
| WTG_Blatt_9.md | 5 | OK |
| **Summe** | **174** | **OK** |

## 检查项

- PDF 与 Markdown 主文件一一对应：OK。
- `README.md`、`AUDIT.md`、`THEMEN_INDEX.md` 不计入题解文件数：OK。
- 检查残留 `<!-- Seite -->`：0 命中。
- 检查典型 OCR 乱码和 `(cid:)`：0 命中。
- 公式统一使用 Obsidian 兼容 `$...$` 与 `$$...$$`：已整理。
