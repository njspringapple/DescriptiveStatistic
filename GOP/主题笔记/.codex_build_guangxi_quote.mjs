import fs from "node:fs/promises";
import path from "node:path";
import { Workbook, SpreadsheetFile } from "@oai/artifact-tool";

const root = "D:/mygithub/mynote/DescriptiveStatistic/GOP/主题笔记";
const sourcePath = path.join(root, "广西报价.md");
const outputDir = path.join(root, "outputs", "019fb4bf-cf51-7e10-bb88-f0ccbdb22ba7");
const outputPath = path.join(outputDir, "广西报价-正式版.xlsx");
const previewDir = path.join(outputDir, ".preview");

const UNIT_PRICE = 1200;
const WORKLOAD_FACTOR = 1.30;
const RESEARCH_COST = 50000;
const DELIVERY_COST = 100000;
const THIRD_PARTY_TEST_COST = 30000;
const COPYRIGHT_SUPPORT_COST = 20000;
const VAT_RATE = 0.06;

const estimates = {
  1:  { category: "车辆管理与调度", complexity: "中", days: 32, rationale: "多字段车辆档案、动态状态、图片及里程信息，含基础增删改查和数据校验" },
  2:  { category: "车辆管理与调度", complexity: "高", days: 58, rationale: "事故、年审、维修、保养、保险、器材等多业务链，含到期提醒、统计和历史追溯" },
  3:  { category: "车辆管理与调度", complexity: "高", days: 55, rationale: "审批派遣、派车单打印、车牌门禁联动、车位事件和大屏状态同步" },
  4:  { category: "车辆管理与调度", complexity: "中高", days: 38, rationale: "道闸主动控制、临时回场判断、操作留痕及大屏实时状态联动" },
  5:  { category: "车辆管理与调度", complexity: "中", days: 28, rationale: "运行数据采集/录入、里程与百公里油耗计算、周期统计和趋势展示" },
  6:  { category: "车辆管理与调度", complexity: "中", days: 30, rationale: "按车辆状态、技术状况和用车需求生成排班，含规则校验及制式导出" },
  7:  { category: "人员管理", complexity: "中", days: 36, rationale: "驾驶员档案、照片附件、大屏展示及生物特征授权接口" },
  8:  { category: "人员管理", complexity: "高", days: 55, rationale: "年审、复训、鉴定、违法、评比、训练、黑名单及全过程追溯" },
  9:  { category: "方案与计划", complexity: "高", days: 62, rationale: "六类运输保障方案、模板编制、结构化生成及多格式文档转换" },
  10: { category: "方案与计划", complexity: "高", days: 58, rationale: "六类汽车分队计划、个性化模板、结构化文档生成与格式转换" },
  11: { category: "方案与计划", complexity: "中高", days: 38, rationale: "三类应急预案、模板管理、结构化生成及文档格式转换" },
  12: { category: "教育与训练", complexity: "低", days: 16, rationale: "视频/动画内容上传、分类、播放和基础学习记录" },
  13: { category: "教育与训练", complexity: "低中", days: 18, rationale: "事故案例内容管理、定期更新、组织观看和警示学习记录" },
  14: { category: "教育与训练", complexity: "中", days: 20, rationale: "天气/灾害信息维护、规则分析和季节性风险提醒" },
  15: { category: "教育与训练", complexity: "中高", days: 38, rationale: "训练档案、题库导入导出、随机考试、自动评分和年审数据管理" },
  16: { category: "器材与库存", complexity: "低", days: 14, rationale: "仓库和仓管员基础管理、关联数据删除校验及权限授权" },
  17: { category: "器材与库存", complexity: "中高", days: 36, rationale: "器材主数据、统一编码、上下限预警、台账查询与导出" },
  18: { category: "器材与库存", complexity: "中", days: 30, rationale: "出入库、领用归还、调拨、盘点、盘盈盘亏和统计分析" },
  19: { category: "器材与库存", complexity: "低", days: 14, rationale: "维修设备档案、状态、取用及维修情况动态维护" },
  20: { category: "器材与库存", complexity: "低", days: 14, rationale: "附属油料品种、来源、收发记录和库存状态维护" },
  21: { category: "器材与库存", complexity: "低", days: 14, rationale: "蓄电池档案、充放电记录和到期充电提醒" },
  22: { category: "场区与态势", complexity: "高", days: 58, rationale: "门禁/存取柜/车牌/RFID/人脸等多设备联动，含访客、黑白名单、报警和统计" },
  23: { category: "场区与态势", complexity: "高", days: 68, rationale: "图层、视频、车位、车辆、人员、告警和消息中心聚合，含大屏可视化及报告生成" },
  24: { category: "数据与集成", complexity: "很高", days: 120, rationale: "主数据、权限、车辆/人员/场区/资料、电子履历、批量导入导出和离线数据支撑" },
  25: { category: "数据与集成", complexity: "高", days: 60, rationale: "总部与34个下属单位数据互通、离线运行、恢复上传及同步异常处理" },
  26: { category: "移动端", complexity: "很高", days: 80, rationale: "综合填报APP、服务端接口、附件/数据同步及麒麟、统信等国产系统适配" },
  27: { category: "移动端", complexity: "高", days: 65, rationale: "移动信息APP、服务端接口、移动交互及国产系统兼容测试" },
};

