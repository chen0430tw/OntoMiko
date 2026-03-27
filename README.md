# OntoMiko

**OntoMiko / 宇宙许可占卜姬**

日本心理测验风格的宇宙权限占验产品。

![OntoMiko](https://img.shields.io/badge/version-0.1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 快速开始

### 使用启动脚本（推荐）

**Linux / macOS:**
```bash
chmod +x scripts/dev.sh
./scripts/dev.sh
```

**Windows:**
```cmd
scripts\dev.bat
```

### 手动启动

**后端:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

**前端:**
```bash
cd frontend
npm install
npm run dev
```

访问：
- 前端: http://localhost:3000
- 后端: http://127.0.0.1:8000
- API 文档: http://127.0.0.1:8000/docs

## Docker 部署

```bash
docker-compose up
```

## 技术栈

- **Frontend:** Next.js 14 + TypeScript + Tailwind CSS
- **Backend:** FastAPI + Python 3.11
- **Engine:** Python rule engine (本体许可占验算法)

## 项目结构

```
OntoMiko/
├── frontend/              # Next.js 前端
│   ├── app/              # App router
│   ├── components/       # React 组件
│   ├── lib/              # 工具函数
│   └── tests/            # 前端测试
├── backend/              # FastAPI 后端
│   ├── app/
│   │   ├── main.py       # 应用入口
│   │   ├── routers/      # API 路由
│   │   ├── schemas/      # Pydantic 模型
│   │   └── services/     # 业务逻辑
│   └── tests/            # 后端测试
├── engine/               # 占验引擎
│   └── ontomiko/
│       └── diviner_v2.py # 核心算法
├── scripts/              # 启动脚本
├── docs/                 # 文档
└── docker-compose.yml    # Docker 编排
```

## 核心流程

```
用户输入 → 前端表单 → POST /divine/text
→ 引擎特征提取 → PMM 分类 → 本体判定
→ 结果 JSON → 前端结果卡
```

## API 接口

### POST /divine/text

宇宙许可占验接口。

**请求:**
```json
{
  "text": "未来是否存在依靠潜势和惯性计算的通用拟构处理器？"
}
```

**响应:**
```json
{
  "category": "宇宙同意",
  "state": "qY",
  "reason": "设想具有来源、承载、可判性与可接受代价",
  "permission_score": 0.91,
  "note": "需要高权限",
  "features": {...},
  "pmm": {...}
}
```

## 开发指南

### 前端开发

```bash
cd frontend
npm install              # 安装依赖
npm run dev             # 启动开发服务器
npm run build           # 构建生产版本
npm run lint            # 代码检查
npm run format          # 格式化代码
npm run test            # 运行测试
```

### 后端开发

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt      # 生产依赖
pip install -r requirements-dev.txt  # 开发依赖
pytest tests/                        # 运行测试
black .                              # 格式化代码
ruff check .                         # 代码检查
```

### 代码规范

**前端:**
- 使用 TypeScript 严格模式
- 遵循 ESLint 和 Prettier 配置
- 组件使用函数式组件 + Hooks

**后端:**
- 遵循 PEP 8 代码规范
- 使用 Black 格式化
- 使用类型注解

## 测试

**后端测试:**
```bash
cd backend
pytest tests/ -v
```

**前端测试:**
```bash
cd frontend
npm run test
npm run test:coverage
```

## 贡献指南

请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何贡献代码。

## 许可证

MIT License

## 作者

chen0430tw

---

🌸 把你的天马行空交给宇宙审核。

