# 🎯 Claude Code Skills 配置说明

## 📁 目录结构解释

### 你的 `.claude` 目录结构

```
C:\Users\CSC\.claude\
├── skills.json                          # ❌ 这个文件Claude Code不使用！
├── skills\                              # ✅ 正确的skills目录
│   ├── materials-search\                # ✅ 搜索skill
│   │   ├── SKILL.md                     # ✅ Skill定义文件（必需）
│   │   └── materials_search.py          # ✅ Python脚本
│   ├── materials-export\                # ✅ 导出skill
│   │   ├── SKILL.md                     # ✅ Skill定义文件（必需）
│   │   └── materials_export.py          # ✅ Python脚本
│   ├── materials-compare\               # ✅ 对比skill
│   │   ├── SKILL.md                     # ✅ Skill定义文件（必需）
│   │   └── materials_compare.py         # ✅ Python脚本
│   ├── materials-skills\                # ⚠️ 旧的目录（可删除）
│   ├── high-precision-lit-search\       # ✅ 其他skill
│   │   └── SKILL.md
│   └── academic-pro-plus\               # ✅ 其他skill
│       └── SKILL.md
└── materials-skills\                    # ⚠️ 旧的目录（可删除）
    └── scripts\
```

## 🔑 关键发现

### Claude Code Skills 的正确格式

Claude Code **不使用** `skills.json` 文件！

正确的格式是：
```
~/.claude/skills/[skill-name]/SKILL.md
```

### SKILL.md 文件格式

```markdown
---
name: skill-name
description: |
  Skill description here
version: 1.0.0
---

# Skill Title

## Instructions for Claude

[详细的执行指令...]
```

## ✅ 已完成的配置

### 1. 创建了三个正确的Skills

✅ **materials-search**
- 位置: `~/.claude/skills/materials-search/`
- 文件: `SKILL.md` + `materials_search.py`
- 命令: `/materials-search`

✅ **materials-export**
- 位置: `~/.claude/skills/materials-export/`
- 文件: `SKILL.md` + `materials_export.py`
- 命令: `/materials-export`

✅ **materials-compare**
- 位置: `~/.claude/skills/materials-compare/`
- 文件: `SKILL.md` + `materials_compare.py`
- 命令: `/materials-compare`

### 2. SKILL.md 包含的内容

每个 SKILL.md 文件包含：
- ✅ Skill元数据（name, description, version）
- ✅ 核心能力说明
- ✅ 执行指令（如何调用Python脚本）
- ✅ 参数说明
- ✅ 输出格式
- ✅ 使用示例
- ✅ 错误处理
- ✅ 工作流集成

## 🚀 如何使用

### 1. 重启Claude Code

关闭并重新打开Claude Code，让它加载新的skills。

### 2. 使用Skills

在Claude Code中直接使用：

```bash
# 搜索材料
/materials-search --formula Si

# 导出到Excel
/materials-export --material-id mp-149 --output silicon.xlsx

# 对比材料
/materials-compare mp-149 mp-2534
```

### 3. 查看可用Skills

在Claude Code中输入 `/` 应该能看到：
- `/materials-search`
- `/materials-export`
- `/materials-compare`
- `/high-precision-lit-search`
- `/academic-pro-plus`

## 🔧 故障排除

### 如果Skills没有显示

1. **检查目录结构**
   ```bash
   ls ~/.claude/skills/materials-search/
   # 应该看到: SKILL.md 和 materials_search.py
   ```

2. **检查SKILL.md格式**
   - 必须有YAML front matter（---包围的部分）
   - 必须有name字段
   - 文件名必须是 `SKILL.md`（大写）

3. **重启Claude Code**
   - 完全关闭Claude Code
   - 重新打开

4. **检查环境变量**
   ```bash
   echo $MP_API_KEY
   # 应该显示你的API key
   ```

### 如果Skills执行失败

1. **检查Python脚本路径**
   - SKILL.md中的路径必须正确
   - 当前使用相对路径（脚本在同一目录）

2. **检查Python依赖**
   ```bash
   pip list | grep -E "mp-api|pandas|openpyxl"
   ```

3. **手动测试脚本**
   ```bash
   cd ~/.claude/skills/materials-search
   python materials_search.py --material-id mp-149
   ```

## 📝 与之前配置的区别

### 错误的方式（我们之前做的）
```
~/.claude/skills.json          # ❌ Claude Code不读取这个
~/.claude/materials-skills/    # ❌ 位置错误
```

### 正确的方式（现在的配置）
```
~/.claude/skills/materials-search/SKILL.md    # ✅ 正确
~/.claude/skills/materials-export/SKILL.md    # ✅ 正确
~/.claude/skills/materials-compare/SKILL.md   # ✅ 正确
```

## 🧹 清理建议

可以删除这些不需要的文件/目录：
```bash
# 删除错误的配置
rm ~/.claude/skills.json

# 删除旧的目录
rm -rf ~/.claude/materials-skills
rm -rf ~/.claude/skills/materials-skills
```

## 📚 参考其他Skills

你可以参考已有的skills学习格式：
```bash
cat ~/.claude/skills/high-precision-lit-search/SKILL.md
cat ~/.claude/skills/academic-pro-plus/SKILL.md
```

## 🎊 总结

现在你的Materials Project Skills已经按照**正确的Claude Code格式**配置好了！

**重启Claude Code后**，你应该能够使用：
- `/materials-search` - 搜索材料
- `/materials-export` - 导出Excel
- `/materials-compare` - 对比材料

这些skills现在会在**所有项目**中可用！🚀