const categoryOrder = ["车辆管理与调度", "人员管理", "方案与计划", "教育与训练", "器材与库存", "场区与态势", "数据与集成", "移动端"];

function cleanText(text) {
  return text
    .replace(/\u00a0/g, " ")
    .replace(/\*\*/g, "")
    .replace(/[ \t]+/g, " ")
    .replace(/\s+([，。；：])/g, "$1")
    .trim();
}

function removeVendorLanguage(text) {
  let out = text;
  out = out.replace(/（[^（）]*(?:需提供生产厂家|生产厂家承诺函)[^（）]*）/g, "");
  out = out.replace(/\([^()]*(?:需提供生产厂家|生产厂家承诺函)[^()]*\)/g, "");
  out = out.replace(/（上述所有内容需提供[^）]*）/g, "");
  return cleanText(out);
}

function stripLeadingLabel(text) {
  const idx = text.indexOf("：");
  if (idx > 0 && idx < 24) return text.slice(idx + 1).trim();
  const ascii = text.indexOf(":");
  if (ascii > 0 && ascii < 24) return text.slice(ascii + 1).trim();
  return text;
}

function splitRequirements(lines) {
  const cleanedLines = [];
  for (const raw of lines) {
    if (/具有自主知识产权.*(?:需提供生产厂家|生产厂家国家版权局)/.test(raw)) continue;
    let line = removeVendorLanguage(raw.replace(/^>\s*/, "").replace(/^▲\s*/, ""));
    if (!line || /^(?:估算人天|估算费用)/.test(line)) continue;
    cleanedLines.push(line);
  }

  const parts = [];
  for (let sourceLine of cleanedLines) {
    sourceLine = stripLeadingLabel(sourceLine);
    sourceLine = sourceLine
      .replace(/（\s*(\d{1,2})\s*）/g, "\n§$1 ")
      .replace(/(^|[；。])\s*([一二三四五六七八九十]+)、/g, "$1\n§ $2、")
      .replace(/(^|[；。\s])\s*(\d{1,2})[\.、](?=[\u4e00-\u9fff“])/g, "$1\n§$2 ");

    let candidates = sourceLine.split(/\n§(?:\d+)?\s*/).map(cleanText).filter(Boolean);
    if (candidates.length === 1 && sourceLine.includes("；")) {
      candidates = sourceLine.split("；").map(cleanText).filter(Boolean);
    }
    for (let candidate of candidates) {
      candidate = candidate
        .replace(/^[\d一二三四五六七八九十]+[\.、]\s*/, "")
        .replace(/^▲?\s*\d+\s+/, "")
        .replace(/[；。]+$/, "")
        .trim();
      if (!candidate) continue;
      if (/^(?:具有自主知识产权|需提供生产厂家|上述所有内容需提供)/.test(candidate)) continue;
      parts.push(candidate);
    }
  }

  return parts.length ? parts : ["需求内容待进一步调研确认"];
}

function parseModules(md) {
  const re = /^### 模块(\d+)：(.+?)（对应(?:序号)?(.+?)）\s*$([\s\S]*?)(?=^### 模块\d+：|^## 三、|\z)/gm;
  const modules = [];
  for (const match of md.matchAll(re)) {
    const no = Number(match[1]);
    const title = cleanText(match[2]);
    const corresponding = cleanText(match[3]);
    const block = match[4];
    const quoteLines = block.split(/\r?\n/).filter((line) => /^>/.test(line.trim()));
    const requirements = splitRequirements(quoteLines);
    const estimate = estimates[no];
    if (!estimate) throw new Error(`Missing estimate for module ${no}`);
    modules.push({
      no,
      title,
      corresponding,
      requirements,
      ...estimate,
      days: Number((estimate.days * WORKLOAD_FACTOR).toFixed(1)),
    });
  }
  if (modules.length !== 27) throw new Error(`Expected 27 modules, parsed ${modules.length}`);
  return modules;
}

function a1Col(n) {
  let s = "";
  while (n > 0) {
    n--;
    s = String.fromCharCode(65 + (n % 26)) + s;
    n = Math.floor(n / 26);
  }
  return s;
}

