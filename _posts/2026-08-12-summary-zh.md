---
layout: default
title: "Horizon Summary: 2026-08-12 (ZH)"
date: 2026-08-12
lang: zh
edition: personal
---

> 从 36 条内容中筛选出 10 条重要资讯。

---

1. [Mojo 1.0 正式发布：面向高性能 AI 的 Python 兼容语言](#item-1) ⭐️ 9.0/10
2. [英伟达发布 Nemotron 3.5 Lightning 模型与 NeMo Switchyard 路由库](#item-2) ⭐️ 8.0/10
3. [研究人员从专有 LLM API 中提取隐藏推理轨迹](#item-3) ⭐️ 8.0/10
4. [英伟达在 AI 算力需求上的高风险赌注与软件壁垒](#item-4) ⭐️ 8.0/10
5. [透过 MitM 代理剖析 GitHub Copilot 的内部机制](#item-5) ⭐️ 8.0/10
6. [法国将从 8 月 11 日起禁止主动推销电话](#item-6) ⭐️ 8.0/10
7. [H3-metal：Apple Silicon 上的原生 MiniMax-H3 推理实现](#item-7) ⭐️ 8.0/10
8. [OpenAI 开始在 ChatGPT 中测试广告以支持免费服务](#item-8) ⭐️ 8.0/10
9. [Meta 发布开源 30B 模型 Muse Glimmer，专注智能体任务](#item-9) ⭐️ 8.0/10
10. [军人不信任 AI 军事决策，可解释 AI 能改善](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Mojo 1.0 正式发布：面向高性能 AI 的 Python 兼容语言](https://www.modular.com/blog/modular-26-5-mojo-1-0-is-here) ⭐️ 9.0/10

**原标题**: [Mojo 1.0](https://www.modular.com/blog/modular-26-5-mojo-1-0-is-here)

Modular 正式发布了 Mojo 1.0，这标志着该语言在提供面向高性能 AI/ML 和系统编程的 Python 兼容语言方面迈出了重要里程碑。该版本为开发者提供了一种兼具 Python 易用性与底层控制能力的统一语言。 Mojo 有潜力在 AI/ML 开发中挑战 CUDA，因为它提供了一种更高级、更友好的 Python 替代方案，同时仍能达到类 C 的性能。如果它在生态系统中获得牵引力，可能降低 AI 开发者的门槛，并拓宽 GPU 及其他加速器编程的普及范围。 Mojo 是一种面向 Linux 和 macOS 的专有语言，其语义受 Rust 启发，如静态类型和借用检查器，但语法类似 Python。其长期路线图原本包括成为 Python 的超集，但最近的文档指出 Mojo 可能不会发展成完整的超集。

hackernews · dayanruben · 8月11日 16:56 · [社区讨论](https://news.ycombinator.com/item?id=49261128)

**背景**: Mojo 由 Modular 创建，旨在通过将元编程和系统编程特性与 Python 生态系统相结合，弥合研究到生产之间的鸿沟。它面向整个计算栈，从数据中心到边缘设备，从 CPU 到 NPU，力求成为编写现代系统所有层的单一语言。该语言常被拿来与 CUDA 比较，因为它为 AI 加速器编写高性能代码提供了一种更平易近人的方式。该语言仍在开发中，其编译器仍为闭源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_%28programming_language%29">Mojo (programming language) - Wikipedia</a></li>
<li><a href="https://refine.dev/blog/mojo-programming-language/">Mojo - A New Programming Language for AI | Refine</a></li>
<li><a href="https://mojolang.org/">Mojo</a></li>

</ul>
</details>

**社区讨论**: 讨论中意见不一：一些评论者欢迎 Mojo 作为 CUDA 的潜在替代品，并希望其生态系统成熟，而另一些评论者则对闭源编译器持怀疑态度，并质疑该语言相对于现有使用 Rust 后端高性能的 Python 库的价值。还有人困惑于该语言的范围，并担心“Python 超集”的目标已被淡化。总体情绪是谨慎乐观，同时存在明显保留意见。

**标签**: `#Mojo`, `#programming languages`, `#AI/ML`, `#CUDA`, `#systems programming`

---

<a id="item-2"></a>
## [英伟达发布 Nemotron 3.5 Lightning 模型与 NeMo Switchyard 路由库](https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/) ⭐️ 8.0/10

**原标题**: [Nvidia Nemotron 3.5 Lightning and NeMo Switchyard](https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/)

英伟达发布了 Nemotron 3.5 Lightning 系列，主打一个 300 亿参数的开源混合专家（MoE）模型，其中仅 30 亿参数被激活；同时还推出了 NeMo Switchyard——一个用于 LLM 流量路由的开源 Rust 代理与库。该公告称，Switchyard 可以把每个请求智能地分发到最合适、最有能力的模型，而无需重写现有智能体（agent）堆栈。 这一发布意义重大，因为它直击 LLM 生产部署中两大痛点：成本与延迟。NeMo Switchyard 为开发者提供了一个标准化的开源工具，可按能力、成本和延迟在多个模型之间路由工作负载，进一步推动了行业向小而高效的模型以及多模型智能体系统发展的趋势。 旗舰版 Nemotron 3.5 Lightning 是一个 300 亿参数、30 亿激活参数的 MoE 模型，针对常驻智能体的高吞吐、低延迟执行做了优化；英伟达还发布了 NVFP4 和 BF16 检查点，并在 NeMo Gym 中公开了评估配方。Switchyard 用 Rust 构建，提供了无需调优和可调优两类路由器，但社区评论者指出，路由会带来提示缓存（prompt caching）和会话粘性（session stickiness）等方面的疑问。

hackernews · droidjj · 8月11日 19:35 · [社区讨论](https://news.ycombinator.com/item?id=49263340)

**背景**: LLM 模型路由是指在应用程序与模型提供商之间增加一个层，把每个请求发送给能处理它、且成本最低或最合适的模型。像 Nemotron 3.5 Lightning 这类混合专家（MoE）模型，每个 token 只激活参数中的一小部分，从而在保持大知识容量的同时降低计算成本。英伟达将 Nemotron 3.5 Lightning 定位为长时运行智能体工作负载的执行引擎，而 Switchyard 则是把该模型接入更大模型体系的路由层。这两者共同回应了 AI 应用中对成本与质量优化的日益增长的需求，而不是让每次调用都盲目支付前沿模型的高价。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/">NVIDIA Nemotron 3 . 5 Lightning Delivers Fast, Accurate Specialized...</a></li>
<li><a href="https://github.com/NVIDIA-NeMo/Switchyard">GitHub - NVIDIA-NeMo/Switchyard · GitHub</a></li>
<li><a href="https://developer.nvidia.com/blog/route-ai-agent-workloads-across-models-with-nvidia-nemo-switchyard/">Route AI Agents Across Models with NVIDIA NeMo Switchyard | NVIDIA Technical Blog</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍对小而高效模型的浪潮表示肯定；有人指出多万亿参数模型从根本上缺少一些东西，而更小、更高效的模型将推动结构性进化；还有人称赞 Nemotron 30B 可以通过 MLX 在 Apple Silicon 上运行。另一些评论则提出实际问题：路由如何处理提示缓存、会话是否应该保持粘性；还有评论者批评英伟达在基准图表中刻意遗漏了 Qwen 系列（只保留 Max 变体）。一条轻松的评论建议人类采用极简写作风格，以应对 AI 海量信息带来的冲击。

**标签**: `#AI`, `#Nvidia`, `#LLM`, `#Model Routing`, `#Open Source`

---

<a id="item-3"></a>
## [研究人员从专有 LLM API 中提取隐藏推理轨迹](https://stolen-thoughts.com/) ⭐️ 8.0/10

**原标题**: [Stealing Reasoning Traces from Proprietary LLM APIs](https://stolen-thoughts.com/)

研究人员证明，通过将模型输出重放到一个较弱的、已被越狱的模型中，可以从专有 LLM API 中提取隐藏的推理轨迹。该攻击绕过了前沿 API 提供商用来向用户隐藏思维链推理的安全过滤机制。 这一点很重要，因为主要 LLM 提供商将思维链推理视为专有资产和潜在的安全风险。一种实用的提取方法可能会削弱竞争优势、暴露敏感信息，并迫使提供商重新思考如何保护隐藏推理。 该技术利用了推理轨迹跨模型的可移植性：由前沿模型生成的轨迹可以被重放到一个更容易越狱的较小兄弟模型中，使其泄露隐藏的思维链。作者还指出，API 摘要并不总能保留模型在推导之前先陈述答案这一区别，这会使推理看起来比实际更干净。

hackernews · quantumgarbage · 8月11日 13:22 · [社区讨论](https://news.ycombinator.com/item?id=49257876)

**背景**: 推理轨迹，通常称为思维链（CoT），是 LLM 在生成最终答案之前产生的中间逐步 token，已被证明可以增强复杂任务的表现。许多专有 API 提供商故意隐藏这些轨迹，以防止知识蒸馏，并避免暴露可能有风险的内部推理。越狱是一种攻击技术，通过操纵模型绕过其安全限制，生成被禁止或意外的输出。这项研究将两个概念相结合：由于轨迹可以跨模型移植，攻击者可以将它们重放到一个更容易越狱的较弱模型中，迫使它揭示推理过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2504.09762v1">(How) Do Reasoning Models Reason ?</a></li>
<li><a href="https://research.google/blog/thinking-to-recall-how-reasoning-unlocks-parametric-knowledge-in-llms/">Thinking to recall: How reasoning unlocks parametric knowledge in...</a></li>
<li><a href="https://snyk.io/articles/what-is-ai-jailbreaking-strategies-to-mitigate-llm-jailbreaking/">What is AI jailbreaking? Strategies to Mitigate LLM Jailbreaking | Snyk</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者的反应不一。一些人质疑“窃取”这一说法，认为用户已经为 token 付费，而且用模型输出进行训练应该是寻常事；另一些人则分享了替代方法，比如禁用思考功能并使用“deep\_think”工具来暴露思维链。还有评论者指出，这些结果证实了前沿模型在 AIME 等基准问题上被大量训练。

**标签**: `#llm`, `#security`, `#ai`, `#privacy`, `#api`

---

<a id="item-4"></a>
## [英伟达在 AI 算力需求上的高风险赌注与软件壁垒](https://stratechery.com/2026/nvidias-risky-business/) ⭐️ 8.0/10

**原标题**: [Nvidia&\#x27;s Risky Business](https://stratechery.com/2026/nvidias-risky-business/)

Stratechery 的一篇分析文章审视了英伟达在 AI 算力需求持续增长上的战略赌注，并指出其 CUDA 软件壁垒和硬件主导地位存在的弱点。文章认为，虽然算力需求真实存在，但增长预期可能被夸大。 这很重要，因为英伟达的市值和整个 AI 行业都取决于算力需求能否持续增长。该分析质疑了英伟达软件壁垒的持久性，并对投资论点中的二阶假设提出了担忧。 文章讨论了英伟达 CUDA 软件生态系统既是优势也是弱点，社区评论指出其开发者体验不佳。文章还考虑了英伟达在机器人领域的布局，以及其在西方与中国竞争中的位置。

hackernews · jonbaer · 8月11日 10:02 · [社区讨论](https://news.ycombinator.com/item?id=49255710)

**背景**: CUDA 是英伟达专有的并行计算平台和 API，允许软件使用 GPU 进行通用处理，这使得英伟达深度融入机器学习研究。英伟达的 Tensor Core 是专为 AI 工作负载设计的硬件，而 NVLink 是一种高带宽的 GPU 间互连技术，用于扩展多 GPU 系统。这些技术支撑了英伟达在 AI 基础设施领域的主导地位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nvidia_CUDA">Nvidia CUDA</a></li>
<li><a href="https://en.wikipedia.org/wiki/NVLink">NVLink - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/nvlink/">NVLink &amp; NVLink Switch: Fastest HPC Data Center Platform | NVIDIA</a></li>

</ul>
</details>

**社区讨论**: 社区评论对英伟达的软件壁垒进行了辩论，有人认为 CUDA 在机器学习研究中的根深蒂固是其最大优势，而其开发者体验却极差。另一些人质疑算力需求增长的可持续性，指出关于需求增长的二阶假设可能被夸大。还有人提到英伟达在机器人领域的扩张，以及其在西方相对中国的强势地位。

**标签**: `#Nvidia`, `#AI`, `#semiconductors`, `#investment analysis`, `#machine learning infrastructure`

---

<a id="item-5"></a>
## [透过 MitM 代理剖析 GitHub Copilot 的内部机制](https://www.lighthousenewsletter.com/p/i-put-github-copilot-behind-a-mitm) ⭐️ 8.0/10

**原标题**: [What I learned by putting GitHub Copilot behind a MitM proxy](https://www.lighthousenewsletter.com/p/i-put-github-copilot-behind-a-mitm)

在一篇新的技术深入分析中，作者将 GitHub Copilot 置于中间人代理之后，观察到它如何发现并路由模型、如何从当前文件及近期编辑的文件中组装上下文，以及如何消耗高级请求配额。 GitHub Copilot 是一个闭源服务，因此这种黑盒检查让开发者难得地看到其代码和遥测数据是如何被使用的。理解上下文组装和配额机制，有助于用户避免意外的高级模型费用，并与开源替代方案进行更合理的比较。 作者观察到，Copilot 在每次渲染时都会从头重建整个提示词，而不是增量修改消息；并且最近的编辑可能会把当前编辑文件之外的内容拉入上下文。还有评论者指出，Copilot 默认没有排除 .env 等环境文件的规则，因此这些文件的内容可能被发送给模型。

hackernews · j0selit0 · 8月11日 10:40 · [社区讨论](https://news.ycombinator.com/item?id=49256057)

**背景**: 中间人（MitM）代理位于客户端和服务器之间，只要客户端信任代理签发的 CA 证书，它就能解密 HTTPS 流量，从而查看明文请求和响应。GitHub Copilot 是一个 AI 编程助手，它会利用当前文件、近期编辑以及其他上下文来生成建议，其高级模型按请求计费，受请求配额限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.blog.brightcoding.dev/2025/09/26/intercept-and-inspect-http-https-and-websocket-traffic-with-mitmproxy">Intercept and Inspect HTTP, HTTPS , and WebSocket... - BrightCoding</a></li>
<li><a href="https://medium.com/@toni3095/context-window-management-in-claude-code-and-github-copilot-0d108b9f0a81">Context Window Management in Claude Code and GitHub Copilot</a></li>
<li><a href="https://sessionwatcher.com/guides/copilot-rate-limits-explained">GitHub Copilot Rate Limits Explained – Premium Quota , Multipliers...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍称赞这篇深入分析。p1llus 建议使用 eBPF 在加密前/解密后直接获取明文数据，以规避证书固定和 mTLS 的问题；ameliaquining 指出 Codex 客户端是开源的，对文章做了事实修正。\_davide\_ 不认同关于精心整理上下文的结论，认为高端 LLM 即使没有它也能表现得差不多；tolugenius 则惊讶于默认没有排除 .env 文件。

**标签**: `#GitHub Copilot`, `#AI-assisted development`, `#reverse engineering`, `#network analysis`, `#LLM tooling`

---

<a id="item-6"></a>
## [法国将从 8 月 11 日起禁止主动推销电话](https://www.lemonde.fr/en/france/article/2026/08/06/france-to-ban-unsolicited-telemarketing-calls-from-august-11_6756208_7.html) ⭐️ 8.0/10

**原标题**: [France to ban unsolicited telemarketing calls](https://www.lemonde.fr/en/france/article/2026/08/06/france-to-ban-unsolicited-telemarketing-calls-from-august-11_6756208_7.html)

法国宣布将从 2026 年 8 月 11 日起禁止未经请求的主动推销电话。这项禁令标志着针对侵扰性冷呼叫迈出了重要的监管一步。 这项规定对电信消费者和电话营销行业意义重大，可能在欧洲乃至全球树立更强硬打击骚扰电话的先例。同时，它也提出了运营商如何在屏蔽骚扰电话的同时不误伤正规电话的技术难题。 该禁令从 8 月 11 日起适用于未经请求的电话，但具体执行机制尚未完全公开。评论者指出，如果没有严格的来电身份验证（如 STIR/SHAKEN 的 A 级认证），执行该禁令在技术上可能困难重重。

hackernews · aziaziazi · 8月11日 08:15 · [社区讨论](https://news.ycombinator.com/item?id=49254880)

**背景**: 推销电话长期以来一直是烦扰，许多消费者因此拒接未知号码。在美国，来电显示伪造和数据经纪商出售电话号码使得问题更加严重，评论者认为这是根本原因。法国的禁令是欧洲保护消费者免受未经请求的商业通信侵扰的更广泛监管行动的一部分。

**社区讨论**: Hacker News 评论者大多支持这项禁令，有人称其为‘一个好主意’，并提到美国每天涌来的诈骗电话。然而，也有人质疑禁令在技术上如何执行，提出国家级白名单或强制推行 STIR/SHAKEN 全 A 级认证等解决方案。还有评论认为更根本的问题是企业广泛共享和出售个人电话号码。

**标签**: `#telemarketing`, `#regulation`, `#spam`, `#caller-id`, `#policy`

---

<a id="item-7"></a>
## [H3-metal：Apple Silicon 上的原生 MiniMax-H3 推理实现](https://github.com/antirez/h3.c) ⭐️ 8.0/10

**原标题**: [H3-metal – Native MiniMax-H3 inference for Apple Silicon](https://github.com/antirez/h3.c)

Antirez 发布了 h3.c，这是一个在 Apple Silicon 上原生使用 Metal 运行 MiniMax-H3 视频生成的实现。该项目使 Mac 用户无需依赖外部服务，即可在本地推理 MiniMax-H3（一个可生成最多 15 秒、2K 分辨率并带音频视频的开源全模态模型）。 这为 Apple Silicon 用户提供了一条实用的开源路径，可以在本地运行先进的开放权重视频生成模型，满足了日益增长的设备端生成式媒体需求。同时，它也反映了通过 Metal 将先进扩散模型带到 Mac 硬件上的大趋势。 该实现据称支持量化，并可配合常见的 ComfyUI 工作流使用 GGUF 量化版本（例如 Q5\_K\_M 和 Q8\_0）。生成速度仍是瓶颈——社区报告显示，生成一段约 9 秒、480x864 分辨率、20 步的片段大约需要一小时，而且内存需求较高，建议约 128 GB 才能流畅使用。

hackernews · swyx · 8月11日 01:22 · [社区讨论](https://news.ycombinator.com/item?id=49252179)

**背景**: MiniMax-H3 是 MiniMax 发布的开源权重“全模态”生成模型，将文本、图像、视频和音频的理解与生成统一在一个模型里；它可以在单个模型中合成最长 15 秒、2K/24fps 并带原生立体声的视频。Apple 的 Metal 是 Apple Silicon 上的低开销 GPU 框架，用于加速推理。h3.c 是 antirez（Salvatore Sanfilippo）发起的社区项目，目的是让该模型直接、原生地在 Mac 上运行，而不是依赖 Rosetta 等转译层。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.minimax.io/blog/minimax-h3">MiniMax H 3 : An Open Model Breaking the Boundaries Between Tasks...</a></li>
<li><a href="https://hailuoaiminimax.com/minimax-h3.html">MiniMax H 3 : Open-Weight Omni-Modal Video Model &amp; ComfyUI Setup</a></li>
<li><a href="https://developer.apple.com/metal/">Metal Overview - Apple Developer</a></li>

</ul>
</details>

**社区讨论**: 社区反馈总体积极，但也突出了实际限制：M5 Pro 和 M4 Max 用户报告生成 9 秒片段约需一小时，生成 15 秒 480p 视频则需要一个半小时。有用户询问是否必须要有 128 GB 内存，而 antirez 提到 MiniMax 在 AMA 中透露 H3 可能支持稀疏注意力，这将带来巨大加速，并表示正在测试 --sparse-attention 可选模式。

**标签**: `#Apple Silicon`, `#MiniMax-H3`, `#Video Generation`, `#Metal inference`, `#Open Source`

---

<a id="item-8"></a>
## [OpenAI 开始在 ChatGPT 中测试广告以支持免费服务](https://openai.com/index/testing-ads-in-chatgpt) ⭐️ 8.0/10

**原标题**: [Testing ads in ChatGPT](https://openai.com/index/testing-ads-in-chatgpt)

OpenAI 已开始在 ChatGPT 中测试广告，以帮助维持免费服务。官方表示，这次测试会清晰标识广告、保持回答的独立性、加强隐私保护，并让用户拥有控制权。 ChatGPT 是使用最广泛的 AI 助手之一，引入广告可能改变用户体验和用户信任。此举也标志着 AI 产品在商业化方面出现新趋势，并引发关于如何在免费服务与可持续收入之间取得平衡的重要讨论。 OpenAI 尚未透露哪些用户会看到测试广告，也没有公布更广泛上线的时间。该公司表示，广告将被明确标记，不会影响模型答案，同时数据保护和用户控制仍是测试过程中的核心。

rss · OpenAI News · 8月11日 10:00

**背景**: ChatGPT 是 OpenAI 推出的对话式 AI 助手，提供免费和付费版本。运行大型 AI 模型的成本很高，因此免费服务需要找到可持续的收入来源；广告是互联网常见的变现方式，但把广告嵌入对话式 AI 界面会引发关于用户信任和使用体验的新担忧。

**标签**: `#OpenAI`, `#ChatGPT`, `#Advertising`, `#Monetization`, `#Privacy`

---

<a id="item-9"></a>
## [Meta 发布开源 30B 模型 Muse Glimmer，专注智能体任务](https://simonwillison.net/2026/Aug/10/introducing-muse-glimmer/#atom-everything) ⭐️ 8.0/10

**原标题**: [Introducing Muse Glimmer](https://simonwillison.net/2026/Aug/10/introducing-muse-glimmer/#atom-everything)

Meta 于 2026 年 8 月发布了 Muse Glimmer，这是一个 300 亿参数的开源权重模型，采用宽松的 Apache 2.0 许可证。它专门针对端到端智能体任务完成、可靠工具使用和多步推理进行了优化。 这件事意义重大，因为 Meta 以宽松许可证重返开源权重模型领域，不再使用过去限制较多的 Llama 许可证。一个能在本地运行、具备较强能力的 30B 智能体模型，可能使开发者、爱好者以及整个开源模型生态受益。 Muse Glimmer 是一个视觉模型，Simon Willison 在配备 128 GB 内存的机器上通过 LM Studio 测试了 18.16 GB 的量化版本。Meta 声称该模型在 DeepSearch QA、MCP-Atlas、tau-Bench 和 SWE-Bench 等基准上表现良好，但独立的评测仍然有限。

rss · Simon Willison · 8月10日 23:56

**背景**: 智能体模型（agentic model）旨在通过调用工具、编写代码以及在长时间任务中调整计划来负责任务拆解和完成。MCP-Atlas 等基准通过真实 Model Context Protocol \(MCP\) 服务器评估模型的工具使用能力，而 tau-Bench 则衡量真实世界领域中工具、智能体与用户之间的交互。Agentic scaffolds（智能体脚手架）为自主智能体在这些工作流中的行为提供结构化框架。Apache 2.0 是一种宽松的开源许可证，允许商业使用、修改和再分发，且限制较少。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://llm-stats.com/benchmarks/mcp-atlas">MCP Atlas Leaderboard</a></li>
<li><a href="https://taubench.com/">τ- bench — Benchmarking AI Agents on Real-World Tasks</a></li>
<li><a href="https://www.emergentmind.com/topics/agentic-scaffolds">Agentic Scaffolds in Autonomous Systems</a></li>

</ul>
</details>

**标签**: `#AI`, `#Meta`, `#open-weights`, `#agentic`, `#model release`

---

<a id="item-10"></a>
## [军人不信任 AI 军事决策，可解释 AI 能改善](https://www.schneier.com/blog/archives/2026/08/ai-for-military-support.html) ⭐️ 8.0/10

**原标题**: [AI for Military Support](https://www.schneier.com/blog/archives/2026/08/ai-for-military-support.html)

一项同行评审的实证研究《黑箱战争：AI 时代的人类判断与军事决策》使用高保真复刻的真实军用 AI 决策支持系统，对 2,015 名以色列军人进行了测试。研究发现，军人对 AI 目标选择建议存在明显的算法厌恶，尤其在可能造成高附带损伤的情况下；而加入可解释 AI 功能后，这种厌恶有所降低，决策评估也更审慎。 这一发现挑战了军事人机交互中“自动化偏见”将大行其道的普遍担忧，表明对军事 AI 的信任是动态的、依情境而变化的。这对高利害目标选择场景中 AI 的整合方式具有重要意义，并凸显了人类判断在战争中的持续关键作用。 该研究重建了真实军用目标选择 AI 决策支持系统的界面与功能，并开展了两项涉及战斗决策的实验。在高附带损伤情境下，算法厌恶更为强烈；而可解释 AI 功能促使被试者更深入地思考算法建议，信任程度还随个人倾向和感知行动风险而变化。

rss · Schneier on Security · 8月11日 11:18

**背景**: 算法厌恶（algorithm aversion）指人们即使知道算法通常比人类判断更准确，仍然倾向于不信任或拒绝其建议的心理倾向；自动化偏见（automation bias）则相反，指人类过度依赖自动化系统输出的倾向。可解释人工智能（XAI）旨在让 AI 的决策对用户透明可理解，美国 DARPA 于 2016 年启动大型 XAI 项目，部分就是为了应对军事 AI 的“黑箱”问题。该研究正是在军用 AI 可解释性争论日益激烈的背景下开展的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Algorithm_aversion">Algorithm aversion - Wikipedia</a></li>
<li><a href="https://thedecisionlab.com/reference-guide/psychology/algorithm-aversion">Algorithm Aversion - The Decision Lab</a></li>
<li><a href="https://link.springer.com/article/10.1007/s10676-024-09762-w">Explainable AI in the military domain | Ethics and Information Technology | Springer Nature Link</a></li>

</ul>
</details>

**标签**: `#AI`, `#military`, `#decision-making`, `#algorithmic aversion`, `#explainable AI`

---