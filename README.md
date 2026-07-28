# Horizon 个人每日资讯简报

[![个人简报](https://img.shields.io/badge/GitHub%20Pages-查看每日简报-0969da?logo=github)](https://yushxzh.github.io/Horizon/)
[![CI](https://github.com/yushxzh/Horizon/actions/workflows/ci.yml/badge.svg)](https://github.com/yushxzh/Horizon/actions/workflows/ci.yml)
[![每日发布](https://github.com/yushxzh/Horizon/actions/workflows/daily-summary.yml/badge.svg)](https://github.com/yushxzh/Horizon/actions/workflows/daily-summary.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Horizon 自动汇总最近 24 小时内值得关注的技术资讯，使用 DeepSeek 完成评分、去重、筛选和中文摘要，并发布到 GitHub Pages。

在线页面：<https://yushxzh.github.io/Horizon/>

## 简报内容

- AI 与 LLM
- 软件工程
- 开源工具
- 重要安全事件
- 开发者产品更新

每期最多保留 20 条，正文使用中文，同时保留原标题与原始链接。通用科技融资、营销文章和初级教程不在收录范围内。

## 信息源

- Hacker News
- Reddit：`r/MachineLearning`、`r/LocalLLaMA`、`r/programming`、`r/netsec`
- X：OpenAI、Anthropic、Google DeepMind、Andrej Karpathy 等高信号账号
- 精选 RSS：OpenAI、Google DeepMind、GitHub Engineering、Cloudflare、Kubernetes、Schneier on Security 等
- GitHub Release：vLLM、LangGraph、uv、Bun、Deno、Kubernetes、Docker Compose、Trivy、Grype 和 GitHub CLI

完整配置位于 [`data/config.github.json`](data/config.github.json)。

## 自动运行

GitHub Actions 每天北京时间 06:35 运行一次：

1. 抓取最近 24 小时的候选内容。
2. 使用 DeepSeek 评分、去重并生成中文摘要。
3. 将结果发布到 `gh-pages` 分支。
4. GitHub Pages 构建成功后更新在线页面。

也可以在 [Daily Horizon Summary](https://github.com/yushxzh/Horizon/actions/workflows/daily-summary.yml) 页面手动运行。

CI 在 `main` 分支的 Push 和 Pull Request 上执行依赖锁定检查、配置校验、工作流 YAML 校验和完整单元测试，不调用付费 API。

## GitHub Actions 密钥

在仓库的「Settings → Secrets and variables → Actions」中配置：

| 名称 | 用途 |
| --- | --- |
| `DEEPSEEK_API_KEY` | 内容评分、摘要和背景补充 |
| `APIFY_TOKEN` | 抓取 X 公开账号时间线 |

密钥仅通过 GitHub Actions 环境变量读取，不写入仓库或发布页面。

## 本地运行

要求 Python 3.11 或更高版本，并已安装 [uv](https://docs.astral.sh/uv/)。

```bash
git clone https://github.com/yushxzh/Horizon.git
cd Horizon
uv sync --extra dev --locked
cp data/config.github.json data/config.json
uv run horizon --hours 24
```

运行测试：

```bash
uv run pytest
```

本地生成简报前，需要在当前终端提供 `DEEPSEEK_API_KEY` 和 `APIFY_TOKEN`。

## 页面与归档

- 首页显示最新一期完整简报。
- 每期简报保留独立日期页面。
- 中文 RSS：<https://yushxzh.github.io/Horizon/feed-zh.xml>

## 上游项目

本仓库 Fork 自 [Thysrael/Horizon](https://github.com/Thysrael/Horizon)，保留 MIT License。当前 Fork 使用独立的信息源、中文输出、CI/CD 和 GitHub Pages 配置，不自动同步上游变更。
