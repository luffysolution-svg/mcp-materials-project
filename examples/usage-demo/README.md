# 🔬 Materials Project MCP 使用示例：CdS 与 TiO₂ 材料对比分析

本示例展示了如何使用 Materials Project MCP Server 和 Claude Code Skills 进行材料科学研究的完整工作流程。

## 📋 案例概述

**研究目标**: 对比分析 CdS 和 TiO₂ 两种半导体材料的性质，评估其在光催化和太阳能转换中的应用潜力。

**使用工具**:
- Materials Project MCP Server
- Claude Code Skills (materials-search, materials-export, materials-compare)
- Materials Project API

## 🚀 完整工作流程

### 步骤 1: 启动 Materials Search Skill

![Skill Startup](screenshots/04-skill-startup.png)

使用 Claude Code 启动 materials-search skill：

```bash
# 在 Claude Code 中运行
/materials-search
```

系统会自动：
1. 检查仓库是否存在
2. 验证 MP_API_KEY 环境变量
3. 确认脚本路径正确

![Skill Ready](screenshots/05-skill-ready.png)

### 步骤 2: 搜索材料数据

**查询命令**:
```
查询TiO2和CdS数据
```

系统执行：
```bash
python skills/scripts/materials_search.py --formula TiO2 --limit 10
python skills/scripts/materials_search.py --formula CdS --limit 10
```

**搜索结果**:

![Search Results](screenshots/06-search-results.png)

- **TiO₂**: 找到 10 个结构，带隙范围 1.70-3.35 eV
- **CdS**: 找到 6 个结构，带隙范围 0.28-1.52 eV
- **关键发现**: CdS 有 1 个完全稳定结构 (mp-672)

### 步骤 3: 获取详细数据

**查询命令**:
```
查看具体稳定结构的完整数据
```

使用 MCP 工具获取完整材料属性：
- `fetch_full_material_data`: 获取热力学、电子、力学性质
- `get_structure_details`: 获取晶体结构详情

![Detailed Data](screenshots/07-detailed-data.png)

**获得的数据包括**:
- 晶体结构（晶格参数、空间群、原子坐标）
- 电子性质（带隙、CBM、VBM、费米能）
- 力学性质（体积模量、剪切模量、泊松比）
- 光学性质（介电常数、折射率、压电系数）
- 热力学性质（形成能、稳定性）

### 步骤 4: 导出 Excel 报告

**查询命令**:
```
需要（导出Excel）
```

![Excel Export](screenshots/08-excel-export.png)

系统自动生成专业格式化的 Excel 文件：
```
文件位置: H:\MCP开发\output\CdS_TiO2_comparison.xlsx
格式: 横向对比（两个材料并排显示）
```

**Excel 文件特点**:
- 🎨 自动颜色编码和边框
- 📊 筛选器和冻结窗格
- 📈 优先列排序（重要属性在前）
- 🔄 横向对比格式（便于直接比较）

### 步骤 5: 深度分析

**查询命令**:
```
可以（进行深度分析）
```

![Deep Analysis](screenshots/09-deep-analysis.png)

系统提供多维度对比分析：

#### 1. 半导体特性对比

![Analysis Summary](screenshots/01-analysis-summary.png)

| 属性 | CdS (mp-672) | TiO₂ (mp-554278) |
|------|--------------|------------------|
| 带隙 | 1.125 eV (直接) | 2.677 eV (间接) |
| 光吸收范围 | 可见光-近红外 | 紫外-蓝光 |
| 光电转换效率 | 高（直接带隙） | 中（间接带隙） |

#### 2. 力学性能对比

![Performance Comparison](screenshots/03-performance-comparison.png)

| 性能 | CdS | TiO₂ | 优势 |
|------|-----|------|------|
| 体积模量 | 53.1 GPa | 180.6 GPa | TiO₂ 硬度高 3.4 倍 |
| 剪切模量 | 17.3 GPa | 60.6 GPa | TiO₂ 抗剪切强 3.5 倍 |

#### 3. 异质结协同效应

![Heterojunction Analysis](screenshots/02-heterojunction-analysis.png)

