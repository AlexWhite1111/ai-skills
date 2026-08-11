# Narrative Tutor Skill

一个用于数学、科学、工程、人文与其他复杂主题讲解的可复用 Skill。

它不是“最佳讲解法”的宣言，而是把一套正在使用和迭代的方法公开出来：从学习者当前的理解出发，让旧模型先做一次真实预测，找到最关键的缺口，再引入刚好能修复它的新工具，并立刻回到同一个对象检验。

## 核心思路

- 保持一个具体对象稳定，让解释逐步变强。
- 尊重学习者当前模型中合理的部分，再精确修复关键缺口。
- 让公式、抽象和证据在“它为什么此刻必要”之后出现。
- 区分直觉、类比、经验模型、数值证据、形式证明与开放问题。
- 回答当前问题后，由结果自然推动下一步，而不是机械追问“要不要继续”。

完整规则见 [`SKILL.md`](SKILL.md)。

## 使用方式

### Codex / 支持 Skills 的 Agent

将整个仓库克隆或复制到个人 skills 目录，例如：

```bash
git clone https://github.com/AlexWhite1111/narrative-tutor-skill.git ~/.codex/skills/narrative-tutor
```

之后在讲解任务中调用 `$narrative-tutor`，或让 Agent 根据 Skill 的描述自动触发。

### 其他 AI 助手

可以把 `SKILL.md` 作为自定义指令或系统提示的参考，但不同产品对 Skill、工具调用和上下文的支持并不相同，需要按实际环境裁剪。

## 可选参考语料检索

仓库包含 `scripts/retrieve_corpus.py`，用于从你自己合法持有的参考语料中，按叙事功能检索少量窗口。参考语料本身不包含在仓库中，也不是 Skill 正常运行的必需条件。

```bash
export VERITASIUM_CORPUS=/path/to/your/reference-corpus
python3 scripts/retrieve_corpus.py --move crack --limit 4
```

也可以直接传入 `--corpus /path/to/corpus`。若没有外部语料，使用 `references/` 中的提炼模式即可。

## 一起改进

欢迎通过 Issue 分享：

- 哪种讲解仍然跳步、太抽象或工作记忆负担过重；
- 哪个领域不适合当前的“模型修复”结构；
- 哪条规则在真实对话中产生了副作用；
- 可独立判断的对照案例与改进建议。

也欢迎提交 Pull Request。这里更关心可验证的讲解效果和明确边界，而不是把某一种风格包装成唯一答案。

