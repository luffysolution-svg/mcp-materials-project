# 🚀 Materials Project MCP Server 部署指南

本指南将帮助您从零开始部署 Materials Project MCP Server 和 Claude Code Skills，实现材料科学研究的自动化工作流程。

## 📋 目录

- [系统要求](#系统要求)
- [快速开始](#快速开始)
- [详细部署步骤](#详细部署步骤)
- [配置说明](#配置说明)
- [验证安装](#验证安装)
- [常见问题](#常见问题)
- [使用示例](#使用示例)

## 🖥️ 系统要求

### 必需条件

- **操作系统**: Windows 10/11, macOS, Linux
- **Python**: 3.8 或更高版本
- **Claude Code**: 最新版本
- **Git**: 用于克隆仓库
- **Materials Project API Key**: 免费注册获取

### 推荐配置

- **内存**: 4GB 或以上
- **磁盘空间**: 500MB（用于依赖和数据缓存）
- **网络**: 稳定的互联网连接

## ⚡ 快速开始

如果您熟悉命令行操作，可以使用以下命令快速部署：

```bash
# 1. 克隆仓库
git clone https://github.com/luffysolution-svg/mcp-materials-project.git
cd mcp-materials-project

# 2. 安装依赖
pip install -r requirements.txt

# 3. 设置 API Key（Windows）
setx MP_API_KEY "your_api_key_here"

# 3. 设置 API Key（macOS/Linux）
export MP_API_KEY="your_api_key_here"
echo 'export MP_API_KEY="your_api_key_here"' >> ~/.bashrc

# 4. 安装 Skills（Windows）
cd skills
install-skills-windows.bat

# 4. 安装 Skills（macOS/Linux）
cd skills
chmod +x install-skills-unix.sh
./install-skills-unix.sh

# 5. 验证安装
python skills/verify-installation.py
```

## 📖 详细部署步骤

### 步骤 1: 获取 Materials Project API Key

1. 访问 [Materials Project 官网](https://materialsproject.org/)
2. 点击右上角 "Sign Up" 注册账号（免费）
3. 登录后，访问 [API Dashboard](https://materialsproject.org/api)
4. 复制您的 API Key（格式类似：`abc123def456...`）

**注意**: API Key 是私密信息，请勿分享或提交到公共仓库。

### 步骤 2: 克隆仓库

打开终端（Windows 使用 PowerShell 或 CMD），执行：

```bash
# 克隆仓库到本地
git clone https://github.com/luffysolution-svg/mcp-materials-project.git

# 进入项目目录
cd mcp-materials-project
```

**目录结构**:
```
mcp-materials-project/
├── mcp_materials.py          # MCP Server 主程序
├── requirements.txt          # Python 依赖
├── skills/                   # Claude Code Skills
│   ├── scripts/             # Python 脚本
│   │   ├── materials_search.py
│   │   ├── materials_compare.py
│   │   └── materials_export.py
│   ├── skill-definitions/   # Skill 定义文件
│   ├── install-skills-windows.bat
│   ├── install-skills-unix.sh
│   └── verify-installation.py
├── examples/                # 使用示例
└── README.md
```

### 步骤 3: 安装 Python 依赖

确保您已安装 Python 3.8+：

```bash
# 检查 Python 版本
python --version

# 安装依赖
pip install -r requirements.txt
```

**主要依赖包**:
- `mp-api`: Materials Project API 客户端
- `pandas`: 数据处理
- `openpyxl`: Excel 文件生成

### 步骤 4: 配置 API Key

#### Windows 系统

**方法 1: 使用 setx 命令（推荐）**

```cmd
setx MP_API_KEY "your_api_key_here"
```

**重要**: 设置后需要重启终端才能生效。

**方法 2: 系统环境变量**

1. 右键 "此电脑" → "属性"
2. 点击 "高级系统设置"
3. 点击 "环境变量"
4. 在 "用户变量" 中点击 "新建"
5. 变量名: `MP_API_KEY`
6. 变量值: 您的 API Key
7. 点击 "确定" 保存

#### macOS/Linux 系统

**临时设置（当前会话）**:

```bash
export MP_API_KEY="your_api_key_here"
```

**永久设置（推荐）**:

```bash
# 添加到 .bashrc（Bash）
echo 'export MP_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc

# 或添加到 .zshrc（Zsh）
echo 'export MP_API_KEY="your_api_key_here"' >> ~/.zshrc
source ~/.zshrc
```

**验证 API Key 设置**:

```bash
# Windows (PowerShell)
echo $env:MP_API_KEY

# Windows (CMD)
echo %MP_API_KEY%

# macOS/Linux
echo $MP_API_KEY
```

### 步骤 5: 配置 MCP Server

#### 方法 1: 使用 Smithery（推荐）

Smithery 是 MCP Server 的包管理器，可以自动配置。

1. 访问 [Smithery](https://smithery.ai/)
2. 搜索 "materials-project"
3. 点击 "Install" 按钮
4. 按照提示完成配置

#### 方法 2: 手动配置

编辑 Claude Code 配置文件：

**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Linux**: `~/.config/Claude/claude_desktop_config.json`

添加以下配置：

```json
{
  "mcpServers": {
    "materials-project": {
      "command": "python",
      "args": [
        "H:/MCP开发/mcp_materials.py"
      ],
      "env": {
        "MP_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

**注意**:
- 将路径替换为您的实际路径
- Windows 路径使用正斜杠 `/` 或双反斜杠 `\\`
- 将 `your_api_key_here` 替换为您的实际 API Key

### 步骤 6: 安装 Claude Code Skills

Skills 提供了便捷的命令行接口，推荐安装。

#### Windows 系统

```cmd
cd skills
install-skills-windows.bat
```

#### macOS/Linux 系统

```bash
cd skills
chmod +x install-skills-unix.sh
./install-skills-unix.sh
```

**安装脚本会自动**:
1. 检测 Claude Code 配置目录
2. 复制 skill 定义文件到正确位置
3. 验证安装是否成功

**手动安装（如果自动安装失败）**:

```bash
# 找到 Claude Code skills 目录
# Windows: %USERPROFILE%\.claude\skills
# macOS/Linux: ~/.claude/skills

# 复制 skill 定义文件
cp skills/skill-definitions/*.json ~/.claude/skills/
```

### 步骤 7: 验证安装

运行验证脚本：

```bash
python skills/verify-installation.py
```

**成功输出示例**:

```
✓ Python version: 3.11.0
✓ MP_API_KEY is set
✓ mp-api package installed
✓ pandas package installed
✓ openpyxl package installed
✓ materials_search.py found
✓ materials_compare.py found
✓ materials_export.py found
✓ API connection successful

All checks passed! ✓
```

**如果出现错误**，请参考 [常见问题](#常见问题) 部分。

## ⚙️ 配置说明

### MCP Server 配置选项

在 `claude_desktop_config.json` 中，您可以配置以下选项：

```json
{
  "mcpServers": {
    "materials-project": {
      "command": "python",
      "args": [
        "/path/to/mcp_materials.py"
      ],
      "env": {
        "MP_API_KEY": "your_api_key",
        "MP_CACHE_DIR": "/path/to/cache",  // 可选：缓存目录
        "MP_TIMEOUT": "30"                  // 可选：API 超时时间（秒）
      }
    }
  }
}
```

### Skills 配置

Skills 配置文件位于 `~/.claude/skills/`，每个 skill 有独立的 JSON 文件：

- `materials-search.json`: 材料搜索
- `materials-compare.json`: 材料对比
- `materials-export.json`: 数据导出

**示例配置** (`materials-search.json`):

```json
{
  "name": "materials-search",
  "description": "Search Materials Project database",
  "version": "1.0.0",
  "command": "python",
  "args": [
    "skills/scripts/materials_search.py"
  ],
  "parameters": {
    "formula": {
      "type": "string",
      "description": "Chemical formula"
    },
    "band_gap_min": {
      "type": "number",
      "description": "Minimum band gap (eV)"
    }
  }
}
```

## ✅ 验证安装

### 测试 MCP Server

在 Claude Code 中运行：

```
使用 MCP 工具搜索 Silicon 材料
```

预期输出：
```
找到 X 个 Silicon 材料
- mp-149: Si (带隙 0.61 eV)
- ...
```

### 测试 Skills

在 Claude Code 中运行：

```
/materials-search
```

然后输入：
```
查询 TiO2 数据
```

预期输出：
```
🔍 Materials Search Results
============================================================
Found 10 materials
...
```

## 🔧 常见问题

### 1. API Key 未设置

**错误信息**:
```
MP_API_KEY not found
```

**解决方法**:
- 确认已设置环境变量
- 重启终端或 Claude Code
- 检查拼写是否正确（区分大小写）

### 2. 依赖包安装失败

**错误信息**:
```
ModuleNotFoundError: No module named 'mp_api'
```

**解决方法**:
```bash
# 升级 pip
python -m pip install --upgrade pip

# 重新安装依赖
pip install -r requirements.txt

# 或单独安装
pip install mp-api pandas openpyxl
```

### 3. MCP Server 无法启动

**错误信息**:
```
Failed to start MCP server
```

**解决方法**:
1. 检查 Python 路径是否正确
2. 检查脚本路径是否正确
3. 查看 Claude Code 日志：
   - Windows: `%APPDATA%\Claude\logs`
   - macOS: `~/Library/Logs/Claude`

### 4. Skills 未显示

**解决方法**:
1. 确认 skill 文件已复制到正确目录
2. 重启 Claude Code
3. 检查 JSON 文件格式是否正确

### 5. API 请求超时

**错误信息**:
```
Timeout error when fetching data
```

**解决方法**:
- 检查网络连接
- 增加超时时间（在配置中设置 `MP_TIMEOUT`）
- 减少查询结果数量（使用 `--limit` 参数）

### 6. Excel 导出失败

**错误信息**:
```
Permission denied: output.xlsx
```

**解决方法**:
- 关闭已打开的 Excel 文件
- 检查输出目录是否有写权限
- 指定不同的输出文件名

## 📚 使用示例

### 示例 1: 基本搜索

```bash
# 使用 Skill
/materials-search

# 输入查询
查询 Silicon 材料
```

### 示例 2: 高级搜索

```bash
# 搜索带隙在 1-3 eV 的稳定半导体
python skills/scripts/materials_search.py \
  --band-gap-min 1.0 \
  --band-gap-max 3.0 \
  --stable \
  --limit 20
```

### 示例 3: 材料对比

```bash
# 对比多个材料
python skills/scripts/materials_compare.py \
  --material-ids mp-149,mp-672,mp-390
```

### 示例 4: 导出 Excel

```bash
# 导出搜索结果到 Excel
python skills/scripts/materials_export.py \
  --formula TiO2 \
  --output my_materials.xlsx
```

### 示例 5: 完整工作流程

参见 [usage-demo](usage-demo/README.md) 获取完整的 CdS/TiO₂ 对比分析示例。

## 🔄 更新和维护

### 更新 MCP Server

```bash
cd mcp-materials-project
git pull origin main
pip install -r requirements.txt --upgrade
```

### 更新 Skills

```bash
cd skills
git pull origin main

# Windows
install-skills-windows.bat

# macOS/Linux
./install-skills-unix.sh
```

### 清理缓存

```bash
# 删除 Python 缓存
find . -type d -name "__pycache__" -exec rm -rf {} +

# 删除 API 缓存（如果配置了）
rm -rf $MP_CACHE_DIR/*
```

## 🆘 获取帮助

如果您遇到问题：

1. **查看文档**: 阅读 [README.md](../README.md) 和本指南
2. **搜索 Issues**: 在 [GitHub Issues](https://github.com/luffysolution-svg/mcp-materials-project/issues) 中搜索类似问题
3. **提交 Issue**: 如果问题未解决，创建新的 Issue
4. **社区支持**: 加入 Materials Project 社区论坛

**提交 Issue 时请包含**:
- 操作系统和版本
- Python 版本
- 错误信息完整输出
- 复现步骤

## 📝 下一步

安装完成后，您可以：

1. 📖 阅读 [使用示例](usage-demo/README.md)
2. 🔬 探索 [Skills 文档](../skills/README.md)
3. 🎯 查看 [API 文档](../README.md#api-reference)
4. 💡 贡献您的使用案例

## 🤝 贡献

欢迎贡献改进建议！请参考 [CONTRIBUTING.md](../CONTRIBUTING.md)

## 📄 许可证

本项目遵循 MIT 许可证。详见 [LICENSE](../LICENSE)
