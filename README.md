# OntoMiko

**OntoMiko / 宇宙许可占卜姬**  
日本心理测验风格的宇宙权限占验产品。

## 技术栈

- Frontend: Next.js + TypeScript + Tailwind CSS
- Backend: FastAPI + Python
- Engine: Python rule engine

## 核心流程

User Input
-> frontend form
-> FastAPI /divine/text
-> engine.extract_features
-> engine.classify_pmm
-> engine.divine
-> result JSON
-> frontend result card
