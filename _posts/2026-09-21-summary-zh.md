---
layout: default
title: "Horizon Summary: 2026-09-21 (ZH)"
date: 2026-09-21
lang: zh
edition: personal
---

> 从 26 条内容中筛选出 2 条重要资讯。

---

1. [借助 Claude 将 CADO-NFS 移植到 GPU，RSA-896 被成功分解](#item-1) ⭐️ 9.0/10
2. [Qwen Image 2.1：7B 开源权重文生图模型，原生支持透明通道](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [借助 Claude 将 CADO-NFS 移植到 GPU，RSA-896 被成功分解](https://saweis.net/posts/rsa-896.html) ⭐️ 9.0/10

**原标题**: [RSA-896](https://saweis.net/posts/rsa-896.html)

Anthropic 工程师 Steve Weis 报告称，已成功分解 896 位（约 270 位十进制数字）的 RSA 挑战数 RSA-896，计算于 2026 年 9 月 19 日完成。他让 Claude 将 CADO-NFS 因数分解软件移植到 GPU 上运行，随后调度最多 2048 块 GPU、利用从各处搜集来的空闲算力，在约 10 天内完成，共消耗约 30 GPU 年。 这是一个引人注目的计算里程碑：RSA-896 从“尚未分解”的 RSA 挑战数名单中被划掉，同时表明“AI 辅助代码移植 + 大规模调度闲置 GPU 算力”这一模式，可以攻克过去只有专用高性能计算力量才能处理的问题。它也加剧了长期以来关于 RSA 分解实际难度衰减速度的争论——不过 896 位模数远低于现实部署中普遍使用的 2048 位密钥。 这次计算使用的是已经付费、原本闲置的算力，而非专用硬件；Claude 在给出的声明中还特别强调，功劳首先属于几十年来构建数域筛法与 CADO-NFS 的人，以及此前创下分解纪录的团队。RSA-896 是 RSA 实验室自 1991 年起公布的一系列 RSA 分解挑战数之一；分解它并不意味着生产环境中使用的 RSA 密钥（通常为 2048 或 4096 位）面临风险。

hackernews · madars · 9月20日 02:19 · [社区讨论](https://news.ycombinator.com/item?id=49771966)

**背景**: 通用数域筛法（GNFS）是已知对大于约 10^100 的整数进行因数分解最有效的经典算法，而 CADO-NFS 是由 INRIA 等机构研究者开发的开源 C/C++ 实现。RSA 实验室于 1991 年发起的 RSA 分解挑战，给出了一组基准合数，使研究界能够衡量因数分解的“实际不可行边界”究竟在哪里。RSA-896 是一个 896 位的挑战数，约合 270 位十进制数字，规模超过此前的 RSA-768、RSA-704 等纪录。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Number_field_sieve">Number field sieve</a></li>
<li><a href="https://github.com/cado-nfs/cado-nfs">GitHub - cado - nfs / cado - nfs : Cado - NFS , An Implementation of the...</a></li>
<li><a href="https://en.wikipedia.org/wiki/RSA_Factoring_Challenge">RSA Factoring Challenge - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者看法分歧：有人认为由于闲置 GPU 算力本已付费并预留，这次运行实际上几乎免费（尽管拿去挖矿会更有利可图）；也有人对 Anthropic 持看空态度，认为用 2048 块 GPU 跑 10 天去分解一个已知算法就能解决的问题并不值得；还有人指出，数据中心的多余算力被用于解数学题而不是训练大模型，本身就是一种信号。另一些人则提到 768 位 RSA 仍在使用中——据说 Instagram 至今仍发布 768 位 RSA 的 DKIM 密钥——并调侃说如今分解它大概只是一个“周末 GPU 小项目”。

**标签**: `#cryptography`, `#RSA`, `#GPU computing`, `#AI-assisted development`, `#number field sieve`

---

<a id="item-2"></a>
## [Qwen Image 2.1：7B 开源权重文生图模型，原生支持透明通道](https://qwen.ai/blog?id=qwen-image-2.1) ⭐️ 8.0/10

**原标题**: [Qwen Image 2.1](https://qwen.ai/blog?id=qwen-image-2.1)

Qwen 发布了 Qwen Image 2.1，这是一个仅有 7B 参数的开源权重文生图模型，相比前代 20B 的 Qwen-Image 1 大幅瘦身，同时新增了原生透明通道支持，并显著提升了文字渲染能力。该发布在社区引发高度关注——获得 474 个赞和约 150 条评论，其中大量讨论集中在该模型相比此前采用 Apache 许可的 Qwen 模型更为严格的授权条款上。 凭借 7B 的参数量，Qwen Image 2.1 跻身体积最小的实用级开源权重图像模型之列，使得在消费级硬件上进行高质量本地图像生成成为可能；而其原生的 alpha 通道输出和改进的文字排版能力，正切中大多数竞品仍处理不佳的实际设计与 UI 工作流。不过更严格的许可证也折射出开源权重生态中「宽松分发」与「厂商控制」之间日益凸显的矛盾。 据社区反馈，Qwen Image 2.1 比 20B 的 Qwen-Image 1 更小，在体积上主要仅大于 6B 的 Z-Image Turbo；一位从事 prompt-to-UI 设计站点开发的评论者表示，其文字渲染能力明显优于目前在售的任何开源权重模型，尤其是在小字号文本上。但问题在于授权：与许多此前以 Apache 许可证发布的 Qwen 模型不同，该模型采用了严格得多的许可证，多位评论者将此视为一大缺陷。

hackernews · jmillikin · 9月20日 13:09 · [社区讨论](https://news.ycombinator.com/item?id=49775499)

**背景**: 开源权重模型会公开训练好的权重文件供任何人下载和运行，但真正决定开发者可以合法做什么的是随附的许可证，而非权重本身是否可得——这正是宽松许可与严格许可之争在本地 AI 社区如此激烈的原因。文生图扩散模型长期以来难以在生成图像中渲染出准确、连贯的文字，TextDiffuser 等研究正是针对这一问题。生成模型中的「原生透明」指的是模型直接输出包含逐像素不透明度信息的 alpha 通道（PNG 和 WebP 都支持该通道），而无需额外的抠图后处理步骤；目前包括 Midjourney 和 Flux 在内的多数主流生成器都无法原生生成透明背景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai-tldr.dev/learn/local-open-models/open-model-ecosystem/open-weights-vs-open-source/">Open Weights vs Open Source: What&#x27;s the Difference? | AI/TLDR</a></li>
<li><a href="https://transparify.app/blog/ai-image-generators-transparent-background">Which AI Image Generators Support Transparent PNGs? (2026) | Transparify</a></li>
<li><a href="https://arxiv.org/abs/2305.10855">[2305.10855] TextDiffuser: Diffusion Models as Text Painters TextDiffuser-RL: Efficient and Robust Text Layout ... TextDiffuser: Diffusion Models as Text Painters - microsoft.com TextDiffuser: Diffusion Models as Text Painters - NeurIPS Paper page - TextDiffuser: Diffusion Models as Text Painters Recommendations of Diffusion for Text-Image - GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区整体对模型能力评价积极，但对许可证态度分化：评论者称赞其缩减到 7B 的体积、原生透明支持（有人指出 Qwen 似乎是唯一认真攻克这一点的团队）以及开源权重市场中最顶尖的文字渲染效果。主要争议点是许可证，有评论者将其与此前采用 Apache 许可的 Qwen 模型作对比；也有人认为本地图像生成目前已明显领先于本地代码生成，并询问如何以类似服务端的方式在本地运行该模型。

**标签**: `#AI image generation`, `#Qwen`, `#open-weight models`, `#text rendering`, `#model licensing`

---