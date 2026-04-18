# 🚀 PAO System - 多Agent通信框架

[![OpenClaw](https://img.shields.io/badge/Platform-OpenClaw-blue)](https://github.com/openclaw/openclaw)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green)]()
[![License](https://img.shields.io/badge/License-MIT-yellow)]()

PAO (Personal AI Operator) System — 支持 OpenClaw、Claude Code、Cursor 等多平台的 Agent 互联互通框架。

## 🎯 适用场景

- 🤖 OpenClaw 多 Agent 协作通信
- 🔄 Agent 任务分发与调度
- 🔗 跨平台 AI 能力整合
- 📡 多工作区消息总线

## ✨ 核心功能

| 功能 | 说明 |
|------|------|
| 任务分发 | 向指定 Agent 发送任务并接收结果 |
| 消息总线 | HTTP 接口，支持任意 Agent 互联 |
| 技能管理 | 自动注册和加载 AI 技能 |
| 协议处理 | 支持 WebSocket、HTTP 等多种协议 |

## 🚀 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/hansondong/pao-system.git
cd pao-system

# 2. 安装依赖
pip install -r requirements.txt

# 3. 启动监听服务
python pao_listener.py
```

## 📖 使用示例

```python
import httpx

# 向其他 Agent 发送任务
response = httpx.post('http://localhost:18761/task', json={
    "task_action": "安全扫描",
    "task_params": {"path": "/project"}
})
print(response.json())
```

## 📦 在 OpenClaw 中使用

将本仓库作为 Skill 安装：
```
openclaw skill install https://github.com/hansondong/pao-system
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License - 详见 LICENSE 文件