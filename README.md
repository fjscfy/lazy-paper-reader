# lazy-paper-reader

一个面向研究论文的交互式 Codex Skill。它不会一次性生成论文摘要，而是陪你按阶段读完论文，并把双方确认过的理解持续写入同一份 Markdown 笔记。

## 它怎么读论文

阅读顺序固定为：

1. 标题与任务定位
2. 引言的论证链
3. 方法与动机的对应关系
4. 实验设置、证据与结论
5. 最终记忆点、真实增量、假设与局限

第一遍默认跳过 Related Work；只有在核对创新性时才回看相关段落。每一阶段都会先讲解并回答问题，得到你的明确确认后才更新笔记。

支持本地 PDF、论文链接、论文标题和已有 Markdown 笔记。针对自动驾驶 World Model 论文，仓库还提供了一套额外的分析视角，用来检查闭环价值、因果性、时空一致性和条件信息来源。

## 安装

克隆仓库，并把 `skills/lazy-paper-reader` 目录复制到你的 `$CODEX_HOME/skills/`：

```bash
git clone https://github.com/fjscfy/lazy-paper-reader.git
cp -R lazy-paper-reader/skills/lazy-paper-reader "$CODEX_HOME/skills/lazy-paper-reader"
```

重启 Codex 后，可以这样使用：

```text
Use $lazy-paper-reader to guide me through this paper stage by stage and maintain one Markdown note.
```

## 仓库结构

```text
skills/lazy-paper-reader/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── reading-workflow.md
    ├── markdown-structure.md
    └── autonomous-driving-world-model.md
```

## License

[MIT](LICENSE)
