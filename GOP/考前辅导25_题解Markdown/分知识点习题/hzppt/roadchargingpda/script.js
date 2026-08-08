(() => {
  "use strict";

  const VERSION = "V1.0.8";
  const DEVICE_ID = "PDA-8891";
  const VALID_EMPLOYEE = "A00123";

  const iconPaths = {
    home: '<path d="M3 10.8 12 3l9 7.8v9.1a1.1 1.1 0 0 1-1.1 1.1h-5.3v-6.5H9.4V21H4.1A1.1 1.1 0 0 1 3 19.9Z"/><path d="M8.5 21v-6.5h7V21"/>',
    berth: '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 17V7h4.2a3 3 0 0 1 0 6H8m4.1 0H8"/>',
    ticket: '<path d="M5 3h14v18l-3-2-4 2-4-2-3 2Z"/><path d="M8 8h8M8 12h8M8 16h5"/>',
    report: '<path d="M4 20V9m5 11V4m6 16v-7m5 7V7"/><path d="M2 21h20"/>',
    user: '<circle cx="12" cy="8" r="4"/><path d="M4.5 21a7.5 7.5 0 0 1 15 0"/>',
    back: '<path d="m15 18-6-6 6-6"/>',
    location: '<path d="M12 21s7-6.1 7-12a7 7 0 1 0-14 0c0 5.9 7 12 7 12Z"/><circle cx="12" cy="9" r="2.4"/>',
    bell: '<path d="M18 8a6 6 0 0 0-12 0c0 7-3 7-3 9h18c0-2-3-2-3-9"/><path d="M10 21h4"/>',
    search: '<circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/>',
    refresh: '<path d="M20 11a8 8 0 1 0-2.3 5.7"/><path d="M20 4v7h-7"/>',
    chevron: '<path d="m9 18 6-6-6-6"/>',
    close: '<path d="m6 6 12 12M18 6 6 18"/>',
    camera: '<path d="M4 7h3l2-3h6l2 3h3v13H4Z"/><circle cx="12" cy="13" r="4"/>',
    check: '<path d="m5 12 4 4L19 6"/>',
    clock: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    print: '<path d="M6 9V3h12v6"/><rect x="4" y="9" width="16" height="8" rx="2"/><path d="M7 14h10v7H7Z"/>',
    car: '<path d="m5 16 1.7-6h10.6l1.7 6"/><path d="M3 16h18v4H3Z"/><circle cx="7" cy="20" r="1.5"/><circle cx="17" cy="20" r="1.5"/>',
    more: '<circle cx="5" cy="12" r="1.5"/><circle cx="12" cy="12" r="1.5"/><circle cx="19" cy="12" r="1.5"/>'
  };

  function icon(name, size = 22) {
    const paths = iconPaths[name] || iconPaths.more;
    return `<svg width="${size}" height="${size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${paths}</svg>`;
  }

  function pad(n) {
    return String(n).padStart(2, "0");
  }

  function nowDate() {
    return new Date();
  }

  function formatDate(date = new Date()) {
    const d = new Date(date);
    return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
  }

  function formatDateCN(date = new Date()) {
    const d = new Date(date);
    const week = ["日", "一", "二", "三", "四", "五", "六"][d.getDay()];
    return `${d.getFullYear()}年${d.getMonth() + 1}月${d.getDate()}日 星期${week}`;
  }

  function formatTime(date = new Date()) {
    const d = new Date(date);
    return `${pad(d.getHours())}:${pad(d.getMinutes())}`;
  }

  function formatTimeSeconds(date = new Date()) {
    const d = new Date(date);
    return `${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`;
  }

  function formatDateTime(date) {
    if (!date) return "--";
    const d = new Date(date);
    return `${formatDate(d)} ${formatTimeSeconds(d)}`;
  }

  function isoAgo(minutes) {
    return new Date(Date.now() - minutes * 60000).toISOString();
  }

  function isoDaysAgo(days, hour = 9, minute = 0) {
    const d = new Date();
    d.setDate(d.getDate() - days);
    d.setHours(hour, minute, 0, 0);
    return d.toISOString();
  }

  function money(value) {
    return Number(value || 0).toFixed(2);
  }

  function esc(value) {
    return String(value ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function minutesBetween(start, end = new Date()) {
    if (!start) return 0;
    return Math.max(0, Math.floor((new Date(end) - new Date(start)) / 60000));
  }

  function durationText(start, end = new Date()) {
    const mins = minutesBetween(start, end);
    if (mins < 60) return `${mins}分钟`;
    const h = Math.floor(mins / 60);
    const m = mins % 60;
    return m ? `${h}小时${m}分` : `${h}小时`;
  }

  function calcFee(start, end = new Date()) {
    const mins = minutesBetween(start, end);
    if (mins <= 15) return 0;
    const chargeMins = mins - 15;
    return Math.min(60, Math.ceil(chargeMins / 30) * 2.5);
  }

  function id(prefix) {
    return `${prefix}${Date.now().toString(36).toUpperCase()}${Math.floor(Math.random() * 900 + 100)}`;
  }

  const berthStatusMeta = {
    idle: { label: "空闲", tag: "tag-success" },
    pending: { label: "待录入", tag: "tag-warning" },
    parking: { label: "停车中", tag: "tag-primary" },
    fault: { label: "地磁故障", tag: "tag-gray" },
    risk: { label: "高风险", tag: "tag-danger" },
    monthly: { label: "包月车辆", tag: "tag-purple" }
  };

  const orderStatusMeta = {
    parking: { label: "停车中", tag: "tag-primary" },
    paid: { label: "已支付", tag: "tag-success" },
    arrears: { label: "欠费", tag: "tag-danger" },
    abnormal: { label: "异常", tag: "tag-warning" },
    pending: { label: "待支付", tag: "tag-warning" },
    repaid: { label: "已补缴", tag: "tag-purple" }
  };

  const ticketStatusMeta = {
    pending: { label: "待处理", tag: "tag-warning" },
    processing: { label: "处理中", tag: "tag-primary" },
    completed: { label: "已完成", tag: "tag-success" },
    overdue: { label: "已超期", tag: "tag-danger" },
    returned: { label: "已退回", tag: "tag-gray" }
  };

  const roads = [
    { id: "r1", name: "人民路东段", area: "中心城区一片区", distance: "120m" },
    { id: "r2", name: "建设路南段", area: "中心城区一片区", distance: "680m" },
    { id: "r3", name: "解放路西段", area: "中心城区二片区", distance: "1.2km" }
  ];

  const statusPatterns = {
    r1: ["idle", "pending", "parking", "fault", "risk", "monthly", "idle", "parking", "pending", "idle", "parking", "idle"],
    r2: ["parking", "idle", "pending", "idle", "fault", "idle", "risk", "parking", "monthly", "idle", "pending", "parking"],
    r3: ["idle", "idle", "parking", "monthly", "pending", "fault", "idle", "risk", "parking", "idle", "pending", "idle"]
  };

  const roadPrefixes = { r1: "RM", r2: "JS", r3: "JF" };
  const currentPlates = [
    "浙A·8K92F", "浙A·35M7Q", "浙A·D82G6", "浙A·7Q19K",
    "浙A·6P28S", "浙A·L520X", "浙A·C9T31", "浙A·E72K8",
    "浙A·2R65N", "浙A·U109P", "浙A·9H33D", "浙A·5B18V"
  ];

  const berths = [];
  let plateCursor = 0;

  roads.forEach((road) => {
    statusPatterns[road.id].forEach((status, index) => {
      const occupied = ["parking", "risk", "monthly"].includes(status);
      berths.push({
        id: `${road.id}-b${index + 1}`,
        roadId: road.id,
        no: `${roadPrefixes[road.id]}-${pad(index + 1)}`,
        status,
        plate: occupied ? currentPlates[plateCursor++ % currentPlates.length] : "",
        entryTime: occupied ? isoAgo(25 + index * 17) : null,
        currentFee: occupied && status !== "monthly" ? 5 + index * 1.5 : 0,
        magnet: status === "fault" ? "离线" : "正常",
        deviceId: `GM-${roadPrefixes[road.id]}-${pad(index + 1)}`,
        riskTags: status === "risk" ? ["历史欠费", "逃费高风险"] : status === "monthly" ? ["包月有效"] : [],
        currentOrderId: null
      });
    });
  });

  const orders = [];
  let orderIndex = 1;

  berths
    .filter((b) => ["parking", "risk", "monthly"].includes(b.status))
    .forEach((berth) => {
      const order = {
        id: `o-current-${orderIndex}`,
        orderNo: `P20260717${String(orderIndex).padStart(5, "0")}`,
        roadId: berth.roadId,
        berthId: berth.id,
        plate: berth.plate,
        plateColor: berth.plate.includes("D") || berth.plate.includes("E") ? "绿牌" : "蓝牌",
        vehicleType: "小型车",
        startTime: berth.entryTime,
        endTime: null,
        receivable: berth.status === "monthly" ? 0 : calcFee(berth.entryTime),
        discount: berth.status === "monthly" ? calcFee(berth.entryTime) : 0,
        paid: 0,
        status: "parking",
        paymentMethod: "",
        createdBy: VALID_EMPLOYEE,
        abnormal: berth.status === "risk"
      };
      berth.currentOrderId = order.id;
      orders.push(order);
      orderIndex += 1;
    });

  orders.push(
    {
      id: "o-paid-1",
      orderNo: "P2026071600831",
      roadId: "r1",
      berthId: "r1-b10",
      plate: "浙A·3F19M",
      plateColor: "蓝牌",
      vehicleType: "小型车",
      startTime: isoDaysAgo(1, 9, 12),
      endTime: isoDaysAgo(1, 11, 36),
      receivable: 12.5,
      discount: 0,
      paid: 12.5,
      status: "paid",
      paymentMethod: "车主扫码缴费",
      createdBy: VALID_EMPLOYEE
    },
    {
      id: "o-paid-2",
      orderNo: "P2026071500722",
      roadId: "r2",
      berthId: "r2-b2",
      plate: "浙A·8K92F",
      plateColor: "蓝牌",
      vehicleType: "小型车",
      startTime: isoDaysAgo(2, 14, 5),
      endTime: isoDaysAgo(2, 16, 20),
      receivable: 10,
      discount: 0,
      paid: 10,
      status: "paid",
      paymentMethod: "PDA 扫付款码",
      createdBy: VALID_EMPLOYEE
    },
    {
      id: "o-arrear-1",
      orderNo: "P2026070800518",
      roadId: "r1",
      berthId: "r1-b7",
      plate: "浙A·8K92F",
      plateColor: "蓝牌",
      vehicleType: "小型车",
      startTime: isoDaysAgo(9, 8, 20),
      endTime: isoDaysAgo(9, 12, 42),
      receivable: 22.5,
      discount: 0,
      paid: 0,
      status: "arrears",
      paymentMethod: "",
      createdBy: VALID_EMPLOYEE
    },
    {
      id: "o-arrear-2",
      orderNo: "P2026070300389",
      roadId: "r3",
      berthId: "r3-b1",
      plate: "浙A·8K92F",
      plateColor: "蓝牌",
      vehicleType: "小型车",
      startTime: isoDaysAgo(14, 10, 8),
      endTime: isoDaysAgo(14, 13, 50),
      receivable: 17.5,
      discount: 0,
      paid: 0,
      status: "arrears",
      paymentMethod: "",
      createdBy: VALID_EMPLOYEE
    },
    {
      id: "o-arrear-3",
      orderNo: "P2026062700266",
      roadId: "r2",
      berthId: "r2-b6",
      plate: "浙A·6P28S",
      plateColor: "蓝牌",
      vehicleType: "小型车",
      startTime: isoDaysAgo(20, 16, 12),
      endTime: isoDaysAgo(20, 20, 45),
      receivable: 25,
      discount: 0,
      paid: 0,
      status: "arrears",
      paymentMethod: "",
      createdBy: VALID_EMPLOYEE
    },
    {
      id: "o-abnormal-1",
      orderNo: "P2026071400621",
      roadId: "r3",
      berthId: "r3-b10",
      plate: "浙A·2N77C",
      plateColor: "蓝牌",
      vehicleType: "小型车",
      startTime: isoDaysAgo(3, 11, 15),
      endTime: isoDaysAgo(3, 11, 40),
      receivable: 2.5,
      discount: 0,
      paid: 0,
      status: "abnormal",
      paymentMethod: "",
      createdBy: VALID_EMPLOYEE
    }
  );

  const profiles = {
    "浙A·8K92F": {
      plate: "浙A·8K92F",
      plateColor: "蓝牌",
      vehicleType: "小型车",
      types: ["高风险车主", "欠费车主", "高频车主"],
      currentStatus: "当前在人民路东段停车",
      package: null,
      frequency: [1, 2, 1, 3, 2, 2, 4],
      habit: [
        { label: "7/11", start: 8.2, end: 10.3, status: "paid", orderId: "o-paid-2" },
        { label: "7/12", start: 13.1, end: 15.4, status: "paid", orderId: "o-paid-1" },
        { label: "7/13", start: 9.4, end: 13.2, status: "arrears", orderId: "o-arrear-2" },
        { label: "7/14", start: 17.1, end: 19.5, status: "paid", orderId: "o-paid-2" },
        { label: "7/15", start: 8.6, end: 12.7, status: "arrears", orderId: "o-arrear-1" },
        { label: "7/16", start: 10.2, end: 11.8, status: "paid", orderId: "o-paid-1" },
        { label: "7/17", start: 14.2, end: 18.1, status: "parking", orderId: "o-current-2" }
      ]
    },
    "浙A·35M7Q": {
      plate: "浙A·35M7Q",
      plateColor: "蓝牌",
      vehicleType: "小型车",
      types: ["临停车主", "高频车主"],
      currentStatus: "停车中",
      package: null,
      frequency: [0, 1, 2, 1, 1, 2, 1],
      habit: [
        { label: "7/11", start: 9, end: 11, status: "paid", orderId: "o-paid-1" },
        { label: "7/13", start: 15, end: 17.5, status: "paid", orderId: "o-paid-2" },
        { label: "7/17", start: 12.3, end: 17.2, status: "parking", orderId: "o-current-3" }
      ]
    },
    "浙A·D82G6": {
      plate: "浙A·D82G6",
      plateColor: "绿牌",
      vehicleType: "新能源小型车",
      types: ["包月车主", "高频车主"],
      currentStatus: "包月有效，当前在停",
      package: {
        type: "中心城区新能源包月",
        start: "2026-07-01",
        end: "2026-08-31",
        remainDays: 45,
        roads: "人民路、建设路、解放路授权泊位"
      },
      frequency: [2, 2, 3, 1, 3, 2, 3],
      habit: [
        { label: "7/11", start: 8.5, end: 18.1, status: "free", orderId: "o-current-4" },
        { label: "7/12", start: 8.7, end: 17.8, status: "free", orderId: "o-current-4" },
        { label: "7/14", start: 9.1, end: 18.4, status: "free", orderId: "o-current-4" },
        { label: "7/17", start: 8.4, end: 17.5, status: "free", orderId: "o-current-4" }
      ]
    },
    "浙A·6P28S": {
      plate: "浙A·6P28S",
      plateColor: "蓝牌",
      vehicleType: "小型车",
      types: ["欠费车主", "高风险车主"],
      currentStatus: "高风险车辆在停",
      package: null,
      frequency: [1, 0, 1, 2, 0, 1, 2],
      habit: [
        { label: "7/11", start: 19, end: 22, status: "arrears", orderId: "o-arrear-3" },
        { label: "7/14", start: 8.2, end: 9.5, status: "paid", orderId: "o-paid-1" },
        { label: "7/17", start: 11.5, end: 19.5, status: "parking", orderId: "o-current-6" }
      ]
    },
    "浙A·3F19M": {
      plate: "浙A·3F19M",
      plateColor: "蓝牌",
      vehicleType: "小型车",
      types: ["临停车主"],
      currentStatus: "当前未停车",
      package: null,
      frequency: [0, 1, 0, 1, 0, 1, 0],
      habit: [
        { label: "7/12", start: 11.2, end: 12.7, status: "paid", orderId: "o-paid-1" },
        { label: "7/14", start: 9.1, end: 11.6, status: "paid", orderId: "o-paid-1" },
        { label: "7/16", start: 9.2, end: 11.6, status: "paid", orderId: "o-paid-1" }
      ]
    }
  };

  const warnings = [
    {
      id: "w1",
      type: "超时未录入",
      title: "超时未录入车牌",
      level: "重要",
      roadId: "r1",
      berthId: "r1-b2",
      plate: "待识别",
      triggerTime: isoAgo(8),
      reason: "地磁检测到车辆入位已超过 6 分钟，仍未创建有效停车订单。",
      requirement: "请在 5 分钟内到达现场，拍摄车辆照片并补录车牌。",
      status: "pending"
    },
    {
      id: "w2",
      type: "提前结单",
      title: "疑似提前结单",
      level: "紧急",
      roadId: "r1",
      berthId: "r1-b8",
      plate: "浙A·35M7Q",
      triggerTime: isoAgo(19),
      reason: "地磁持续显示有车，但关联订单已被提前结束。",
      requirement: "请核实车辆是否仍在现场，并反馈订单状态。",
      status: "pending"
    },
    {
      id: "w3",
      type: "地磁离线",
      title: "地磁设备离线",
      level: "重要",
      roadId: "r1",
      berthId: "r1-b4",
      plate: "",
      triggerTime: isoAgo(31),
      reason: "地磁设备连续 12 分钟未上报心跳数据。",
      requirement: "请现场确认设备状态，必要时创建维修工单。",
      status: "pending"
    },
    {
      id: "w4",
      type: "高风险车辆入场",
      title: "高风险车辆入场",
      level: "紧急",
      roadId: "r2",
      berthId: "r2-b7",
      plate: "浙A·6P28S",
      triggerTime: isoAgo(44),
      reason: "车辆存在 3 笔历史欠费，并命中逃费风险规则。",
      requirement: "请关注车辆缴费情况，必要时引导补缴。",
      status: "pending"
    },
    {
      id: "w5",
      type: "长时间停车",
      title: "车辆长时间停车",
      level: "普通",
      roadId: "r3",
      berthId: "r3-b9",
      plate: "浙A·9H33D",
      triggerTime: isoAgo(72),
      reason: "当前停车时长已超过道路建议停放时长。",
      requirement: "请现场巡查并确认车辆状态。",
      status: "pending"
    }
  ];

  const tickets = [
    {
      id: "t1",
      no: "GD202607170021",
      type: "地磁设备故障",
      title: "RM-04 地磁设备离线",
      description: "平台监测到地磁设备连续离线，需现场检查供电及设备状态。",
      source: "平台派发",
      status: "pending",
      priority: "紧急",
      roadId: "r1",
      berthId: "r1-b4",
      deviceId: "GM-RM-04",
      assignee: "张伟",
      creator: "系统",
      createdAt: isoAgo(36),
      deadline: new Date(Date.now() + 80 * 60000).toISOString(),
      attachments: ["设备离线截图"],
      timeline: [
        { title: "工单创建", time: isoAgo(36), desc: "由地磁离线预警自动生成工单。" }
      ]
    },
    {
      id: "t2",
      no: "GD202607170018",
      type: "车辆异常停放",
      title: "建设路南段车辆跨位停放",
      description: "车辆同时占用 JS-03、JS-04 两个泊位，请现场处置并拍照反馈。",
      source: "平台派发",
      status: "processing",
      priority: "重要",
      roadId: "r2",
      berthId: "r2-b3",
      deviceId: "",
      assignee: "张伟",
      creator: "运营中心",
      createdAt: isoAgo(65),
      deadline: new Date(Date.now() + 45 * 60000).toISOString(),
      attachments: ["现场抓拍图"],
      timeline: [
        { title: "工单创建", time: isoAgo(65), desc: "运营中心派发现场核查任务。" },
        { title: "收费员接单", time: isoAgo(52), desc: "张伟已接单并前往现场。" }
      ]
    },
    {
      id: "t3",
      no: "GD202607160097",
      type: "泊位标线问题",
      title: "解放路西段泊位编号模糊",
      description: "JF-10 泊位编号磨损严重，建议安排补漆。",
      source: "我创建的",
      status: "completed",
      priority: "普通",
      roadId: "r3",
      berthId: "r3-b10",
      deviceId: "",
      assignee: "市政维护组",
      creator: "张伟",
      createdAt: isoDaysAgo(1, 10, 20),
      deadline: isoDaysAgo(-1, 18, 0),
      attachments: ["现场照片"],
      timeline: [
        { title: "工单创建", time: isoDaysAgo(1, 10, 20), desc: "收费员现场发现泊位标线模糊。" },
        { title: "转派维护组", time: isoDaysAgo(1, 10, 35), desc: "已转派市政维护组处理。" },
        { title: "工单完成", time: isoDaysAgo(1, 16, 10), desc: "泊位编号已重新喷涂。" }
      ]
    },
    {
      id: "t4",
      no: "GD202607150081",
      type: "收费设备故障",
      title: "蓝牙打印机连接异常",
      description: "PDA 无法连接蓝牙打印机，已尝试重启设备。",
      source: "我创建的",
      status: "overdue",
      priority: "重要",
      roadId: "r1",
      berthId: "",
      deviceId: "PRT-1028",
      assignee: "设备维护组",
      creator: "张伟",
      createdAt: isoDaysAgo(2, 9, 0),
      deadline: isoDaysAgo(1, 9, 0),
      attachments: [],
      timeline: [
        { title: "工单创建", time: isoDaysAgo(2, 9, 0), desc: "收费员反馈蓝牙打印机连接异常。" }
      ]
    },
    {
      id: "t5",
      no: "GD202607140062",
      type: "订单异常",
      title: "车牌识别结果需复核",
      description: "订单车牌与现场照片疑似不一致，请复核原始照片。",
      source: "自动生成",
      status: "completed",
      priority: "普通",
      roadId: "r2",
      berthId: "r2-b11",
      deviceId: "",
      assignee: "张伟",
      creator: "系统",
      createdAt: isoDaysAgo(3, 13, 8),
      deadline: isoDaysAgo(3, 15, 0),
      attachments: ["入场照片"],
      timeline: [
        { title: "工单创建", time: isoDaysAgo(3, 13, 8), desc: "车牌识别置信度低于阈值。" },
        { title: "复核完成", time: isoDaysAgo(3, 13, 32), desc: "现场照片确认车牌为浙A·7K18P。" }
      ]
    }
  ];

  const monthlyIncome = [286, 305, 268, 352, 318, 391, 416, 375, 428, 396, 455, 472, 438, 501, 486, 512, 368];

  const state = {
    route: "login",
    params: {},
    history: [],
    loggedIn: false,
    clockedIn: false,
    clockedOut: false,
    clockInTime: null,
    login: {
      employeeNo: localStorage.getItem("parkingEmployee") || VALID_EMPLOYEE,
      remember: true,
      error: ""
    },
    attendance: {
      locating: false,
      locationSuccess: true,
      beacon: true,
      fenceEnabled: true,
      insideFence: true,
      photo: null,
      error: ""
    },
    currentRoadId: "r1",
    berthFilter: "all",
    berthSearch: "",
    berthRefreshing: false,
    build: {
      roadId: "r1",
      berthId: "",
      photos: [],
      recognizing: false,
      plate: "",
      plateColor: "蓝牌",
      error: ""
    },
    query: {
      term: "",
      status: "all"
    },
    arrears: {
      plate: "浙A·8K92F",
      searchedPlate: "浙A·8K92F",
      selected: [],
      error: ""
    },
    orderCheckoutArrears: [],
    payment: {
      kind: "order",
      orderIds: [],
      amount: 0,
      method: "pda",
      status: "idle",
      countdown: 60,
      error: ""
    },
    lastPayment: null,
    profilePlate: "浙A·8K92F",
    profileHabitOrderId: null,
    warningFilter: "all",
    warningForm: {
      result: "已处理",
      note: "",
      photo: null,
      video: null,
      error: ""
    },
    ticketTab: "related",
    ticketFeedback: {
      note: "",
      photo: null,
      error: ""
    },
    newTicket: {
      roadId: "r1",
      berthId: "",
      type: "地磁设备故障",
      faultType: "离线",
      description: "",
      photo: null,
      priority: "重要",
      error: ""
    },
    reportPeriod: "today",
    reportCustom: {
      start: formatDate(new Date(Date.now() - 6 * 86400000)),
      end: formatDate()
    },
    clockOut: {
      photo: null,
      error: ""
    },
    location: {
      success: true,
      reporting: false,
      lastReport: new Date().toISOString(),
      accuracy: 12,
      network: "5G 在线",
      longitude: 120.123456,
      latitude: 30.123456
    },
    shiftStats: {
      creationCount: 18,
      parkingCount: 42,
      manualCreationCount: 2,
      receivable: 386.5,
      received: 332,
      ownerScan: 165.5,
      pdaScan: 126.5,
      cash: 0,
      arrears: 40,
      arrearsCount: 2,
      taskCount: 4,
      warningFeedback: 2,
      ticketCount: 3,
      printCount: 5,
      queryCount: 12,
      inspectedBerths: 36
    },
    modal: null,
    returnReason: "",
    transferPerson: "李强",
    selectedOrderId: null,
    selectedWarningId: null,
    selectedTicketId: null
  };

  let clockTimer = null;
  let reportTimer = null;
  let paymentTimer = null;
  let lastRenderedRoute = null;

  const app = document.getElementById("app");
  const modalRoot = document.getElementById("modal-root");
  const toastRoot = document.getElementById("toast-root");

  function getRoad(roadId) {
    return roads.find((r) => r.id === roadId);
  }

  function getBerth(berthId) {
    return berths.find((b) => b.id === berthId);
  }

  function getOrder(orderId) {
    return orders.find((o) => o.id === orderId);
  }

  function getWarning(warningId) {
    return warnings.find((w) => w.id === warningId);
  }

  function getTicket(ticketId) {
    return tickets.find((t) => t.id === ticketId);
  }

  function currentRoad() {
    return getRoad(state.currentRoadId);
  }

  function berthSummary(roadId) {
    const list = berths.filter((b) => b.roadId === roadId);
    const result = {
      total: list.length,
      idle: 0,
      pending: 0,
      parking: 0,
      fault: 0,
      risk: 0,
      monthly: 0
    };
    list.forEach((b) => {
      result[b.status] += 1;
    });
    return result;
  }

  function pendingWarnings() {
    return warnings.filter((w) => w.status === "pending").length;
  }

  function roadName(roadId) {
    return getRoad(roadId)?.name || "--";
  }

  function berthNo(berthId) {
    return getBerth(berthId)?.no || "--";
  }

  function profileForPlate(plate) {
    if (!profiles[plate]) {
      profiles[plate] = {
        plate,
        plateColor: "蓝牌",
        vehicleType: "小型车",
        types: ["临停车主", "首次停车"],
        currentStatus: "当前停车中",
        package: null,
        frequency: [0, 0, 0, 0, 0, 0, 1],
        habit: []
      };
    }
    return profiles[plate];
  }

  function arrearsOrdersForPlate(plate) {
    return orders.filter((o) => o.plate === plate && o.status === "arrears");
  }

  function toast(message, type = "success") {
    const el = document.createElement("div");
    el.className = `toast ${type}`;
    el.innerHTML = `<span>${type === "success" ? "✓" : type === "error" ? "!" : "i"}</span><span>${esc(message)}</span>`;
    toastRoot.appendChild(el);
    setTimeout(() => {
      el.style.opacity = "0";
      el.style.transform = "translateY(-8px)";
      setTimeout(() => el.remove(), 180);
    }, 2600);
  }

  function navigate(route, params = {}, replace = false) {
    if (!replace && state.route !== route) {
      state.history.push({ route: state.route, params: state.params });
    }
    state.route = route;
    state.params = params;
    state.modal = null;
    window.scrollTo({ top: 0, behavior: "instant" });
    render();
  }

  function goBack() {
    const previous = state.history.pop();
    if (previous) {
      state.route = previous.route;
      state.params = previous.params;
      state.modal = null;
      render();
    } else if (state.clockedIn) {
      navigate("dashboard", {}, true);
    } else {
      navigate("login", {}, true);
    }
  }

  function menuButton() {
    return `<button class="module-menu-btn" data-action="open-side-nav" aria-label="打开菜单"><span></span><span></span><span></span></button>`;
  }

  function pageHeader(title, options = {}) {
    const { back = true, right = "", subtitle = "", menu = false } = options;
    return `
      <div class="page-header ${back ? "subpage-header" : "home-header"} ${menu ? "module-home-header" : ""}">
        ${
          back
            ? `<button class="back-btn" data-action="back" aria-label="返回">${icon("back")}</button>`
            : menu
              ? menuButton()
              : ""
        }
        ${
          back
            ? `<div class="page-title">${esc(title)}</div>`
            : `<div><div class="page-title">${esc(title)}</div>${subtitle ? `<div class="header-subtitle">${esc(subtitle)}</div>` : ""}</div>`
        }
        ${right || (back ? "<div></div>" : "")}
      </div>
    `;
  }

  function bottomNav(active) {
    const items = [
      ["dashboard", "home", "工作台"],
      ["berths", "berth", "泊位"],
      ["tickets", "ticket", "工单"],
      ["reports", "report", "报表"],
      ["mine", "user", "我的"]
    ];
    return `
      <div class="side-nav-shell" data-side-nav>
        <button class="side-nav-backdrop" data-action="close-side-nav" aria-label="关闭菜单"></button>
        <aside class="side-drawer" aria-label="主导航">
          <div class="side-drawer-head">
            <div class="side-drawer-title">功能菜单</div>
            <button class="side-drawer-close" data-action="close-side-nav" aria-label="关闭">×</button>
          </div>
          <nav class="side-nav-list">
            ${items
              .map(
                ([route, ico, label]) => `
                  <button class="side-nav-item ${active === route ? "active" : ""}" data-action="nav" data-route="${route}">
                    <span class="side-nav-icon">${icon(ico)}</span>
                    <span>${label}</span>
                    ${
                      route === "tickets" && tickets.filter((t) => ["pending", "overdue"].includes(t.status)).length
                        ? `<span class="badge">${tickets.filter((t) => ["pending", "overdue"].includes(t.status)).length}</span>`
                        : ""
                    }
                  </button>
                `
              )
              .join("")}
          </nav>
          <div class="side-drawer-footer">
            <button class="side-clock-out-btn" data-action="go-clock-out">
              <span class="side-clock-out-icon">${icon("clock")}</span>
              <span>
                <strong>下班打卡</strong>
                <small>结束本次收费班次</small>
              </span>
              <span class="side-clock-out-arrow">→</span>
            </button>
          </div>
        </aside>
      </div>
    `;
  }

  function shell(content, options = {}) {
    const { nav = "", noNav = false, classes = "" } = options;
    return `
      <div class="phone-shell">
        <main class="screen ${noNav ? "no-nav" : ""} ${nav ? "has-side-nav" : ""} ${classes}">
          ${content}
        </main>
        ${nav ? bottomNav(nav) : ""}
      </div>
    `;
  }

  function renderLogin() {
    return shell(
      `
        <div class="login-screen">
          <div class="login-brand">
            <div class="brand-logo">
              <div style="font-size:33px">🅿</div>
            </div>
            <div class="brand-title">惠泊云智慧停车</div>
            <div class="brand-subtitle">道路停车收费员 PDA</div>
          </div>

          <div class="login-card">
            <div class="login-welcome">收费员登录</div>
            <div class="login-hint">请输入本人有效工号进入当日工作流程</div>

            <div class="form-group">
              <div class="form-label">
                <span>收费员工号</span>
                <span class="form-hint">演示工号：A00123</span>
              </div>
              <div class="input-wrap">
                <span style="color:var(--primary)">👤</span>
                <input
                  type="text"
                  autocomplete="off"
                  maxlength="12"
                  value="${esc(state.login.employeeNo)}"
                  placeholder="请输入工号"
                  data-model="login.employeeNo"
                />
              </div>
            </div>

            <div class="switch-line">
              <span>记住本机工号</span>
              <button class="switch ${state.login.remember ? "on" : ""}" data-action="toggle-remember" aria-label="记住工号"></button>
            </div>

            ${state.login.error ? `<div class="error-box">${esc(state.login.error)}</div>` : ""}

            <button class="primary-btn login-submit" data-action="login">
              进入系统
              <span>→</span>
            </button>

            <div class="device-status-grid">
              <div class="device-status">网络状态<strong style="color:var(--success)">● 5G 在线</strong></div>
              <div class="device-status">设备编号<strong>${DEVICE_ID}</strong></div>
              <div class="device-status">当前版本<strong>${VERSION}</strong></div>
            </div>
          </div>

          <div class="login-footer">
            <div>${formatDateCN()}</div>
            <div>城市智慧停车运营中心 · 安全接入</div>
          </div>
        </div>
      `,
      { noNav: true, classes: "login-route" }
    );
  }

  function photoBlock(photo, type, meta = {}) {
    if (!photo) {
      return `
        <div class="photo-placeholder">
          <div>
            <div class="big-icon">📷</div>
            <div style="font-size:var(--font-item-title);font-weight:900;color:var(--text-2)">尚未拍摄照片</div>
            <div style="font-size:var(--font-helper);margin-top:6px;line-height:1.6">拍摄后系统将自动叠加时间、定位、人员与设备水印</div>
          </div>
        </div>
      `;
    }

    const isAttendance = type === "上班打卡" || type === "下班打卡";
    return `
      <div class="photo-mock ${isAttendance ? "attendance" : ""}">
        <div class="photo-watermark">
          <strong>${esc(state.staffName || "张伟")}　工号：${VALID_EMPLOYEE}</strong><br/>
          业务类型：${esc(type)}　${formatDateTime(photo.time)}<br/>
          ${esc(meta.road || currentRoad().name)} ${meta.berth ? `　泊位：${esc(meta.berth)}` : ""}<br/>
          经度：${state.location.longitude.toFixed(6)}　纬度：${state.location.latitude.toFixed(6)}<br/>
          定位精度：${state.location.accuracy}m　围栏内　设备：${DEVICE_ID}
        </div>
      </div>
    `;
  }

  function renderAttendance() {
    const a = state.attendance;
    return shell(
      `
        <div class="content">
          <div class="card attendance-profile">
            <div class="attendance-person">
              <div class="staff-name">张伟</div>
              <div class="staff-meta">工号 ${VALID_EMPLOYEE} · 中心城区一片区</div>
            </div>
            <div class="attendance-time" style="text-align:right">
              <div class="js-time" style="font-size:18px;font-weight:950">${formatTimeSeconds()}</div>
              <div style="font-size:var(--font-helper);color:var(--text-3);margin-top:3px">${formatDateCN()}</div>
            </div>
          </div>

          <section class="section">
            <div class="section-head">
              <div class="section-title">现场校验</div>
              <button class="section-link" data-action="relocate" ${a.locating ? "disabled" : ""}>
                ${a.locating ? "定位中…" : "重新定位"}
              </button>
            </div>
            <div class="card card-pad">
              <div class="info-list">
                <div class="info-row">
                  <span class="info-label">当前定位</span>
                  <span class="info-value">${a.locating ? "正在获取高精度定位…" : "人民路东段收费岗亭附近"}</span>
                </div>
                <div class="info-row">
                  <span class="info-label">定位状态</span>
                  <span class="check-status ${a.locating ? "warning" : a.locationSuccess ? "success" : "danger"}">
                    <span class="dot"></span>
                    ${a.locating ? "定位中" : a.locationSuccess ? `定位成功 · ${state.location.accuracy}m` : "定位失败"}
                  </span>
                </div>
                <div class="info-row">
                  <span class="info-label">蓝牙信标</span>
                  <span class="check-status ${a.beacon ? "success" : "danger"}">
                    <span class="dot"></span>${a.beacon ? "已检测 B-1009" : "未检测"}
                  </span>
                </div>
                <div class="info-row">
                  <span class="info-label">电子围栏</span>
                  <span class="check-status ${a.insideFence ? "success" : "danger"}">
                    <span class="dot"></span>${a.insideFence ? "围栏内" : "围栏外"}
                  </span>
                </div>
                <div class="info-row">
                  <span class="info-label">设备编号</span>
                  <span class="info-value">${DEVICE_ID}</span>
                </div>
              </div>
            </div>
          </section>

          <section class="section">
            <div class="section-head">
              <div class="section-title">打卡照片</div>
              ${a.photo ? `<span class="status-tag tag-success"><span class="dot"></span>已拍摄</span>` : ""}
            </div>
            ${photoBlock(a.photo, "上班打卡", { road: "中心城区一片区 / 人民路东段" })}
            <div class="capture-controls">
              <button class="secondary-btn" data-action="capture-attendance">
                ${icon("camera")} ${a.photo ? "重新拍摄打卡照片" : "拍摄打卡照片"}
              </button>
            </div>
          </section>

          ${a.error ? `<div class="error-box">${esc(a.error)}</div>` : ""}

          <section class="section">
            <button class="primary-btn" data-action="submit-clock-in">提交上班打卡</button>
          </section>
        </div>
      `,
      { noNav: true, classes: "attendance-scroll-route attendance-route" }
    );
  }

  function dashboardOverview() {
    const summary = berthSummary(state.currentRoadId);
    return `
      <div class="overview-grid">
        <div class="overview-item idle"><div class="overview-num">${summary.idle}</div><div class="overview-label">空闲</div></div>
        <div class="overview-item pending"><div class="overview-num">${summary.pending}</div><div class="overview-label">待录入</div></div>
        <div class="overview-item fault"><div class="overview-num">${summary.fault}</div><div class="overview-label">地磁故障</div></div>
        <div class="overview-item risk"><div class="overview-num">${summary.risk}</div><div class="overview-label">高风险</div></div>
      </div>
    `;
  }

  function renderDashboard() {
    const road = currentRoad();
    const pending = warnings.filter((w) => w.status === "pending").slice(0, 2);
    const stats = state.shiftStats;
    const rate = stats.receivable ? Math.min(100, (stats.received / stats.receivable) * 100) : 0;

    return shell(
      `
        <div class="hero-gradient">
          <div class="dashboard-top">
            ${menuButton()}
            <div class="staff-line dashboard-identity">
              <div class="staff-name">张伟</div>
            </div>
            <div class="dashboard-actions">
              <button class="location-button" data-action="open-location">
                ${icon("location", 22)}
                <span class="location-dot ${state.location.success ? "" : "fail"}"></span>
              </button>
              <button class="location-button message-btn" data-action="nav" data-route="warnings">
                ${icon("bell", 22)}
                ${pendingWarnings() ? `<span class="badge">${pendingWarnings()}</span>` : ""}
              </button>
            </div>
          </div>

          <div class="road-switch">
            <div>
              <div class="road-name">📍 ${esc(road.name)}</div>
              <div class="road-meta">${esc(road.area)} · ${road.distance} · <span class="dashboard-online">定位正常</span></div>
            </div>
            <button class="road-change-btn" data-action="open-road-switch">切换道路</button>
          </div>
        </div>

        <div class="content compact">
          <section class="section dashboard-overview-section">
            <div class="section-head">
              <div class="section-title">道路泊位概览</div>
              <button class="section-link" data-action="nav" data-route="berths">查看泊位</button>
            </div>
            ${dashboardOverview()}
          </section>

          <section class="section dashboard-quick-section">
            <div class="section-head">
              <div class="section-title">快捷操作</div>
            </div>
            <div class="card card-pad dashboard-quick-card">
              <div class="quick-grid">
                <button class="quick-item" data-action="open-arrears">
                  <div class="quick-icon orange-soft">￥</div>
                  <div class="quick-label">欠费补缴</div>
                </button>
                <button class="quick-item" data-action="nav" data-route="orderQuery">
                  <div class="quick-icon cyan-soft">⌕</div>
                  <div class="quick-label">订单查询</div>
                </button>
                <button class="quick-item" data-action="nav" data-route="reports">
                  <div class="quick-icon blue-soft">▥</div>
                  <div class="quick-label">收费报表</div>
                </button>
                <button class="quick-item" data-action="nav" data-route="warnings">
                  <div class="quick-icon red-soft">!</div>
                  <div class="quick-label">预警任务</div>
                </button>
              </div>
            </div>
          </section>

          <section class="section dashboard-income-section">
            <div class="section-head">
              <div class="section-title">当班收入</div>
              <button class="section-link" data-action="nav" data-route="reports">查看报表</button>
            </div>
            <div class="card income-card income-summary-strip">
              <div class="income-strip-cell primary">
                <div class="income-strip-label">收入 / 应收</div>
                <div class="income-strip-value"><strong>¥${money(stats.received)}</strong><span>/ ¥${money(stats.receivable)}</span></div>
              </div>
              <div class="income-strip-cell orders">
                <div class="income-strip-label">创单 / 停车次数</div>
                <div class="income-strip-value"><strong>${stats.creationCount}</strong><span>/ ${stats.parkingCount}</span></div>
              </div>
              <div class="income-strip-cell recovered">
                <div class="income-strip-label">欠费追缴金额</div>
                <div class="income-strip-value"><strong>¥${money(stats.arrears)}</strong></div>
              </div>
              <div class="income-strip-cell outstanding">
                <div class="income-strip-label">当班欠费金额</div>
                <div class="income-strip-value"><strong>¥${money(Math.max(0, stats.receivable - stats.received))}</strong></div>
              </div>
            </div>
          </section>

          <section class="section dashboard-warning-section">
            <div class="section-head">
              <div class="section-title">平台预警</div>
              <button class="section-link" data-action="nav" data-route="warnings">全部 ${pendingWarnings()} 条</button>
            </div>
            <div class="warning-list dashboard-warning-grid">
              ${pending.length ? pending.map(warningCard).join("") : emptyState("🎉", "暂无待处理预警", "当前道路运行正常")}
            </div>
          </section>
        </div>
      `,
      { nav: "dashboard", classes: "dashboard-route" }
    );
  }

  function warningCard(w) {
    const levelClass = w.level === "紧急" ? "tag-danger" : w.level === "重要" ? "tag-warning" : "tag-gray";
    const levelTone = w.level === "紧急" ? "level-danger" : w.level === "重要" ? "level-warning" : "level-normal";
    return `
      <button class="warning-card ${levelTone}" data-action="open-warning" data-id="${w.id}">
        <div class="warning-top">
          <div>
            <div class="warning-title">${esc(w.title)}</div>
            <div class="warning-info">
              <span>📍 ${esc(roadName(w.roadId))}</span>
              <span>泊位 ${esc(berthNo(w.berthId))}</span>
              <span>${formatTime(w.triggerTime)}</span>
            </div>
          </div>
          <span class="status-tag ${w.status === "done" ? "tag-success" : levelClass}">
            <span class="dot"></span>${w.status === "done" ? "已处理" : w.level}
          </span>
        </div>
        <div class="warning-reason">${esc(w.reason)}</div>
      </button>
    `;
  }

  function emptyState(iconText, title, desc) {
    return `
      <div class="empty-state">
        <div>
          <div class="empty-icon">${iconText}</div>
          <div style="font-size:var(--font-item-title);font-weight:900;color:var(--text-2)">${esc(title)}</div>
          <div style="font-size:var(--font-helper);margin-top:6px;line-height:1.6">${esc(desc)}</div>
        </div>
      </div>
    `;
  }

  function filteredBerths() {
    let list = berths.filter((b) => b.roadId === state.currentRoadId);
    if (state.berthFilter !== "all") {
      list = list.filter((b) => b.status === state.berthFilter);
    }
    const keyword = state.berthSearch.trim().toUpperCase();
    if (keyword) {
      list = list.filter(
        (b) =>
          b.no.toUpperCase().includes(keyword) ||
          (b.plate && b.plate.toUpperCase().includes(keyword.replace("·", ""))) ||
          (b.plate && b.plate.toUpperCase().includes(keyword))
      );
    }
    return list;
  }

  function berthAction(b) {
    if (b.status === "idle") {
      return `<button class="small-btn small-success" data-action="create-from-berth" data-id="${b.id}">拍照建单</button>`;
    }
    if (b.status === "pending") {
      return `<button class="small-btn small-warning" data-action="create-from-berth" data-id="${b.id}">录入车牌</button>`;
    }
    if (b.status === "parking") {
      return `<button class="small-btn small-primary" data-action="open-order" data-id="${b.currentOrderId}">查看订单 / 结账</button>`;
    }
    if (b.status === "fault") {
      return `<button class="small-btn small-gray" data-action="new-fault-ticket" data-id="${b.id}">创建故障工单</button>`;
    }
    if (b.status === "risk") {
      return `<button class="small-btn small-danger" data-action="open-profile" data-plate="${esc(b.plate)}">画像 / 补缴</button>`;
    }
    return `<button class="small-btn small-purple" data-action="open-profile" data-plate="${esc(b.plate)}">查看套餐</button>`;
  }

  function berthCard(b) {
    const meta = berthStatusMeta[b.status];
    const order = b.currentOrderId ? getOrder(b.currentOrderId) : null;
    const fee = order && order.status === "parking" ? calcFee(order.startTime) : b.currentFee;
    return `
      <article class="berth-card ${b.status}">
        <div class="berth-top">
          <button class="berth-no" style="background:transparent;color:var(--text);padding:0" data-action="open-berth" data-id="${b.id}">
            ${esc(b.no)}
          </button>
          <span class="mini-tag ${meta.tag}">${meta.label}</span>
        </div>
        ${
          b.plate
            ? `<button class="berth-plate" data-action="open-profile" data-plate="${esc(b.plate)}">${esc(b.plate)}</button>`
            : `<div class="berth-empty">${b.status === "pending" ? "检测到车辆，等待录入" : b.status === "fault" ? "设备离线，现场状态未知" : "当前无车辆"}</div>`
        }
        <div class="berth-meta">
          ${
            b.entryTime
              ? `<span>入场 ${formatTime(b.entryTime)}</span><span>已停 ${durationText(b.entryTime)}</span><span>当前费用 ¥${money(fee)}</span>`
              : ""
          }
          <span>地磁：${esc(b.magnet)} ${b.riskTags.length ? `· ${esc(b.riskTags.join(" / "))}` : ""}</span>
        </div>
        <div class="berth-action">${berthAction(b)}</div>
      </article>
    `;
  }

  function renderBerths() {
    const road = currentRoad();
    const list = filteredBerths();
    const filters = [
      ["all", "全部"],
      ["idle", "空闲"],
      ["pending", "待录入"],
      ["parking", "停车中"],
      ["fault", "故障"],
      ["risk", "高风险"],
      ["monthly", "包月"]
    ];

    return shell(
      `
        ${pageHeader("泊位管理", {
          back: false,
          menu: true,
          subtitle: `${road.name} · 共 ${berthSummary(state.currentRoadId).total} 个泊位`,
          right: `<button class="header-icon-btn" data-action="open-road-switch">${icon("chevron")}</button>`
        })}
        <div class="content">
          <div class="search-row">
            <label class="search-input">
              ${icon("search", 18)}
              <input
                type="text"
                value="${esc(state.berthSearch)}"
                placeholder="搜索泊位号或车牌号"
                data-model="berthSearch"
              />
            </label>
            <button class="square-btn" data-action="refresh-berths">
              <span class="${state.berthRefreshing ? "refreshing" : ""}">${icon("refresh", 19)}</span>
            </button>
          </div>

          <div class="chips">
            ${filters
              .map(
                ([key, label]) => `
                  <button class="chip ${state.berthFilter === key ? "active" : ""}" data-action="berth-filter" data-filter="${key}">
                    ${esc(label)}
                  </button>
                `
              )
              .join("")}
          </div>

          ${
            state.berthRefreshing
              ? `
                <div class="loading-state">
                  <div>
                    <div class="loading-spinner"></div>
                    <div>正在刷新泊位状态…</div>
                  </div>
                </div>
              `
              : list.length
                ? `<div class="berth-grid">${list.map(berthCard).join("")}</div>`
                : emptyState("🅿", "未找到匹配泊位", "请调整状态筛选或搜索条件")
          }
        </div>
        <button class="floating-warning-entry" data-action="nav" data-route="warnings" aria-label="查看平台预警">
          ${icon("bell", 20)}
          <span>预警</span>
          <strong>${pendingWarnings()}</strong>
        </button>
      `,
      { nav: "berths", classes: "module-scroll-route berths-route" }
    );
  }

  function renderBerthDetail() {
    const berth = getBerth(state.params.id);
    if (!berth) return renderBerths();
    const meta = berthStatusMeta[berth.status];
    const order = berth.currentOrderId ? getOrder(berth.currentOrderId) : null;

    return shell(
      `
        ${pageHeader("泊位详情")}
        <div class="detail-hero">
          <div class="hero-label">${roadName(berth.roadId)}</div>
          <div class="hero-value">${esc(berth.no)}</div>
          <div class="hero-meta-grid">
            <div class="hero-meta"><strong>${meta.label}</strong><span>泊位状态</span></div>
            <div class="hero-meta"><strong>${berth.magnet}</strong><span>地磁状态</span></div>
            <div class="hero-meta"><strong>${berth.plate || "--"}</strong><span>当前车牌</span></div>
          </div>
        </div>

        <div class="content">
          <div class="card card-pad">
            <div class="info-list">
              <div class="info-row"><span class="info-label">所属道路</span><span class="info-value">${esc(roadName(berth.roadId))}</span></div>
              <div class="info-row"><span class="info-label">泊位编号</span><span class="info-value">${esc(berth.no)}</span></div>
              <div class="info-row"><span class="info-label">地磁设备</span><span class="info-value">${esc(berth.deviceId)}</span></div>
              <div class="info-row"><span class="info-label">设备状态</span><span class="status-tag ${berth.magnet === "正常" ? "tag-success" : "tag-danger"}">${esc(berth.magnet)}</span></div>
              ${
                berth.plate
                  ? `
                    <div class="info-row">
                      <span class="info-label">车牌号</span>
                      <button class="section-link" data-action="open-profile" data-plate="${esc(berth.plate)}">${esc(berth.plate)} →</button>
                    </div>
                    <div class="info-row"><span class="info-label">入场时间</span><span class="info-value">${formatDateTime(berth.entryTime)}</span></div>
                    <div class="info-row"><span class="info-label">停车时长</span><span class="info-value">${durationText(berth.entryTime)}</span></div>
                  `
                  : ""
              }
            </div>
          </div>

          ${
            order
              ? `
                <section class="section">
                  <div class="section-head"><div class="section-title">关联订单</div></div>
                  ${orderCard(order)}
                </section>
              `
              : ""
          }

          <section class="section">
            ${berthAction(berth)}
          </section>
        </div>
      `,
      { noNav: true }
    );
  }

  function initializeBuild(berthId = "") {
    const berth =
      getBerth(berthId) ||
      berths.find((b) => b.roadId === state.currentRoadId && ["pending", "idle"].includes(b.status));

    state.build = {
      roadId: berth?.roadId || state.currentRoadId,
      berthId: berth?.id || "",
      photos: [],
      recognizing: false,
      plate: "",
      plateColor: "蓝牌",
      error: ""
    };
  }

  function renderCreateOrder() {
    const build = state.build;
    const photos = Array.isArray(build.photos) ? build.photos : [];
    const roadBerths = berths.filter(
      (b) => b.roadId === build.roadId && ["idle", "pending", "fault"].includes(b.status)
    );
    const berth = getBerth(build.berthId);

    return shell(
      `
        ${pageHeader("拍照建单")}
        <div class="content">
          <div class="card card-pad">
            <div class="form-group" style="margin-top:0">
              <div class="form-label">
                <span>泊位编号</span>
                <span class="form-hint">当前道路：${esc(getRoad(build.roadId)?.name || currentRoad().name)}</span>
              </div>
              <select class="select" data-model="build.berthId">
                <option value="">请选择泊位</option>
                ${roadBerths
                  .map(
                    (b) => `<option value="${b.id}" ${build.berthId === b.id ? "selected" : ""}>${esc(b.no)} · ${berthStatusMeta[b.status].label}</option>`
                  )
                  .join("")}
              </select>
            </div>
          </div>

          <section class="section create-order-photo-section">
            <div class="section-head">
              <div>
                <div class="section-title">车辆照片</div>
                <div class="card-sub">至少拍摄 1 张，最多 3 张</div>
              </div>
              <span class="status-tag ${photos.length ? "tag-success" : ""}">${photos.length} / 3</span>
            </div>
            ${
              photos.length
                ? `
                  <div class="build-photo-grid">
                    ${photos
                      .map(
                        (photo, index) => `
                          <article class="build-photo-card">
                            <div class="build-photo-thumb">
                              <span class="build-photo-car">🚙</span>
                              <strong>车辆照片 ${index + 1}</strong>
                              <small>${formatTimeSeconds(photo.time)}</small>
                            </div>
                            <div class="build-photo-actions">
                              <button data-action="retake-vehicle-photo" data-index="${index}">重拍</button>
                              <button class="danger" data-action="delete-vehicle-photo" data-index="${index}">删除</button>
                            </div>
                          </article>
                        `
                      )
                      .join("")}
                  </div>
                `
                : photoBlock(null, "建单", {
                    road: getRoad(build.roadId)?.name || "请选择道路",
                    berth: berth?.no || "未选择"
                  })
            }
            <div class="capture-controls">
              <button class="secondary-btn" data-action="capture-vehicle" ${photos.length >= 3 ? "disabled" : ""}>
                ${icon("camera")} ${photos.length ? `继续拍摄（${photos.length}/3）` : "拍摄车辆照片"}
              </button>
            </div>
          </section>

          <section class="section">
            <div class="section-head">
              <div class="section-title">车牌信息</div>
              ${
                build.recognizing
                  ? `<span class="status-tag tag-primary"><span class="refreshing">${icon("refresh", 13)}</span>识别中</span>`
                  : ""
              }
            </div>
            <div class="card card-pad">
              <button class="outline-btn" data-action="recognize-plate" ${!photos.length || build.recognizing ? "disabled" : ""}>
                ${build.recognizing ? '<span class="loading-spinner" style="width:20px;height:20px;margin:0;border-width:2px"></span> 正在识别车牌' : "▣ 识别车牌"}
              </button>

              <div class="form-group">
                <div class="form-label">
                  <span>车牌号</span>
                  <span class="form-hint">支持手动修改识别结果</span>
                </div>
                <div class="input-wrap">
                  <span style="color:var(--primary)">🚙</span>
                  <input
                    type="text"
                    value="${esc(build.plate)}"
                    placeholder="例如：浙A·8K92F"
                    data-model="build.plate"
                    maxlength="10"
                  />
                </div>
              </div>

              <div class="form-group">
                <div class="form-label">车牌颜色</div>
                <div class="chips">
                  ${["蓝牌", "绿牌", "黄牌"]
                    .map(
                      (color) => `<button class="chip ${build.plateColor === color ? "active" : ""}" data-action="plate-color" data-color="${color}">${color}</button>`
                    )
                    .join("")}
                </div>
              </div>
            </div>
          </section>

          ${build.error ? `<div class="error-box">${esc(build.error)}</div>` : ""}

          <section class="section">
            <button class="primary-btn" data-action="create-order">创建停车订单</button>
          </section>
        </div>
      `,
      { noNav: true, classes: "module-scroll-route create-order-route" }
    );
  }

  function orderCard(order) {
    const meta = orderStatusMeta[order.status];
    return `
      <article class="order-card">
        <div class="order-top">
          <button style="text-align:left;background:transparent;color:inherit;padding:0;min-width:0" data-action="open-order" data-id="${order.id}">
            <div class="order-title">${esc(order.plate)} · ${esc(berthNo(order.berthId))}</div>
            <div class="order-info">
              <span>${esc(roadName(order.roadId))}</span>
              <span>${formatDateTime(order.startTime)}</span>
            </div>
          </button>
          <span class="status-tag ${meta.tag}">${meta.label}</span>
        </div>
        <div class="warning-reason" style="display:flex;justify-content:space-between;align-items:center">
          <span>订单 ${esc(order.orderNo)}</span>
          <strong style="color:${order.status === "arrears" ? "var(--danger)" : "var(--text)"}">¥${money(order.status === "parking" ? calcFee(order.startTime) : order.receivable)}</strong>
        </div>
        <div style="display:flex;justify-content:space-between;align-items:center;margin-top:9px">
          <button class="section-link" data-action="open-profile" data-plate="${esc(order.plate)}">查看车主画像</button>
          <button class="small-btn small-primary" data-action="open-order" data-id="${order.id}">订单详情</button>
        </div>
      </article>
    `;
  }

  function renderCreatedVehicleNotice(order) {
    const profile = profileForPlate(order.plate);
    const arrears = arrearsOrdersForPlate(order.plate);
    const now = new Date();
    const threeMonthsAgo = new Date(now);
    const oneYearAgo = new Date(now);
    threeMonthsAgo.setMonth(threeMonthsAgo.getMonth() - 3);
    oneYearAgo.setFullYear(oneYearAgo.getFullYear() - 1);

    const inPeriod = (item, cutoff) => {
      const occurredAt = new Date(item.endTime || item.startTime);
      return !Number.isNaN(occurredAt.getTime()) && occurredAt >= cutoff;
    };
    const summarize = (list) => ({
      count: list.length,
      amount: list.reduce((sum, item) => sum + Number(item.receivable || 0), 0)
    });
    const total = summarize(arrears);
    const recentThreeMonths = summarize(arrears.filter((item) => inPeriod(item, threeMonthsAgo)));
    const recentYear = summarize(arrears.filter((item) => inPeriod(item, oneYearAgo)));
    const packageInfo = profile.package;
    const packageEnd = packageInfo ? new Date(`${packageInfo.end}T23:59:59`) : null;
    const packageActive = packageInfo && packageEnd && !Number.isNaN(packageEnd.getTime()) && packageEnd >= now;

    return `
      <section class="section created-vehicle-section">
        ${
          packageInfo
            ? `
              <div class="card created-package-card">
                <div class="created-package-head">
                  <div>
                    <div class="created-card-eyebrow">包月套餐</div>
                    <div class="created-package-name">${esc(packageInfo.type)}</div>
                  </div>
                  <span class="status-tag ${packageActive ? "tag-purple" : "tag-gray"}">${packageActive ? "有效" : "已过期"}</span>
                </div>
                <div class="created-package-period">
                  <span>有效期</span>
                  <strong>${esc(packageInfo.start)} 至 ${esc(packageInfo.end)}</strong>
                </div>
              </div>
            `
            : ""
        }

        <div class="card created-arrears-card">
          <div class="created-arrears-head">
            <div>
              <div class="created-card-eyebrow">车主缴费提醒</div>
              <div class="card-title">车辆历史欠费</div>
            </div>
            <span class="status-tag ${total.count ? "tag-danger" : "tag-success"}">${total.count ? "有欠费" : "无欠费"}</span>
          </div>
          <div class="created-arrears-grid">
            <div class="created-arrears-stat">
              <span>累计欠费</span>
              <strong>${total.count} 笔</strong>
              <em>¥${money(total.amount)}</em>
            </div>
            <div class="created-arrears-stat">
              <span>近 3 个月</span>
              <strong>${recentThreeMonths.count} 笔</strong>
              <em>¥${money(recentThreeMonths.amount)}</em>
            </div>
            <div class="created-arrears-stat">
              <span>近 1 年</span>
              <strong>${recentYear.count} 笔</strong>
              <em>¥${money(recentYear.amount)}</em>
            </div>
          </div>
          <div class="created-arrears-reminder ${total.count ? "warning" : "clear"}">
            ${
              total.count
                ? `该车累计欠费 ${total.count} 笔，共 ¥${money(total.amount)}。请主动提醒车主及时补缴。`
                : "当前未发现历史欠费，无需额外提醒。"
            }
          </div>
        </div>
      </section>
    `;
  }

  function renderOrderDetail() {
    const order = getOrder(state.params.id || state.selectedOrderId);
    if (!order) return renderOrderQuery();

    state.selectedOrderId = order.id;
    const justCreated = Boolean(state.params.justCreated);
    const meta = orderStatusMeta[order.status];
    const currentFee = order.status === "parking" ? calcFee(order.startTime) : order.receivable;
    const end = order.endTime || new Date();
    const historicalArrears = order.status === "parking" && !justCreated ? arrearsOrdersForPlate(order.plate) : [];
    const selectedArrears = historicalArrears.filter((item) => state.orderCheckoutArrears.includes(item.id));
    const selectedArrearsTotal = selectedArrears.reduce((sum, item) => sum + item.receivable, 0);
    const checkoutTotal = currentFee + selectedArrearsTotal;

    return shell(
      `
        ${pageHeader("订单详情", {
          right: justCreated
            ? `<button class="header-icon-btn" data-action="open-parking-slip" data-id="${order.id}" aria-label="打印停车凭条">${icon("print")}</button>`
            : ""
        })}
        <div class="detail-hero">
          <div class="hero-label">停车订单</div>
          <button class="hero-value" style="background:transparent;color:white;padding:0" data-action="open-profile" data-plate="${esc(order.plate)}">
            ${esc(order.plate)}
          </button>
          <div class="hero-meta-grid">
            <div class="hero-meta"><strong>${esc(berthNo(order.berthId))}</strong><span>泊位编号</span></div>
            <div class="hero-meta"><strong>${durationText(order.startTime, end)}</strong><span>停车时长</span></div>
            <div class="hero-meta"><strong>${meta.label}</strong><span>订单状态</span></div>
          </div>
        </div>

        <div class="content">
          <div class="card card-pad">
            <div class="info-list">
              <div class="info-row"><span class="info-label">订单编号</span><span class="info-value">${esc(order.orderNo)}</span></div>
              <div class="info-row"><span class="info-label">车牌号</span><button class="section-link" data-action="open-profile" data-plate="${esc(order.plate)}">${esc(order.plate)} →</button></div>
              <div class="info-row"><span class="info-label">车牌颜色</span><span class="info-value">${esc(order.plateColor)}</span></div>
              <div class="info-row"><span class="info-label">道路 / 泊位</span><span class="info-value">${esc(roadName(order.roadId))} / ${esc(berthNo(order.berthId))}</span></div>
              <div class="info-row"><span class="info-label">入场时间</span><span class="info-value">${formatDateTime(order.startTime)}</span></div>
              <div class="info-row"><span class="info-label">当前 / 结束时间</span><span class="info-value">${formatDateTime(end)}</span></div>
              <div class="info-row"><span class="info-label">收费规则</span><span class="info-value">首 15 分钟免费，之后 ¥2.5/30分钟</span></div>
              <div class="info-row"><span class="info-label">订单状态</span><span class="status-tag ${meta.tag}">${meta.label}</span></div>
              ${
                order.paymentMethod
                  ? `<div class="info-row"><span class="info-label">支付方式</span><span class="info-value">${esc(order.paymentMethod)}</span></div>`
                  : ""
              }
            </div>
          </div>

          ${
            justCreated
              ? renderCreatedVehicleNotice(order)
              : `
                <section class="section">
                  <div class="card amount-summary">
                    <div class="amount-main">
                      <div>
                        <div class="card-sub">当前应收金额</div>
                        <div class="amount-number"><small>¥</small>${money(currentFee)}</div>
                      </div>
                      <span class="status-tag ${meta.tag}">${meta.label}</span>
                    </div>
                    <div class="amount-lines">
                      <div class="amount-line"><span>原始应收</span><strong>¥${money(currentFee + (order.discount || 0))}</strong></div>
                      <div class="amount-line"><span>优惠减免</span><strong>- ¥${money(order.discount)}</strong></div>
                      <div class="amount-line"><span>实收金额</span><strong>¥${money(order.paid)}</strong></div>
                    </div>
                  </div>
                </section>
              `
          }

          ${
            order.status === "parking" && historicalArrears.length
              ? `
                <section class="section order-arrears-section">
                  <div class="section-head">
                    <div>
                      <div class="section-title">历史欠费订单</div>
                      <div class="card-sub">可勾选后与本次停车费一并缴纳</div>
                    </div>
                    <button class="small-btn small-primary" data-action="select-all-order-arrears" data-plate="${esc(order.plate)}">
                      ${selectedArrears.length === historicalArrears.length ? "取消全选" : "全选"}
                    </button>
                  </div>
                  <div class="check-list">
                    ${historicalArrears
                      .map((item) => {
                        const checked = state.orderCheckoutArrears.includes(item.id);
                        return `
                          <button class="check-card" data-action="toggle-order-arrear" data-id="${item.id}">
                            <span class="checkbox ${checked ? "checked" : ""}">${checked ? "✓" : ""}</span>
                            <span style="text-align:left">
                              <span class="check-card-title">${esc(item.orderNo)}</span>
                              <span class="check-card-sub">${esc(roadName(item.roadId))} · ${esc(berthNo(item.berthId))}<br/>${formatDateTime(item.startTime)}</span>
                            </span>
                            <span class="check-card-amount">¥${money(item.receivable)}</span>
                          </button>
                        `;
                      })
                      .join("")}
                  </div>
                  <div class="card order-combined-total">
                    <span>已选 ${selectedArrears.length} 笔欠费</span>
                    <strong>欠费 ¥${money(selectedArrearsTotal)} · 合计 ¥${money(checkoutTotal)}</strong>
                  </div>
                </section>
              `
              : ""
          }

          ${
            ["paid", "repaid"].includes(order.status)
              ? ""
              : `
                <section class="section">
                  ${
                    order.status === "parking"
                      ? justCreated
                        ? `<button class="primary-btn" data-action="nav" data-route="berths">返回泊位管理</button>`
                        : `<button class="primary-btn" data-action="checkout" data-id="${order.id}">${selectedArrears.length ? "合并收款" : "结账并收款"} ¥${money(checkoutTotal)}</button>`
                      : order.status === "arrears"
                        ? `<button class="danger-btn" data-action="arrears-from-order" data-plate="${esc(order.plate)}">进入欠费补缴</button>`
                        : `<button class="outline-btn" data-action="nav" data-route="warnings">查看关联异常</button>`
                  }
                </section>
              `
          }
        </div>
      `,
      { noNav: true, classes: "module-scroll-route order-detail-route" }
    );
  }

  function renderPayment() {
    const payment = state.payment;
    const order = payment.kind === "arrears" ? null : getOrder(payment.currentOrderId || payment.orderIds[0]);
    const title = payment.kind === "arrears" ? "欠费补缴收款" : "停车费收款";
    const methods = [
      ["pda", "PDA 扫付款码", "扫描车主微信或支付宝付款码", "▣", "green-soft"],
      ["cash", "现金登记", "登记现金收款并记录收费员", "￥", "orange-soft"]
    ];

    return shell(
      `
        ${pageHeader(title)}
        <div class="content">
          <div class="card amount-summary">
            <div class="amount-main">
              <div>
                <div class="card-sub">${payment.kind === "arrears" ? `${payment.orderIds.length} 笔欠费订单` : payment.kind === "combined" ? `${esc(order?.plate || "")} · 含 ${payment.arrearsCount} 笔历史欠费` : esc(order?.plate || "")}</div>
                <div class="amount-number"><small>¥</small>${money(payment.amount)}</div>
              </div>
              <span class="status-tag tag-warning">待支付</span>
            </div>
            <div class="amount-lines">
              <div class="amount-line"><span>业务类型</span><strong>${payment.kind === "arrears" ? "历史欠费补缴" : payment.kind === "combined" ? "停车费 + 历史欠费" : "停车订单结账"}</strong></div>
              <div class="amount-line"><span>订单范围</span><strong>${payment.kind === "arrears" ? `${payment.orderIds.length} 笔欠费合并支付` : payment.kind === "combined" ? `本次停车 + ${payment.arrearsCount} 笔欠费` : esc(order?.orderNo || "--")}</strong></div>
              ${payment.kind === "combined" ? `<div class="amount-line"><span>本次停车费</span><strong>¥${money(payment.currentAmount)}</strong></div><div class="amount-line"><span>历史欠费</span><strong>¥${money(payment.arrearsAmount)}</strong></div>` : ""}
            </div>
          </div>

          <section class="section">
            <div class="section-head"><div class="section-title">选择支付方式</div></div>
            <div class="payment-methods">
              ${methods
                .map(
                  ([key, name, desc, ico, color]) => `
                    <button class="payment-method ${payment.method === key ? "active" : ""}" data-action="payment-method" data-method="${key}">
                      <div class="payment-method-icon ${color}">${ico}</div>
                      <div>
                        <div class="payment-method-name">${name}</div>
                        <div class="payment-method-desc">${desc}</div>
                      </div>
                      <div class="payment-method-check">${payment.method === key ? "✓" : ""}</div>
                    </button>
                  `
                )
                .join("")}
            </div>
          </section>

          <section class="section">
            ${renderPaymentOperation()}
          </section>

          ${payment.error ? `<div class="error-box">${esc(payment.error)}</div>` : ""}
        </div>
      `,
      { noNav: true, classes: "module-scroll-route payment-route" }
    );
  }

  function renderPaymentOperation() {
    const p = state.payment;

    if (p.method === "pda") {
      if (p.status === "failed") {
        return `
          <div class="card card-pad">
            <div style="text-align:center;padding:13px 0">
              <div style="font-size:42px">⚠️</div>
              <div style="font-size:16px;font-weight:950;margin-top:7px;color:var(--danger)">付款码识别失败</div>
              <div style="font-size:var(--font-helper);color:var(--text-3);margin-top:6px">付款码可能过期或屏幕亮度过低，请重新扫描。</div>
            </div>
            <button class="primary-btn" data-action="start-pda-scan">重新扫描</button>
          </div>
        `;
      }

      const statusText = {
        idle: "将付款码放入框内",
        scanning: "正在识别付款码…",
        recognized: "付款码识别成功",
        paying: "支付处理中…"
      }[p.status] || "将付款码放入框内";

      return `
        <div class="scan-frame">
          <div class="scan-corners">
            <i></i><i></i><i></i><i></i>
            ${["scanning", "recognized", "paying"].includes(p.status) ? '<div class="scan-line"></div>' : ""}
          </div>
          <div class="scan-status">
            ${
              p.status === "recognized"
                ? "✓ 付款码识别成功，正在核验金额"
                : p.status === "paying"
                  ? '<span class="loading-spinner" style="width:18px;height:18px;border-width:2px;margin:0 auto 6px"></span>正在请求支付平台'
                  : statusText
            }
          </div>
        </div>
        <div class="button-row" style="margin-top:11px">
          <button class="primary-btn" data-action="start-pda-scan" ${["scanning", "recognized", "paying"].includes(p.status) ? "disabled" : ""}>开始扫码</button>
          <button class="outline-btn" data-action="fail-pda-scan" ${["scanning", "recognized", "paying"].includes(p.status) ? "disabled" : ""}>模拟失败</button>
        </div>
      `;
    }

    return `
      <div class="card card-pad">
        <div class="info-list">
          <div class="info-row"><span class="info-label">收款金额</span><span class="info-value" style="font-size:19px;color:var(--danger)">¥${money(p.amount)}</span></div>
          <div class="info-row"><span class="info-label">登记人员</span><span class="info-value">张伟 · ${VALID_EMPLOYEE}</span></div>
          <div class="info-row"><span class="info-label">设备编号</span><span class="info-value">${DEVICE_ID}</span></div>
          <div class="info-row"><span class="info-label">审计说明</span><span class="info-value">现金收款将纳入当班实收</span></div>
        </div>
        <button class="success-btn" style="margin-top:14px" data-action="confirm-cash">确认已收现金</button>
      </div>
    `;
  }

  function makeQR(seed) {
    let hash = 0;
    for (let i = 0; i < seed.length; i++) {
      hash = (hash * 31 + seed.charCodeAt(i)) >>> 0;
    }

    const finder = (x, y) => {
      const boxes = [
        [0, 0],
        [14, 0],
        [0, 14]
      ];
      return boxes.some(([bx, by]) => {
        const dx = x - bx;
        const dy = y - by;
        if (dx < 0 || dy < 0 || dx > 6 || dy > 6) return false;
        return (
          dx === 0 ||
          dy === 0 ||
          dx === 6 ||
          dy === 6 ||
          (dx >= 2 && dx <= 4 && dy >= 2 && dy <= 4)
        );
      });
    };

    let cells = "";
    for (let y = 0; y < 21; y++) {
      for (let x = 0; x < 21; x++) {
        const fixed = finder(x, y);
        const pseudo = ((x * 17 + y * 29 + hash + ((x * y) << 2)) % 7) < 3;
        cells += `<i class="${fixed || pseudo ? "on" : ""}"></i>`;
      }
    }
    return `<div class="qr" aria-label="模拟支付二维码">${cells}</div>`;
  }

  function renderPaymentSuccess() {
    const p = state.lastPayment;
    if (!p) return renderDashboard();

    return shell(
      `
        <div class="detail-hero success" style="padding-top:30px;padding-bottom:28px">
          <div class="success-mark">✓</div>
          <div class="success-amount">¥${money(p.amount)}</div>
          <div class="success-caption">支付成功</div>
        </div>

        <div class="content">
          <div class="card card-pad">
            <div class="info-list">
              <div class="info-row"><span class="info-label">支付方式</span><span class="info-value">${esc(p.methodLabel)}</span></div>
              <div class="info-row"><span class="info-label">支付时间</span><span class="info-value">${formatDateTime(p.time)}</span></div>
              <div class="info-row"><span class="info-label">订单编号</span><span class="info-value">${esc(p.orderNo)}</span></div>
              <div class="info-row"><span class="info-label">业务类型</span><span class="info-value">${p.kind === "arrears" ? "欠费补缴" : p.kind === "combined" ? "停车费及欠费合并结算" : "停车费结算"}</span></div>
              <div class="info-row"><span class="info-label">收费员</span><span class="info-value">张伟 · ${VALID_EMPLOYEE}</span></div>
            </div>
          </div>

          <section class="section">
            <button class="secondary-btn" data-action="print-last-payment">${icon("print")} 打印小票</button>
          </section>
          <section class="section">
            <div class="button-row">
              <button class="outline-btn" data-action="nav" data-route="berths">返回泊位管理</button>
              ${
                p.kind !== "arrears"
                  ? `<button class="primary-btn" data-action="open-order" data-id="${p.currentOrderId || p.orderIds[0]}">查看订单</button>`
                  : `<button class="primary-btn" data-action="open-arrears" data-plate="${esc(p.plate)}">查看补缴记录</button>`
              }
            </div>
          </section>
        </div>
      `,
      { noNav: true }
    );
  }

  function renderArrears() {
    const searched = state.arrears.searchedPlate;
    const profile = searched ? profileForPlate(searched) : null;
    const list = searched ? arrearsOrdersForPlate(searched) : [];
    const selectedOrders = list.filter((o) => state.arrears.selected.includes(o.id));
    const total = selectedOrders.reduce((sum, o) => sum + o.receivable, 0);

    return shell(
      `
        ${pageHeader("欠费补缴")}
        <div class="content">
          <div class="search-row">
            <label class="search-input">
              ${icon("search", 18)}
              <input type="text" value="${esc(state.arrears.plate)}" placeholder="输入车牌号查询欠费" data-model="arrears.plate" />
            </label>
            <button class="square-btn" data-action="search-arrears">查询</button>
          </div>

          ${
            profile
              ? `
                <div class="card card-pad arrears-profile-card">
                  <div class="arrears-profile-row">
                    <div class="plate-large arrears-profile-plate ${profile.plateColor === "绿牌" ? "green" : ""}">${esc(profile.plate)}</div>
                    <div class="arrears-profile-copy">
                      <div class="card-title">${esc(profile.types.join(" · "))}</div>
                      <button class="section-link" style="padding-left:0" data-action="open-profile" data-plate="${esc(profile.plate)}">查看车主画像 →</button>
                    </div>
                  </div>
                </div>
              `
              : ""
          }

          <section class="section">
            <div class="section-head">
              <div class="section-title">历史欠费</div>
              <span class="status-tag ${list.length ? "tag-danger" : "tag-success"}">${list.length} 笔</span>
            </div>
            ${
              list.length
                ? `
                  <div class="check-list">
                    ${list
                      .map((o) => {
                        const checked = state.arrears.selected.includes(o.id);
                        return `
                          <button class="check-card" data-action="toggle-arrear" data-id="${o.id}">
                            <span class="checkbox ${checked ? "checked" : ""}">${checked ? "✓" : ""}</span>
                            <span style="text-align:left">
                              <span class="check-card-title">${esc(o.orderNo)}</span>
                              <span class="check-card-sub">${esc(roadName(o.roadId))} · ${esc(berthNo(o.berthId))}<br/>${formatDateTime(o.startTime)}</span>
                            </span>
                            <span class="check-card-amount">¥${money(o.receivable)}</span>
                          </button>
                        `;
                      })
                      .join("")}
                  </div>
                `
                : emptyState("✓", "暂无未缴欠费", "该车辆当前不存在待补缴订单")
            }
          </section>

          ${state.arrears.error ? `<div class="error-box">${esc(state.arrears.error)}</div>` : ""}

        </div>
        ${
          list.length
            ? `
              <div class="arrears-checkout-bar">
                <div class="arrears-checkout-info">
                  <span>已选 ${selectedOrders.length} / ${list.length} 笔</span>
                  <strong>¥${money(total)}</strong>
                </div>
                <button class="small-btn small-primary" data-action="select-all-arrears">${selectedOrders.length === list.length ? "取消全选" : "全选"}</button>
                <button class="primary-btn" data-action="pay-arrears" ${selectedOrders.length ? "" : "disabled"}>补缴 ¥${money(total)}</button>
              </div>
            `
            : ""
        }
      `,
      { noNav: true, classes: "module-scroll-route arrears-route" }
    );
  }

  function filteredOrders() {
    const keyword = state.query.term.trim().toUpperCase();
    let list = [...orders].sort((a, b) => new Date(b.startTime) - new Date(a.startTime));

    if (state.query.status !== "all") {
      list = list.filter((o) => o.status === state.query.status);
    }

    if (keyword) {
      list = list.filter((o) => {
        return (
          o.plate.toUpperCase().includes(keyword) ||
          o.orderNo.toUpperCase().includes(keyword) ||
          berthNo(o.berthId).toUpperCase().includes(keyword)
        );
      });
    }

    return list;
  }

  function renderOrderQuery() {
    const list = filteredOrders();
    const filters = [
      ["all", "全部"],
      ["parking", "停车中"],
      ["paid", "已支付"],
      ["arrears", "欠费"],
      ["abnormal", "异常"],
      ["repaid", "已补缴"]
    ];

    return shell(
      `
        ${pageHeader("订单查询")}
        <div class="content">
          <div class="search-row order-query-search">
            <label class="search-input">
              ${icon("search", 18)}
              <input
                type="text"
                value="${esc(state.query.term)}"
                placeholder="车牌号 / 订单编号 / 泊位编号"
                data-model="query.term"
              />
            </label>
            <button class="square-btn order-query-submit" data-action="search-orders">查询</button>
          </div>

          <div class="chips">
            ${filters
              .map(
                ([key, label]) => `<button class="chip ${state.query.status === key ? "active" : ""}" data-action="order-filter" data-filter="${key}">${label}</button>`
              )
              .join("")}
          </div>

          <section class="section">
            <div class="section-head">
              <div class="section-title">查询结果</div>
              <span class="status-tag tag-gray">${list.length} 条</span>
            </div>
            ${
              list.length
                ? `<div class="order-list">${list.map(orderCard).join("")}</div>`
                : emptyState("⌕", "没有匹配订单", "请修改车牌、订单号、泊位号或状态筛选")
            }
          </section>
        </div>
      `,
      { noNav: true, classes: "module-scroll-route order-query-route" }
    );
  }

  function frequencyChart(values) {
    const width = 344;
    const height = 145;
    const left = 27;
    const bottom = 24;
    const top = 10;
    const chartHeight = height - bottom - top;
    const max = Math.max(...values, 4);
    const barGap = 8;
    const barWidth = (width - left - 10 - barGap * (values.length - 1)) / values.length;
    const labels = ["7/11", "7/12", "7/13", "7/14", "7/15", "7/16", "7/17"];

    let svg = `
      <svg viewBox="0 0 ${width} ${height}" role="img" aria-label="停车频率柱状图">
        <line x1="${left}" y1="${height - bottom}" x2="${width - 3}" y2="${height - bottom}" stroke="#dce5ef" stroke-width="1"/>
        <line x1="${left}" y1="${top}" x2="${left}" y2="${height - bottom}" stroke="#dce5ef" stroke-width="1"/>
    `;

    [0, Math.ceil(max / 2), max].forEach((tick) => {
      const y = height - bottom - (tick / max) * chartHeight;
      svg += `<line x1="${left}" y1="${y}" x2="${width - 3}" y2="${y}" stroke="#edf2f7" stroke-width="1"/><text x="${left - 7}" y="${y + 3}" text-anchor="end" font-size="8" fill="#94a3b8">${tick}</text>`;
    });

    values.forEach((value, index) => {
      const x = left + index * (barWidth + barGap) + 5;
      const h = Math.max(3, (value / max) * chartHeight);
      const y = height - bottom - h;
      svg += `
        <rect x="${x}" y="${y}" width="${barWidth}" height="${h}" rx="5" fill="#1677ff"/>
        <text x="${x + barWidth / 2}" y="${y - 4}" text-anchor="middle" font-size="8" font-weight="700" fill="#536079">${value}</text>
        <text x="${x + barWidth / 2}" y="${height - 8}" text-anchor="middle" font-size="8" fill="#8995aa">${labels[index]}</text>
      `;
    });

    svg += "</svg>";
    return svg;
  }

  function habitChart(profile) {
    const width = 350;
    const height = 230;
    const left = 34;
    const right = 8;
    const top = 12;
    const bottom = 24;
    const chartHeight = height - top - bottom;
    const labels = ["7/11", "7/12", "7/13", "7/14", "7/15", "7/16", "7/17"];
    const columnWidth = (width - left - right) / labels.length;
    const color = {
      paid: "#22c55e",
      arrears: "#ef4444",
      free: "#94a3b8",
      parking: "#1677ff"
    };

    let svg = `<svg viewBox="0 0 ${width} ${height}" role="img" aria-label="停车习惯图">`;

    [0, 6, 12, 18, 24].forEach((hour) => {
      const y = top + (hour / 24) * chartHeight;
      svg += `
        <line x1="${left}" y1="${y}" x2="${width - right}" y2="${y}" stroke="#edf2f7" stroke-width="1"/>
        <text x="${left - 6}" y="${y + 3}" text-anchor="end" font-size="8" fill="#94a3b8">${pad(hour)}:00</text>
      `;
    });

    labels.forEach((label, index) => {
      const x = left + index * columnWidth + columnWidth / 2;
      svg += `<text x="${x}" y="${height - 7}" text-anchor="middle" font-size="8" fill="#8995aa">${label}</text>`;
    });

    profile.habit.forEach((item) => {
      const index = labels.indexOf(item.label);
      if (index < 0) return;
      const x = left + index * columnWidth + columnWidth * 0.27;
      const y = top + (item.start / 24) * chartHeight;
      const h = Math.max(5, ((item.end - item.start) / 24) * chartHeight);
      svg += `
        <rect
          x="${x}"
          y="${y}"
          width="${columnWidth * 0.46}"
          height="${h}"
          rx="4"
          fill="${color[item.status] || color.paid}"
          opacity="0.92"
          data-action="habit-order"
          data-id="${esc(item.orderId)}"
          style="cursor:pointer"
        />
      `;
    });

    svg += "</svg>";
    return svg;
  }

  function renderProfile() {
    const profile = profileForPlate(state.profilePlate || state.params.plate);
    const arrears = arrearsOrdersForPlate(profile.plate);
    const arrearsAmount = arrears.reduce((sum, o) => sum + o.receivable, 0);
    const selectedHabitOrder = state.profileHabitOrderId ? getOrder(state.profileHabitOrderId) : null;

    return shell(
      `
        ${pageHeader("车主画像")}
        <div class="profile-header">
          <div class="plate-large ${profile.plateColor === "绿牌" ? "green" : ""}">${esc(profile.plate)}</div>
          <div class="profile-tags">
            ${profile.types.map((type) => `<span class="status-tag">${esc(type)}</span>`).join("")}
          </div>
          <div class="profile-status-line">车辆类型：${esc(profile.vehicleType)} · ${esc(profile.currentStatus)}</div>
        </div>

        <div class="content">
          <section class="section">
            <div class="section-head"><div class="section-title">套餐信息</div></div>
            <div class="card card-pad">
              ${
                profile.package
                  ? `
                    <div class="info-list">
                      <div class="info-row"><span class="info-label">是否包月</span><span class="status-tag tag-purple">包月有效</span></div>
                      <div class="info-row"><span class="info-label">套餐类型</span><span class="info-value">${esc(profile.package.type)}</span></div>
                      <div class="info-row"><span class="info-label">有效期</span><span class="info-value">${esc(profile.package.start)} 至 ${esc(profile.package.end)}</span></div>
                      <div class="info-row"><span class="info-label">剩余天数</span><span class="info-value" style="color:var(--purple)">${profile.package.remainDays} 天</span></div>
                      <div class="info-row"><span class="info-label">适用范围</span><span class="info-value">${esc(profile.package.roads)}</span></div>
                    </div>
                  `
                  : `
                    <div style="text-align:center;padding:10px 0">
                      <div style="font-size:30px">🅿</div>
                      <div style="font-size:var(--font-item-title);font-weight:900;margin-top:7px">暂无有效停车套餐</div>
                      <div style="font-size:var(--font-helper);color:var(--text-3);margin-top:5px">当前车辆按道路临时停车规则计费</div>
                    </div>
                  `
              }
            </div>
          </section>

          <section class="section">
            <div class="section-head"><div class="section-title">欠费风险</div></div>
            <div class="stats-grid">
              <div class="stat-card">
                <div class="stat-label">欠费订单数</div>
                <div class="stat-value" style="color:${arrears.length ? "var(--danger)" : "var(--success)"}">${arrears.length} 笔</div>
              </div>
              <div class="stat-card">
                <div class="stat-label">欠费总金额</div>
                <div class="stat-value" style="color:${arrearsAmount ? "var(--danger)" : "var(--success)"}">¥${money(arrearsAmount)}</div>
              </div>
              <div class="stat-card">
                <div class="stat-label">最早欠费</div>
                <div class="stat-value" style="font-size:var(--font-item-title)">${arrears.length ? formatDate(arrears[arrears.length - 1].startTime) : "--"}</div>
              </div>
              <div class="stat-card">
                <div class="stat-label">最近欠费</div>
                <div class="stat-value" style="font-size:var(--font-item-title)">${arrears.length ? formatDate(arrears[0].startTime) : "--"}</div>
              </div>
            </div>
            ${
              arrears.length
                ? `<button class="danger-btn" style="margin-top:10px" data-action="open-arrears" data-plate="${esc(profile.plate)}">立即补缴 ¥${money(arrearsAmount)}</button>`
                : `<div class="success-box">该车辆暂无历史欠费，当前信用状态正常。</div>`
            }
          </section>

          <section class="section">
            <div class="card chart-card">
              <div class="card-title">近 7 天停车频率</div>
              <div class="card-sub">X 轴为日期，Y 轴为停车次数</div>
              <div class="chart-wrap">${frequencyChart(profile.frequency)}</div>
            </div>
          </section>

          <section class="section">
            <div class="card chart-card">
              <div class="card-title">停车习惯</div>
              <div class="card-sub">点击停车时段可查看对应订单摘要</div>
              <div class="chart-wrap">${habitChart(profile)}</div>
              <div class="habit-legend">
                <span class="legend-item"><span class="legend-dot" style="background:var(--success)"></span>正常缴费</span>
                <span class="legend-item"><span class="legend-dot" style="background:var(--danger)"></span>历史欠费</span>
                <span class="legend-item"><span class="legend-dot" style="background:var(--gray-2)"></span>包月 / 免费</span>
                <span class="legend-item"><span class="legend-dot" style="background:var(--primary)"></span>停车中</span>
              </div>
              ${
                selectedHabitOrder
                  ? `
                    <div class="habit-summary">
                      <strong>${esc(selectedHabitOrder.orderNo)} · ${esc(selectedHabitOrder.plate)}</strong><br/>
                      ${esc(roadName(selectedHabitOrder.roadId))} / ${esc(berthNo(selectedHabitOrder.berthId))}<br/>
                      入场：${formatDateTime(selectedHabitOrder.startTime)}<br/>
                      状态：${orderStatusMeta[selectedHabitOrder.status]?.label || "历史订单"}，金额 ¥${money(selectedHabitOrder.receivable)}
                    </div>
                  `
                  : `<div class="habit-summary">点击图中的停车时段，查看对应订单时间、道路、泊位及缴费状态。</div>`
              }
            </div>
          </section>
        </div>
      `,
      { noNav: true, classes: "module-scroll-route vehicle-profile-route" }
    );
  }

  function renderWarnings() {
    const filters = [
      ["all", "全部"],
      ["pending", "待处理"],
      ["done", "已处理"]
    ];
    const list = warnings
      .filter((w) => state.warningFilter === "all" || w.status === state.warningFilter)
      .sort((a, b) => new Date(b.triggerTime) - new Date(a.triggerTime));

    return shell(
      `
        ${pageHeader("平台预警")}
        <div class="content">
          <div class="chips">
            ${filters
              .map(([key, label]) => `<button class="chip ${state.warningFilter === key ? "active" : ""}" data-action="warning-filter" data-filter="${key}">${label}</button>`)
              .join("")}
          </div>

          <section class="section">
            ${
              list.length
                ? `<div class="warning-list">${list.map(warningCard).join("")}</div>`
                : emptyState("✓", "暂无对应预警", "当前筛选条件下没有预警任务")
            }
          </section>
        </div>
      `,
      { nav: "dashboard", classes: "module-scroll-route warnings-route" }
    );
  }

  function renderWarningDetail() {
    const warning = getWarning(state.selectedWarningId || state.params.id);
    if (!warning) return renderWarnings();
    state.selectedWarningId = warning.id;
    const form = state.warningForm;

    return shell(
      `
        ${pageHeader("预警处理")}
        <div class="content">
          <div class="card card-pad">
            <div class="warning-detail-summary">
              <div>
                <div class="warning-title">${esc(warning.title)}</div>
                <div class="warning-info">
                  <span>${esc(warning.type)}</span>
                  <span>泊位 ${esc(berthNo(warning.berthId))}</span>
                  <span>${warning.status === "done" ? "已处理" : "待反馈"}</span>
                </div>
              </div>
              <span class="status-tag ${warning.level === "紧急" ? "tag-danger" : warning.level === "重要" ? "tag-warning" : "tag-gray"}">${esc(warning.level)}</span>
            </div>
            <div class="info-list">
              <div class="info-row"><span class="info-label">道路</span><span class="info-value">${esc(roadName(warning.roadId))}</span></div>
              <div class="info-row"><span class="info-label">泊位编号</span><span class="info-value">${esc(berthNo(warning.berthId))}</span></div>
              <div class="info-row"><span class="info-label">车牌号</span><span class="info-value">${esc(warning.plate || "--")}</span></div>
              <div class="info-row"><span class="info-label">触发时间</span><span class="info-value">${formatDateTime(warning.triggerTime)}</span></div>
            </div>
            <div class="warning-reason"><strong>预警原因：</strong>${esc(warning.reason)}</div>
            <div class="warning-reason" style="border-left:3px solid var(--primary)"><strong>处理要求：</strong>${esc(warning.requirement)}</div>
          </div>

          ${
            warning.status === "done"
              ? `
                <section class="section">
                  <div class="success-box">
                    该预警已由 ${esc(warning.feedback?.operator || "张伟")} 于 ${formatDateTime(warning.feedback?.time)} 处理。<br/>
                    处理结果：${esc(warning.feedback?.result || "已处理")}。${warning.feedback?.note ? `<br/>说明：${esc(warning.feedback.note)}` : ""}
                  </div>
                </section>
              `
              : `
                <section class="section">
                  <div class="section-head"><div class="section-title">处理反馈</div></div>
                  <div class="card card-pad">
                    <div class="form-group" style="margin-top:0">
                      <div class="form-label">处理结果</div>
                      <select class="select" data-model="warning.result">
                        ${["已处理", "现场无车", "设备异常", "车牌错误", "无法处理"]
                          .map((r) => `<option value="${r}" ${form.result === r ? "selected" : ""}>${r}</option>`)
                          .join("")}
                      </select>
                    </div>
                    <div class="form-group">
                      <div class="form-label">文字说明</div>
                      <textarea class="textarea" data-model="warning.note" placeholder="请输入现场核查情况和处理说明">${esc(form.note)}</textarea>
                    </div>

                    <div class="button-row" style="margin-top:12px">
                      <button class="secondary-btn" data-action="warning-photo">${icon("camera")} ${form.photo ? "重拍图片" : "拍摄图片"}</button>
                      <button class="outline-btn" data-action="warning-video">▶ ${form.video ? "重录视频" : "上传视频"}</button>
                    </div>

                    ${
                      form.photo
                        ? `<div class="attachment-grid"><div class="attachment-card"><div><strong>📷</strong>现场处理照片<br/>${formatTime(form.photo.time)}</div></div></div>`
                        : ""
                    }

                    ${
                      form.video
                        ? `
                          <div class="video-card">
                            <div class="video-play">▶</div>
                            <div>
                              <div style="font-size:var(--font-helper);font-weight:900">现场处置视频.mp4</div>
                              <div class="video-meta">00:12 · 3.8 MB · 已缓存</div>
                            </div>
                          </div>
                        `
                        : ""
                    }

                    <div class="info-row" style="margin-top:11px">
                      <span class="info-label">当前定位</span>
                      <span class="check-status success"><span class="dot"></span>${esc(roadName(warning.roadId))}附近 · ${state.location.accuracy}m</span>
                    </div>
                  </div>
                </section>

                ${form.error ? `<div class="error-box">${esc(form.error)}</div>` : ""}

                <section class="section">
                  <button class="primary-btn" data-action="submit-warning">提交反馈</button>
                </section>
              `
          }
        </div>
      `,
      { noNav: true, classes: "module-scroll-route warning-detail-route" }
    );
  }

  function ticketMatchesTab(ticket) {
    if (state.ticketTab === "related") return true;
    if (state.ticketTab === "pending") return ["pending", "processing"].includes(ticket.status);
    if (state.ticketTab === "completed") return ticket.status === "completed";
    if (state.ticketTab === "overdue") return ticket.status === "overdue";
    if (state.ticketTab === "created") return ticket.creator === "张伟";
    return true;
  }

  function ticketCard(ticket) {
    const status = ticketStatusMeta[ticket.status];
    const priorityClass = ticket.priority === "紧急" ? "tag-danger" : ticket.priority === "重要" ? "tag-warning" : "tag-gray";
    return `
      <button class="ticket-card" data-action="open-ticket" data-id="${ticket.id}">
        <div class="ticket-top">
          <div>
            <div class="ticket-title">${esc(ticket.title)}</div>
            <div class="ticket-info">
              <span>${esc(ticket.no)}</span>
              <span>${esc(roadName(ticket.roadId))}</span>
              ${ticket.berthId ? `<span>${esc(berthNo(ticket.berthId))}</span>` : ""}
            </div>
          </div>
          <span class="status-tag ${status.tag}">${status.label}</span>
        </div>
        <div class="ticket-desc">${esc(ticket.description)}</div>
        <div style="display:flex;justify-content:space-between;align-items:center;margin-top:10px">
          <span class="mini-tag ${priorityClass}">${esc(ticket.priority)}</span>
          <span style="font-size:var(--font-helper);color:var(--text-3)">截止 ${formatDateTime(ticket.deadline)}</span>
        </div>
      </button>
    `;
  }

  function renderTickets() {
    const tabs = [
      ["related", "与我相关"],
      ["pending", "待处理"],
      ["completed", "已完成"],
      ["overdue", "已超期"],
      ["created", "我创建的"]
    ];
    const list = tickets.filter(ticketMatchesTab).sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt));

    return shell(
      `
        ${pageHeader("工单管理", {
          back: false,
          menu: true,
          subtitle: `共 ${tickets.length} 个工单`,
          right: `<button class="header-icon-btn" data-action="new-general-ticket">＋</button>`
        })}
        <div class="content">
          <div class="chips">
            ${tabs
              .map(([key, label]) => `<button class="chip ${state.ticketTab === key ? "active" : ""}" data-action="ticket-tab" data-tab="${key}">${label}</button>`)
              .join("")}
          </div>

          <section class="section">
            ${
              list.length
                ? `<div class="ticket-list">${list.map(ticketCard).join("")}</div>`
                : emptyState("▤", "暂无对应工单", "当前分类下没有需要展示的工单")
            }
          </section>
        </div>
      `,
      { nav: "tickets", classes: "module-scroll-route tickets-route" }
    );
  }

  function renderTicketDetail() {
    const ticket = getTicket(state.selectedTicketId || state.params.id);
    if (!ticket) return renderTickets();
    state.selectedTicketId = ticket.id;
    const status = ticketStatusMeta[ticket.status];

    return shell(
      `
        ${pageHeader("工单详情")}
        <div class="detail-hero">
          <div class="hero-label">${esc(ticket.no)}</div>
          <div class="hero-value" style="font-size:21px;line-height:1.35">${esc(ticket.title)}</div>
          <div class="hero-meta-grid">
            <div class="hero-meta"><strong>${status.label}</strong><span>当前状态</span></div>
            <div class="hero-meta"><strong>${esc(ticket.priority)}</strong><span>优先级</span></div>
            <div class="hero-meta"><strong>${esc(ticket.source)}</strong><span>来源</span></div>
          </div>
        </div>

        <div class="content">
          <div class="card card-pad">
            <div class="warning-reason" style="margin-top:0">${esc(ticket.description)}</div>
            <div class="info-list" style="margin-top:9px">
              <div class="info-row"><span class="info-label">工单类型</span><span class="info-value">${esc(ticket.type)}</span></div>
              <div class="info-row"><span class="info-label">道路 / 泊位</span><span class="info-value">${esc(roadName(ticket.roadId))}${ticket.berthId ? ` / ${esc(berthNo(ticket.berthId))}` : ""}</span></div>
              <div class="info-row"><span class="info-label">设备编号</span><span class="info-value">${esc(ticket.deviceId || "--")}</span></div>
              <div class="info-row"><span class="info-label">当前处理人</span><span class="info-value">${esc(ticket.assignee)}</span></div>
              <div class="info-row"><span class="info-label">创建时间</span><span class="info-value">${formatDateTime(ticket.createdAt)}</span></div>
              <div class="info-row"><span class="info-label">截止时间</span><span class="info-value">${formatDateTime(ticket.deadline)}</span></div>
            </div>
          </div>

          <section class="section">
            <div class="section-head"><div class="section-title">附件</div></div>
            ${
              ticket.attachments.length
                ? `<div class="attachment-grid">${ticket.attachments.map((a) => `<div class="attachment-card"><div><strong>📎</strong>${esc(a)}</div></div>`).join("")}</div>`
                : `<div class="card card-pad" style="font-size:var(--font-helper);color:var(--text-3);text-align:center">暂无附件</div>`
            }
          </section>

          <section class="section">
            <div class="section-head"><div class="section-title">处理时间轴</div></div>
            <div class="card card-pad">
              <div class="timeline">
                ${ticket.timeline
                  .map(
                    (item) => `
                      <div class="timeline-item">
                        <div class="timeline-title">${esc(item.title)}</div>
                        <div class="timeline-time">${formatDateTime(item.time)}</div>
                        <div class="timeline-desc">${esc(item.desc)}</div>
                      </div>
                    `
                  )
                  .join("")}
              </div>
            </div>
          </section>

          <section class="section">
            ${ticketActions(ticket)}
          </section>
        </div>
      `,
      { noNav: true, classes: "module-scroll-route ticket-detail-route" }
    );
  }

  function ticketActions(ticket) {
    if (ticket.status === "completed") {
      return `<div class="success-box">工单已完成闭环，无需继续处理。</div>`;
    }

    if (ticket.status === "pending" || ticket.status === "overdue" || ticket.status === "returned") {
      return `
        <div class="button-row">
          <button class="primary-btn" data-action="accept-ticket" data-id="${ticket.id}">接单处理</button>
          <button class="outline-btn" data-action="open-transfer" data-id="${ticket.id}">转派</button>
        </div>
      `;
    }

    return `
      <div class="button-row">
        <button class="secondary-btn" data-action="ticket-feedback" data-id="${ticket.id}">提交反馈</button>
        <button class="success-btn" data-action="complete-ticket" data-id="${ticket.id}">完成工单</button>
      </div>
      <div class="button-row" style="margin-top:10px">
        <button class="outline-btn" data-action="open-transfer" data-id="${ticket.id}">转派</button>
        <button class="outline-btn" data-action="open-return" data-id="${ticket.id}">退回</button>
      </div>
    `;
  }

  function renderTicketFeedback() {
    const ticket = getTicket(state.selectedTicketId || state.params.id);
    if (!ticket) return renderTickets();
    const form = state.ticketFeedback;

    return shell(
      `
        ${pageHeader("工单处理反馈")}
        <div class="content">
          <div class="card card-pad">
            <div class="card-title">${esc(ticket.title)}</div>
            <div class="card-sub">${esc(ticket.no)} · ${esc(roadName(ticket.roadId))}</div>

            <div class="form-group">
              <div class="form-label">处理说明</div>
              <textarea class="textarea" data-model="ticketFeedback.note" placeholder="描述现场检查、处置措施和处理结果">${esc(form.note)}</textarea>
            </div>

            <div class="form-group">
              <div class="form-label">现场照片</div>
              ${
                form.photo
                  ? `<div class="attachment-card"><div><strong>📷</strong>工单处理照片<br/>${formatTime(form.photo.time)}</div></div>`
                  : `<button class="secondary-btn" data-action="ticket-feedback-photo">${icon("camera")} 拍摄现场照片</button>`
              }
            </div>
          </div>

          ${form.error ? `<div class="error-box">${esc(form.error)}</div>` : ""}

          <section class="section">
            <button class="primary-btn" data-action="submit-ticket-feedback">提交处理反馈</button>
          </section>
        </div>
      `,
      { noNav: true }
    );
  }

  function renderNewTicket() {
    const form = state.newTicket;
    const availableBerths = berths.filter((b) => b.roadId === form.roadId);
    const berth = getBerth(form.berthId);

    return shell(
      `
        ${pageHeader("新建工单")}
        <div class="content">
          <div class="card card-pad">
            <div class="form-group" style="margin-top:0">
              <div class="form-label">工单类型</div>
              <select class="select" data-model="newTicket.type">
                ${["地磁设备故障", "泊位标线问题", "车辆异常停放", "拒缴 / 逃费", "订单异常", "收费设备故障", "其他问题"]
                  .map((v) => `<option value="${v}" ${form.type === v ? "selected" : ""}>${v}</option>`)
                  .join("")}
              </select>
            </div>

            <div class="form-group">
              <div class="form-label">道路</div>
              <select class="select" data-model="newTicket.roadId">
                ${roads.map((r) => `<option value="${r.id}" ${form.roadId === r.id ? "selected" : ""}>${esc(r.name)}</option>`).join("")}
              </select>
            </div>

            <div class="form-group">
              <div class="form-label">泊位编号</div>
              <select class="select" data-model="newTicket.berthId">
                <option value="">请选择泊位</option>
                ${availableBerths.map((b) => `<option value="${b.id}" ${form.berthId === b.id ? "selected" : ""}>${esc(b.no)} · ${berthStatusMeta[b.status].label}</option>`).join("")}
              </select>
            </div>

            ${
              form.type === "地磁设备故障"
                ? `
                  <div class="form-group">
                    <div class="form-label">地磁设备编号</div>
                    <div class="input-wrap" style="background:#eef3f8">
                      <input type="text" disabled value="${esc(berth?.deviceId || "选择泊位后自动带出")}" />
                    </div>
                  </div>
                  <div class="form-group">
                    <div class="form-label">故障类型</div>
                    <select class="select" data-model="newTicket.faultType">
                      ${["离线", "误报", "有车显示无车", "无车显示有车"]
                        .map((v) => `<option value="${v}" ${form.faultType === v ? "selected" : ""}>${v}</option>`)
                        .join("")}
                    </select>
                  </div>
                `
                : ""
            }

            <div class="form-group">
              <div class="form-label">问题描述</div>
              <textarea class="textarea" data-model="newTicket.description" placeholder="请描述现场问题、影响范围和已采取措施">${esc(form.description)}</textarea>
            </div>

            <div class="form-group">
              <div class="form-label">紧急程度</div>
              <div class="chips">
                ${["普通", "重要", "紧急"]
                  .map(
                    (v) => `<button class="chip ${form.priority === v ? "active" : ""} ${v === "紧急" ? "danger-active" : ""}" data-action="ticket-priority" data-value="${v}">${v}</button>`
                  )
                  .join("")}
              </div>
            </div>

            <div class="form-group">
              <div class="form-label">现场照片</div>
              ${
                form.photo
                  ? `<div class="attachment-card"><div><strong>📷</strong>现场故障照片<br/>${formatTime(form.photo.time)}</div></div>`
                  : `<button class="secondary-btn" data-action="new-ticket-photo">${icon("camera")} 拍摄现场照片</button>`
              }
            </div>
          </div>

          ${form.error ? `<div class="error-box">${esc(form.error)}</div>` : ""}

          <section class="section">
            <button class="primary-btn" data-action="submit-new-ticket">提交工单</button>
          </section>
        </div>
      `,
      { noNav: true, classes: "module-scroll-route new-ticket-route" }
    );
  }

  function reportData(period) {
    const scale = {
      today: 1,
      week: 6.3,
      month: 22.5,
      custom: 8.7
    }[period] || 1;

    return {
      receivable: 386.5 * scale,
      received: 332 * scale,
      arrears: 54.5 * scale,
      repayment: 40 * scale,
      ownerScan: 165.5 * scale,
      pdaScan: 126.5 * scale,
      cash: 0,
      created: Math.round(18 * scale),
      paidCount: Math.round(15 * scale),
      printCount: Math.round(5 * scale),
      rate: 85.9,
      dayPerformance: 92,
      monthPerformance: 88,
      trend:
        period === "today"
          ? [22, 36, 58, 44, 70, 52, 50]
          : period === "week"
            ? [286, 335, 298, 372, 418, 396, 421]
            : period === "month"
              ? monthlyIncome
              : [268, 312, 355, 332, 408, 390, 424]
    };
  }

  function barChart(values, labels = []) {
    const width = 350;
    const height = 160;
    const left = 30;
    const bottom = 25;
    const top = 12;
    const max = Math.max(...values, 1);
    const chartHeight = height - top - bottom;
    const areaWidth = width - left - 8;
    const gap = values.length > 10 ? 3 : 8;
    const barWidth = Math.max(5, (areaWidth - gap * (values.length - 1)) / values.length);

    let svg = `
      <svg viewBox="0 0 ${width} ${height}">
        <line x1="${left}" y1="${height - bottom}" x2="${width - 4}" y2="${height - bottom}" stroke="#dce5ef"/>
        <line x1="${left}" y1="${top}" x2="${left}" y2="${height - bottom}" stroke="#dce5ef"/>
    `;

    [0, 0.5, 1].forEach((ratio) => {
      const y = height - bottom - chartHeight * ratio;
      const val = Math.round(max * ratio);
      svg += `
        <line x1="${left}" y1="${y}" x2="${width - 4}" y2="${y}" stroke="#edf2f7"/>
        <text x="${left - 6}" y="${y + 3}" text-anchor="end" font-size="8" fill="#94a3b8">${val}</text>
      `;
    });

    values.forEach((value, index) => {
      const x = left + index * (barWidth + gap) + 3;
      const h = Math.max(3, (value / max) * chartHeight);
      const y = height - bottom - h;
      const label = labels[index] || String(index + 1);
      const showLabel = values.length <= 10 || index % 3 === 0 || index === values.length - 1;
      svg += `
        <defs>
          <linearGradient id="barGrad${index}" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#1677ff"/>
            <stop offset="100%" stop-color="#76b8ff"/>
          </linearGradient>
        </defs>
        <rect x="${x}" y="${y}" width="${barWidth}" height="${h}" rx="${Math.min(5, barWidth / 2)}" fill="url(#barGrad${index})"/>
        ${showLabel ? `<text x="${x + barWidth / 2}" y="${height - 8}" text-anchor="middle" font-size="8" fill="#8995aa">${esc(label)}</text>` : ""}
      `;
    });

    svg += "</svg>";
    return svg;
  }

  function renderReports() {
    const data = reportData(state.reportPeriod);
    const periods = [
      ["today", "今日"],
      ["week", "本周"],
      ["month", "本月"],
      ["custom", "自定义"]
    ];
    const labels =
      state.reportPeriod === "today"
        ? ["08", "10", "12", "14", "16", "18", "20"]
        : state.reportPeriod === "month"
          ? monthlyIncome.map((_, i) => String(i + 1))
          : ["周一", "周二", "周三", "周四", "周五", "周六", "周日"];

    return shell(
      `
        <div class="module-filter-header">
          ${menuButton()}
          <div class="report-period report-period-inline">
            <div class="chips">
              ${periods.map(([key, label]) => `<button class="chip ${state.reportPeriod === key ? "active" : ""}" data-action="report-period" data-period="${key}">${label}</button>`).join("")}
            </div>
          </div>
        </div>
        ${
          state.reportPeriod === "custom"
            ? `
              <div class="custom-date-box report-custom-range">
                <input type="date" value="${state.reportCustom.start}" data-model="report.start"/>
                <span>至</span>
                <input type="date" value="${state.reportCustom.end}" data-model="report.end"/>
              </div>
            `
            : ""
        }

        <div class="content">
          <div class="report-grid">
            <div class="report-card primary">
              <div class="report-label">应收金额</div>
              <div class="report-value">¥${money(data.receivable)}</div>
              <div class="report-change">较同期 +8.4%</div>
            </div>
            <div class="report-card">
              <div class="report-label">实收金额</div>
              <div class="report-value" style="color:var(--primary)">¥${money(data.received)}</div>
              <div class="report-change">较同期 +6.7%</div>
            </div>
            <div class="report-card">
              <div class="report-label">收缴率</div>
              <div class="report-value" style="color:var(--success)">${data.rate}%</div>
              <div class="report-change">目标 88%</div>
            </div>
            <div class="report-card">
              <div class="report-label">欠费金额</div>
              <div class="report-value" style="color:var(--danger)">¥${money(data.arrears)}</div>
              <div class="report-change" style="color:var(--danger)">待持续跟进</div>
            </div>
            <div class="report-card">
              <div class="report-label">补缴金额</div>
              <div class="report-value" style="color:var(--purple)">¥${money(data.repayment)}</div>
            </div>
            <div class="report-card">
              <div class="report-label">创单数量</div>
              <div class="report-value">${data.created}</div>
            </div>
            <div class="report-card">
              <div class="report-label">支付笔数</div>
              <div class="report-value">${data.paidCount}</div>
            </div>
            <div class="report-card">
              <div class="report-label">小票打印</div>
              <div class="report-value">${data.printCount}</div>
            </div>
          </div>

          <section class="section">
            <div class="card chart-card">
              <div class="card-title">收费趋势</div>
              <div class="card-sub">实收金额 · 单位：元</div>
              <div class="chart-wrap">${barChart(data.trend, labels)}</div>
            </div>
          </section>

          <section class="section">
            <div class="card chart-card">
              <div class="card-title">支付方式占比</div>
              <div class="donut-layout">
                <div class="donut">
                  <div class="donut-center"><strong>¥${money(data.received)}</strong>实收合计</div>
                </div>
                <div class="donut-legend">
                  <div class="donut-line"><span class="donut-name"><span class="legend-dot" style="background:var(--primary)"></span>车主扫码</span><strong>47%</strong></div>
                  <div class="donut-line"><span class="donut-name"><span class="legend-dot" style="background:var(--success)"></span>PDA 扫码</span><strong>31%</strong></div>
                  <div class="donut-line"><span class="donut-name"><span class="legend-dot" style="background:var(--warning)"></span>欠费补缴</span><strong>13%</strong></div>
                  <div class="donut-line"><span class="donut-name"><span class="legend-dot" style="background:var(--purple)"></span>其他</span><strong>9%</strong></div>
                </div>
              </div>
            </div>
          </section>

          <section class="section">
            <div class="card chart-card">
              <div class="card-title">绩效达成</div>
              <div class="card-sub">基于收费、创单、补缴和预警响应综合计算</div>
              <div class="progress-list">
                ${progressItem("当日考核达成率", data.dayPerformance, "primary")}
                ${progressItem("当月考核达成率", data.monthPerformance, "success")}
                ${progressItem("收费目标", 86, "primary")}
                ${progressItem("创单目标", 94, "success")}
                ${progressItem("补缴目标", 72, "warning")}
                ${progressItem("预警响应及时率", 96, "success")}
              </div>
            </div>
          </section>

          <section class="section">
            <div class="stats-grid">
              <div class="stat-card"><div class="stat-label">车主扫码金额</div><div class="stat-value">¥${money(data.ownerScan)}</div></div>
              <div class="stat-card"><div class="stat-label">PDA 扫码金额</div><div class="stat-value">¥${money(data.pdaScan)}</div></div>
            </div>
          </section>
        </div>
      `,
      { nav: "reports", classes: "module-scroll-route reports-route" }
    );
  }

  function progressItem(label, value, type) {
    return `
      <div>
        <div class="progress-head"><span>${esc(label)}</span><span>${value}%</span></div>
        <div class="progress-track"><div class="progress-bar ${type}" style="width:${Math.min(100, value)}%"></div></div>
      </div>
    `;
  }

  function renderMine() {
    return shell(
      `
        <div class="profile-header profile-identity-header">
          ${menuButton()}
          <div class="profile-identity">
            <div class="staff-name">张伟</div>
            <div class="staff-meta">收费员 ${VALID_EMPLOYEE} · 中心城区一片区</div>
          </div>
          <button class="location-button" data-action="open-location">
            ${icon("location", 22)}
            <span class="location-dot ${state.location.success ? "" : "fail"}"></span>
          </button>
        </div>

        <div class="content">
          <div class="card card-pad">
            <div class="info-list">
              <div class="info-row"><span class="info-label">今日上班时间</span><span class="info-value">${state.clockInTime ? formatDateTime(state.clockInTime) : "2026-07-17 08:28:35"}</span></div>
              <div class="info-row"><span class="info-label">当前设备编号</span><span class="info-value">${DEVICE_ID}</span></div>
              <div class="info-row"><span class="info-label">当前道路</span><span class="info-value">${esc(currentRoad().name)}</span></div>
              <div class="info-row"><span class="info-label">定位上报状态</span><button class="section-link" data-action="open-location">${state.location.success ? "正常上报" : "上报失败"} →</button></div>
              <div class="info-row"><span class="info-label">APP 版本</span><span class="info-value">${VERSION}</span></div>
            </div>
          </div>

          <section class="section">
            <div class="section-head"><div class="section-title">系统权限</div></div>
            <div class="permission-list">
              ${permissionItem("📍", "定位权限", "已允许")}
              ${permissionItem("ᛒ", "蓝牙权限", "已允许")}
              ${permissionItem("📷", "相机权限", "已允许")}
              ${permissionItem("🔔", "通知权限", "已允许")}
            </div>
          </section>

          <section class="section">
            <button class="danger-btn" data-action="go-clock-out">下班打卡</button>
          </section>
        </div>
      `,
      { nav: "mine", classes: "module-scroll-route mine-route" }
    );
  }

  function permissionItem(iconText, label, value) {
    return `
      <div class="permission-item">
        <div class="permission-left">
          <div class="permission-icon blue-soft">${iconText}</div>
          <span>${esc(label)}</span>
        </div>
        <span class="status-tag tag-success"><span class="dot"></span>${esc(value)}</span>
      </div>
    `;
  }

  function shiftDuration() {
    return state.clockInTime ? durationText(state.clockInTime) : "9小时32分";
  }

  function renderClockOut() {
    const s = state.shiftStats;
    const monthlyTotal = monthlyIncome.reduce((sum, n) => sum + n, 0);
    const labels = monthlyIncome.map((_, i) => String(i + 1));

    return shell(
      `
        ${pageHeader("下班打卡")}
        <div class="content">
          <div class="monthly-hero">
            <div style="font-size:var(--font-helper);opacity:.78">当班实收金额</div>
            <div class="monthly-total">¥${money(s.received)}</div>
            <div class="monthly-change">收缴率 ${(s.received / s.receivable * 100).toFixed(1)}% · 创单 ${s.creationCount} 笔</div>
          </div>

          <section class="section">
            <div class="section-head"><div class="section-title">当班统计</div></div>
            <div class="card card-pad">
              <div class="info-list">
                <div class="info-row"><span class="info-label">上班时间</span><span class="info-value">${state.clockInTime ? formatDateTime(state.clockInTime) : "2026-07-17 08:28:35"}</span></div>
                <div class="info-row"><span class="info-label">工作时长</span><span class="info-value">${shiftDuration()}</span></div>
                <div class="info-row"><span class="info-label">拍照创单次数</span><span class="info-value">${s.creationCount}</span></div>
                <div class="info-row"><span class="info-label">应收金额</span><span class="info-value">¥${money(s.receivable)}</span></div>
                <div class="info-row"><span class="info-label">实收金额</span><span class="info-value" style="color:var(--success)">¥${money(s.received)}</span></div>
                <div class="info-row"><span class="info-label">车主扫码缴费</span><span class="info-value">¥${money(s.ownerScan)}</span></div>
                <div class="info-row"><span class="info-label">PDA 扫付款码</span><span class="info-value">¥${money(s.pdaScan)}</span></div>
                <div class="info-row"><span class="info-label">欠费补缴金额</span><span class="info-value">¥${money(s.arrears)}</span></div>
                <div class="info-row"><span class="info-label">处置平台任务</span><span class="info-value">${s.taskCount} 次</span></div>
                <div class="info-row"><span class="info-label">工单处理数量</span><span class="info-value">${s.ticketCount} 个</span></div>
              </div>
            </div>
          </section>

          <section class="section">
            <div class="section-head"><div class="section-title">当月统计</div></div>
            <div class="stats-grid">
              <div class="stat-card"><div class="stat-label">当月出勤天数</div><div class="stat-value">16 天</div></div>
              <div class="stat-card"><div class="stat-label">当月绩效达成率</div><div class="stat-value" style="color:var(--success)">88%</div></div>
              <div class="stat-card"><div class="stat-label">当月累计应收</div><div class="stat-value">¥8,760</div></div>
              <div class="stat-card"><div class="stat-label">当月累计实收</div><div class="stat-value">¥${money(monthlyTotal)}</div></div>
              <div class="stat-card"><div class="stat-label">当月创单数量</div><div class="stat-value">386</div></div>
              <div class="stat-card"><div class="stat-label">当月补缴金额</div><div class="stat-value">¥920</div></div>
            </div>
            <div class="success-box">同比增长 8.6%，当月收缴率较去年同期提升 2.4 个百分点。</div>
          </section>

          <section class="section">
            <div class="card chart-card">
              <div class="card-title">当月实收金额</div>
              <div class="card-sub">X 轴：日期　Y 轴：实收金额（元）</div>
              <div class="chart-wrap">${barChart(monthlyIncome, labels)}</div>
            </div>
          </section>

          <section class="section">
            <div class="section-head">
              <div class="section-title">下班照片</div>
              ${state.clockOut.photo ? `<span class="status-tag tag-success">已拍摄</span>` : ""}
            </div>
            ${photoBlock(state.clockOut.photo, "下班打卡", { road: currentRoad().name })}
            <button class="secondary-btn" style="margin-top:11px" data-action="capture-clock-out">
              ${icon("camera")} ${state.clockOut.photo ? "重新拍摄下班照片" : "拍摄下班照片"}
            </button>
          </section>

          ${state.clockOut.error ? `<div class="error-box">${esc(state.clockOut.error)}</div>` : ""}

          <section class="section">
            <button class="danger-btn" data-action="submit-clock-out">确认下班打卡并登出</button>
          </section>
        </div>
      `,
      { noNav: true, classes: "attendance-scroll-route clock-out-route" }
    );
  }

  function renderModal() {
    const modal = state.modal;
    if (!modal) {
      modalRoot.innerHTML = "";
      return;
    }

    if (modal.type === "roads") {
      modalRoot.innerHTML = `
        <div class="modal-backdrop">
          <div class="modal-sheet" data-modal-panel>
            <div class="sheet-grip"></div>
            <div class="modal-head">
              <div>
                <div class="modal-title">切换管理道路</div>
                <div class="card-sub">选择后将刷新泊位、订单和任务数据</div>
              </div>
              <button class="modal-close" data-action="close-modal">${icon("close", 18)}</button>
            </div>
            <div class="road-list">
              ${roads
                .map((road) => {
                  const summary = berthSummary(road.id);
                  return `
                    <button class="road-card ${state.currentRoadId === road.id ? "active" : ""}" data-action="select-road" data-id="${road.id}">
                      <div class="road-card-name">
                        <span>${esc(road.name)}</span>
                        ${state.currentRoadId === road.id ? `<span class="status-tag tag-primary">当前道路</span>` : `<span style="font-size:var(--font-helper);color:var(--text-3)">${road.distance}</span>`}
                      </div>
                      <div class="card-sub">${esc(road.area)} · 距离 ${road.distance}</div>
                      <div class="road-card-stats">
                        <div class="road-stat"><strong>${summary.total}</strong><span>总泊位</span></div>
                        <div class="road-stat"><strong style="color:var(--success)">${summary.idle}</strong><span>空闲</span></div>
                        <div class="road-stat"><strong style="color:var(--primary)">${summary.parking}</strong><span>停车中</span></div>
                        <div class="road-stat"><strong style="color:var(--warning)">${summary.pending}</strong><span>待录入</span></div>
                        <div class="road-stat"><strong style="color:var(--danger)">${summary.fault}</strong><span>故障</span></div>
                      </div>
                    </button>
                  `;
                })
                .join("")}
            </div>
          </div>
        </div>
      `;
      return;
    }

    if (modal.type === "location") {
      modalRoot.innerHTML = `
        <div class="modal-backdrop">
          <div class="modal-sheet" data-modal-panel>
            <div class="sheet-grip"></div>
            <div class="modal-head">
              <div>
                <div class="modal-title">定位上报状态</div>
                <div class="card-sub">收费员在岗定位周期性上报</div>
              </div>
              <button class="modal-close" data-action="close-modal">${icon("close", 18)}</button>
            </div>
            <div class="content">
              <div class="location-map ${state.location.success ? "" : "fail"}"></div>
              <div class="card card-pad" style="margin-top:11px">
                <div class="info-list">
                  <div class="info-row">
                    <span class="info-label">当前定位状态</span>
                    <span class="check-status ${state.location.success ? "success" : "danger"}"><span class="dot"></span>${state.location.success ? "定位及上报成功" : "定位上报失败"}</span>
                  </div>
                  <div class="info-row"><span class="info-label">最近上报时间</span><span class="info-value last-report-text">${formatDateTime(state.location.lastReport)}</span></div>
                  <div class="info-row"><span class="info-label">定位精度</span><span class="info-value">${state.location.success ? `${state.location.accuracy} 米` : "--"}</span></div>
                  <div class="info-row"><span class="info-label">网络状态</span><span class="info-value">${esc(state.location.network)}</span></div>
                  <div class="info-row"><span class="info-label">经纬度</span><span class="info-value">${state.location.success ? `${state.location.longitude.toFixed(6)}, ${state.location.latitude.toFixed(6)}` : "--"}</span></div>
                </div>
              </div>
              <button class="${state.location.success ? "danger-btn" : "success-btn"}" style="margin-top:12px" data-action="toggle-location">
                ${state.location.success ? "模拟定位失败" : "恢复定位上报"}
              </button>
            </div>
          </div>
        </div>
      `;
      return;
    }

    if (modal.type === "parkingSlip") {
      const order = getOrder(modal.orderId);
      if (!order) {
        state.modal = null;
        modalRoot.innerHTML = "";
        return;
      }
      const currentFee = order.status === "parking" ? calcFee(order.startTime) : order.receivable;
      modalRoot.innerHTML = `
        <div class="modal-backdrop">
          <div class="modal-dialog parking-slip-modal" data-modal-panel>
            <div class="modal-head">
              <div>
                <div class="modal-title">停车凭条预览</div>
                <div class="card-sub">蓝牙打印机：已连接</div>
              </div>
              <button class="modal-close" data-action="close-modal">${icon("close", 18)}</button>
            </div>
            <div class="receipt parking-slip">
              <div class="receipt-title">惠泊云道路停车缴费凭条</div>
              <div class="receipt-subtitle">请将本凭条夹于车辆前挡风玻璃雨刮器处</div>
              <div class="receipt-divider"></div>
              ${receiptRow("订单编号", order.orderNo)}
              ${receiptRow("车牌号", order.plate)}
              ${receiptRow("停车道路", roadName(order.roadId))}
              ${receiptRow("泊位编号", berthNo(order.berthId))}
              ${receiptRow("入场时间", formatDateTime(order.startTime))}
              ${receiptRow("当前停车时长", durationText(order.startTime, new Date()))}
              ${receiptRow("当前应付金额", `¥${money(currentFee)}`)}
              <div class="receipt-divider"></div>
              <div class="parking-slip-qr">
                ${makeQR(`owner-payment.html?order=${encodeURIComponent(order.id)}`)}
                <strong>微信扫码缴纳停车费</strong>
                <span>支持勾选历史欠费合并支付</span>
              </div>
              <div class="receipt-footer">
                离场费用以实际支付时间为准<br/>
                客服电话：400-889-8891
              </div>
            </div>
            <div class="content parking-slip-actions">
              <button class="primary-btn" data-action="confirm-parking-slip" data-id="${order.id}">${icon("print")} 发送至蓝牙打印机</button>
            </div>
          </div>
        </div>
      `;
      return;
    }

    if (modal.type === "receipt") {
      const order = getOrder(modal.orderId) || getOrder(state.lastPayment?.orderIds?.[0]);
      if (!order) {
        state.modal = null;
        modalRoot.innerHTML = "";
        return;
      }
      modalRoot.innerHTML = `
        <div class="modal-backdrop">
          <div class="modal-dialog" data-modal-panel>
            <div class="modal-head">
              <div>
                <div class="modal-title">收费小票预览</div>
                <div class="card-sub">蓝牙打印机：已连接</div>
              </div>
              <button class="modal-close" data-action="close-modal">${icon("close", 18)}</button>
            </div>
            <div class="receipt">
              <div class="receipt-title">城市道路停车收费小票</div>
              <div class="receipt-subtitle">${esc(roadName(order.roadId))}</div>
              <div class="receipt-divider"></div>
              ${receiptRow("订单编号", order.orderNo)}
              ${receiptRow("车牌号", order.plate)}
              ${receiptRow("泊位编号", berthNo(order.berthId))}
              ${receiptRow("入场时间", formatDateTime(order.startTime))}
              ${receiptRow("支付时间", formatDateTime(order.endTime || state.lastPayment?.time || new Date()))}
              ${receiptRow("停车时长", durationText(order.startTime, order.endTime || new Date()))}
              ${receiptRow("应收金额", `¥${money(order.receivable)}`)}
              ${receiptRow("优惠金额", `¥${money(order.discount)}`)}
              ${receiptRow("实收金额", `¥${money(order.paid || order.receivable)}`)}
              ${receiptRow("支付方式", order.paymentMethod || state.lastPayment?.methodLabel || "扫码支付")}
              ${receiptRow("收费员", `张伟 / ${VALID_EMPLOYEE}`)}
              <div class="receipt-divider"></div>
              <div class="receipt-amount">¥${money(order.paid || order.receivable)}</div>
              <div class="receipt-footer">
                客服电话：400-889-8891<br/>
                请妥善保管本小票，感谢您的配合
              </div>
            </div>
            <div class="content" style="padding-top:0">
              <button class="primary-btn" data-action="confirm-print" data-id="${order.id}">${icon("print")} 发送至蓝牙打印机</button>
            </div>
          </div>
        </div>
      `;
      return;
    }

    if (modal.type === "transfer") {
      modalRoot.innerHTML = `
        <div class="modal-backdrop">
          <div class="modal-sheet" data-modal-panel>
            <div class="sheet-grip"></div>
            <div class="modal-head">
              <div class="modal-title">转派工单</div>
              <button class="modal-close" data-action="close-modal">${icon("close", 18)}</button>
            </div>
            <div class="content">
              <div class="card card-pad">
                <div class="form-label">选择接收人员</div>
                <div class="check-list">
                  ${["李强", "王敏", "设备维护组", "市政维护组"]
                    .map(
                      (person) => `
                        <button class="check-card" data-action="select-transfer-person" data-person="${person}">
                          <span class="checkbox ${state.transferPerson === person ? "checked" : ""}">${state.transferPerson === person ? "✓" : ""}</span>
                          <span class="check-card-title" style="text-align:left">${person}</span>
                          <span class="status-tag tag-gray">${person.includes("组") ? "班组" : "人员"}</span>
                        </button>
                      `
                    )
                    .join("")}
                </div>
              </div>
              <button class="primary-btn" style="margin-top:12px" data-action="confirm-transfer" data-id="${modal.ticketId}">确认转派</button>
            </div>
          </div>
        </div>
      `;
      return;
    }

    if (modal.type === "return") {
      modalRoot.innerHTML = `
        <div class="modal-backdrop">
          <div class="modal-sheet" data-modal-panel>
            <div class="sheet-grip"></div>
            <div class="modal-head">
              <div class="modal-title">退回工单</div>
              <button class="modal-close" data-action="close-modal">${icon("close", 18)}</button>
            </div>
            <div class="content">
              <div class="card card-pad">
                <div class="form-label">退回原因</div>
                <textarea class="textarea" data-model="returnReason" placeholder="请说明无法继续处理或需要补充的信息">${esc(state.returnReason)}</textarea>
              </div>
              <button class="danger-btn" style="margin-top:12px" data-action="confirm-return" data-id="${modal.ticketId}">确认退回</button>
            </div>
          </div>
        </div>
      `;
    }
  }

  function receiptRow(label, value) {
    return `<div class="receipt-row"><span>${esc(label)}</span><strong>${esc(value)}</strong></div>`;
  }

  function render() {
    const currentScrollContainer = app.querySelector(".screen.module-scroll-route > .content");
    const preservedScrollTop =
      lastRenderedRoute === state.route && currentScrollContainer
        ? currentScrollContainer.scrollTop
        : null;
    let html;

    switch (state.route) {
      case "login":
        html = renderLogin();
        break;
      case "attendance":
        html = renderAttendance();
        break;
      case "dashboard":
        html = renderDashboard();
        break;
      case "berths":
        html = renderBerths();
        break;
      case "berthDetail":
        html = renderBerthDetail();
        break;
      case "createOrder":
        html = renderCreateOrder();
        break;
      case "orderDetail":
        html = renderOrderDetail();
        break;
      case "payment":
        html = renderPayment();
        break;
      case "paymentSuccess":
        html = renderPaymentSuccess();
        break;
      case "arrears":
        html = renderArrears();
        break;
      case "orderQuery":
        html = renderOrderQuery();
        break;
      case "profile":
        html = renderProfile();
        break;
      case "warnings":
        html = renderWarnings();
        break;
      case "warningDetail":
        html = renderWarningDetail();
        break;
      case "tickets":
        html = renderTickets();
        break;
      case "ticketDetail":
        html = renderTicketDetail();
        break;
      case "ticketFeedback":
        html = renderTicketFeedback();
        break;
      case "newTicket":
        html = renderNewTicket();
        break;
      case "reports":
        html = renderReports();
        break;
      case "mine":
        html = renderMine();
        break;
      case "clockOut":
        html = renderClockOut();
        break;
      default:
        html = renderLogin();
    }

    app.innerHTML = html;
    renderModal();
    afterRender();

    lastRenderedRoute = state.route;
    if (preservedScrollTop !== null) {
      const nextScrollContainer = app.querySelector(".screen.module-scroll-route > .content");
      if (nextScrollContainer) {
        nextScrollContainer.scrollTop = preservedScrollTop;
        requestAnimationFrame(() => {
          if (nextScrollContainer.isConnected && lastRenderedRoute === state.route) {
            nextScrollContainer.scrollTop = preservedScrollTop;
          }
        });
      }
    }
  }

  function afterRender() {
    clearInterval(paymentTimer);
    paymentTimer = null;

    if (state.route === "payment" && state.payment.method === "owner") {
      paymentTimer = setInterval(() => {
        if (state.route !== "payment" || state.payment.method !== "owner") {
          clearInterval(paymentTimer);
          return;
        }
        state.payment.countdown -= 1;
        if (state.payment.countdown <= 0) {
          state.payment.countdown = 60;
          toast("支付二维码已自动刷新", "info");
        }
        const el = document.getElementById("payment-countdown");
        if (el) {
          el.textContent = `${pad(Math.floor(state.payment.countdown / 60))}:${pad(state.payment.countdown % 60)}`;
        }
      }, 1000);
    }
  }

  function startLocationReporting() {
    clearInterval(reportTimer);
    if (!state.clockedIn) return;

    reportTimer = setInterval(() => {
      if (!state.clockedIn) return;
      if (state.location.success) {
        state.location.reporting = true;
        state.location.lastReport = new Date().toISOString();
        state.location.longitude += (Math.random() - 0.5) * 0.00006;
        state.location.latitude += (Math.random() - 0.5) * 0.00006;
        state.location.accuracy = 8 + Math.floor(Math.random() * 10);
        document.querySelectorAll(".last-report-text").forEach((el) => {
          el.textContent = formatTimeSeconds(state.location.lastReport);
        });
        setTimeout(() => {
          state.location.reporting = false;
        }, 500);
      }
    }, 12000);
  }

  function completePayment(methodLabel) {
    const p = state.payment;
    const paidAt = new Date().toISOString();
    let plate = "";
    let orderNo = "";

    if (p.kind === "order" || p.kind === "combined") {
      const currentOrder = getOrder(p.currentOrderId || p.orderIds[0]);
      if (!currentOrder) return;
      const currentAmount = Number(p.currentAmount ?? p.amount);
      const combinedArrears = p.kind === "combined"
        ? p.orderIds.slice(1).map(getOrder).filter((item) => item && item.status === "arrears")
        : [];

      currentOrder.endTime = paidAt;
      currentOrder.receivable = currentAmount;
      currentOrder.paid = currentAmount;
      currentOrder.paymentMethod = methodLabel;
      currentOrder.status = "paid";
      combinedArrears.forEach((item) => {
        item.status = "repaid";
        item.paid = item.receivable;
        item.paymentMethod = methodLabel;
        item.endTime = paidAt;
      });

      const berth = getBerth(currentOrder.berthId);
      if (berth) {
        berth.status = "idle";
        berth.plate = "";
        berth.entryTime = null;
        berth.currentFee = 0;
        berth.currentOrderId = null;
        berth.riskTags = [];
      }

      plate = currentOrder.plate;
      orderNo = combinedArrears.length ? `${currentOrder.orderNo} + ${combinedArrears.length}笔欠费` : currentOrder.orderNo;
      state.shiftStats.received += p.amount;
      state.shiftStats.receivable += currentAmount;
      state.shiftStats.arrears += combinedArrears.reduce((sum, item) => sum + item.receivable, 0);
      state.shiftStats.arrearsCount += combinedArrears.length;
    } else {
      const paymentOrders = p.orderIds.map(getOrder).filter(Boolean);
      paymentOrders.forEach((item) => {
        item.status = "repaid";
        item.paid = item.receivable;
        item.paymentMethod = methodLabel;
        item.endTime = paidAt;
      });
      plate = paymentOrders[0]?.plate || state.arrears.searchedPlate;
      orderNo = `${paymentOrders.length}笔欠费合并补缴`;
      state.shiftStats.received += p.amount;
      state.shiftStats.arrears += p.amount;
      state.shiftStats.arrearsCount += paymentOrders.length;
      state.arrears.selected = [];
    }

    if (p.method === "pda") state.shiftStats.pdaScan += p.amount;
    if (p.method === "cash") state.shiftStats.cash += p.amount;
    state.orderCheckoutArrears = [];

    state.lastPayment = {
      kind: p.kind,
      orderIds: [...p.orderIds],
      currentOrderId: p.currentOrderId || (p.kind !== "arrears" ? p.orderIds[0] : null),
      amount: p.amount,
      methodLabel,
      time: paidAt,
      plate,
      orderNo
    };

    state.payment.status = "success";
    navigate("paymentSuccess", {}, true);
    toast("支付成功，业务数据已同步");
  }

  function createAutoTicketFromWarning(warning, result) {
    const berth = getBerth(warning.berthId);
    const ticket = {
      id: id("t"),
      no: `GD${formatDate().replaceAll("-", "")}${String(tickets.length + 1).padStart(4, "0")}`,
      type: result === "设备异常" ? "地磁设备故障" : "平台核查任务",
      title: result === "设备异常" ? `${berthNo(warning.berthId)} 设备异常维修` : `${warning.title}升级处理`,
      description: `由预警“${warning.title}”自动生成。收费员反馈结果：${result}。${state.warningForm.note || ""}`,
      source: "预警自动生成",
      status: "pending",
      priority: warning.level,
      roadId: warning.roadId,
      berthId: warning.berthId,
      deviceId: berth?.deviceId || "",
      assignee: "张伟",
      creator: "系统",
      createdAt: new Date().toISOString(),
      deadline: new Date(Date.now() + 2 * 3600000).toISOString(),
      attachments: state.warningForm.photo ? ["预警反馈现场照片"] : [],
      timeline: [
        {
          title: "工单自动创建",
          time: new Date().toISOString(),
          desc: `预警处理结果为“${result}”，系统自动转为工单。`
        }
      ]
    };
    tickets.unshift(ticket);
    return ticket;
  }

  document.addEventListener("click", (event) => {
    if (event.target.classList.contains("modal-backdrop")) {
      state.modal = null;
      renderModal();
      return;
    }

    const target = event.target.closest("[data-action]");
    if (!target || target.disabled) return;

    const action = target.dataset.action;

    switch (action) {
      case "back":
        goBack();
        break;

      case "open-side-nav":
        document.querySelector("[data-side-nav]")?.classList.add("open");
        break;

      case "close-side-nav":
        document.querySelector("[data-side-nav]")?.classList.remove("open");
        break;

      case "nav":
        navigate(target.dataset.route);
        break;

      case "toggle-remember":
        state.login.remember = !state.login.remember;
        render();
        break;

      case "login": {
        const employeeNo = state.login.employeeNo.trim().toUpperCase();
        if (!employeeNo) {
          state.login.error = "请输入收费员工号。";
          render();
          break;
        }
        if (employeeNo !== VALID_EMPLOYEE) {
          state.login.error = "工号不存在或已停用，请核对后重新输入。";
          render();
          break;
        }

        state.login.error = "";
        if (state.login.remember) {
          localStorage.setItem("parkingEmployee", employeeNo);
        } else {
          localStorage.removeItem("parkingEmployee");
        }

        state.loggedIn = true;
        if (state.clockedIn) {
          navigate("berths");
        } else {
          state.attendance.error = "";
          state.attendance.photo = null;
          navigate("attendance");
        }
        break;
      }

      case "relocate":
        state.attendance.locating = true;
        state.attendance.error = "";
        render();
        setTimeout(() => {
          state.attendance.locating = false;
          state.attendance.locationSuccess = true;
          state.attendance.insideFence = true;
          state.location.success = true;
          state.location.accuracy = 10;
          state.location.lastReport = new Date().toISOString();
          render();
          toast("高精度定位成功", "success");
        }, 900);
        break;

      case "capture-attendance":
        state.attendance.photo = { time: new Date().toISOString() };
        state.attendance.error = "";
        render();
        toast("打卡照片已拍摄并添加水印");
        break;

      case "submit-clock-in":
        if (!state.attendance.photo) {
          state.attendance.error = "请先拍摄上班打卡照片，再提交打卡。";
          render();
          break;
        }
        if (!state.attendance.locationSuccess) {
          state.attendance.error = "当前定位失败，请重新定位后提交。";
          render();
          break;
        }
        if (state.attendance.fenceEnabled && !state.attendance.insideFence) {
          state.attendance.error = "当前位置不在允许打卡电子围栏内。";
          render();
          break;
        }
        if (!state.attendance.beacon) {
          state.attendance.error = "未检测到绑定蓝牙信标，请靠近打卡点。";
          render();
          break;
        }

        state.clockedIn = true;
        state.clockedOut = false;
        state.loggedIn = true;
        state.clockInTime = new Date().toISOString();
        state.location.lastReport = new Date().toISOString();
        startLocationReporting();
        navigate("berths", {}, true);
        toast("上班打卡成功，已开始定位上报");
        break;

      case "open-location":
        state.modal = { type: "location" };
        renderModal();
        break;

      case "toggle-location":
        state.location.success = !state.location.success;
        if (state.location.success) {
          state.location.lastReport = new Date().toISOString();
          state.location.network = "5G 在线";
          toast("定位服务已恢复");
        } else {
          state.location.network = "5G 在线";
          toast("已模拟定位失败", "error");
        }
        render();
        break;

      case "open-road-switch":
        state.modal = { type: "roads" };
        renderModal();
        break;

      case "select-road":
        state.currentRoadId = target.dataset.id;
        state.berthSearch = "";
        state.berthFilter = "all";
        state.build.roadId = state.currentRoadId;
        state.modal = null;
        render();
        toast(`已切换至${currentRoad().name}`);
        break;

      case "close-modal":
        state.modal = null;
        renderModal();
        break;

      case "berth-filter":
        state.berthFilter = target.dataset.filter;
        render();
        break;

      case "refresh-berths":
        state.berthRefreshing = true;
        render();
        setTimeout(() => {
          state.berthRefreshing = false;
          render();
          toast("泊位状态已刷新");
        }, 750);
        break;

      case "open-berth":
        navigate("berthDetail", { id: target.dataset.id });
        break;

      case "create-from-berth":
        initializeBuild(target.dataset.id);
        navigate("createOrder");
        break;

      case "capture-vehicle": {
        const photos = state.build.photos || (state.build.photos = []);
        if (photos.length >= 3) {
          toast("车辆照片最多拍摄 3 张", "info");
          break;
        }
        photos.push({ id: id("vehicle-photo"), time: new Date().toISOString() });
        state.build.error = "";
        render();
        toast(`车辆照片 ${photos.length} 已拍摄并添加建单水印`);
        break;
      }

      case "retake-vehicle-photo": {
        const index = Number(target.dataset.index);
        const photos = state.build.photos || [];
        if (!Number.isInteger(index) || !photos[index]) return;
        photos[index] = { ...photos[index], time: new Date().toISOString() };
        state.build.error = "";
        render();
        toast(`车辆照片 ${index + 1} 已重新拍摄`);
        break;
      }

      case "delete-vehicle-photo": {
        const index = Number(target.dataset.index);
        const photos = state.build.photos || [];
        if (!Number.isInteger(index) || !photos[index]) return;
        photos.splice(index, 1);
        state.build.error = "";
        render();
        toast("车辆照片已删除", "info");
        break;
      }

      case "recognize-plate":
        if (!(state.build.photos || []).length) return;
        state.build.recognizing = true;
        state.build.error = "";
        render();
        setTimeout(() => {
          state.build.recognizing = false;
          state.build.plate = "浙A·8K92F";
          state.build.plateColor = "蓝牌";
          render();
          toast("车牌识别成功，请核对结果");
        }, 1150);
        break;

      case "plate-color":
        state.build.plateColor = target.dataset.color;
        render();
        break;

      case "create-order": {
        const build = state.build;
        const berth = getBerth(build.berthId);
        if (!berth) {
          build.error = "请选择需要创建订单的泊位。";
          render();
          break;
        }
        if (!(build.photos || []).length) {
          build.error = "请至少拍摄 1 张车辆照片。";
          render();
          break;
        }
        if (!build.plate.trim()) {
          build.error = "请识别或手动输入车牌号。";
          render();
          break;
        }
        if (berth.status === "parking") {
          build.error = "该泊位已有停车中订单，无法重复建单。";
          render();
          break;
        }

        const duplicate = orders.find(
          (o) => o.plate === build.plate.trim().toUpperCase() && o.status === "parking"
        );
        if (duplicate) {
          build.error = `车牌 ${build.plate.trim().toUpperCase()} 已存在在停订单，请先核对车辆。`;
          render();
          break;
        }

        const orderId = id("o");
        const newOrder = {
          id: orderId,
          orderNo: `P${formatDate().replaceAll("-", "")}${String(orders.length + 1).padStart(5, "0")}`,
          roadId: build.roadId,
          berthId: build.berthId,
          plate: build.plate.trim().toUpperCase(),
          plateColor: build.plateColor,
          vehicleType: build.plateColor === "绿牌" ? "新能源小型车" : "小型车",
          startTime: new Date().toISOString(),
          endTime: null,
          receivable: 0,
          discount: 0,
          paid: 0,
          status: "parking",
          paymentMethod: "",
          createdBy: VALID_EMPLOYEE
        };

        orders.unshift(newOrder);
        berth.status = "parking";
        berth.plate = newOrder.plate;
        berth.entryTime = newOrder.startTime;
        berth.currentFee = 0;
        berth.currentOrderId = newOrder.id;
        berth.magnet = berth.magnet === "离线" ? "离线" : "正常";
        profileForPlate(newOrder.plate);

        state.shiftStats.creationCount += 1;
        state.shiftStats.parkingCount += 1;
        state.selectedOrderId = newOrder.id;
        state.orderCheckoutArrears = [];
        navigate("orderDetail", { id: newOrder.id, justCreated: true }, true);
        toast("停车订单创建成功，泊位状态已更新");
        break;
      }

      case "open-order":
        state.selectedOrderId = target.dataset.id;
        state.orderCheckoutArrears = [];
        navigate("orderDetail", { id: target.dataset.id });
        break;

      case "toggle-order-arrear": {
        const orderId = target.dataset.id;
        if (state.orderCheckoutArrears.includes(orderId)) {
          state.orderCheckoutArrears = state.orderCheckoutArrears.filter((id) => id !== orderId);
        } else {
          state.orderCheckoutArrears.push(orderId);
        }
        render();
        break;
      }

      case "select-all-order-arrears": {
        const list = arrearsOrdersForPlate(target.dataset.plate);
        const selectedCount = list.filter((item) => state.orderCheckoutArrears.includes(item.id)).length;
        state.orderCheckoutArrears = selectedCount === list.length ? [] : list.map((item) => item.id);
        render();
        break;
      }

      case "checkout": {
        const order = getOrder(target.dataset.id);
        if (!order) return;
        const currentAmount = calcFee(order.startTime);
        const selectedArrears = state.orderCheckoutArrears
          .map(getOrder)
          .filter((item) => item && item.status === "arrears" && item.plate === order.plate);
        const arrearsAmount = selectedArrears.reduce((sum, item) => sum + item.receivable, 0);
        order.receivable = currentAmount;
        state.payment = {
          kind: selectedArrears.length ? "combined" : "order",
          orderIds: [order.id, ...selectedArrears.map((item) => item.id)],
          currentOrderId: order.id,
          currentAmount,
          arrearsAmount,
          arrearsCount: selectedArrears.length,
          amount: currentAmount + arrearsAmount,
          method: "pda",
          status: "idle",
          countdown: 60,
          error: ""
        };
        navigate("payment");
        break;
      }

      case "payment-method":
        state.payment.method = target.dataset.method;
        state.payment.status = "idle";
        state.payment.error = "";
        state.payment.countdown = 60;
        render();
        break;

      case "start-pda-scan":
        state.payment.status = "scanning";
        state.payment.error = "";
        render();
        setTimeout(() => {
          if (state.route !== "payment") return;
          state.payment.status = "recognized";
          render();
          setTimeout(() => {
            if (state.route !== "payment") return;
            state.payment.status = "paying";
            render();
            setTimeout(() => {
              if (state.route !== "payment") return;
              completePayment("PDA 扫付款码");
            }, 900);
          }, 650);
        }, 1000);
        break;

      case "fail-pda-scan":
        state.payment.status = "failed";
        render();
        break;

      case "confirm-cash":
        completePayment("现金登记");
        break;

      case "open-parking-slip":
        state.modal = { type: "parkingSlip", orderId: target.dataset.id };
        renderModal();
        break;

      case "confirm-parking-slip":
        state.shiftStats.printCount += 1;
        state.modal = null;
        renderModal();
        toast("停车凭条已发送至蓝牙打印机，请夹在车辆雨刮器处");
        break;

      case "open-receipt":
        state.modal = { type: "receipt", orderId: target.dataset.id };
        renderModal();
        break;

      case "print-last-payment":
        state.modal = { type: "receipt", orderId: state.lastPayment?.orderIds?.[0] };
        renderModal();
        break;

      case "confirm-print":
        state.shiftStats.printCount += 1;
        state.modal = null;
        renderModal();
        toast("小票已发送至蓝牙打印机");
        break;

      case "quick-print": {
        const recent = orders.find((o) => ["paid", "repaid"].includes(o.status));
        if (recent) {
          state.modal = { type: "receipt", orderId: recent.id };
          renderModal();
        } else {
          toast("当前没有可打印的已支付订单", "error");
        }
        break;
      }

      case "quick-charge": {
        const berth = berths.find(
          (b) => b.roadId === state.currentRoadId && ["parking", "risk"].includes(b.status) && b.currentOrderId
        );
        if (berth) {
          navigate("orderDetail", { id: berth.currentOrderId });
        } else {
          toast("当前道路暂无可结账订单", "info");
        }
        break;
      }

      case "open-arrears": {
        const plate = target.dataset.plate || state.arrears.searchedPlate || "浙A·8K92F";
        state.arrears.plate = plate;
        state.arrears.searchedPlate = plate;
        state.arrears.selected = [];
        state.arrears.error = "";
        navigate("arrears");
        break;
      }

      case "arrears-from-order":
        state.arrears.plate = target.dataset.plate;
        state.arrears.searchedPlate = target.dataset.plate;
        state.arrears.selected = [];
        navigate("arrears");
        break;

      case "search-arrears":
        if (!state.arrears.plate.trim()) {
          state.arrears.error = "请输入需要查询的车牌号。";
          render();
          break;
        }
        state.arrears.searchedPlate = state.arrears.plate.trim().toUpperCase();
        state.arrears.selected = [];
        state.arrears.error = "";
        state.shiftStats.queryCount += 1;
        render();
        break;

      case "toggle-arrear": {
        const orderId = target.dataset.id;
        if (state.arrears.selected.includes(orderId)) {
          state.arrears.selected = state.arrears.selected.filter((id) => id !== orderId);
        } else {
          state.arrears.selected.push(orderId);
        }
        render();
        break;
      }

      case "select-all-arrears": {
        const list = arrearsOrdersForPlate(state.arrears.searchedPlate);
        state.arrears.selected =
          state.arrears.selected.length === list.length ? [] : list.map((o) => o.id);
        render();
        break;
      }

      case "pay-arrears": {
        const selected = state.arrears.selected.map(getOrder).filter(Boolean);
        if (!selected.length) return;
        state.payment = {
          kind: "arrears",
          orderIds: selected.map((o) => o.id),
          amount: selected.reduce((sum, o) => sum + o.receivable, 0),
          method: "pda",
          status: "idle",
          countdown: 60,
          error: ""
        };
        navigate("payment");
        break;
      }

      case "search-orders":
        render();
        toast(state.query.term.trim() ? "订单查询完成" : "已显示全部订单", "info");
        break;

      case "order-filter":
        state.query.status = target.dataset.filter;
        render();
        break;

      case "open-profile":
        state.profilePlate = target.dataset.plate;
        state.profileHabitOrderId = null;
        navigate("profile", { plate: target.dataset.plate });
        break;

      case "habit-order":
        state.profileHabitOrderId = target.dataset.id;
        render();
        break;

      case "warning-filter":
        state.warningFilter = target.dataset.filter;
        render();
        break;

      case "open-warning":
        state.selectedWarningId = target.dataset.id;
        state.warningForm = {
          result: "已处理",
          note: "",
          photo: null,
          video: null,
          error: ""
        };
        navigate("warningDetail", { id: target.dataset.id });
        break;

      case "warning-photo":
        state.warningForm.photo = { time: new Date().toISOString() };
        render();
        toast("现场图片已拍摄");
        break;

      case "warning-video":
        state.warningForm.video = { time: new Date().toISOString(), duration: 12 };
        render();
        toast("视频附件已生成");
        break;

      case "submit-warning": {
        const warning = getWarning(state.selectedWarningId);
        if (!warning) return;
        if (!state.warningForm.result) {
          state.warningForm.error = "请选择处理结果。";
          render();
          break;
        }
        if (["设备异常", "车牌错误", "无法处理"].includes(state.warningForm.result) && !state.warningForm.note.trim()) {
          state.warningForm.error = "当前处理结果需要填写现场说明。";
          render();
          break;
        }

        warning.status = "done";
        warning.feedback = {
          result: state.warningForm.result,
          note: state.warningForm.note.trim(),
          photo: state.warningForm.photo,
          video: state.warningForm.video,
          time: new Date().toISOString(),
          operator: "张伟"
        };

        let generatedTicket = null;
        if (["设备异常", "无法处理"].includes(state.warningForm.result)) {
          generatedTicket = createAutoTicketFromWarning(warning, state.warningForm.result);
        }

        state.shiftStats.taskCount += 1;
        state.shiftStats.warningFeedback += 1;
        navigate("warnings", {}, true);
        toast(generatedTicket ? `预警已处理，并自动生成工单 ${generatedTicket.no}` : "预警处理反馈已提交");
        break;
      }

      case "ticket-tab":
        state.ticketTab = target.dataset.tab;
        render();
        break;

      case "open-ticket":
        state.selectedTicketId = target.dataset.id;
        navigate("ticketDetail", { id: target.dataset.id });
        break;

      case "accept-ticket": {
        const ticket = getTicket(target.dataset.id);
        ticket.status = "processing";
        ticket.assignee = "张伟";
        ticket.timeline.push({
          title: "收费员接单",
          time: new Date().toISOString(),
          desc: "张伟已接单并开始现场处理。"
        });
        render();
        toast("工单已接单，状态更新为处理中");
        break;
      }

      case "ticket-feedback":
        state.selectedTicketId = target.dataset.id;
        state.ticketFeedback = { note: "", photo: null, error: "" };
        navigate("ticketFeedback", { id: target.dataset.id });
        break;

      case "ticket-feedback-photo":
        state.ticketFeedback.photo = { time: new Date().toISOString() };
        render();
        toast("工单处理照片已拍摄");
        break;

      case "submit-ticket-feedback": {
        const ticket = getTicket(state.selectedTicketId);
        if (!state.ticketFeedback.note.trim()) {
          state.ticketFeedback.error = "请填写工单处理说明。";
          render();
          break;
        }
        if (!state.ticketFeedback.photo) {
          state.ticketFeedback.error = "请拍摄现场处理照片。";
          render();
          break;
        }

        ticket.timeline.push({
          title: "提交处理反馈",
          time: new Date().toISOString(),
          desc: state.ticketFeedback.note.trim()
        });
        ticket.attachments.push("处理现场照片");
        ticket.status = "processing";
        navigate("ticketDetail", { id: ticket.id }, true);
        toast("工单处理反馈已提交");
        break;
      }

      case "complete-ticket": {
        const ticket = getTicket(target.dataset.id);
        ticket.status = "completed";
        ticket.timeline.push({
          title: "工单完成",
          time: new Date().toISOString(),
          desc: "收费员确认现场问题已处理完成，工单闭环。"
        });
        state.shiftStats.ticketCount += 1;
        render();
        toast("工单已完成");
        break;
      }

      case "open-transfer":
        state.modal = { type: "transfer", ticketId: target.dataset.id };
        state.transferPerson = "李强";
        renderModal();
        break;

      case "select-transfer-person":
        state.transferPerson = target.dataset.person;
        renderModal();
        break;

      case "confirm-transfer": {
        const ticket = getTicket(target.dataset.id);
        ticket.assignee = state.transferPerson;
        ticket.status = "processing";
        ticket.timeline.push({
          title: "工单转派",
          time: new Date().toISOString(),
          desc: `工单已转派给 ${state.transferPerson}。`
        });
        state.modal = null;
        render();
        toast(`工单已转派给${state.transferPerson}`);
        break;
      }

      case "open-return":
        state.returnReason = "";
        state.modal = { type: "return", ticketId: target.dataset.id };
        renderModal();
        break;

      case "confirm-return": {
        if (!state.returnReason.trim()) {
          toast("请填写退回原因", "error");
          break;
        }
        const ticket = getTicket(target.dataset.id);
        ticket.status = "returned";
        ticket.timeline.push({
          title: "工单退回",
          time: new Date().toISOString(),
          desc: state.returnReason.trim()
        });
        state.modal = null;
        render();
        toast("工单已退回");
        break;
      }

      case "new-fault-ticket": {
        const berth = getBerth(target.dataset.id);
        state.newTicket = {
          roadId: berth.roadId,
          berthId: berth.id,
          type: "地磁设备故障",
          faultType: berth.magnet === "离线" ? "离线" : "误报",
          description: `${berth.no} 地磁设备状态异常，请安排现场检查。`,
          photo: null,
          priority: "重要",
          error: ""
        };
        navigate("newTicket");
        break;
      }

      case "new-general-ticket":
        state.newTicket = {
          roadId: state.currentRoadId,
          berthId: "",
          type: "地磁设备故障",
          faultType: "离线",
          description: "",
          photo: null,
          priority: "重要",
          error: ""
        };
        navigate("newTicket");
        break;

      case "ticket-priority":
        state.newTicket.priority = target.dataset.value;
        render();
        break;

      case "new-ticket-photo":
        state.newTicket.photo = { time: new Date().toISOString() };
        render();
        toast("现场故障照片已拍摄");
        break;

      case "submit-new-ticket": {
        const form = state.newTicket;
        const berth = getBerth(form.berthId);

        if (!form.berthId) {
          form.error = "请选择关联泊位。";
          render();
          break;
        }
        if (!form.description.trim()) {
          form.error = "请填写问题描述。";
          render();
          break;
        }
        if (!form.photo) {
          form.error = "请拍摄至少一张现场照片。";
          render();
          break;
        }

        const ticket = {
          id: id("t"),
          no: `GD${formatDate().replaceAll("-", "")}${String(tickets.length + 1).padStart(4, "0")}`,
          type: form.type,
          title:
            form.type === "地磁设备故障"
              ? `${berth.no} 地磁${form.faultType}`
              : `${berth.no} ${form.type}`,
          description: form.description.trim(),
          source: "我创建的",
          status: "pending",
          priority: form.priority,
          roadId: form.roadId,
          berthId: form.berthId,
          deviceId: berth.deviceId,
          assignee: "张伟",
          creator: "张伟",
          createdAt: new Date().toISOString(),
          deadline: new Date(Date.now() + (form.priority === "紧急" ? 1 : form.priority === "重要" ? 2 : 4) * 3600000).toISOString(),
          attachments: ["现场故障照片"],
          timeline: [
            {
              title: "收费员创建工单",
              time: new Date().toISOString(),
              desc: form.description.trim()
            }
          ]
        };

        tickets.unshift(ticket);
        state.selectedTicketId = ticket.id;
        navigate("ticketDetail", { id: ticket.id }, true);
        toast(`工单 ${ticket.no} 创建成功`);
        break;
      }

      case "report-period":
        state.reportPeriod = target.dataset.period;
        render();
        break;

      case "go-clock-out":
        state.clockOut.error = "";
        state.clockOut.photo = null;
        navigate("clockOut");
        break;

      case "capture-clock-out":
        state.clockOut.photo = { time: new Date().toISOString() };
        state.clockOut.error = "";
        render();
        toast("下班照片已拍摄并添加水印");
        break;

      case "submit-clock-out":
        if (!state.clockOut.photo) {
          state.clockOut.error = "请先拍摄下班打卡照片。";
          render();
          break;
        }
        if (!state.location.success) {
          state.clockOut.error = "当前定位失败，请恢复定位后提交下班打卡。";
          render();
          break;
        }

        state.clockedIn = false;
        state.clockedOut = true;
        state.loggedIn = false;
        state.clockInTime = null;
        state.history = [];
        state.login.error = "";
        state.attendance.photo = null;
        state.clockOut.photo = null;
        clearInterval(reportTimer);
        clearInterval(paymentTimer);
        navigate("login", {}, true);
        toast("下班打卡成功，已安全退出系统");
        break;
    }
  });

  document.addEventListener("input", (event) => {
    const model = event.target.dataset.model;
    if (!model) return;

    switch (model) {
      case "login.employeeNo":
        state.login.employeeNo = event.target.value;
        state.login.error = "";
        break;
      case "berthSearch":
        state.berthSearch = event.target.value;
        render();
        break;
      case "build.plate":
        state.build.plate = event.target.value.toUpperCase();
        state.build.error = "";
        break;
      case "arrears.plate":
        state.arrears.plate = event.target.value.toUpperCase();
        state.arrears.error = "";
        break;
      case "query.term":
        state.query.term = event.target.value;
        break;
      case "warning.note":
        state.warningForm.note = event.target.value;
        state.warningForm.error = "";
        break;
      case "ticketFeedback.note":
        state.ticketFeedback.note = event.target.value;
        state.ticketFeedback.error = "";
        break;
      case "newTicket.description":
        state.newTicket.description = event.target.value;
        state.newTicket.error = "";
        break;
      case "returnReason":
        state.returnReason = event.target.value;
        break;
    }
  });

  document.addEventListener("change", (event) => {
    const model = event.target.dataset.model;
    if (!model) return;

    switch (model) {
      case "build.berthId":
        state.build.berthId = event.target.value;
        state.build.error = "";
        render();
        break;
      case "warning.result":
        state.warningForm.result = event.target.value;
        state.warningForm.error = "";
        render();
        break;
      case "newTicket.type":
        state.newTicket.type = event.target.value;
        render();
        break;
      case "newTicket.roadId": {
        state.newTicket.roadId = event.target.value;
        state.newTicket.berthId = "";
        render();
        break;
      }
      case "newTicket.berthId":
        state.newTicket.berthId = event.target.value;
        state.newTicket.error = "";
        render();
        break;
      case "newTicket.faultType":
        state.newTicket.faultType = event.target.value;
        break;
      case "report.start":
        state.reportCustom.start = event.target.value;
        break;
      case "report.end":
        state.reportCustom.end = event.target.value;
        break;
    }
  });

  clockTimer = setInterval(() => {
    document.querySelectorAll(".js-time").forEach((el) => {
      el.textContent = formatTimeSeconds();
    });
  }, 1000);

  render();
})();
  
