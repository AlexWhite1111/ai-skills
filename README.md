# AI Skills

这是一个面向 Codex 和其他支持 Skills 的 AI Agent 的公开能力库。每个 Skill 都是一套可独立安装、调用、评测和演进的工作协议，不保存个人状态，也不与某个具体软件项目绑定。

## 当前 Skills

| Skill | 调用名 | 作用 |
|---|---|---|
| [Narrative Tutor](.agents/skills/narrative-tutor/README.zh-CN.md) | `$narrative-tutor` | 从学习者当前模型出发，用具体对象、认知缺口、必要工具和边界组织复杂概念讲解。 |
| [Learning Novel Engine](.agents/skills/learning-novel-engine/README.zh-CN.md) | `$learning-novel-engine` | 把真实知识变成由人物选择、证据与后果驱动的长篇小说，并维护知识依赖、读者证据、视觉来源、连续性、隔离审计和盲式基线评测。 |
| [Research Orchestrator](.agents/skills/research-orchestrator/README.zh-CN.md) | `$research-orchestrator` | 对困难证明、数学物理建模、因果研究、工程设计和复杂排障进行多路线搜索与敌对审计。 |

个人学习状态、掌握度、复习计划和多设备同步不放在这里。它们由独立的私有 [`LearningOS`](https://github.com/AlexWhite1111/LearningOS) 仓库及其 `learningos-manager` Skill 管理。

## 仓库结构

```text
ai-skills/
├── README.md
├── AGENTS.md
├── MANIFEST.json
└── .agents/
    └── skills/
        ├── narrative-tutor/
        │   ├── SKILL.md
        │   ├── agents/
        │   ├── references/
        │   └── scripts/
        ├── learning-novel-engine/
        │   ├── SKILL.md
        │   ├── agents/
        │   ├── references/
        │   ├── evals/
        │   └── scripts/
        └── research-orchestrator/
            ├── SKILL.md
            ├── agents/
            ├── assets/
            └── references/
```

每个 Skill 的 `SKILL.md` 是精简入口。详细方法按任务从同目录下的 `references/` 渐进加载；可机械化的重复工作放在经过测试的 `scripts/` 中。

## 安装

克隆本仓库：

```bash
git clone <this-repository-url> ai-skills
```

安装全部 Skills：

```bash
mkdir -p ~/.codex/skills
cp -R ai-skills/.agents/skills/narrative-tutor ~/.codex/skills/
cp -R ai-skills/.agents/skills/learning-novel-engine ~/.codex/skills/
cp -R ai-skills/.agents/skills/research-orchestrator ~/.codex/skills/
```

也可以只复制需要的目录。更新时重新拉取仓库，再覆盖对应 Skill 目录即可。

## 调用示例

```text
使用 $narrative-tutor 给我讲清楚这个概念。保持一个具体对象稳定，先修复我当前理解里最关键的缺口。
```

```text
使用 $learning-novel-engine 把 OFDM 和它的上下游通信原理做成一部长篇学习小说。让剧情压力产生知识需要，让知识更新改变人物选择与后果，并维护真实数据来源、读者证据、连续性和盲式评测。
```

```text
使用 $research-orchestrator 研究这个问题。隔离观察、假设、假说和验证，维持真正不同的路线，并在接受候选结果前进行敌对审计。
```

## 设计边界

- Skill 负责可复用的思考与工作方法。
- 项目仓库中的 `AGENTS.md` 负责该项目的施工规则。
- CLI、MCP 和其他工具接口负责执行真实操作。
- 个人状态、公司资料、密钥、客户数据和私有语料不得进入本公开仓库。
- “预期读者证据”只描述书稿提供了哪些认知机会，不等于任何真实读者的个人掌握度。
- 同一模型的多次赞同不等于独立验证，有限计算也不自动构成普适证明。
- 回归用例通过不等于作品更好。重要 Skill 修改应与无 Skill 和当前发布版做盲式真实输出比较。

维护规则见 [`AGENTS.md`](AGENTS.md)，机器可读索引见 [`MANIFEST.json`](MANIFEST.json)。
