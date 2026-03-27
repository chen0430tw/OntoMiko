# Contributing to OntoMiko

感谢你考虑为 OntoMiko 做出贡献！

## 开发环境设置

### 1. Fork 仓库

点击右上角的 Fork 按钮。

### 2. 克隆你的 fork

```bash
git clone https://github.com/YOUR_USERNAME/OntoMiko.git
cd OntoMiko
```

### 3. 创建虚拟环境

**后端:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

**前端:**
```bash
cd frontend
npm install
```

## 开发流程

### 1. 创建分支

```bash
git checkout -b feature/your-feature-name
```

### 2. 进行开发

- 遵循现有的代码风格
- 添加必要的测试
- 更新相关文档

### 3. 运行测试

**后端:**
```bash
cd backend
pytest tests/ -v
```

**前端:**
```bash
cd frontend
npm run lint
npm run test
```

### 4. 提交更改

```bash
git add .
git commit -m "feat: add your feature description"
```

### 5. 推送到你的 fork

```bash
git push origin feature/your-feature-name
```

### 6. 创建 Pull Request

在 GitHub 上创建 Pull Request 到主仓库。

## 代码规范

### 前端 (TypeScript/React)

- 使用函数式组件和 Hooks
- 遵循 ESLint 和 Prettier 配置
- 组件文件名使用 PascalCase
- 工具函数文件名使用 camelCase

### 后端 (Python)

- 遵循 PEP 8
- 使用类型注解
- 函数使用 snake_case
- 类名使用 PascalCase

### 提交信息格式

使用 Conventional Commits 格式：

```
<type>(<scope>): <subject>

<body>

<footer>
```

类型:
- `feat`: 新功能
- `fix`: 修复 bug
- `docs`: 文档更新
- `style`: 代码格式（不影响功能）
- `refactor`: 重构
- `test`: 添加测试
- `chore`: 构建过程或工具变更

示例:
```
feat(engine): add new PMM detection algorithm

Add support for detecting Rule-PM type in perpetual motion
machine classification.

Closes #123
```

## 测试要求

- 新功能必须包含测试
- 测试覆盖率不应降低
- 所有测试必须通过

## 问题报告

使用 GitHub Issues 报告 bug 或请求功能。

## 许可证

通过贡献代码，你同意你的贡献将在 MIT 许可证下发布。
