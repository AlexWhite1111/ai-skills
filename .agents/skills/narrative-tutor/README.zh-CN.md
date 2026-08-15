# Narrative Tutor Skill

这是一个用于数学、科学、工程、人文与其他复杂主题讲解的可复用 Skill。

它从学习者当前的理解出发，让旧模型先做一次真实预测，找到最关键的缺口，再引入刚好能够修复它的新工具，并立刻回到同一个对象检验。

## 核心思路

- 保持一个具体对象稳定，让解释逐步变强。
- 尊重学习者当前模型中合理的部分，再精确修复关键缺口。
- 让公式、抽象和证据在“它为什么此刻必要”之后出现。
- 区分直觉、类比、经验模型、数值证据、形式证明与开放问题。
- 回答当前问题后，由结果自然推动下一步，而不是机械追问是否继续。

完整规则见 [`SKILL.md`](SKILL.md)。

## 安装与调用

从本仓库根目录复制该 Skill：

```bash
mkdir -p ~/.codex/skills
cp -R .agents/skills/narrative-tutor ~/.codex/skills/
```

之后调用：

```text
Use $narrative-tutor to teach this topic from a concrete problem, updating one mental model at a time and stating evidence and limits.
```

## 可选参考语料检索

`scripts/retrieve_corpus.py` 可以从你自己合法持有的参考语料中，按叙事功能检索少量窗口。参考语料本身不包含在仓库中，也不是 Skill 正常运行的必要条件。

```bash
export VERITASIUM_CORPUS=/path/to/your/reference-corpus
python3 scripts/retrieve_corpus.py --move crack --limit 4
```

也可以直接传入 `--corpus /path/to/corpus`。若没有外部语料，使用 `references/` 中的提炼模式即可。

## 评测与改进

修改核心行为前先阅读 [`references/evaluation-cases.md`](references/evaluation-cases.md)。这里关心的是可验证的讲解效果、工作记忆负担和推理边界，而不是把某一种风格包装成唯一答案。