const colors = {
  navy: "#17365D",
  blue: "#1F4E78",
  blue2: "#D9EAF7",
  blue3: "#EAF3F8",
  teal: "#0F6B78",
  green: "#E2F0D9",
  greenText: "#2F6B2F",
  amber: "#FFF2CC",
  amberText: "#8A5A00",
  red: "#FCE4D6",
  redText: "#A61C00",
  gray: "#F2F2F2",
  gray2: "#D9E1F2",
  line: "#C9D2DC",
  white: "#FFFFFF",
  black: "#1F1F1F",
  inputBlue: "#0000FF",
};

function setBaseFont(range, size = 10) {
  range.format.font = { name: "Microsoft YaHei", size, color: colors.black };
  range.format.verticalAlignment = "center";
}

function styleTitle(sheet, address, title, subtitle = null) {
  const range = sheet.getRange(address);
  range.merge();
  range.values = [[title]];
  range.format = {
    fill: colors.navy,
    font: { name: "Microsoft YaHei", size: 18, bold: true, color: colors.white },
    horizontalAlignment: "left",
    verticalAlignment: "center",
  };
  range.format.rowHeight = 34;
  if (subtitle) {
    const parts = address.match(/([A-Z]+)(\d+):([A-Z]+)(\d+)/);
    const nextRow = Number(parts[2]) + 1;
    const sub = sheet.getRange(`${parts[1]}${nextRow}:${parts[3]}${nextRow}`);
    sub.merge();
    sub.values = [[subtitle]];
    sub.format = {
      fill: colors.blue3,
      font: { name: "Microsoft YaHei", size: 9, color: colors.blue },
      horizontalAlignment: "left",
      verticalAlignment: "center",
      wrapText: true,
    };
    sub.format.rowHeight = 26;
  }
}

function styleHeader(range) {
  range.format = {
    fill: colors.blue,
    font: { name: "Microsoft YaHei", size: 10, bold: true, color: colors.white },
    horizontalAlignment: "center",
    verticalAlignment: "center",
    wrapText: true,
    borders: { preset: "all", style: "thin", color: colors.line },
  };
  range.format.rowHeight = 30;
}

function styleTableBody(range) {
  setBaseFont(range, 10);
  range.format.wrapText = true;
  range.format.borders = {
    insideHorizontal: { style: "thin", color: "#DCE3EA" },
    insideVertical: { style: "thin", color: "#E6EBF0" },
    bottom: { style: "thin", color: colors.line },
  };
}