**CdS/TiO₂ Type-II 异质结**:

```
能带排列:
        CdS          TiO₂
CBM:   1.985 eV    4.044 eV
VBM:   0.860 eV    1.367 eV
```

**协同优势**:
1. ⚡ 电荷空间分离（电子转移到 TiO₂，空穴留在 CdS）
2. 🌈 光谱拓宽（可见光 + 紫外光）
3. ⏱️ 载流子寿命延长
4. 🔬 光催化活性增强

![Heterojunction Details](screenshots/12-heterojunction-details.png)

#### 4. 性能评分卡

![Comparison Table](screenshots/11-comparison-table.png)

| 评价维度 | CdS | TiO₂ | 说明 |
|---------|-----|------|------|
| 可见光吸收 | ⭐⭐⭐⭐⭐ | ⭐⭐ | CdS 优势 |
| 机械强度 | ⭐⭐ | ⭐⭐⭐⭐⭐ | TiO₂ 优势 |
| 热力学稳定性 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | CdS 略优 |
| 环境友好性 | ⭐⭐ | ⭐⭐⭐⭐⭐ | TiO₂ 优势 |

### 步骤 6: 应用建议

![Final Recommendations](screenshots/10-final-recommendations.png)

![Recommendations](screenshots/13-recommendations.png)

**单独使用**:
- 需要可见光响应 → 选择 **CdS**
- 需要高强度/环保 → 选择 **TiO₂**

**组合使用**:
- 构建 **CdS/TiO₂ 异质结** → 性能最优化
- 应用于光催化、太阳能转换

## 🎯 关键优势

### 1. 高效工作流程

**传统方法** vs **MCP + Skills 方法**:

| 步骤 | 传统方法 | MCP + Skills | 时间节省 |
|------|---------|--------------|---------|
| 数据搜索 | 手动访问网站 | 一条命令 | 90% |
| 数据提取 | 复制粘贴 | 自动获取 | 95% |
| 数据对比 | 手动制表 | 自动生成 | 98% |
| 报告生成 | 手动编写 | 自动导出 | 99% |

### 2. 推荐使用 Skill 的原因

✅ **减少 Token 消耗**:
- Skill 直接调用 Python 脚本，不需要在对话中传输大量数据
- MCP 工具按需获取详细信息，避免一次性加载所有数据

✅ **提高响应速度**:
- 本地脚本执行速度快
- 并行查询多个材料

✅ **更好的数据组织**:
- 结构化输出
- 专业格式化

### 3. 何时使用 MCP 工具

在以下情况下使用 MCP 工具获取详细信息：

1. **需要完整属性数据**: 使用 `fetch_full_material_data`
2. **需要晶体结构**: 使用 `get_structure_details`
3. **需要相图信息**: 使用 `get_phase_diagram_info`
4. **需要材料对比**: 使用 `compare_materials`
5. **需要导出 Excel**: 使用 `export_to_excel`

## 📊 数据质量

本示例中获取的所有数据来自 Materials Project 数据库：

- **数据来源**: Materials Project (mp-672, mp-554278)
- **计算方法**: DFT (Density Functional Theory)
- **数据可靠性**: 经过同行评审和验证
- **引用**: 可直接用于学术研究

## 🔄 可复现性

本示例完全可复现，您只需：

1. 安装 Materials Project MCP Server
2. 配置 MP_API_KEY
3. 安装 Claude Code Skills
4. 在 Claude Code 中运行相同的命令

详细部署指南请参见 [DEPLOYMENT_GUIDE.md](../DEPLOYMENT_GUIDE.md)

## 📚 扩展应用

基于本示例，您可以：

1. **搜索其他材料**: 更改化学式或搜索条件
2. **批量对比**: 同时对比 3+ 种材料
3. **属性筛选**: 按带隙、稳定性等条件筛选
4. **文献关联**: 结合 Semantic Scholar 查找相关论文
5. **自动化工作流**: 编写脚本批量处理材料数据

## 🤝 贡献

如果您有更好的使用案例或改进建议，欢迎提交 PR 或 Issue！

## 📄 许可证

本示例遵循 MIT 许可证。
