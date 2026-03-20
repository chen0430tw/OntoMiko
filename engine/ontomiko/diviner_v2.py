from __future__ import annotations

from dataclasses import dataclass, asdict
from enum import Enum
from math import exp
from typing import Dict, Optional


class UniverseCategory(str, Enum):
    ALLOW = "宇宙同意"
    DENY = "宇宙不同意"
    INDIFFERENT = "宇宙不在乎"
    UNKNOWN = "宇宙也不知道"


class MachineState(str, Enum):
    QY = "qY"
    QN = "qN"
    QIND = "qInd"
    QU = "qU"


class PMClass(str, Enum):
    STRONG = "Strong-PM"
    WEAK = "Weak-PM"
    FAKE = "Fake-PM"
    RULE = "Rule-PM"


@dataclass
class FeatureVector:
    source: float
    locus: float
    access: float
    cost: float
    consistency: int
    decidability: int
    impact: float


@dataclass
class PMMAnalysis:
    detected: bool
    pm_class: Optional[PMClass] = None
    source_note: Optional[str] = None
    decay_note: Optional[str] = None
    audit_note: Optional[str] = None


@dataclass
class Result:
    category: UniverseCategory
    state: MachineState
    reason: str
    permission_score: Optional[float] = None
    note: Optional[str] = None
    features: Optional[FeatureVector] = None
    pmm: Optional[PMMAnalysis] = None

    def to_dict(self) -> Dict:
        data = asdict(self)
        if self.features is not None:
            data["features"] = asdict(self.features)
        if self.pmm is not None:
            data["pmm"] = asdict(self.pmm)
        return data


@dataclass
class Config:
    epsilon_impact: float = 0.15
    theta_source: float = 0.35
    theta_locus: float = 0.35
    theta_cost: float = 0.85
    alpha: float = 1.0
    beta: float = 1.0
    gamma: float = 0.4
    delta: float = 1.2
    eta: float = 0.8
    mu: float = 1.0


def sigmoid(z: float) -> float:
    return 1.0 / (1.0 + exp(-z))


def interpret_access_level(access: float) -> str:
    if access < 0.25:
        return "普通层可访问"
    if access < 0.50:
        return "需要特殊条件"
    if access < 0.75:
        return "需要高权限"
    return "需要异常主体或稀有接口"


PMM_KEYWORDS = ["永动", "永动机", "perpetual motion", "pmm", "不停发电", "无限输出", "自循环发电", "自维持输出"]
STRONG_HINTS = ["太阳能", "风能", "水力", "核裂变", "核聚变", "燃料", "氢能", "外部输入", "源项明确", "账本闭合", "可审计"]
WEAK_HINTS = ["库存", "慢变量", "恒星", "地热", "潮汐", "飞轮", "超导储能", "长期衰减", "慢慢漏"]
RULE_HINTS = ["minecraft", "红石", "tick", "规则注入", "协议", "掉落", "刷新", "规则源项"]
FAKE_HINTS = ["磁铁永动", "重力轮", "过平衡轮", "水泵自循环", "浮力永动", "虹吸", "毛细", "单一热源", "布朗棘轮", "水变氢再发电", "无输入", "不需要输入", "凭空输出"]


def detect_pmm_context(text: str) -> bool:
    lower = text.lower()
    return any((k in text) or (k in lower) for k in PMM_KEYWORDS)


def classify_pmm(text: str) -> PMMAnalysis:
    lower = text.lower()
    def contains_any(keys):
        return any((k in text) or (k in lower) for k in keys)

    if contains_any(RULE_HINTS):
        return PMMAnalysis(True, PMClass.RULE, "检测到规则源项。", "规则可维持。", "若规则注入计账则闭合。")
    if contains_any(STRONG_HINTS):
        return PMMAnalysis(True, PMClass.STRONG, "检测到明确源项。", "长期稳态可成立。", "账本可望闭合。")
    if contains_any(WEAK_HINTS):
        return PMMAnalysis(True, PMClass.WEAK, "检测到库存/慢变量。", "长时间窗会衰减。", "若库存可计账则闭合。")
    return PMMAnalysis(True, PMClass.FAKE, "未给出明确源项。", "默认先按漏项风险处理。", "账本高概率不闭合。")