function createParametersSheet(workbook, modules) {
  const sheet = workbook.worksheets.add("参数与校验");
  sheet.showGridLines = false;
  styleTitle(sheet, "A1:F1", "报价参数与计算校验", "蓝色数字为可编辑输入；金额公式自动更新。当前口径：开发＋测试 1,200 元/人天，固定服务费参与计税。 ");

  sheet.getRange("A4:B4").values = [["参数", "数值"]];
  styleHeader(sheet.getRange("A4:B4"));
  const inputs = [
    ["开发＋测试人天单价（元/人天）", UNIT_PRICE],
    ["需求调研成本（元）", RESEARCH_COST],
    ["交付实施差旅人工（元）", DELIVERY_COST],
    ["配合第三方软件测试（元）", THIRD_PARTY_TEST_COST],
    ["配合软件著作权办理（元）", COPYRIGHT_SUPPORT_COST],
    ["增值税率", VAT_RATE],
  ];
  sheet.getRange("A5:B10").values = inputs;
  styleTableBody(sheet.getRange("A5:B10"));
  sheet.getRange("B5:B10").format.font = { name: "Microsoft YaHei", size: 10, color: colors.inputBlue };
  sheet.getRange("B5:B9").format.numberFormat = "¥#,##0";
  sheet.getRange("B10").format.numberFormat = "0%";
  sheet.getRange("A5:A10").format.fill = colors.blue3;

  sheet.getRange("D4:F4").values = [["校验项", "结果", "状态"]];
  styleHeader(sheet.getRange("D4:F4"));
  const totalDays = modules.reduce((s, m) => s + m.days, 0);
  const removedTextPass = modules.every((m) => m.requirements.every((x) => !/(承诺函|需提供生产厂家)/.test(x)));
  sheet.getRange("D5:D10").values = [
    ["模块数量应为27"],
    ["估算工作量合计"],
    ["模块金额＝工作量×单价"],
    ["未税金额＝模块费＋固定服务费"],
    ["价税合计＝未税金额＋税额"],
    ["非功能资质类表述已清理"],
  ];
  sheet.getRange("E5").formulas = [["=COUNTA('模块报价'!$A$6:$A$32)"]];
  sheet.getRange("E6").formulas = [["=SUM('模块报价'!$F$6:$F$32)"]];
  sheet.getRange("E7").formulas = [["=SUM('模块报价'!$H$6:$H$32)-E6*$B$5"]];
  sheet.getRange("E8").formulas = [["='报价总览'!$B$22-SUM('模块报价'!$H$6:$H$32)-SUM($B$6:$B$9)"]];
  sheet.getRange("E9").formulas = [["='报价总览'!$B$24-'报价总览'!$B$22-'报价总览'!$B$23"]];
  sheet.getRange("E10").values = [[removedTextPass ? 0 : 1]];
  sheet.getRange("F5").formulas = [["=IF(E5=27,\"PASS\",\"FAIL\")"]];
  sheet.getRange("F6").formulas = [[`=IF(E6=${totalDays},\"PASS\",\"FAIL\")`]];
  sheet.getRange("F7:F10").formulas = [["=IF(ABS(E7)<0.01,\"PASS\",\"FAIL\")"],["=IF(ABS(E8)<0.01,\"PASS\",\"FAIL\")"],["=IF(ABS(E9)<0.01,\"PASS\",\"FAIL\")"],["=IF(E10=0,\"PASS\",\"FAIL\")"]];
  styleTableBody(sheet.getRange("D5:F10"));
  sheet.getRange("F5:F10").format.font = { name: "Microsoft YaHei", size: 10, bold: true, color: colors.greenText };
  sheet.getRange("E6").format.numberFormat = "#,##0.0";
  sheet.getRange("E7:E10").format.numberFormat = "0.00";
  sheet.getRange("A13:F13").merge();
  sheet.getRange("A13:F13").values = [["估算边界与使用说明"]];
  sheet.getRange("A13:F13").format = { fill: colors.blue, font: { name: "Microsoft YaHei", size: 11, bold: true, color: colors.white } };
  const notes = [
    "1. 人天为开发＋测试口径，含模块编码、单元测试、集成测试及常规联调；需求调研和现场交付另行列示。",
    "2. 估算依据为当前需求文字。接口协议、制式表单数量、数据迁移量、国产化环境、离线同步策略和硬件设备协议确认后，应复核人天。",
    "3. 不含服务器、门禁、道闸、大屏、摄像头、RFID、打印设备等硬件采购和安装费用。",
    "4. 不含云资源/专线、短信、地图、商业中间件、OFD转换组件等第三方授权或持续服务费用。",
    "5. 配合第三方测试按3万元计，配合软件著作权办理按2万元计；若测试机构或知识产权代理机构直接收费，以实际合同为准。",
    "6. 增值税按未税项目总额的6%计算；如开票政策或税率发生变化，以实际开票为准。",
  ];
  sheet.getRange("A14:F19").merge(true);
  sheet.getRange("A14:A19").values = notes.map((x) => [x]);
  sheet.getRange("A14:F19").format = {
    fill: colors.gray,
    font: { name: "Microsoft YaHei", size: 10, color: colors.black },
    verticalAlignment: "center",
    wrapText: true,
  };
  sheet.getRange("A14:F19").format.rowHeight = 30;

  sheet.getRange("A1:F19").format.borders = { preset: "outside", style: "thin", color: colors.line };
  sheet.getRange("A:A").format.columnWidth = 35;
  sheet.getRange("B:B").format.columnWidth = 16;
  sheet.getRange("C:C").format.columnWidth = 3;
  sheet.getRange("D:D").format.columnWidth = 28;
  sheet.getRange("E:E").format.columnWidth = 16;
  sheet.getRange("F:F").format.columnWidth = 12;
  sheet.freezePanes.freezeRows(4);
  return sheet;
}

