---
layout: default
title: "Horizon Summary: 2026-08-26 (ZH)"
date: 2026-08-26
lang: zh
edition: personal
---

> 从 35 条内容中筛选出 9 条重要资讯。

---

1. [OpenAI 称其 Jalapeño 芯片性能超越 Nvidia Blackwell](#item-1) ⭐️ 9.0/10
2. [Firefox 157 默认在所有平台启用 JPEG XL](#item-2) ⭐️ 9.0/10
3. [FDA 批准首款连续监测酮体和血糖的可穿戴设备](#item-3) ⭐️ 8.0/10
4. [苹果发布 M6 与 M5 Ultra 芯片，性能与 AI 算力大幅跃升](#item-4) ⭐️ 8.0/10
5. [苹果发布搭载 M5 Max 与 M5 Ultra 的新 Mac Studio，主打本地 AI](#item-5) ⭐️ 8.0/10
6. [Nitter 收到停止函，实例暂停服务等待法律咨询](#item-6) ⭐️ 8.0/10
7. [SpaceX 正式宣布 Starbase Louisiana 发射场](#item-7) ⭐️ 8.0/10
8. [开放权重模型上的持续学习为主权 AI 提供路径](#item-8) ⭐️ 8.0/10
9. [Papers with Code 用 pgvector 与 Qwen3 实现 SOTA 混合搜索](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 称其 Jalapeño 芯片性能超越 Nvidia Blackwell](https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia) ⭐️ 9.0/10

**原标题**: [OpenAI Jalapeño: Better than Nvidia Blackwell](https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia)

OpenAI 发布了与 Broadcom 联合设计的定制推理芯片 Jalapeño，并声称其在测试中性能优于 Nvidia 的 Blackwell 处理器。据称，该芯片能为现代大语言模型提供更快、更节能的推理，具备更高吞吐量和更低延迟。 这是对 Nvidia 在 AI 硬件领域主导地位的重大挑战，可能重塑 AI 推理的经济性，影响模型部署成本和 token 定价。如果得到验证，可能会加速整个行业向针对特定 AI 工作负载定制芯片的方向转变。 Jalapeño 是专为 LLM 推理设计的专用 ASIC，而非通用 GPU，并且与 OpenAI 到 2029 年 10 GW 基础设施承诺相关联。这些说法基于彭博社报道的 OpenAI 自身测试，仍需要独立基准测试和实际部署验证。

hackernews · bmulholland · 8月25日 14:06 · [社区讨论](https://news.ycombinator.com/item?id=49434378)

**背景**: Nvidia 的 Blackwell 架构是该公司最新的 GPU 微架构，是 Hopper 和 Ada Lovelace 的继任者；Blackwell GPU 拥有 2080 亿个晶体管，采用定制的 TSMC 4NP 工艺。OpenAI 历来严重依赖 Nvidia GPU，但近年来越来越积极地投资定制芯片，以降低成本和减少依赖。Jalapeño 是 OpenAI 首款定制 AI 芯片，与 Broadcom 合作打造，旨在让大规模推理更便宜、更快。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/openais-jalape%C3%B1o-chip-what-developers-need-know-its-move-ashish-jain-9uoof">OpenAI ’s Jalapeño Chip : What Developers Need to Know About Its...</a></li>
<li><a href="https://www.stork.ai/blog/jalapeo-openais-nvidia-killer">OpenAI &#x27;s Jalapeño Chip : A Custom ASIC to Challenge... | Stork.AI</a></li>
<li><a href="https://www.spheron.network/blog/openai-jalapeno-chip-gpu-cloud-inference-2026/">OpenAI Jalapeño Chip Explained: What... | Spheron Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Blackwell_%28microarchitecture%29">Blackwell (microarchitecture) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者总体非常热情，将新兴推理芯片市场比作早期 3dfx、Riva 和 PowerVR 的时代。多人认为硬件持续改进很可能让 token 价格进一步下降。有评论者提出，在 OpenAI/Anthropic 的规模下，将 LLM 权重直接烧入定制芯片可带来巨大的成本和速度优势；还有评论者指出，人类语言的能效目前仍比模型推理高约 22 倍。

**标签**: `#OpenAI`, `#AI hardware`, `#Nvidia`, `#semiconductors`, `#inference`

---

<a id="item-2"></a>
## [Firefox 157 默认在所有平台启用 JPEG XL](https://groups.google.com/a/mozilla.org/g/dev-platform/c/3YMV4MS34KA?pli=1) ⭐️ 9.0/10

**原标题**: [Firefox 157 will include JPEG XL by default on all platforms](https://groups.google.com/a/mozilla.org/g/dev-platform/c/3YMV4MS34KA?pli=1)

Firefox 157 将在所有平台上默认启用 JPEG XL 图像格式。社区消息表明 Chromium 也在效仿类似做法，采用这一格式。 浏览器默认支持是 JPEG XL 的一个重要里程碑，与旧版 JPEG 相比，它在压缩率和图像质量上更具优势。Firefox 和 Chromium 的广泛采用可能使 JPEG XL 成为标准的网页图像格式，惠及开发者和用户。 据报道，Firefox 和 Chromium 都将使用基于 Rust 的 jxl-rs 实现，而非 C++ 的 libjxl 库。这是继 Chromium 此前放弃 JPEG XL 支持之后的新动向，具体版本号和时间表仍在确认中。

hackernews · yboris · 8月25日 17:55 · [社区讨论](https://news.ycombinator.com/item?id=49437946)

**背景**: JPEG XL 是一种现代图像格式，支持有损和无损压缩，由联合图像专家组（JPEG）、Google 和 Cloudinary 共同开发。它是一个自由开放的标准（ISO/IEC 18181），在图像质量和压缩率上明显优于传统 JPEG，并且以软件实现即可高效编码和解码，即使在移动设备上也不需要硬件加速。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/JPEG_XL">JPEG XL - Wikipedia</a></li>
<li><a href="https://jpeg.org/jpegxl/">JPEG - JPEG XL</a></li>

</ul>
</details>

**社区讨论**: 评论者对于苹果在已有 C++ libjxl 支持的情况下的策略表示好奇，并希望看到 jxl-rs 与 libjxl 之间的基准测试。一些人欢迎 Chromium 对 JPEG XL 的采纳，认为这是对其先前立场的逆转，另一些人则提出了实际担忧，比如不支持 JPEG XL 的上传字段，以及 Windows 7/8 上旧版 Firefox ESR 的兼容性问题。

**标签**: `#JPEG XL`, `#Firefox`, `#Web Standards`, `#Image Compression`, `#Browsers`

---

<a id="item-3"></a>
## [FDA 批准首款连续监测酮体和血糖的可穿戴设备](https://www.fda.gov/news-events/press-announcements/fda-authorizes-first-wearable-device-continuously-monitors-both-ketone-levels-and-blood-sugar) ⭐️ 8.0/10

**原标题**: [FDA authorizes first wearable device that monitors ketone and blood sugar levels](https://www.fda.gov/news-events/press-announcements/fda-authorizes-first-wearable-device-continuously-monitors-both-ketone-levels-and-blood-sugar)

美国 FDA 已批准首款可同时连续监测酮体水平和血糖的可穿戴设备。这一监管里程碑为糖尿病管理增添了一种新工具。 对于糖尿病患者，尤其是 1 型糖尿病患者，同时追踪酮体和血糖有助于及早发现糖尿病酮症酸中毒等危险状况。这也标志着可穿戴设备向多生物标志物传感方向发展的更广泛趋势。 该设备可连续追踪两种生物标志物，但 FDA 公告未披露其传感机制。评论者提醒，酮体水平主要对极低碳水饮食者或血糖控制不佳的糖尿病患者有意义，且报销问题仍是主要障碍。

hackernews · sunnynagra · 8月25日 19:07 · [社区讨论](https://news.ycombinator.com/item?id=49439017)

**背景**: 酮体是身体在无法利用葡萄糖供能、转而燃烧脂肪时产生的分子，常见于禁食、极低碳水饮食或胰岛素不足等情况。连续血糖监测仪（CGM）是一种可穿戴设备，通过测量皮下组织间液中的葡萄糖来实时反映血糖变化趋势。连续监测酮体的能力有助于发现糖尿病酮症酸中毒——当酮体水平过高时，血液中酸性物质大量积聚的危险状态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://my.clevelandclinic.org/health/body/25177-ketones">Ketones: What They Are, Function, Tests &amp; Normal Levels</a></li>
<li><a href="https://www.cdc.gov/diabetes/treatment/continuous-glucose-monitors.html">Continuous Glucose Monitors | Diabetes | CDC</a></li>
<li><a href="https://en.wikipedia.org/wiki/Continuous_glucose_monitor">Continuous glucose monitor - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了情感和实用层面的回应：有人分享了朋友因糖尿病酮症酸中毒去世的亲身经历，也有人对无创血糖传感技术持怀疑态度，并质疑该设备对普通糖尿病患者的实用价值。不少人欢迎可穿戴设备迈向血糖检测的总体趋势，同时就现有替代产品和报销问题提出疑问。

**标签**: `#wearables`, `#health tech`, `#FDA`, `#diabetes`, `#medical devices`

---

<a id="item-4"></a>
## [苹果发布 M6 与 M5 Ultra 芯片，性能与 AI 算力大幅跃升](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/) ⭐️ 8.0/10

**原标题**: [Apple introduces M6 and M5 Ultra](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/)

2026 年 8 月 25 日，苹果发布了 M6 和 M5 Ultra 芯片。M6 是苹果首款 2nm 芯片，配备 12 核 CPU 和双 16 核神经引擎；M5 Ultra 则是苹果首款四晶粒 SoC，是迄今最强的芯片。 这标志着苹果芯片性能和 AI 算力的重大飞跃，可能重塑高端 Mac 产品线及竞争格局。M5 Ultra 的四晶粒架构和 M6 的 2nm 工艺将影响专业工作流、AI 开发与能效表现。 M5 Ultra 最高配备 36 核 CPU，包括 12 个超级核心和 24 个性能核心，与 M3 Ultra 相比单线程性能提升最高 1.25 倍、多线程性能提升最高 1.3 倍。它采用新一代 UltraFusion 技术连接四个晶粒；M6 则配备 12 核 GPU 和双 16 核神经引擎。

hackernews · interpol\_p · 8月25日 13:01 · [社区讨论](https://news.ycombinator.com/item?id=49433292)

**背景**: Apple silicon 是苹果为 Mac 和 iPad 设计的基于 ARM 的系统级芯片系列，最早于 2020 年随 M1 推出，取代了 Intel 处理器。此后 M 系列从基础芯片扩展到 Pro、Max 和 Ultra 版本，其中 M1 Ultra 通过 UltraFusion 互连组合了两颗 M1 Max 芯片。M5 Ultra 将这一概念扩展到四个晶粒，而 M6 则是首款采用 2nm 工艺的芯片。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/">Apple introduces M6 and M5 Ultra for a big leap in performance and AI compute - Apple</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_M6">Apple M6 - Wikipedia</a></li>
<li><a href="https://9to5mac.com/2026/08/25/apple-launches-next-gen-apple-silicon-chips-m6-and-m5-ultra/">Apple launches next-gen Apple Silicon chips: M6 and M5 Ultra - 9to5Mac</a></li>

</ul>
</details>

**社区讨论**: 评论者既兴奋又谨慎：一些人惊叹于性能提升，并认为尽管价格上涨仍有价值；另一些人则指出新款 Studio 机型的内存/存储升级成本较高。还有流传的传闻称，苹果可能跳过 M6 Pro/Max/Ultra，专注于 AI 导向的 M7 芯片，这引发了对其路线图的猜测。

**标签**: `#Apple`, `#Hardware`, `#AI-compute`, `#Chips`, `#Performance`

---

<a id="item-5"></a>
## [苹果发布搭载 M5 Max 与 M5 Ultra 的新 Mac Studio，主打本地 AI](https://www.apple.com/newsroom/2026/08/apple-introduces-new-mac-studio-with-m5-max-and-m5-ultra/) ⭐️ 8.0/10

**原标题**: [New Mac Studio with M5 Max and M5 Ultra](https://www.apple.com/newsroom/2026/08/apple-introduces-new-mac-studio-with-m5-max-and-m5-ultra/)

苹果发布了全新 Mac Studio，可选配 M5 Max 或 M5 Ultra 芯片，并称其为最强大的本地 AI 工作负载 Mac。M5 Ultra 是苹果首款四芯粒（quad-die）芯片，配备 36 核 CPU、80 核 GPU 和 1.2TB/s 内存带宽。 此次发布标志着苹果在端侧 AI 领域加速布局，为开发者与研究人员提供了高带宽统一内存架构，可在本地运行大规模模型。M5 Ultra 通过 4.4TB/s 的芯粒间互连将内存带宽提升至 M5 Max 的两倍，进一步巩固了苹果在 AI 推理定制芯片方面的领先地位。 M5 Max 此前已用于 14 英寸 MacBook Pro，拥有 18 核 CPU、32 核 GPU 和 460GB/s 内存带宽。苹果还强调两款芯片新增了“GPU 神经加速器”，而 512GB 内存的更大配置预计将于 10 月推出。

hackernews · interpol\_p · 8月25日 13:03 · [社区讨论](https://news.ycombinator.com/item?id=49433316)

**背景**: Mac Studio 是苹果面向视频剪辑师、开发者和研究人员的专业桌面产品线，定位介于 Mac mini 与 Mac Pro 之间。苹果 M 系列芯片采用统一内存架构，让 CPU 和 GPU 共享同一高带宽内存池，这是本地运行大语言模型的关键优势。此次发布延续了苹果在端侧 AI 领域的推进，此前 M5 Pro 与 M5 Max 已率先于 2026 年上半年搭载于 MacBook Pro。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/">Apple introduces M6 and M5 Ultra for a big leap in ...</a></li>
<li><a href="https://support.apple.com/en-us/126318">MacBook Pro (14-inch, M5 Pro or M5 Max) - Tech Specs - Apple Support</a></li>
<li><a href="https://www.macworld.com/article/2973459/2026-mac-studio-m5-release-date-specs-price-rumors.html">New Mac Studio M5 Max and M5 Ultra: Everything you need to ...</a></li>

</ul>
</details>

**社区讨论**: 评论者观点不一：有人因内存/SSD 短缺带来的定价“疯狂”而望而却步，也有人认为用 Mac Studio 作为常驻桌面的替代方案，比买一台长期连接扩展坞的 MacBook Pro 更合理。技术用户指出，1.2TB/s 的带宽对于超 1 万亿参数的模型来说仍不够“面向未来”，但估算在 Ultra 上以非量化模型运行可达到约 1,000 tokens/s 的预填充和 50+ tokens/s 的解码速度。还有评论称赞苹果积极拥抱“本地 AI”，并希望它能预装并针对性优化一个开放权重的前沿模型。

**标签**: `#apple`, `#hardware`, `#m5`, `#mac-studio`, `#ai`

---

<a id="item-6"></a>
## [Nitter 收到停止函，实例暂停服务等待法律咨询](https://github.com/zedeus/nitter/issues/1442) ⭐️ 8.0/10

**原标题**: [Nitter project received cease and desist](https://github.com/zedeus/nitter/issues/1442)

Nitter 项目收到了停止与终止函（cease and desist），导致所有公共 Nitter 实例在获得法律建议之前保持离线。该公告是通过项目仓库的 GitHub issue 发布的。 这对开源隐私工具领域意义重大，因为 Nitter 提供无广告、无追踪的 Twitter/X 访问方式。此次下架可能影响许多依赖 Nitter 无需账户即可查看 Twitter 内容的用户，尤其是在对 X 近期变化普遍不满的背景下。 维护者表示他们正在等待法律咨询，并预计所有实例将在“可预见的未来”保持离线。停止函的具体内容未公开透露，社区也在讨论哪些司法管辖区可能更不容易受到此类主张的影响。

hackernews · Banditoz · 8月25日 17:08 · [社区讨论](https://news.ycombinator.com/item?id=49437283)

**背景**: Nitter 是一个免费、开源的 Twitter 替代前端，注重隐私和性能，允许用户无需 JavaScript、广告或追踪即可浏览推文。它通常通过自托管或社区运行的实例来使用，这些实例承压比 Twitter 小得多，同时页面加载更快。该项目此前曾遭受 Twitter/X 的间歇性屏蔽，但正式的停止函更直接地升级了法律层面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nitter">Nitter - Wikipedia</a></li>
<li><a href="https://nitter.app/about">nitter</a></li>

</ul>
</details>

**社区讨论**: 评论区情绪复杂：有人感叹失去了访问仍在使用 X 的组织的渠道，也有人质疑该平台是否还有现实意义。一些用户推测可能为 Nitter 实例提供避风港的法律策略和司法管辖区；还有评论者借该话题称赞 Hacker News 版主支持社区项目而不是发下架函。

**标签**: `#Nitter`, `#privacy`, `#legal`, `#open source`, `#Twitter/X`

---

<a id="item-7"></a>
## [SpaceX 正式宣布 Starbase Louisiana 发射场](https://www.spacex.com/sites/starbase-la) ⭐️ 8.0/10

**原标题**: [Starbase, LA](https://www.spacex.com/sites/starbase-la)

SpaceX 已在其官网正式宣布 Starbase Louisiana，这是一个新的发射设施，此前已有多个月的传闻。该基地预计将为路易斯安那州沿海地区带来重大经济效益，并改善对太阳同步轨道的访问能力。 这标志着 SpaceX 将其发射基础设施从得克萨斯州和佛罗里达州进一步扩展，对轨道访问和区域经济发展具有重要意义。这也表明美国在雄心勃勃的大型太空项目上持续进行投资。 根据社区讨论，路易斯安那州的位置提供了通往太阳同步轨道（SSO）的优势，发射倾角相对于赤道约 98 度。一些评论者指出，公告页面的部分内容与其他部分几乎相同，引发了对 AI 生成内容的担忧。

hackernews · bilsbie · 8月25日 16:37 · [社区讨论](https://news.ycombinator.com/item?id=49436822)

**背景**: SpaceX 已经在得克萨斯州运营 Starbase，这是一个私人的发射设施和 Starship 的生产基地，并于 2025 年 5 月成立为一座城市。自 2010 年代末以来，公司一直将该基地作为下一代火箭开发的主要中心。新的路易斯安那州设施似乎遵循类似的模式，将发射业务设在经济落后的沿海地区。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Starbase">SpaceX Starbase</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一，但总体乐观：一些人强调这为贫困沿海地区的焊工、混凝土工人和承包商创造了就业机会，另一些人则对雄心勃勃的实体工程项目感到兴奋。然而，也有评论者对该公告的真实性表示怀疑，指出重复的文本可能是由大型语言模型生成的。

**标签**: `#SpaceX`, `#aerospace`, `#Louisiana`, `#space exploration`, `#infrastructure`

---

<a id="item-8"></a>
## [开放权重模型上的持续学习为主权 AI 提供路径](https://www.reddit.com/r/MachineLearning/comments/1vxvzju/continual_learning_of_frontier_models_for/) ⭐️ 8.0/10

**原标题**: [Continual Learning of Frontier Models for SovereignAI. Tech Report + Open Weights Model \[R\]](https://www.reddit.com/r/MachineLearning/comments/1vxvzju/continual_learning_of_frontier_models_for/)

一份新的技术报告介绍了 Thomson，这是一个通过在现成的开放权重模型上进行持续学习而构建的通用前沿模型。作者声称 Thomson 在显著降低算力和人力预算的情况下，达到了与近期前沿模型相当的性能。 该报告提供了一条具体且可短期实现的路径，使更广泛的机构能够获得前沿 AI 性能，从而解决少数大型开发者与更广泛的 AI 用户群体之间的经济和权力不对称问题。它直接支持主权 AI 的目标，使组织能够独立构建、部署和管理 AI 系统。 Thomson 专注于高风险专业工作，包括法律、税务、多语言和深度研究，并呈现出独特的π形性能模式：在多种能力上广泛提升，同时几乎完全消除了窄域适应中常见的灾难性遗忘问题。该方法强调持续学习、以数据为中心和高效率，在保持可塑性和稳定性的同时，对参数进行最少的高影响干预。

reddit · r/MachineLearning · /u/Forsaken\_Scientist · 8月25日 10:30

**背景**: 持续学习是一种 AI 方法，它让模型能够按顺序学习新任务，同时保留先前学到的知识，这与常导致灾难性遗忘的传统微调不同。开放权重模型是指训练好的参数被公开发布的 AI 模型，任何人都可以下载并修改它们。主权 AI 是指组织或国家利用自己的数据、基础设施和人才，独立开发、部署和治理 AI 的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2302.00487">[2302.00487] A Comprehensive Survey of Continual Learning: Theory, Method and Application</a></li>
<li><a href="https://www.ibm.com/think/topics/continual-learning">What is Continual Learning? | IBM</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**标签**: `#continual learning`, `#open-weight models`, `#AI sovereignty`, `#frontier models`, `#technical report`

---

<a id="item-9"></a>
## [Papers with Code 用 pgvector 与 Qwen3 实现 SOTA 混合搜索](https://www.reddit.com/r/MachineLearning/comments/1vxyrsr/how_we_built_a_sota_search_engine_using/) ⭐️ 8.0/10

**原标题**: [How we built a SOTA search engine using PostgreSQL, pgvector, and Qwen3 embeddings \[P\]](https://www.reddit.com/r/MachineLearning/comments/1vxyrsr/how_we_built_a_sota_search_engine_using/)

Hugging Face 工程师 Niels Rogge 发布了一篇技术详解，说明 Papers with Code 的搜索是如何工作的。该系统将关键词搜索与基于 PostgreSQL、pgvector 和 Qwen3-Embedding-0.6B 的语义搜索相结合，并报告称这种混合方法优于单独使用任何一种方法。 这展示了使用广泛可用的开源工具实现混合搜索的实际案例，为构建类似系统的开发者提供了有价值的参考。它还体现了搜索组件可兼任推荐引擎的常见模式，这正在成为机器学习平台的主流做法。 该技术栈包括用于向量相似性搜索的 pgvector、用于生成文本嵌入的 Qwen3-Embedding-0.6B、使用 NVIDIA L4 GPU 的 Hugging Face Jobs 用于批量嵌入生成，以及用于存储工件的 Hugging Face Buckets。实时嵌入模型通过 Hugging Face Inference Endpoints 提供，同一基础设施也为论文页面上的“相关论文”推荐提供支持。

reddit · r/MachineLearning · /u/NielsRogge · 8月25日 12:42

**背景**: 混合搜索将 BM25 等词汇（关键词）搜索与基于向量的语义搜索相结合，以提高相关性。这样做是必要的，因为纯关键词搜索会遗漏同义词，而纯向量搜索在精确匹配或罕见术语上可能不准确。pgvector 是一个开源的 PostgreSQL 扩展，增加了向量存储和近似最近邻搜索功能；Qwen3-Embedding-0.6B 是 Qwen 系列中的一个密集文本嵌入模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pgvector">Pgvector</a></li>
<li><a href="https://github.com/QwenLM/Qwen3-Embedding">GitHub - QwenLM/Qwen3-Embedding</a></li>
<li><a href="https://grokipedia.com/page/Hybrid_search">Hybrid search</a></li>

</ul>
</details>

**标签**: `#PostgreSQL`, `#pgvector`, `#embeddings`, `#hybrid search`, `#machine learning`

---