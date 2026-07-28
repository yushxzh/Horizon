---
layout: default
title: 每日资讯简报
---

# 每日资讯简报

本页面每天汇总最近 24 小时内值得关注的 AI / LLM、软件工程、开源工具、安全和开发者产品动态。内容来自 Reddit、X、Hacker News、RSS 与 GitHub Release，每期最多保留 20 条。

{% assign zh_posts = site.posts | where: "lang", "zh" %}
{% assign latest_zh = zh_posts | first %}

{% if latest_zh %}

## 最新一期

<p><a href="{{ latest_zh.url | relative_url }}">{{ latest_zh.date | date: "%Y-%m-%d" }} 完整页面</a></p>

{{ latest_zh.content }}

{% else %}

## 最新一期

首次简报尚未生成。

{% endif %}

## 历史归档

<ul>
  {% for post in zh_posts %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.date | date: "%Y-%m-%d" }}</a>
    </li>
  {% else %}
    <li><em>暂无历史简报</em></li>
  {% endfor %}
</ul>

## 信息源与配置

- [Horizon Fork](https://github.com/yushxzh/Horizon)
- [中文 RSS]({{ '/feed-zh.xml' | relative_url }})
- [配置说明]({{ '/configuration' | relative_url }})