function createModuleSheet(workbook, modules) {
  const sheet = workbook.worksheets.add("模块报价");
  sheet.showGridLines = false;
  styleTitle(sheet, "A1:I1", "软件模块估算工作量与未税报价明细", "工作量已按模块复杂度、业务链数量、接口/设备联动、国产化适配及离线同步风险综合估算。蓝色人天可按最终SRS调整。 ");
  sheet.getRange("A4:I4").merge();
  sheet.getRange("A4:I4").values = [["金额口径：模块未税金额＝估算工作量 × 1,200 元/人天。需求调研、交付实施、第三方测试配合、软著办理配合及增值税在总览中另计。"]];
  sheet.getRange("A4:I4").format = { fill: colors.amber, font: { name: "Microsoft YaHei", size: 10, color: colors.amberText }, wrapText: true };
  sheet.getRange("A4:I4").format.rowHeight = 28;
  sheet.getRange("A5:I5").values = [["模块", "业务域", "对应需求序号", "模块名称", "复杂度", "估算工作量（人天）", "单价（元/人天）", "模块未税金额（元）", "估算依据"]];
  styleHeader(sheet.getRange("A5:I5"));
  const start = 6;
  const end = start + modules.length - 1;
  const rows = modules.map((m) => [m.no, m.category, m.corresponding, m.title, m.complexity, m.days, null, null, m.rationale]);
  sheet.getRange(`A${start}:I${end}`).values = rows;
  sheet.getRange(`G${start}`).formulas = [["='参数与校验'!$B$5"]];
  sheet.getRange(`G${start}:G${end}`).fillDown();
  sheet.getRange(`H${start}`).formulas = [[`=F${start}*G${start}`]];
  sheet.getRange(`H${start}:H${end}`).fillDown();
  styleTableBody(sheet.getRange(`A${start}:I${end}`));
  sheet.getRange(`A${start}:A${end}`).format.horizontalAlignment = "center";
  sheet.getRange(`B${start}:E${end}`).format.horizontalAlignment = "center";
  sheet.getRange(`F${start}:H${end}`).format.horizontalAlignment = "right";
  sheet.getRange(`F${start}:F${end}`).format.font = { name: "Microsoft YaHei", size: 10, color: colors.inputBlue };
  sheet.getRange(`F${start}:F${end}`).format.numberFormat = "#,##0.0";
  sheet.getRange(`G${start}:G${end}`).format.numberFormat = "#,##0";
  sheet.getRange(`H${start}:H${end}`).format.numberFormat = "¥#,##0";
  sheet.getRange(`A${start}:I${end}`).format.rowHeight = 36;
  for (let r = start; r <= end; r++) {
    if ((r - start) % 2 === 1) sheet.getRange(`A${r}:I${r}`).format.fill = "#F8FAFC";
  }
  const totalRow = end + 1;
  sheet.getRange(`A${totalRow}:E${totalRow}`).merge();
  sheet.getRange(`A${totalRow}:E${totalRow}`).values = [["软件模块合计"]];
  sheet.getRange(`F${totalRow}`).formulas = [[`=SUM(F${start}:F${end})`]];
  sheet.getRange(`G${totalRow}`).values = [[null]];
  sheet.getRange(`H${totalRow}`).formulas = [[`=SUM(H${start}:H${end})`]];
  sheet.getRange(`I${totalRow}`).values = [["不含固定服务费及增值税"]];
  sheet.getRange(`A${totalRow}:I${totalRow}`).format = {
    fill: colors.blue2,
    font: { name: "Microsoft YaHei", size: 10, bold: true, color: colors.navy },
    verticalAlignment: "center",
    borders: { preset: "all", style: "thin", color: colors.line },
  };
  sheet.getRange(`F${totalRow}`).format.numberFormat = "#,##0.0";
  sheet.getRange(`H${totalRow}`).format.numberFormat = "¥#,##0";
  sheet.getRange(`A${totalRow}:I${totalRow}`).format.rowHeight = 28;
  const table = sheet.tables.add(`A5:I${end}`, true, "ModuleQuoteTable");
  table.style = "TableStyleMedium2";
  table.showFilterButton = true;
  sheet.freezePanes.freezeRows(5);
  sheet.freezePanes.freezeColumns(4);
  const widths = [8, 18, 15, 24, 10, 16, 16, 19, 52];
  widths.forEach((w, i) => { sheet.getRange(`${a1Col(i + 1)}:${a1Col(i + 1)}`).format.columnWidth = w; });
  return sheet;
}

function chunkRequirements(items, maxItems = 4, maxChars = 560) {
  const chunks = [];
  let current = [];
  let chars = 0;
  for (let i = 0; i < items.length; i++) {
    const item = `${i + 1}. ${items[i]}`;
    if (current.length && (current.length >= maxItems || chars + item.length > maxChars)) {
      chunks.push(current);
      current = [];
      chars = 0;
    }
    current.push(item);
    chars += item.length;
  }
  if (current.length) chunks.push(current);
  return chunks;
}

function createRequirementsSheet(workbook, modules) {
  const sheet = workbook.worksheets.add("需求明细");
  sheet.showGridLines = false;
  styleTitle(sheet, "A1:F1", "完整需求明细", "每个需求项均按 1.、2.、3.……逐行排列；较长模块分段展示，条目编号在同一模块内连续。 ");
  sheet.getRange("A4:F4").values = [["模块", "对应需求序号", "业务域", "模块名称", "分段", "需求内容（逐项换行）"]];
  styleHeader(sheet.getRange("A4:F4"));
  const rows = [];
  for (const m of modules) {
    const chunks = chunkRequirements(m.requirements);
    chunks.forEach((chunk, idx) => {
      rows.push([m.no, m.corresponding, m.category, m.title, `${idx + 1}/${chunks.length}`, chunk.join("\n")]);
    });
  }
  const start = 5;
  const end = start + rows.length - 1;
  sheet.getRange(`A${start}:F${end}`).values = rows;
  styleTableBody(sheet.getRange(`A${start}:F${end}`));
  sheet.getRange(`A${start}:E${end}`).format.horizontalAlignment = "center";
  sheet.getRange(`F${start}:F${end}`).format.horizontalAlignment = "left";
  for (let i = 0; i < rows.length; i++) {
    const r = start + i;
    const lines = String(rows[i][5]).split("\n").length;
    const chars = String(rows[i][5]).length;
    const height = Math.min(150, Math.max(38, lines * 18 + Math.ceil(chars / 80) * 10));
    sheet.getRange(`A${r}:F${r}`).format.rowHeight = height;
    if (i % 2 === 1) sheet.getRange(`A${r}:F${r}`).format.fill = "#F8FAFC";
  }
  const table = sheet.tables.add(`A4:F${end}`, true, "RequirementsTable");
  table.style = "TableStyleMedium2";
  table.showFilterButton = true;
  sheet.freezePanes.freezeRows(4);
  sheet.freezePanes.freezeColumns(4);
  const widths = [8, 15, 18, 24, 8, 100];
  widths.forEach((w, i) => { sheet.getRange(`${a1Col(i + 1)}:${a1Col(i + 1)}`).format.columnWidth = w; });
  return { sheet, end, rows };
}

