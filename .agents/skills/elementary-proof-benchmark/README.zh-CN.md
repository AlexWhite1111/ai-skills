# Elementary Proof Benchmark

`$elementary-proof-benchmark` 用来设计和运行一种很具体的数学推理评测：

> 题面与知识门槛尽量朴素，但完整证明必须把多个独立结构拼合起来；评分重点是证明链是否闭合，而不是模型是否猜中了答案。

## 它测什么

它主要测四件事：

1. 模型能否在没有现成标签的情况下发现多个局部结构；
2. 找到漂亮表示以后，能否继续完成全局覆盖、最优性与等号条件；
3. 面对针对性反例或审计时，能否真正修复证明，而不是换一种措辞掩盖缺口；
4. 在公开题、隐藏题、允许搜索和禁止搜索等不同条件下，结果是否仍然可比较。

## 三种常用模式

### 出题

```text
使用 $elementary-proof-benchmark 设计一个高中基础知识可读、但需要至少三个独立证明锁才能闭合的新题。先做撞题检索、完整证明、反例搜索和模型试测，再决定是否收入 private-test。
```

### 盲测

```text
使用 $elementary-proof-benchmark 对这些模型运行 blind-proof。固定同一题面、时间和工具权限，保存原始输出，按 strict proof rubric 评分，不把答案正确等同于证明通过。
```

### 敌对修复

```text
使用 $elementary-proof-benchmark 审计这份证明。只指出最小充分缺口，让模型修复；记录它是否关闭了原缺口、是否引入新缺口，以及最终能否给出自包含证明。
```

## 当前内容

- 一套 benchmark 设计与运行规范；
- 一套严格证明评分与修复评分规则；
- 一个公开开发集：
  - 1 道 proof-integrity challenge；
  - 2 道 calibration 题；
- 每道公开题的参考证明与已知攻击点；
- 一个机器可读运行记录模板；
- 一个只依赖 Python 标准库的数据校验脚本。

公开开发题用于验证评测流程，**不能**作为无污染排行榜成绩。真正比较模型时，应使用冻结的 `private-test` 或即时生成并审计完成的 `live` 题目，待评测结束后再公开。

## 快速校验

在仓库根目录运行：

```bash
python .agents/skills/elementary-proof-benchmark/scripts/validate_benchmark.py
```

## 与 Research Orchestrator 的关系

这个 Skill 可以借用 `$research-orchestrator` 的多路线搜索、显式缺口跟踪与敌对审计思想，但它是独立可复制的：即使单独安装，也包含完成 benchmark 设计、运行和评分所需的全部规范。
