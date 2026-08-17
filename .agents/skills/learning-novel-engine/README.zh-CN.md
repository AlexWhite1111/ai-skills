# Learning Novel Engine

`$learning-novel-engine` 用于创作、修订和评测“真正靠小说教会知识”的长篇作品。

V2 的重点不再只是防止知识错误、前置泄漏和连续性崩坏，而是补上正向生成发动机：

```text
人物欲望与压力
→ 旧模型驱动一次真实行动
→ 世界返回可观察证据
→ 最小知识修补
→ 人物必须据此选择
→ 选择改变剧情、关系或系统状态
```

知识不是人物对白里的课程，而是行动的分水岭。

## 核心改进

### 双向因果

每个重要教学场景都必须同时成立：

```text
剧情压力 -> 产生知识需要
知识更新 -> 改变选择与后果
```

删掉知识后剧情结局不变，或者删掉剧情后解释仍以同样方式出现，都说明融合失败。

### 正向小说工艺

V2 增加了独立的小说执行层，覆盖：

- 视角人物的注意力过滤；
- 心理距离与自由间接叙述；
- 人物声音和压力变形；
- 对话中的关系、隐瞒和争夺；
- 段落与句子节奏；
- 信息省略、潜台词和读者推断；
- 从后果而不是课程目录结束章节。

### 人物模拟

连续性账本只负责“什么必须为真”。人物模拟负责“这个人此刻会怎么做”。

每个核心人物可以维护：

```text
证据偏好 | 推理习惯 | 注意力偏向 | 冲突策略
压力反应 | 语言节奏 | 隐瞒内容 | 关系特异行为
```

学习不会把所有人物变成同一种冷静的小老师。

### 多维读者证据

保留兼容的摘要状态：

```text
unseen -> exposed -> intuitive -> operational -> formal -> transfer-ready
```

但状态必须由更具体的证据向量支撑：

```text
识别 | 预测 | 表示映射 | 操作
辨别 | 解释 | 延迟提取 | 迁移
```

这些仍然只是“书稿提供了什么机会”，不是对真实读者掌握度的诊断。

### 图像与真实数据

图、公式、频谱、星座图、相关峰、模拟和真实 IQ 数据必须承担证据工作：

```text
问题 | 来源 | 处理流程 | 坐标与单位 | 观察目标
支持什么推断 | 不支持什么推断 | 改变哪个决定
```

真实、模拟、示意、重建和虚构数据必须明确区分。

### 隔离审计

写作者、技术审计、教学审计、故事评论、首次读者、编辑和编年者使用不同信息包。

首次读者不能看到章节合同、教学目标或未来解释。同一个模型连续扮演多个角色仍属于相关审查，不能称为独立验证。

### 基线评测

修改 Skill 时，至少比较：

```text
无 Skill
当前发布版
候选版
```

使用相同任务、固定来源、多次采样、隐藏标签、随机 A/B、硬性有效性门槛、读者偏好和独立迁移题。

回归用例通过，只能说明规则没有明显破坏，不能说明小说写得更好。

## 参考文件

- [`references/scene-fusion.md`](references/scene-fusion.md)：场景双向因果与教学融合。
- [`references/fiction-craft.md`](references/fiction-craft.md)：视角、语言、对话、节奏和信息经济。
- [`references/character-simulation.md`](references/character-simulation.md)：人物行为与能动性。
- [`references/reader-cognition.md`](references/reader-cognition.md)：认知证据、延迟提取和迁移。
- [`references/visual-evidence.md`](references/visual-evidence.md)：图像、公式、模拟和真实数据。
- [`references/audit-protocol.md`](references/audit-protocol.md)：隔离式多镜头审计。
- [`references/evaluation-rubric.md`](references/evaluation-rubric.md)：盲式基线评测。
- [`references/project-layout.md`](references/project-layout.md)：长篇项目状态。
- [`references/evaluation-cases.md`](references/evaluation-cases.md)：原有行为回归用例。
- [`references/evaluation-cases-v2.md`](references/evaluation-cases-v2.md)：V2 场景、人物、视觉和评测回归用例。

## 工具与评测资产

验证项目结构：

```bash
python3 scripts/validate_project.py /path/to/project
```

输出机器可读结果：

```bash
python3 scripts/validate_project.py /path/to/project --json
```

准备盲式 A/B：

```bash
python3 scripts/prepare_blind_eval.py \
  --baseline /path/to/baseline \
  --candidate /path/to/candidate \
  --output /path/to/blind-eval \
  --seed 2026
```

起始评测任务与配对量表位于：

- [`evals/prompts.json`](evals/prompts.json)
- [`evals/pairwise-rubric.json`](evals/pairwise-rubric.json)

脚本只验证或组织明确的机械属性，不证明技术事实、教学效果或文学质量。

## 调用示例

```text
使用 $learning-novel-engine，把 OFDM 及其上下游知识设计成一部长篇学习小说。使用真实 IQ 数据时维护来源与处理记录。每个教学场景必须通过双向因果门，并在章节确认前运行隔离式故事、技术、教学和首次读者审计。
```

```text
使用 $learning-novel-engine 修订这一章。现在它像导师讲课，请先重建人物欲望、错误行动、可观察证据、决定分叉和后果，再进行小说工艺与知识审计。
```

困难事实研究和敌对验证可调用 `$research-orchestrator`。局部认知模型修补可调用 `$narrative-tutor`。