function createSummarySheet(workbook, modules) {
  const sheet = workbook.worksheets.add("报价总览");
  sheet.showGridLines = false;
  styleTitle(sheet, "A1:H1", "广西项目软件系统开发报价估算", "基于当前需求清单编制｜版本：V1.0｜报价日期：2026-08-19｜单位：人民币元（含税总价另行列示）");

  sheet.getRange("A4:B4").merge();
  sheet.getRange("A4:B4").values = [["报价对象"]];
  sheet.getRange("C4:D4").merge();
  sheet.getRange("C4:D4").values = [["广西项目（具体名称待补充）"]];
  sheet.getRange("E4:F4").merge();
  sheet.getRange("E4:F4").values = [["报价单位"]];
  sheet.getRange("G4:H4").merge();
  sheet.getRange("G4:H4").values = [["待补充"]];
  sheet.getRange("A4:H4").format = { fill: colors.gray, font: { name: "Microsoft YaHei", size: 10, color: colors.black }, borders: { preset: "all", style: "thin", color: colors.line } };
  sheet.getRange("A4:B4,E4:F4").format.font = { name: "Microsoft YaHei", size: 10, bold: true, color: colors.navy };

  const cards = [
    ["模块数量", "=COUNTA('模块报价'!$A$6:$A$32)", "个"],
    ["估算工作量", "=SUM('模块报价'!$F$6:$F$32)", "人天"],
    ["软件模块费", "=SUM('模块报价'!$H$6:$H$32)", "元"],
    ["含税总价", "=$B$24", "元"],
  ];
  const cardStarts = ["A6:B8", "C6:D8", "E6:F8", "G6:H8"];
  cards.forEach((card, i) => {
    const [label, formula, unit] = card;
    const match = cardStarts[i].match(/([A-Z])(\d+):([A-Z])(\d+)/);
    const c1 = match[1], r1 = Number(match[2]), c2 = match[3], r2 = Number(match[4]);
    sheet.getRange(`${c1}${r1}:${c2}${r1}`).merge();
    sheet.getRange(`${c1}${r1}:${c2}${r1}`).values = [[label]];
    sheet.getRange(`${c1}${r1 + 1}:${c2}${r2 - 1}`).merge();
    sheet.getRange(`${c1}${r1 + 1}`).formulas = [[formula]];
    sheet.getRange(`${c1}${r2}:${c2}${r2}`).merge();
    sheet.getRange(`${c1}${r2}:${c2}${r2}`).values = [[unit]];
    const fill = i === 3 ? colors.green : colors.blue3;
    const fontColor = i === 3 ? colors.greenText : colors.blue;
    sheet.getRange(cardStarts[i]).format = { fill, font: { name: "Microsoft YaHei", size: 9, color: fontColor }, horizontalAlignment: "center", verticalAlignment: "center", borders: { preset: "outside", style: "thin", color: colors.line } };
    sheet.getRange(`${c1}${r1 + 1}`).format.font = { name: "Microsoft YaHei", size: i >= 2 ? 14 : 16, bold: true, color: fontColor };
    sheet.getRange(`${c1}${r1 + 1}`).format.numberFormat = i >= 2 ? "¥#,##0" : (i === 1 ? "#,##0.0" : "#,##0");
  });

  sheet.getRange("A11:D11").values = [["费用构成", "数量/基数", "单价/税率", "未税金额（元）"]];
  styleHeader(sheet.getRange("A11:D11"));
  const costRows = [
    ["软件模块开发＋测试", null, null, null],
    ["需求调研", 1, null, null],
    ["交付实施差旅人工", 1, null, null],
    ["配合第三方软件测试", 1, null, null],
    ["配合软件著作权办理", 1, null, null],
  ];
  sheet.getRange("A12:D16").values = costRows;
  sheet.getRange("B12").formulas = [["=SUM('模块报价'!$F$6:$F$32)"]];
  sheet.getRange("C12").formulas = [["='参数与校验'!$B$5"]];
  sheet.getRange("D12").formulas = [["=SUM('模块报价'!$H$6:$H$32)"]];
  sheet.getRange("C13:C16").formulas = [["='参数与校验'!$B$6"],["='参数与校验'!$B$7"],["='参数与校验'!$B$8"],["='参数与校验'!$B$9"]];
  sheet.getRange("D13").formulas = [["=B13*C13"]];
  sheet.getRange("D13:D16").fillDown();
  styleTableBody(sheet.getRange("A12:D16"));
  sheet.getRange("B12:D16").format.horizontalAlignment = "right";
  sheet.getRange("B12").format.numberFormat = "#,##0.0";
  sheet.getRange("B13:B16").format.numberFormat = "#,##0";
  sheet.getRange("C12:D16").format.numberFormat = "¥#,##0";
  sheet.getRange("A17:C17").merge();
  sheet.getRange("A17:C17").values = [["未税项目合计"]];
  sheet.getRange("D17").formulas = [["=SUM(D12:D16)"]];
  sheet.getRange("A17:D17").format = { fill: colors.blue2, font: { name: "Microsoft YaHei", size: 10, bold: true, color: colors.navy }, borders: { preset: "all", style: "thin", color: colors.line } };
  sheet.getRange("D17").format.numberFormat = "¥#,##0";

  sheet.getRange("A20:B20").values = [["价税汇总", "金额（元）"]];
  styleHeader(sheet.getRange("A20:B20"));
  sheet.getRange("A21:A24").values = [["软件开发测试费"],["未税总额"],["增值税（6%）"],["价税合计"]];
  sheet.getRange("B21").formulas = [["=D12"]];
  sheet.getRange("B22").formulas = [["=D17"]];
  sheet.getRange("B23").formulas = [["=B22*'参数与校验'!$B$10"]];
  sheet.getRange("B24").formulas = [["=B22+B23"]];
  styleTableBody(sheet.getRange("A21:B24"));
  sheet.getRange("B21:B24").format.numberFormat = "¥#,##0";
  sheet.getRange("A24:B24").format = { fill: colors.green, font: { name: "Microsoft YaHei", size: 12, bold: true, color: colors.greenText }, borders: { preset: "doubleBottom", style: "medium", color: colors.greenText } };

  sheet.getRange("D20:H20").merge();
  sheet.getRange("D20:H20").values = [["报价说明"]];
  sheet.getRange("D20:H20").format = { fill: colors.blue, font: { name: "Microsoft YaHei", size: 10, bold: true, color: colors.white } };
  sheet.getRange("D21:H24").merge();
  sheet.getRange("D21:H24").values = [[
    "• 本报价以当前需求清单为估算基础，建议在需求调研和SRS确认后形成最终合同价。\n" +
    "• 软件模块按估算工作量和1,200元/人天计算。\n" +
    "• 需求调研5万元；交付实施差旅人工10万元。\n" +
    "• 配合第三方软件测试3万元；配合软件著作权办理2万元。\n" +
    "• 所有上述费用统一按6%增值税计税；不含硬件采购及第三方商业授权。"
  ]];
  sheet.getRange("D21:H24").format = { fill: colors.amber, font: { name: "Microsoft YaHei", size: 10, color: colors.amberText }, verticalAlignment: "top", wrapText: true, borders: { preset: "outside", style: "thin", color: colors.line } };

  sheet.getRange("A27:H27").merge();
  sheet.getRange("A27:H27").values = [["分类人天概览"]];
  sheet.getRange("A27:H27").format = { fill: colors.blue, font: { name: "Microsoft YaHei", size: 10, bold: true, color: colors.white } };
  sheet.getRange("A28:C28").values = [["业务域", "模块数", "建议人天"]];
  styleHeader(sheet.getRange("A28:C28"));
  const catRows = categoryOrder.map((cat) => {
    const ms = modules.filter((m) => m.category === cat);
    return [cat, ms.length, ms.reduce((s, m) => s + m.days, 0)];
  });
  sheet.getRange(`A29:C${28 + catRows.length}`).values = catRows;
  styleTableBody(sheet.getRange(`A29:C${28 + catRows.length}`));
  sheet.getRange(`B29:B${28 + catRows.length}`).format.numberFormat = "#,##0";
  sheet.getRange(`C29:C${28 + catRows.length}`).format.numberFormat = "#,##0.0";
  sheet.getRange(`B29:C${28 + catRows.length}`).format.horizontalAlignment = "right";
  sheet.getRange("E28:H28").merge();
  sheet.getRange("E28:H28").values = [["关键风险提示"]];
  styleHeader(sheet.getRange("E28:H28"));
  sheet.getRange("E29:H36").merge();
  sheet.getRange("E29:H36").values = [[
    "1. 模块22、23涉及门禁、道闸、RFID、人脸、大屏和视频等设备/平台接口，协议不明确会显著影响联调成本。\n" +
    "2. 模块9—11涉及Word/PDF/OFD生成与转换，应明确模板数量、版式精度和转换组件授权。\n" +
    "3. 模块24、25涉及多单位数据、离线运行和恢复同步，应在SRS中明确数据量、冲突策略、加密和审计要求。\n" +
    "4. 模块26、27的国产操作系统版本、设备型号和应用商店/签名方式需在开发前锁定。\n" +
    "5. 若新增等保、密评、信创测评、数据迁移清洗或驻场周期，应另行核价。"
  ]];
  sheet.getRange("E29:H36").format = { fill: colors.red, font: { name: "Microsoft YaHei", size: 10, color: colors.redText }, verticalAlignment: "top", wrapText: true, borders: { preset: "outside", style: "thin", color: colors.line } };

  const widths = [19, 16, 16, 18, 19, 16, 16, 18];
  widths.forEach((w, i) => { sheet.getRange(`${a1Col(i + 1)}:${a1Col(i + 1)}`).format.columnWidth = w; });
  sheet.getRange("A1:H36").format.borders = { preset: "outside", style: "thin", color: colors.line };
  sheet.freezePanes.freezeRows(2);
  return sheet;
}