def rewrite_features_by_pmm_class(features: FeatureVector, pmm: PMMAnalysis) -> FeatureVector:
    f = FeatureVector(**asdict(features))
    if pmm.pm_class == PMClass.STRONG:
        f.source = max(f.source, 0.85)
        f.locus = max(f.locus, 0.85)
        f.cost = max(f.cost, 0.35)
    elif pmm.pm_class == PMClass.WEAK:
        f.source = max(f.source, 0.70)
        f.locus = max(f.locus, 0.85)
        f.cost = max(f.cost, 0.45)
    elif pmm.pm_class == PMClass.RULE:
        f.source = max(f.source, 0.85)
        f.locus = max(f.locus, 0.80)
        f.access = max(f.access, 0.45)
        f.cost = max(f.cost, 0.20)
    elif pmm.pm_class == PMClass.FAKE:
        f.source = min(f.source, 0.15)
        f.cost = min(f.cost, 0.10)
        f.impact = max(f.impact, 0.65)
    return f


KEYWORDS = {
    "无源": ("source", 0.0),
    "凭空": ("source", 0.0),
    "白嫖": ("source", 0.0),
    "隐源": ("source", 0.65),
    "潜势": ("source", 0.75),
    "惯性": ("source", 0.70),
    "结构": ("locus", 0.70),
    "承载": ("locus", 0.75),
    "高权限": ("access", 0.70),
    "无代价": ("cost", 0.0),
    "免费": ("cost", 0.0),
    "高代价": ("cost", 0.95),
    "自相矛盾": ("consistency", 0),
    "不可判": ("decidability", 0),
    "命名": ("impact", 0.05),
    "配色": ("impact", 0.03),
    "主题": ("impact", 0.03),
}

def extract_features_from_text(text: str) -> FeatureVector:
    f = FeatureVector(0.50, 0.50, 0.40, 0.45, 1, 1, 0.60)
    lower = text.lower()
    for k, (field, value) in KEYWORDS.items():
        if (k in text) or (k in lower):
            setattr(f, field, value)
    if ("宇宙" in text) and ("自己" in text) and ("预测" in text):
        f.decidability = 0
        f.impact = 0.9
    return f


class UniversePermissionDiviner:
    def __init__(self, config: Optional[Config] = None):
        self.cfg = config or Config()

    def permission_potential(self, f: FeatureVector) -> float:
        return self.cfg.alpha * f.source + self.cfg.beta * f.locus + self.cfg.gamma * f.access + self.cfg.delta * f.consistency + self.cfg.eta * f.decidability - self.cfg.mu * f.cost

    def divine(self, features: FeatureVector, pmm: Optional[PMMAnalysis] = None) -> Result:
        if features.consistency == 0:
            return Result(UniverseCategory.DENY, MachineState.QN, "设想在本体层不一致或自相矛盾", note="一致项 K=0，优先否决。", features=features, pmm=pmm)
        if features.decidability == 0:
            return Result(UniverseCategory.UNKNOWN, MachineState.QU, "问题超出当前可判定域", note="可判项 D=0，转入未知态。", features=features, pmm=pmm)
        if features.impact < self.cfg.epsilon_impact:
            return Result(UniverseCategory.INDIFFERENT, MachineState.QIND, "该设想对本体结构影响过低", note="影响度不足，宇宙不在乎。", features=features, pmm=pmm)
        if features.locus < self.cfg.theta_locus:
            return Result(UniverseCategory.DENY, MachineState.QN, "缺少足够承载结构", note="承载项 L 低于阈值。", features=features, pmm=pmm)
        if features.cost > self.cfg.theta_cost:
            return Result(UniverseCategory.DENY, MachineState.QN, "代价过高或代价函数失控", note=interpret_access_level(features.access), features=features, pmm=pmm)
        if features.source < self.cfg.theta_source:
            return Result(UniverseCategory.DENY, MachineState.QN, "来源不足，接近无源净生成", note=interpret_access_level(features.access), features=features, pmm=pmm)
        lam = self.permission_potential(features)
        p_allow = sigmoid(lam)
        if lam >= 0:
            return Result(UniverseCategory.ALLOW, MachineState.QY, "设想具有来源、承载、可判性与可接受代价", permission_score=p_allow, note=interpret_access_level(features.access), features=features, pmm=pmm)
        return Result(UniverseCategory.DENY, MachineState.QN, "综合许可势不足", permission_score=p_allow, note=interpret_access_level(features.access), features=features, pmm=pmm)


def divine_text(text: str) -> Result:
    diviner = UniversePermissionDiviner()
    features = extract_features_from_text(text)
    pmm = None
    if detect_pmm_context(text):
        pmm = classify_pmm(text)
        features = rewrite_features_by_pmm_class(features, pmm)
    return diviner.divine(features, pmm=pmm)
