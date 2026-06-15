# 电商商品图与详情页批量生成工具

**ecommerce-product-visual-generator** 是一个专业的淘宝/电商详情页批量生成系统，帮助美工团队快速生成主图、详情页模块、卖点图和 AI 生图提示词。

## 🎯 核心功能

### MVP 版本（第一期）

- ✅ **主图生成**：产品图 + 卖点文案 + 背景风格
- ✅ **AI 提示词生成**：支持 Midjourney / DALL-E / 即梦 / 可灵等工具
- ✅ **详情页模块模板**：8 个常用模块（卖点、场景、规格、材质等）
- ✅ **批量导入**：支持 Excel/CSV 批量导入商品信息
- ✅ **图片输出**：高质量 PNG 导出
- ✅ **配置保存**：JSON 格式保存生成配置

### 第二期计划

- [ ] HTML 预览和截图导出
- [ ] 详情页长图拼接
- [ ] 场景图、细节图、规格图模板
- [ ] 更多行业模板库
- [ ] Web 模板编辑器

## 🚀 快速开始

### 系统要求

- Python 3.8+
- Pillow 9.0+
- openpyxl 3.8+

### 安装

```bash
git clone https://github.com/zzyayuan123-a11y/ecommerce-product-visual-generator.git
cd ecommerce-product-visual-generator
pip install -r requirements.txt
```

### 基本使用

#### 1. 准备商品数据

编辑 `examples/sample_data.xlsx`

#### 2. 生成商品图

```bash
python main.py --input examples/sample_data.xlsx --output ./output
```

#### 3. 查看输出

所有文件存储在 `./output/` 目录

## 📁 项目结构

```
├── README.md
├── requirements.txt
├── main.py
├── config/
│   ├── templates.json          # 详情页模块定义
│   ├── styles.json             # 设计风格配置
│   ├── categories.json         # 行业类目配置
│   └── keywords.json           # AI 关键词库
├── src/
│   ├── __init__.py
│   ├── image_processor.py      # 图片处理核心
│   ├── template_generator.py   # 模板生成引擎
│   ├── prompt_generator.py     # 提示词生成器
│   ├── batch_processor.py      # 批量处理队列
│   ├── config_manager.py       # 配置管理
│   └── utils/
├── examples/
│   ├── sample_data.xlsx        # 示例数据
│   ├── usage_demo.py           # 使用演示
│   └── README.md               # 使用说明
├── tests/
│   └── __init__.py
└── output/                     # 生成输出目录
```

## 📊 8 个详情页基础模块

1. **Hero Banner** - 主图（750x900）
2. **Selling Points** - 卖点模块（750x500）
3. **Usage Scene** - 使用场景（750x600）
4. **Material Details** - 材质工艺（750x800）
5. **Size & Specs** - 尺寸规格（750x600）
6. **Product Comparison** - 产品对比（750x700）
7. **Audience Match** - 适用人群（750x500）
8. **Trust & Warranty** - 保障信息（750x600）

## 🎨 支持的行业类目

- 🍰 烘焙食品
- 🎁 包装礼盒
- 💄 美妆个护
- 🏠 家居百货
- 🛍️ 小商品

## 📄 许可证

MIT License