async function build() {
  const md = await fs.readFile(sourcePath, "utf8");
  const modules = parseModules(md);
  const totalDays = modules.reduce((s, m) => s + m.days, 0);
  const moduleCost = totalDays * UNIT_PRICE;
  const fixedCost = RESEARCH_COST + DELIVERY_COST + THIRD_PARTY_TEST_COST + COPYRIGHT_SUPPORT_COST;
  const preTax = moduleCost + fixedCost;
  const vat = preTax * VAT_RATE;
  const taxIncluded = preTax + vat;

  if (totalDays !== 1501.5) throw new Error(`Unexpected total days ${totalDays}`);
  if (moduleCost !== 1801800 || preTax !== 2001800 || vat !== 120108 || taxIncluded !== 2121908) {
    throw new Error("Pricing arithmetic mismatch");
  }
  const forbidden = modules.flatMap((m) => m.requirements).filter((x) => /(承诺函|需提供生产厂家)/.test(x));
  if (forbidden.length) throw new Error(`Forbidden vendor language remains: ${forbidden[0]}`);

  const workbook = Workbook.create();
  const summary = createSummarySheet(workbook, modules);
  const moduleSheet = createModuleSheet(workbook, modules);
  const req = createRequirementsSheet(workbook, modules);
  const checks = createParametersSheet(workbook, modules);

  await fs.mkdir(outputDir, { recursive: true });
  await fs.mkdir(previewDir, { recursive: true });

  const inspections = [];
  inspections.push((await workbook.inspect({ kind: "table", range: "报价总览!A1:H36", include: "values,formulas", tableMaxRows: 40, tableMaxCols: 10, maxChars: 12000 })).ndjson);
  inspections.push((await workbook.inspect({ kind: "table", range: "模块报价!A1:I33", include: "values,formulas", tableMaxRows: 40, tableMaxCols: 10, maxChars: 14000 })).ndjson);
  inspections.push((await workbook.inspect({ kind: "table", range: "参数与校验!A1:F19", include: "values,formulas", tableMaxRows: 30, tableMaxCols: 8, maxChars: 9000 })).ndjson);
  const errors = await workbook.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 100 }, summary: "final formula error scan" });
  inspections.push(errors.ndjson);
  await fs.writeFile(path.join(previewDir, "inspection.txt"), inspections.join("\n\n"), "utf8");

  const previews = [
    ["报价总览", "A1:H36", "01-summary.png"],
    ["模块报价", "A1:I33", "02-modules.png"],
    ["需求明细", "A1:F35", "03-requirements-start.png"],
    ["需求明细", `A${Math.max(5, req.end - 34)}:F${req.end}`, "04-requirements-end.png"],
    ["参数与校验", "A1:F19", "05-parameters-checks.png"],
  ];
  for (const [sheetName, range, file] of previews) {
    const blob = await workbook.render({ sheetName, range, scale: 1.25, format: "png" });
    await fs.writeFile(path.join(previewDir, file), new Uint8Array(await blob.arrayBuffer()));
  }

  const out = await SpreadsheetFile.exportXlsx(workbook);
  await out.save(outputPath);
  console.log(JSON.stringify({ outputPath, moduleCount: modules.length, requirementRows: req.rows.length, totalDays, moduleCost, fixedCost, preTax, vat, taxIncluded, previews: previews.map((x) => x[2]) }, null, 2));
}

await build();
