---
layout: default
title: "Horizon Summary: 2026-09-11 (ZH)"
date: 2026-09-11
lang: zh
edition: personal
---

> 从 41 条内容中筛选出 10 条重要资讯。

---

1. [OpenAI 的 Navier-Stokes 反例附带 Lean 4 形式化证明](#item-1) ⭐️ 9.0/10
2. [DeepSeek 发布 V4.1 Flash，缓存命中价格极具攻击性](#item-2) ⭐️ 9.0/10
3. [Shopify 放弃 React Native，回归原生 Swift 与 Kotlin](#item-3) ⭐️ 8.0/10
4. [研究者还能信任 OpenAI 处理未发表的数学工作吗？](#item-4) ⭐️ 8.0/10
5. [OpenAI 推出托管式 Agents API，支持可选的自托管沙箱](#item-5) ⭐️ 8.0/10
6. [Forgejo 16.0.4 修复严重的模板扩展远程代码执行漏洞](#item-6) ⭐️ 8.0/10
7. [微软将 Rust 列为一级（Tier-1）语言](#item-7) ⭐️ 8.0/10
8. [trynix.dev 让任意 Nix 包在浏览器虚拟机中启动](#item-8) ⭐️ 8.0/10
9. [Calif Research 演示 WeWorm：用 AI 打造的微信零点击蠕虫](#item-9) ⭐️ 8.0/10
10. [AI 智能体仅凭漏洞传闻就能找出可利用的漏洞](#item-10) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 的 Navier-Stokes 反例附带 Lean 4 形式化证明](https://www.johndcook.com/blog/2026/09/09/formal-method-revolution/) ⭐️ 9.0/10

**原标题**: [OpenAI’s Navier-Stokes release included a Lean 4 formal proof](https://www.johndcook.com/blog/2026/09/09/formal-method-revolution/)

2026 年 9 月 8 日，OpenAI 宣布给出了 Navier-Stokes 方程存在性与光滑性问题的一个无界反例，并且此次发布还附带了用 Lean 4 撰写的形式化证明。这意味着该论证在逻辑层面原则上可以由 Lean 的内核进行机器检验，而不仅仅依赖人类数学家阅读。 如果 AI 系统既能提出新的数学结果，又能交付可机器检验的证明，那么接受争议性结论的瓶颈就会从人工审稿转移到形式化验证，这可能改变数学主张的验证方式。同时这也带来归属与训练数据方面的尖锐问题，因为 Levent Alpöge 与 Tristan Buckmaster 的相关工作先于此次发布。 有评论提到，对于费马大定理量级的证明，Lean 验证约需 15 小时、230GB 内存，而智能体生成代码约需 11 天，并估算 OpenAI 的智能体集群成本约为 4000 万美元。关键在于，Lean 证明只能保证形式化陈述可由公理推出，并不能单凭自身确认该形式化是否忠实表达了原本想证明的数学命题；此外 OpenAI 的解尚未经过外部数学家验证。

hackernews · ibobev · 9月10日 21:22 · [社区讨论](https://news.ycombinator.com/item?id=49650326)

**背景**: Navier-Stokes 方程描述黏性流体的运动，在空气动力学、血流建模等众多领域都处于核心地位；而三维空间中光滑解是否始终存在的问题，是七大千禧年数学难题之一。Lean 4 是一种证明助手，也是依赖类型的函数式编程语言，其证明由一个小型可信内核检验，因此一旦检验通过，逻辑上的可信度极高。用 AI 生成这类形式化验证产物近来被称为&quot;vericoding&quot;（形式化编程），是形式化方法领域对应&quot;vibecoding&quot;的说法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_equations">Navier-Stokes equations</a></li>
<li><a href="https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_existence_and_smoothness">Navier–Stokes existence and smoothness - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_%28proof_assistant%29">Lean (proof assistant)</a></li>

</ul>
</details>

**社区讨论**: 评论者大多跳过结果本身，转而讨论 Lean 的性能与成本经济学：有人指出验证费马大定理约需 15 小时，而智能体生成代码约需 11 天，并追问在不牺牲可审计性的前提下 Lean 还能优化到什么程度。也有人反驳相关的表述方式——估算人类等效成本约为 1.32 亿美元，而智能体约为 4000 万美元，并认为&quot;每页四十小时&quot;这一经验法则反映的是 2005 年的证明自动化水平，而非今天的 Lean。还有评论提出了更深层的担忧：未来可能出现人类或可负担的工具都无法独立验证的 AI 证明。

**标签**: `#AI`, `#formal-verification`, `#Lean 4`, `#Navier-Stokes`, `#proof-assistants`

---

<a id="item-2"></a>
## [DeepSeek 发布 V4.1 Flash，缓存命中价格极具攻击性](https://twitter.com/deepseek_ai/status/2097930608790167907) ⭐️ 9.0/10

**原标题**: [DeepSeek v4.1 Flash](https://twitter.com/deepseek_ai/status/2097930608790167907)

DeepSeek 发布了 DeepSeek-V4.1-Flash，并在 Hugging Face 上同步公开了一份细节异常丰富的技术报告，其缓存命中（cache-hit）输入价格仅为每百万 token 0.003 美元。该模型据称规模达到 552B 参数，几乎是初代 V4 Flash（284B）的两倍。 由于 DeepSeek 的每次发布都曾多次重塑 AI 领域格局，其新的前沿级模型自然备受关注；而其近乎为零的缓存命中价格，可能让网络上下文传输而非 token 生成成为长时运行智能体任务中占主导地位的成本。这将改变开发者设计聊天补全 API 与长上下文智能体的方式。 DeepSeek 模型的缓存命中输入价格大约比缓存未命中便宜 50 倍，这意味着缓存设计对账单的影响甚至超过模型选择本身。社区指出的缺点是：552B 参数的 V4.1 Flash 对大多数本地部署场景已不再现实，而初代 284B 版本尚可接受。

hackernews · Liwink · 9月10日 06:11 · [社区讨论](https://news.ycombinator.com/item?id=49639090)

**背景**: DeepSeek 是一家中国 AI 实验室，其开源权重模型发布一向能达到甚至超过前沿规模。提示缓存（prompt caching）指服务商保存重复提示前缀的处理结果，使后续请求无需重新计算，这正是缓存命中 token 远便宜于未命中 token 的原因；对于在共享代码库上运行数百轮的长时间编程智能体会话，绝大多数输入 token 都可能是缓存命中。上下文传输则指在客户端与推理服务器之间通过网络搬运这些累积上下文的成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.layer3labs.io/guides/deepseek-pricing">DeepSeek Pricing 2026: API Rates, Free Tier &amp; Subscription</a></li>
<li><a href="https://arxiv.org/abs/2506.04645">[2506.04645] Inference economics of language models - arXiv.org The Hidden Economics of LLM Inference - hebbia.com Inference economics of language models | Epoch AI LLM Inference Economics – Production AI: An Engineering Guide More Tokens, Less Intelligence: The Hidden Economics of LLM ... LARGE LANGUAGE MODELS - economics.mit.edu</a></li>
<li><a href="https://www.hebbia.com/blog/the-hidden-economics-of-llm-inference">The Hidden Economics of LLM Inference - hebbia.com</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者称赞 DeepSeek 的技术报告充满工程细节，并将其与其他实验室偏重安全与“模型福祉”说明的系统卡作对比，同时赞赏该实验室敢于在接近前沿的规模上训练新颖的架构想法。讨论最热烈的是每百万 token 0.003 美元的缓存命中价格：有评论者认为，通过网络传输一百万 token 的成本可能很快就会超过一次缓存命中，从而使上下文传输成为任务总成本中的主导项。也有人指出，552B 参数的规模实际上已不再适合本地运行的“Flash”定位。

**标签**: `#AI/ML`, `#LLM`, `#DeepSeek`, `#model-release`, `#inference-cost`

---

<a id="item-3"></a>
## [Shopify 放弃 React Native，回归原生 Swift 与 Kotlin](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

**原标题**: [Shopify is moving from React Native back to Swift and Kotlin](https://shopify.engineering/back-to-native)

Shopify 在其工程博客上宣布，将把移动应用从 React Native 迁移回完全原生的 iOS 和 Android 代码库，分别使用 Swift 与 Kotlin 编写。这篇题为“回归原生”（Back to Native）的文章描述了该公司如何逆转多年来公开推崇的跨平台技术路线。 Shopify 曾是 React Native 最引人注目的企业级采用者和推广者之一，因此它的转向对整个行业的移动架构选型具有很强的信号意义。这一举动很可能加剧关于“共享代码库”与“平台专属原生开发”的长期争论，并可能促使其他大公司重新考虑跨平台技术栈。 这次迁移意味着把单一共享的 JavaScript/TypeScript 代码库改写为两套独立的平台原生代码库，通常被视为在“初期开发速度”与“性能、平台贴合度、以及更快接入新系统 API”之间的取舍。评论者指出，如今大语言模型正被用来加速这类重写工作，但 Shopify 全量迁移的规模意味着仍需要相当长的时间和工程投入。

hackernews · fnthawar2 · 9月10日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49643982)

**背景**: React Native 是 Meta 推出的开源 UI 框架，允许开发者用 JavaScript/React 编写移动应用，并通过原生平台组件进行渲染，其卖点是 iOS 和 Android 共用一套代码库。Swift 是苹果为 iOS/macOS 打造的编译型语言，Kotlin 则是 JetBrains 开发、被谷歌指定为 Android 首选开发语言的语言，其中 Kotlin Multiplatform 提供了跨平台共享业务逻辑的途径。Shopify 当年押注 React Native 曾是跨平台方案的知名案例，因此如今拆分回 Swift 与 Kotlin 两套原生应用是一次颇具标志性的逆转。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/React_Native">React Native</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kotlin">Kotlin</a></li>
<li><a href="https://en.wikipedia.org/wiki/Swift_%28programming_language%29">Swift (programming language) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（约 728 分、483 条评论）总体上对放弃 React Native 持认同态度，一位 iOS 工程师表示这一决定印证了他多年来反对“共享代码库”的立场。也有不少评论者质疑 Shopify 为何不选择 Kotlin Multiplatform，另一些人则反驳“是 LLM 才让迁移变得可行”的说法，指出他们早在 LLM 辅助出现之前就完成过类似的原生重写。一个普遍观点是：React Native 最初让 Web 开发者做移动端的吸引力，在大量代码由 AI 生成的今天已经减弱，而专门的原生工程师依然最能针对各平台做优化。

**标签**: `#React Native`, `#Shopify`, `#Mobile Development`, `#Swift`, `#Kotlin`

---

<a id="item-4"></a>
## [研究者还能信任 OpenAI 处理未发表的数学工作吗？](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

**原标题**: [More questions about whether researchers can trust OpenAI with unpublished math](https://mathstodon.xyz/@andreasthom/117240535270608201)

一个 Hacker News 讨论帖（617 分、607 条评论）围绕数学家是否还能放心把未发表的工作交给 OpenAI 展开，起因是 @andreasthom 在 Mathstodon 上就署名与数据使用提出质疑。讨论的核心说法是：OpenAI 获取了研究者的 Codex 提示词与聊天内容，向约十万名研究者提供了免费模型访问权限，随后在未给予署名的情况下公布了这些研究者正在攻关问题的进展。 这场争议触及支撑学术数学的署名与优先权规范，也关乎 AI 实验室究竟可被视为可信的合作者，还是会吸收他人想法的竞争者。如果研究者判定与 OpenAI 分享未发表成果可能丧失署名权，专家知识流入前沿模型的渠道就会收窄，整体上也会拖慢 AI 辅助数学的进展。 评论者指出，对 OpenAI 成果的两种解释可以并存：超大模型可能记住了预训练中见过的聊天内容所带来的洞见，而在可验证数学问题上用大规模算力做强化学习，也可能真的发现全新的技巧。有位评论者认为可疑的是，OpenAI 在得知某个重要数学证明很可能已存在于该模型训练数据中之后，旋即用一个仍在训练中的模型生成了 3000 亿输出 token，他把这种做法形容为一种“平行构建证据”；帖中引述 OpenAI 的说法称，某位研究者的 Codex 提示词影响结果这件事“不可能”发生。

hackernews · pred\_ · 9月10日 06:49 · [社区讨论](https://news.ycombinator.com/item?id=49639408)

**背景**: 这场讨论发生在 Mathstodon 上——一个面向数学人、支持 LaTeX 渲染的 Mastodon 实例，随后被搬上 Hacker News；帖中链接还指向 X（可通过基于 Nitter 的镜像 xcancel 查看）以及 Bluesky，后者的账号由 did:plc 去中心化标识符来识别。在这个语境下，OpenAI 的模型先在大规模文本语料上预训练（其中可能包含用户对话），再利用可自动判定的问题（例如竞赛式数学题）做强化学习微调。数学领域极其看重署名与优先权，因为一个证明的价值和研究者的声誉都取决于谁最先发表结果，这也正是未经署名使用他人未发表想法会被视为严重越界的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mathstodon.xyz/">About - Mathstodon</a></li>
<li><a href="https://atprotocol.dev/bluesky-and-did-plc/">Bluesky and DID PLC</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nitter">Nitter - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 整体情绪对 OpenAI 持怀疑态度。不少评论者认为“把 OpenAI 类比为人类合作者”很有说服力：如果一个人从对话中拿走研究者的想法并发表却不予署名，那显然是不道德的，同样的标准也应适用于 OpenAI。另一些人则主张两种解释可以同时成立——模型可能在预训练中吸收聊天内容，同时也能通过强化学习发现真正超越人类的新技巧；还有一派质疑在于：AI 在开放问题上的快速进展究竟是真实的，还是研究者不断把新鲜训练数据喂给模型、模型再把这些输出当作突破汇报回来的假象。

**标签**: `#AI ethics`, `#OpenAI`, `#research integrity`, `#attribution`, `#mathematics`

---

<a id="item-5"></a>
## [OpenAI 推出托管式 Agents API，支持可选的自托管沙箱](https://developers.openai.com/api/docs/guides/agents-api/overview) ⭐️ 8.0/10

**原标题**: [OpenAI Agents API](https://developers.openai.com/api/docs/guides/agents-api/overview)

OpenAI 发布了 Agents API，把 Codex harness 以完全托管服务的形式提供给开发者：会话维持、编排、上下文压缩与故障恢复都由 OpenAI 负责，开发者只需提供自己的工具并选择执行环境。该 API 支持托管、合作伙伴以及自托管三类沙箱，并且是建立在早前开源的 OpenAI Agents SDK 之上，而非取而代之。 这把目前大多数团队必须自行搭建的智能体基础设施产品化了，把一条极深的工程“兔子洞”变成可插拔的 API，也可能为 OpenAI 带来比单纯提供模型访问更持久的护城河。它会影响所有构建智能体应用的开发者，而自托管选项通过降低迁移成本，缓解了人们通常担心的供应商锁定问题。 该服务是围绕 Codex harness 构建的托管运行时，负责会话、编排、上下文压缩与恢复，工具由应用侧自行接入；沙箱可由 OpenAI 托管、由合作伙伴托管，也可自托管，文档指出这有助于在不同供应商之间迁移。它与此前轻量级的开源 Agents SDK（Swarm 的生产级继任者）不同，后者提供的是让开发者自建 harness 的基础原语。

hackernews · aquir · 9月10日 19:43 · [社区讨论](https://news.ycombinator.com/item?id=49649213)

**背景**: AI 智能体是让大语言模型调用工具、在多步之间保持状态并持续完成任务的系统；包裹模型并管理这一循环的代码通常被称为 harness。自建 harness 工作量巨大，因为你需要决定状态保存在哪里、工具如何被沙箱隔离、失败后如何恢复——在像 Cloudflare Workers 这类没有本地文件系统的无服务器环境中尤其困难。自托管沙箱是安全运行智能体生成代码的常见做法，E2B、Beam 等项目提供了可自托管或 Apache-2.0 许可的运行时。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/agents-api/overview">Agents API | OpenAI API</a></li>
<li><a href="https://runtimewire.com/article/openai-agents-api-managed-codex-harness">OpenAI launches Agents API to run the Codex harness as...</a></li>
<li><a href="https://e2b.dev/">E2B | The Enterprise AI Agent Cloud</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为业界仍在摸索“智能体即服务”的正确抽象，有人指出在自身没有文件系统或运行环境时，能直接插拔工具非常方便。也有人对供应商锁定表示担忧，甚至要求返还他们所付费的推理 token；另一些人则强调文档中深藏的自托管选项是一大亮点，并推测 OpenAI 将其视为相对众多本地 harness 的持久护城河。

**标签**: `#openai`, `#ai-agents`, `#api`, `#developer-tools`, `#vendor-lock-in`

---

<a id="item-6"></a>
## [Forgejo 16.0.4 修复严重的模板扩展远程代码执行漏洞](https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md) ⭐️ 8.0/10

**原标题**: [Forgejo &lt;=16.0.3 Critical RCE](https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md)

Forgejo 发布 16.0.4 版本，修复了一个影响 16.0.3 及之前所有版本的严重远程代码执行（RCE）漏洞，其根源是变量模板扩展干扰了 git 仓库的初始化过程。当用户基于模板仓库生成新仓库时，Forgejo 会克隆模板、删除 .git 目录、对 .forgejo/template 中列出的文件执行变量模板扩展，然后初始化一个新的 git 仓库，漏洞正发生在这一流程中。 任何自托管 Forgejo 16.0.3 及以下版本的用户都应将其视为紧急补丁，因为 Git 代码托管平台上的 RCE 可能危及源代码、凭据和 CI 密钥。此次披露还使人们重新关注 Forgejo 限制性 LLM 贡献政策可能拖慢漏洞发现速度，而攻击者却在越来越多地使用 AI 工具。 由于 Codeberg 的限流，许多访问者无法读取 Forgejo 在 Codeberg 上的发布说明页面，因此社区成员手动转贴了该版本中的两项修复，其中第二项是同一版本中的另一个安全缺陷修复。Gitea 项目的维护者指出 Gitea 对这两个问题均免疫，因为 Forgejo 是从 Gitea 分叉而来，共享大量代码。

hackernews · weierstass · 9月10日 15:57 · [社区讨论](https://news.ycombinator.com/item?id=49645907)

**背景**: Forgejo 是一个由社区治理、可自托管的“软件协作平台”（software forge）——一个基于 Go 运行时构建的 Web 服务器，除托管 Git 仓库外还提供问题跟踪、代码审查、维基和 CI 等功能，同时也是非营利托管平台 Codeberg 所使用的软件。模板仓库允许用户通过复制起始仓库并向其文件中替换变量来快速创建新项目，而正是这条代码路径上未经净化的模板扩展可能让攻击者控制的内容得以执行代码。这类模板注入漏洞是服务端漏洞中广为人知的一类，因为如果扩展输出没有沙箱保护，许多模板引擎都可以被逃逸从而达成命令执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Forgejo">Forgejo</a></li>
<li><a href="https://en.wikipedia.org/wiki/Codeberg">Codeberg</a></li>
<li><a href="https://forgejo.org/">Forgejo – Beyond coding. We forge .</a></li>

</ul>
</details>

**社区讨论**: 评论者争论 Forgejo 禁止 LLM 生成贡献的政策是否使其处于劣势，认为即便维护者不用 AI，攻击者仍会用 AI 来发掘漏洞。Gitea 项目的一位负责人澄清 Gitea 对这两个问题均免疫，同时提醒不应苛责安全漏洞报告者，否则会减少整体报告量；还有多位用户因 Codeberg 限流导致页面无法访问而手动转贴了发布说明内容。

**标签**: `#security`, `#vulnerability`, `#forgejo`, `#git`, `#self-hosted`

---

<a id="item-7"></a>
## [微软将 Rust 列为一级（Tier-1）语言](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 8.0/10

**原标题**: [Rust is tier-1 language at Microsoft](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/)

微软已正式将 Rust 认定为一级（Tier-1）语言，Rust 基金会网站上的一篇客座文章对此进行了说明，这意味着 Rust 在公司内部获得了与成熟语言同等的工程待遇。一级语言地位为微软各团队提供了一条从本地开发直通生产环境的“铺装道路”，涵盖安全工具链构建、开发者工具、质量工作流、深度平台集成，以及满足微软软件必须遵守的 SDL（安全开发生命周期）合规要求。 这一认定表明 Rust 已从有前景的社区项目跨入主流企业基础设施行列，也印证了 Rust 在系统编程领域已成为 C++ 和 C\# 的有力竞争者。由于所有同时维护 C/C++ 工具链的主流操作系统厂商如今都已多元化其系统编程语言选项，此举可能加速 Rust 在整个行业的全新项目（greenfield）采用，并影响招聘、工具链与平台支持的重心。 一级语言地位属于微软内部的工程分类，而非产品发布，实际含义是微软内部 Rust 代码可享有安全工具链构建、一等公民级的开发者工具以及 SDL 合规支持。社区讨论还提到传闻中的 Rust 与 MSVC 集成，以及一项（虽非官方正式目标）内部愿景：借助自动化工具在 2030 年前将十亿行代码转换为 Rust；此外还有 DARPA 资助的 C 到 Rust 自动化转换项目，由六个采用不同方法的团队并行推进。

hackernews · mmastrac · 9月10日 13:39 · [社区讨论](https://news.ycombinator.com/item?id=49643546)

**背景**: Rust 是一门通用系统编程语言，由 Graydon Hoare 于 2006 年在 Mozilla 创建，2015 年 5 月发布首个稳定版本 Rust 1.0，自 2021 年 2 月起由 Rust 基金会赞助。Rust 强调性能、类型安全与并发能力，并通过编译期的“借用检查器”（borrow checker）在没有垃圾回收器的情况下保证内存安全，防止悬垂引用和数据竞争。这些特性对大型厂商意义重大，因为 C 和 C++ 代码库中大多数严重安全漏洞都属于内存安全类缺陷，而这正是 Rust 在设计上默认消除的问题类别。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier-1 Language at Microsoft</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rust_%28programming_language%29">Rust (programming language)</a></li>
<li><a href="https://lobste.rs/s/eerwba/rust_is_tier_1_language_at_microsoft">Rust Is Tier-1 Language at Microsoft | Lobsters</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者总体上对这条消息表示欢迎，认为它体现了 Rust 的成熟：一位有五年专业 Rust 经验的开发者表示，在高层次应用开发上已经看不到选择其他语言的技术理由；另一位则称，这一公告说明 Rust 不再是那种“快速迭代、打破常规”的新生语言，而是 C++ 和 C\# 的严肃竞争对手。也有人从战略角度解读，指出内存安全对微软漏洞（CVE）高发产品组合的价值、所有主流操作系统厂商多元化系统编程语言的意义，以及对 MSVC 集成传闻的期待。Lobsters 上则出现了一些质疑声音，有人追问微软是否会在新产品中使用 Rust、是否会提供更多 Rust 绑定，甚至质疑人们是否应当在系统编程语言中编写高层次应用代码。

**标签**: `#Rust`, `#Microsoft`, `#Programming Languages`, `#Systems Programming`, `#Industry Adoption`

---

<a id="item-8"></a>
## [trynix.dev 让任意 Nix 包在浏览器虚拟机中启动](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 8.0/10

**原标题**: [Any Nix package, live in your browser](https://simonwillison.net/2026/Sep/10/trynix/)

Farid Zakaria 发布了 trynix.dev，它通过 WebAssembly 在浏览器内运行一个基于 qemu-wasm 的 x86\_64 Linux 虚拟机，能够启动过去 13 年里构建的任意 Nix 包，并且可通过 URL 直接寻址，例如 https://trynix.dev/?pkg=python3%403.6.2 会打开一个运行 2017 年 Python 3.6.2 的交互式 shell。他还发布了 trynix-preview，这是一个 GitHub Action，会在 pull request 下评论一个链接，让评审者直接在浏览器中启动该 PR 的构建产物，全程不需要服务器。 它让可复现环境变成一条可以直接发给别人的 URL：任意软件包的某个历史版本都能在沙箱化的浏览器标签页中运行，无需安装、无需容器镜像、也无需远程基础设施。trynix-preview 的工作流是代码评审的一个很有说服力的概念验证，因为评审者可以直接启动 pull request 产出的确切构建产物，而不是仅凭 diff 进行推断，而且纯客户端模式让成本和隐私方面的顾虑都很低。 qemu-wasm 是 ktock 的项目，它把 QEMU 编译为 WebAssembly，同时支持 TCI（IR 解释器）和 TCG，其中只有被频繁执行的翻译块（例如执行超过 1000 次）才会被编译为 Wasm 以提升速度。由于一切都在浏览器沙箱内运行，性能和内存受客户端机器限制，大型软件包或重负载任务会比原生执行明显更慢。

rss · Simon Willison · 9月10日 23:44

**背景**: Nix 是一个纯函数式包管理器：每个软件包都存放在不可变路径下，该路径内嵌了其全部输入的哈希值，因此多个版本可以共存而不冲突，构建也能在不同机器上复现。qemu-wasm 是把 QEMU 模拟器移植到 WebAssembly 的项目，能让一台完整的 x86\_64 机器运行在浏览器标签页里，Leaning Technologies 的 WebVM 等项目也采用了类似思路。WebAssembly 是一种可移植的二进制指令格式，浏览器在沙箱中执行它，这正是这些虚拟机能够在客户端安全运行不受信任二进制文件的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ktock/qemu-wasm">GitHub - ktock/ qemu - wasm : QEMU on browser · GitHub</a></li>
<li><a href="https://nixos.org/">Nix &amp; NixOS | Declarative builds and deployments</a></li>
<li><a href="https://medium.com/leaningtech/webvm-linux-virtual-machine-in-the-browser-with-full-networking-via-tailscale-dac11f844b46">WebVM: Linux virtualization in WebAssembly with full... | Medium</a></li>

</ul>
</details>

**标签**: `#nix`, `#webassembly`, `#virtualization`, `#qemu`, `#reproducible-builds`

---

<a id="item-9"></a>
## [Calif Research 演示 WeWorm：用 AI 打造的微信零点击蠕虫](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 8.0/10

**原标题**: [Quoting Calif Research](https://simonwillison.net/2026/Sep/10/calif-research/)

Calif Research 发布了一个名为 WeWorm 的演示，声称这是首个可通过微信通话在 iOS 和 Android 之间传播的零点击蠕虫，即便受害者从未接听电话，账号也会被攻陷。该团队表示，借助 AI 他们在大约两天内找到了漏洞并写出第一个远程代码执行（RCE）利用程序，随后又花了约一周时间把它改造成可自我传播的蠕虫。 微信拥有约 14 亿用户，因此针对其通话栈的零点击、可自我传播攻击属于影响两大主流移动平台的极为严重的威胁类型。更广泛地看，所谓 AI 把过去需要多人团队耗时数月的漏洞利用开发压缩到约两天，很可能会加剧关于 AI 正多快降低攻击性安全研究门槛的争论。 根据对该演示的报道，WeWorm 利用了微信 VoIP（IP 语音）栈中的内存破坏漏洞，可在数秒内劫持目标账号并向其联系人自我传播；即便受害者接听电话也听不到任何异常声音。但需要注意的重要限制是：这只是一个概念验证演示，独立验证非常有限，而且此处的信息来源仅是 Simon Willison 摘录的一段简短引文，而非包含可复现细节的完整技术报告。

rss · Simon Willison · 9月10日 00:56

**背景**: 所谓“零点击”攻击不需要受害者做任何操作——不用点击、不用接听、不用打开消息——因此比依赖用户失误的攻击更难防御。“远程代码执行”（RCE）指攻击者能通过网络在目标设备上运行任意自己选择的代码，通常是最受重视的一类漏洞；而“蠕虫”是无需人工干预即可自动从一台设备复制到另一台的恶意程序。微信是腾讯旗下主导中国市场的即时通讯与通话应用，覆盖 iOS 和 Android，这正是其 VoIP 栈中出现跨平台蠕虫后果如此严重的原因。历史上，把可靠的 RCE 与蠕虫传播链结合起来通常需要一支熟练团队耗时数月，因此这次声称中真正新颖之处在于 AI 辅助下的开发时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/weworm-first-0-click-worm/">WeWorm – First 0-Click Worm Spreading Through WeChat Calls ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/RCE_exploit">RCE exploit</a></li>

</ul>
</details>

**标签**: `#security`, `#ai-security-research`, `#zero-click-exploit`, `#vulnerability-research`, `#ai-assisted-development`

---

<a id="item-10"></a>
## [AI 智能体仅凭漏洞传闻就能找出可利用的漏洞](https://www.schneier.com/blog/archives/2026/09/ais-compress-exploit-timeline.html) ⭐️ 8.0/10

**原标题**: [AIs Compress Exploit Timeline](https://www.schneier.com/blog/archives/2026/09/ais-compress-exploit-timeline.html)

在 Schneier on Security 于 2026 年 9 月转载的一篇博文中，Bruce Schneier 重点介绍了 Anil（anil.recoil.org）的一则笔记：只要给 AI 智能体一个关于安全漏洞的模糊传闻，它就足以定位到真正的漏洞，这意味着攻击者可能在公开补丁发布之前很久就已利用该漏洞。Simon Willison 进一步指出，这种发现速度与现有的开源漏洞禁运（embargo）流程不相容，社区需要制定新的流程来保障安全。 如果仅凭传闻就足以让 AI 智能体还原出可用的漏洞利用，那么支撑协调漏洞披露（CVD）和开源禁运机制的保密假设就基本失效，维护者将被迫转向更快或更透明的修补模式。这直接影响到开源维护者、安全响应团队和漏洞赏金项目——他们可能面临漏洞报告激增，以及从“耳语”到“武器化”之间窗口大幅缩短的局面。 Anil 指出，这些智能体之所以成功，仅仅是因为大致知道该问题涉及什么，这意味着它可以在信息极为有限的语境下复现漏洞，而无需泄露具体技术细节。相关评论还指出，这一趋势与维护者面临的漏洞报告激增、分诊工作量上升以及获取 CVE 编号延迟等问题同时出现；应将其视为专家评论与流程警示，而非正式的研究突破。

rss · Schneier on Security · 9月10日 10:40

**背景**: 协调漏洞披露（CVD，有时也称“负责任披露”）是业界通行做法：发现者先私下告知厂商，待修复方案准备好后才向公众公开漏洞，通常会有一段从几天到数月不等的临时禁运期。该模型假设在补丁窗口期内对细节保密能够保护用户。而基于大语言模型的 AI 智能体可以自主搜索代码、推测可能的漏洞类型并反复迭代概念验证代码，因此它们能仅凭传闻、提交信息或含糊的安全公告等极少线索推断出漏洞，从而削弱了这一保密假设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://anil.recoil.org/notes/rumour-is-the-exploit">Just a rumour of a bug is enough to find a security exploit these days</a></li>
<li><a href="https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure">Coordinated vulnerability disclosure</a></li>
<li><a href="https://devblogs.co/posts/just-a-rumour-of-a-bug-is-enough-to-find-a-security-exploit-these-days">Just a rumour of a bug is enough to find a security ... | devblogs.sh</a></li>

</ul>
</details>

**标签**: `#AI security`, `#vulnerability disclosure`, `#open source security`, `#exploit development`, `#LLM agents`

---