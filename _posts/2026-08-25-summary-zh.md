---
layout: default
title: "Horizon Summary: 2026-08-25 (ZH)"
date: 2026-08-25
lang: zh
edition: personal
---

> 从 31 条内容中筛选出 9 条重要资讯。

---

1. [微软画图与照片应用在 AI 编辑图片中隐藏嵌入 GUID 水印](#item-1) ⭐️ 8.0/10
2. [旧金山被真实 GIS 数据重建成可探索 3D 游戏](#item-2) ⭐️ 8.0/10
3. [seL4 在 AArch64 上的安全验证完成](#item-3) ⭐️ 8.0/10
4. [AI 编程工具或削弱开发者专业技能，文章指出](#item-4) ⭐️ 8.0/10
5. [可执行文件即 SQLite 数据库：一种新型二进制格式构想](#item-5) ⭐️ 8.0/10
6. [开发者打造低延迟 AI 伴侣，与他共玩《天际》](#item-6) ⭐️ 8.0/10
7. [可执行文件即 SQLite 数据库：将 ELF 组件存为数据表](#item-7) ⭐️ 8.0/10
8. [Cloudflare 将博客迁移至 EmDash 以大规模验证其技术栈](#item-8) ⭐️ 8.0/10
9. [用 AI 作为空间软件生成器创建可编程 3D 对象](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [微软画图与照片应用在 AI 编辑图片中隐藏嵌入 GUID 水印](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

**原标题**: [MS Paint and Photos inivisibly watermark even locally generated output with GUID](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/)

安全研究者李旭升通过逆向工程发现，微软画图（MS Paint）和照片（Photos）应用会在使用 AI 功能编辑的图片中静默嵌入一个由服务器颁发的 GUID 水印，即使处理完全在本地设备上完成也不例外。用户无法关闭这一不可见的水印。 这一发现引发严重的隐私与匿名性担忧，因为每个 GUID 都可关联到用户的微软账户，分享图片可能导致身份暴露。水印机制从云端 AI 扩展到本地 AI 工具，进一步削弱了用户对自己内容的控制权。 该隐形 GUID 水印与可见且可关闭的 C2PA 内容凭证同时添加，并在后台静默嵌入，用户不会收到任何通知。目前尚不确定 AI 增强背景删除等操作是否也会触发水印，但该 GUID 可被解码并从图片中提取出来。

hackernews · ComputerGuru · 8月24日 15:28 · [社区讨论](https://news.ycombinator.com/item?id=49421158)

**背景**: 数字水印是一种在媒体中嵌入隐藏信号以验证所有权或来源的技术，隐形水印被设计成即使在裁剪、压缩或截屏后仍可被检测。C2PA（内容来源与真实性联盟，Content Credentials）是一个更广泛的标准，通过加密签名元数据记录内容的创建和编辑过程。微软在画图和照片应用中的 AI 图像编辑功能结合了这两种技术：既附加 C2PA 元数据，又嵌入与用户微软账户关联的唯一 GUID。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/">Microsoft Paint and Photos Embed Server-Issued GUIDs ... :: Xusheng Li</a></li>
<li><a href="https://contentcredentials.org/">Content Credentials | Verify Media Authenticity</a></li>
<li><a href="https://www.imatag.com/digital-watermarking">Invisible Digital Watermarking | The smart way to protect your online content</a></li>

</ul>
</details>

**社区讨论**: 评论区普遍批评这一行为，认为隐形 GUID 是对互联网匿名性的新威胁，而非正当的 AI 防护措施。多位用户指出即使本地 AI 编辑也会被加水印，还有人提到微软此前曾将 Copilot 水印错误地应用到 Azure DevOps 提交，进一步加深了不信任。也有用户对画图应用加入 AI 功能感到意外，并质疑微软的产品策略。

**标签**: `#privacy`, `#watermarking`, `#Microsoft`, `#AI`, `#digital rights`

---

<a id="item-2"></a>
## [旧金山被真实 GIS 数据重建成可探索 3D 游戏](https://sf.thijs.gg/) ⭐️ 8.0/10

**原标题**: [The entire city of San Francisco as a video game](https://sf.thijs.gg/)

一个基于网页的项目利用真实 GIS 数据将整个旧金山市重建成可探索的视频游戏，在 Hacker News 上引发了强烈关注。该项目展示了一条将真实城市数据集转换为交互式 3D 环境的技术管线。 该项目展示了如何将开放的 GIS 地理空间数据转化为沉浸式游戏体验，有可能降低独立开发者和游戏工作室构建真实世界场景的技术门槛。它还引发了关于将 GIS 数据与游戏引擎及高斯泼溅等渲染技术集成的讨论。 该项目主要基于网页运行，并使用真实的 GIS 数据来构建城市布局。虽然新闻正文没有明确说明渲染方式，但评论者反复询问是否使用了高斯泼溅技术——一种将照片转换为实时 3D 场景的技术。

hackernews · centrosphere · 8月24日 17:05 · [社区讨论](https://news.ycombinator.com/item?id=49422784)

**背景**: GIS（地理信息系统）数据是指与地球位置相关联的空间信息，例如建筑物轮廓、高程、道路和土地利用等。高斯泼溅是一种体渲染技术，于 2023 年流行，可以将一组普通照片转换成可从任意角度实时探索的照片级 3D 场景。将 GIS 数据与这类渲染技术结合，可以将真实城市数字化为交互式环境。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gaussian_splatting">Gaussian splatting</a></li>
<li><a href="https://en.wikipedia.org/wiki/GIS_data">GIS data</a></li>
<li><a href="https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/">3D Gaussian Splatting for Real-Time Radiance Field Rendering</a></li>

</ul>
</details>

**社区讨论**: 社区反馈总体积极且带有情感色彩，多位评论者分享了在旧金山熟悉地点漫步的个人回忆。其他人则讨论了类似项目，比如费城的 cityrider 游戏，以及关于用高斯泼溅或构建可靠数据到游戏管线的技术问题。也有一位用户反馈页面加载失败。

**标签**: `#gaussian-splatting`, `#webgl`, `#city-recreation`, `#game-dev`, `#gis`

---

<a id="item-3"></a>
## [seL4 在 AArch64 上的安全验证完成](https://proofcraft.systems/news-2026/#2026-08-21) ⭐️ 8.0/10

**原标题**: [SeL4 security proofs now complete on AArch64](https://proofcraft.systems/news-2026/#2026-08-21)

2026 年 8 月 21 日，seL4 项目宣布其正式安全证明已在 AArch64 架构上全部完成。这将该微内核的验证保证扩展到了 64 位 ARM 系统。 这一里程碑将机器检查的正确性和安全性保证带到了广泛使用的 64 位处理器架构上，使 seL4 对安全关键和保密关键应用更具吸引力。这可能会加速其在日益依赖 ARMv8/AArch64 硬件的汽车、航空航天和国防系统中的采用。 验证工作覆盖到 seL4 的 C 实现，但仍假定编译器、汇编代码、硬件和启动代码正确。正如社区讨论中指出的，当前 AArch64 证明针对的是非 MCS（混合关键性系统）配置和单核（unicore）系统。

hackernews · snvzz · 8月24日 11:32 · [社区讨论](https://news.ycombinator.com/item?id=49418255)

**背景**: seL4 是一个从头设计的微内核，源于 L4 微内核家族，并以正式验证为核心目标。2009 年，该项目完成了从抽象规范到 C 实现的机器检查的功能正确性证明，使之成为第一个在如此程度上完全正式验证的通用操作系统内核。AArch64 是 ARM 架构的 64 位执行状态，常见于现代智能手机、嵌入式设备和服务器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SeL4">seL4 - Wikipedia</a></li>
<li><a href="https://sel4.systems/">The seL4 Microkernel | seL4</a></li>
<li><a href="https://cacm.acm.org/research/sel4-formal-verification-of-an-operating-system-kernel/">seL 4 : Formal Verification of an Operating-System Kernel...</a></li>

</ul>
</details>

**社区讨论**: 评论者既表达了怀疑，也表达了谨慎的赞赏。有人指出侧信道时序攻击可能“彻底否定”这一结果，另有人强调证明仅限非 MCS、单核配置这一细节。还有人讨论了采用情况，询问哪些操作系统使用 seL4，并认为 seL4 需要一个原生的 seL4/Linux 才能有意义地提升整体系统安全性。

**标签**: `#formal verification`, `#seL4`, `#microkernel`, `#AArch64`, `#security`

---

<a id="item-4"></a>
## [AI 编程工具或削弱开发者专业技能，文章指出](https://larsfaye.com/articles/ai-coding-will-prevent-expertise) ⭐️ 8.0/10

**原标题**: [Coding expertise is going to collapse from AI reliance](https://larsfaye.com/articles/ai-coding-will-prevent-expertise)

Lars Faye 在一篇观点文章中指出，对 AI 编程工具的依赖将导致编程专业技能崩溃，因为开发者失去了深度技能形成所需的‘摩擦（friction）’。这篇题为《Coding expertise is going to collapse from AI reliance》的文章发表在 larsfaye.com 上，引发了社区的热烈讨论。 这一观点之所以重要，是因为它挑战了‘AI 编程工具必然提升开发者生产力’的主流叙事。如果摩擦（即适当的难度与认知努力）对形成专业技能至关重要，那么一代工程师可能会依赖 AI 生成自己无法完全理解或维护的代码，对软件质量和整个行业产生严重影响。 核心论点是：移除摩擦——即调试、搜索和分析所需耗费的认知努力——会削弱长期技能的形成，这与将‘生产性摩擦’与深度学习联系起来的研究一致。社区评论补充了相关背景，例如企业要求所有代码都由 AI 生成，导致人类工程师难以审查并真正理解 AI 输出的代码。

hackernews · larsfaye · 8月24日 15:52 · [社区讨论](https://news.ycombinator.com/item?id=49421554)

**背景**: 大型语言模型（LLM）是在海量文本数据上训练、能够理解和生成类人语言的 AI 系统；它们为 Copilot、Claude、Cursor 等编程助手提供支持，这些助手可根据自然语言提示直接生成代码。在学习科学中，‘摩擦（friction）’指的是能够促进深度加工和专业技能形成的适度困难或认知努力，而过于顺畅的体验可能导致浅层学习。这篇文章将该概念应用到软件开发领域，警告 AI 移除了那些有助益的挣扎——经验丰富的程序员正是通过这些挣扎构建心理模型和直觉。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/large-language-models">What Are Large Language Models (LLMs)? | IBM</a></li>
<li><a href="https://www.stultiferanavis.it/la-rivista/the-generative-value-of-friction-in-digital-media-neuroscience-education-and-play">Stultifera Navis - The Generative Value of Friction in Digital Media: Neuroscience, Education, and Play</a></li>

</ul>
</details>

**社区讨论**: 评论区大体赞同这一论点，并引用了现实中的证据：一位用户提到企业领导层强制要求使用 AI 生成代码，导致代码产出速度快到人类难以审查。也有用户提出更细致的看法，例如一位 15 年经验的开发者称赞‘引导式编程（guided coding）’——即把 LLM 助手融入日常开发——既高质量又有乐趣；还有人将现状比作‘蛇吞自己的尾巴’，警告优秀开发者可能被迫去审查质量低劣的 AI 生成代码。

**标签**: `#AI coding`, `#software engineering`, `#expertise`, `#LLM tools`, `#developer productivity`

---

<a id="item-5"></a>
## [可执行文件即 SQLite 数据库：一种新型二进制格式构想](https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database) ⭐️ 8.0/10

**原标题**: [Executable Is a SQLite Database](https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database)

该文章提出一种新的可执行文件格式：将二进制本身设计为 SQLite 数据库，从而可以通过 SQL 查询对二进制进行检视和修改。它特别建议利用 SQLite 的虚拟表机制，将 ELF 的各个节暴露为可查询的表。 如果这一构想被广泛采用，二进制文件将变得自描述且可检视，从而改变逆向工程、调试和二进制修改的工作流程。它还提供了一种将代码与数据融合在同一个可查询文件中的新思路。 SQLite 的虚拟表机制可让外部资源以表的形式呈现，文章提议用它将 ELF 的节（如 .text 和 .data）暴露为可查询的表。评论者指出，ELF 布局紧凑且难以修改，而 SQLite 的动态链接与 ELF 兼容，暗示了实际实现的可行性。

hackernews · setheron · 8月24日 04:48 · [社区讨论](https://news.ycombinator.com/item?id=49415271)

**背景**: ELF（可执行与可链接格式）是类 Unix 系统上的标准二进制格式，它将代码和数据组织为命名的节。SQLite 是一种嵌入式关系数据库，支持虚拟表，使 SQL 查询能够像访问普通表一样访问外部资源。该文基于这些概念，提出了一种混合格式，将可执行文件的结构通过标准查询接口暴露出来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sqlite.org/vtab.html">The Virtual Table Mechanism Of SQLite</a></li>
<li><a href="https://www.sqlite.org/vtablist.html">List Of Virtual Tables</a></li>
<li><a href="https://en.wikipedia.org/wiki/Executable_and_Linkable_Format">Executable and Linkable Format - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 讨论总体上非常热情：读者惊叹于 SQLite 虚拟表的能力，有些人认为 ELF 本身就已是一种数据库，将此提案视为演进而非革命。另一些人则强调了运行时可修改表以及替代 AppImage 等潜在用途，而作者提到学术评审并不认可这一想法。

**标签**: `#SQLite`, `#executable formats`, `#ELF`, `#software architecture`, `#databases`

---

<a id="item-6"></a>
## [开发者打造低延迟 AI 伴侣，与他共玩《天际》](https://pantel.is/projects/ai-gaming-companion/) ⭐️ 8.0/10

**原标题**: [I built a low-latency AI companion that plays Skyrim with me](https://pantel.is/projects/ai-gaming-companion/)

一位开发者创建了一个低延迟 AI 伴侣，与他一起玩《天际》，利用嵌入（embeddings）和结构理解来稳健地解析语音指令。该系统在 M4 MacBook 上运行音频处理和 AI 大脑，而游戏则在 Windows 上运行。 该项目展示了 AI 在游戏中的实用低延迟集成，可能影响未来游戏中 NPC 和同伴的设计方式。它同时引发了关于本地运行 AI 模型以及面向主机的人工智能硬件可行性的讨论。 该系统包含一个名为 ALE 的自定义模型，设计上对措辞基本不敏感，因此像&quot;pick up&quot;、&quot;grab&quot;或&quot;go get the sword&quot;这样的指令都能被理解。它通过在创建嵌入之前解析句子结构来分解多个命令，并且可以在拥有约 12GB 或更多显存的 Windows 上运行。

hackernews · pantelisk · 8月23日 23:18 · [社区讨论](https://news.ycombinator.com/item?id=49413561)

**背景**: 嵌入（embeddings）是机器学习系统用来理解复杂知识领域的现实世界对象的数值表示；相似的概念会映射到高维空间中的邻近向量。自然语言处理中的结构理解涉及语法、语义、语用和形态学，帮助机器有意义地解析句子结构。该项目结合这些技术来理解语音指令，而无需精确的短语匹配。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Embedding_%28machine_learning%29">Embedding (machine learning) - Wikipedia</a></li>
<li><a href="https://aws.amazon.com/what-is/embeddings-in-machine-learning/">What is Embedding? - Embeddings in Machine Learning Explained - AWS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Natural_language_processing">Natural language processing - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者热情高涨，称赞该项目的延迟和完成度，一些人建议它可以成为游戏的主要功能或作为小型本地模型运行。其他人则对主机应用场景以及它是否完全在本地运行表示好奇，还有一位评论者指出，即将推出的 GPT-Live 模型最终可能使自定义 ALE 模型变得不必要。

**标签**: `#AI companion`, `#gaming`, `#low-latency`, `#embeddings`, `#NLP`

---

<a id="item-7"></a>
## [可执行文件即 SQLite 数据库：将 ELF 组件存为数据表](https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/) ⭐️ 8.0/10

**原标题**: [Your executable is a SQLite database](https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/)

Farid Zakaria 展示了一种 Linux 模式：通过将 ELF 组件存入 SQLite 数据表，并把文件的应用 ID 标记为“SELF”，使同一个文件既是可执行文件也是 SQLite 数据库。自定义解释器 self-exec 会读取这些表并执行程序，binfmt\_misc 可被配置来自动调用它。 这个技巧创造性地把 SQLite 的自包含文件格式、ELF 结构和 Linux 的 binfmt\_misc 融合到一个文件里。它可能启发新的软件打包、分发和校验方式，让熟悉 SQLite 的工具能直接读取和查询可执行文件的内部结构。 SQLite 文件头在偏移 68 字节处保存一个 4 字节应用 ID，本方案将其设为 ASCII 字符串“SELF”（Structured Executable &amp; Linkable Format）。原型使用一个 SQLite schema 存放 ELF 组件，用 C 语言编写的 self-exec 加载器执行，并通过类似 &\#x27;:self:M:68:SELF::/usr/local/bin/self-exec:&\#x27; 的 binfmt\_misc 注册项来触发。

rss · Simon Willison · 8月24日 11:38

**背景**: SQLite 是一种自包含的、基于文件的数据库，其文件头包含一个常用于标识自定义文件格式的应用 ID。ELF 是 Linux 上标准的可执行文件格式，通常包含头部、节（section）和程序段（program segment）。binfmt\_misc 是 Linux 内核的一项功能，能识别任意的二进制魔数模式并调用指定解释器，这正是这种基于 SQLite 的可执行格式能直接从 shell 启动的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database">Your executable is a SQLite database | Farid Zakaria’s Blog</a></li>
<li><a href="https://docs.kernel.org/admin-guide/binfmt-misc.html">Kernel Support for miscellaneous Binary Formats (binfmt_misc) — The Linux Kernel documentation</a></li>
<li><a href="https://sqlite.work/sqlite-application-id-and-magic-number-registration-for-file-type-recognition/">SQLite Application ID and Magic Number... - SQLite Help Docs</a></li>

</ul>
</details>

**标签**: `#SQLite`, `#Linux`, `#ELF`, `#executables`, `#binfmt\_misc`

---

<a id="item-8"></a>
## [Cloudflare 将博客迁移至 EmDash 以大规模验证其技术栈](https://blog.cloudflare.com/cloudflare-blog-uses-emdash/) ⭐️ 8.0/10

**原标题**: [The Cloudflare Blog – Brought to you by EmDash](https://blog.cloudflare.com/cloudflare-blog-uses-emdash/)

Cloudflare 宣布将其博客迁移到自有平台 EmDash，并发布文章详细介绍团队如何对性能进行压力测试、安全路由生产流量以及重新设计前端。此次迁移被视为对其技术栈的大规模验证。 这之所以重要，是因为 Cloudflare 正在展示其自有基础设施可承载互联网上访问量最大的工程博客之一。这些关于生产流量路由和前端性能的技术见解对其他大规模 Web 运营非常有价值。 这篇博文涵盖性能压力测试、安全路由生产流量以及前端重新设计。文章未披露具体性能指标，但将这次迁移定位为 EmDash 在大规模场景下的试验。

rss · Cloudflare Blog · 8月24日 19:00

**背景**: Cloudflare 是一家主要的 Web 基础设施公司，以内容分发网络和边缘计算服务闻名。这篇博文说明，Cloudflare 将博客迁移到名为 EmDash 的平台，作为对其自身技术栈的大规模测试。名称“EmDash”似乎是在向 em dash（长破折号）标点符号致敬，这种标点在 Cloudflare 的文章中非常常见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://prowritingaid.com/em-dash">Em Dash : What Is It and How to Use It</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#EmDash`, `#performance`, `#migration`, `#frontend`

---

<a id="item-9"></a>
## [用 AI 作为空间软件生成器创建可编程 3D 对象](https://www.reddit.com/r/MachineLearning/comments/1vxcc1h/r_using_ai_as_a_spatial_software_generator_to/) ⭐️ 8.0/10

**原标题**: [\[R\] Using AI as a spatial software generator to create 3D objects that are inherently programmable](https://www.reddit.com/r/MachineLearning/comments/1vxcc1h/r_using_ai_as_a_spatial_software_generator_to/)

该论文提出使用大型语言模型（LLM）作为空间软件生成器，以程序化代码而非静态网格的形式创建 3D 对象。这些对象天生可编程、可动画化，并能适应不同的计算环境。 这种方法可能通过让对象从一开始就灵活且可交互，从而变革 3D 内容制作流程。工业设计、游戏开发、仿真以及 AR/VR/XR 等行业可能会受到重大影响。 生成的 3D 对象在创作时具备完整的层次结构和铰链/插槽关节。不过，它们目前难以创建复杂的有机形状，相关代码已开源，演示可在 nova3d.xyz 查看。

reddit · r/MachineLearning · /u/mhb\_11 · 8月24日 19:10

**背景**: 传统基于 AI 的 3D 生成器通常输出难以编辑或动画化的单体网格块。空间编程涉及用代码描述 3D 几何和行为，而大型语言模型正越来越擅长根据文本提示生成此类代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://spatial-vlm.github.io/">SpatialVLM: Endowing Vision-Language Models with Spatial ...</a></li>
<li><a href="https://github.com/simoncwang/LLMSpatialLayout">simoncwang/LLMSpatialLayout: An extension of the LLM -based...</a></li>
<li><a href="https://scispace.com/pdf/spatial-programming-for-industrial-robots-through-task-2hgq9k2325.pdf">Spatial Programming for Industrial Robots Through Task...</a></li>

</ul>
</details>

**标签**: `#AI`, `#3D generation`, `#LLM`, `#spatial computing`, `#computational design`

---