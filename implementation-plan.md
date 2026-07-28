# 个人每日资讯简报实施方案

## 目标

基于 `Thysrael/Horizon` 的公开 Fork，通过 GitHub Actions 每天生成个人每日资讯简报，并发布到 `https://yushxzh.github.io/Horizon/`。

## 简报范围

- 语言：中文摘要，保留原始标题与链接
- 时间范围：最近 24 小时
- 每日上限：20 条入选资讯
- 关注主题：AI / LLM、软件工程、开源工具、重要安全事件、开发者产品更新
- 排除内容：泛科技融资、营销软文、入门教程
- 信息源：Reddit、X、Hacker News、精选 RSS、指定 GitHub 仓库的 Release

## 模型与外部服务

- 使用 DeepSeek 完成评分、筛选、去重后的摘要和背景说明
- 使用 Apify 获取 X 内容
- X 默认不抓取回复正文，并限制每次获取数量
- Reddit 使用 Horizon 内置的无 API Key 抓取方式

## 页面

- 首页展示最新一期简报
- 历史简报按日期永久保留
- 页面提供历史归档入口
- 仓库、信息源配置和简报公开
- API Key 与 Token 仅存放在 GitHub Actions Secret

## CI

向 `main` 推送或提交 Pull Request 时执行：

1. 按锁文件安装依赖
2. 运行单元测试
3. 校验资讯配置
4. 校验工作流 YAML

CI 不调用 DeepSeek、Apify 或其他付费服务。

## CD

- 每天北京时间 06:35 自动运行
- 支持手动触发
- 获取最近 24 小时的候选资讯
- 完成评分、去重、主题平衡和摘要后，最多发布 20 条入选资讯
- 全部生成步骤完成后才部署到 GitHub Pages
- 生成或部署失败时保留上一期正常页面

## 上游同步

不自动合并上游改动，避免自动更新破坏个人配置。需要升级 Horizon 时，单独检查上游差异后再合并。

## 所需 Secret

- `DEEPSEEK_API_KEY`
- `APIFY_TOKEN`

Secret 不写入代码、配置文件、Actions 日志或文档。

## 验收标准

- `yushxzh/Horizon` 是 `Thysrael/Horizon` 的公开 Fork
- CI 在 `main` 上通过
- 每日任务和手动任务均可触发
- 首次手动任务生成不超过 20 条中文资讯
- `https://yushxzh.github.io/Horizon/` 可以访问
- 首页展示最新一期，归档页可访问历史简报
- 工作流失败时不会覆盖上一期正常页面
- 仓库和 Actions 日志中不存在明文 Secret
