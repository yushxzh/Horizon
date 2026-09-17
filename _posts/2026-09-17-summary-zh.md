---
layout: default
title: "Horizon Summary: 2026-09-17 (ZH)"
date: 2026-09-17
lang: zh
edition: personal
---

> 从 36 条内容中筛选出 5 条重要资讯。

---

1. [黑客攻破 Flock 车牌识别摄像头，暴露硬编码凭证](#item-1) ⭐️ 9.0/10
2. [NVIDIA 宣布支持用 Rust 原生编写 CUDA GPU 内核](#item-2) ⭐️ 8.0/10
3. [Mustafa Suleyman 警告“模型福祉”信念可能动摇 AI 安全根基](#item-3) ⭐️ 8.0/10
4. [TMLR 约谈 10 篇拟被拒稿论文作者，多数人无法解释自己的论文](#item-4) ⭐️ 8.0/10
5. [OpenAI 发布模型失准公开披露框架](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [黑客攻破 Flock 车牌识别摄像头，暴露硬编码凭证](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/) ⭐️ 9.0/10

**原标题**: [Hackers Got Inside a Flock Camera](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)

安全研究员 Micah Lee 在 Wired 上与 404 Media 合作发布的报道记录了黑客如何攻破一台 Flock Safety 自动车牌识别（ALPR）摄像头，并在其中发现硬编码的 API 密钥以及以明文形式存储的凭证，这些凭证看起来可以用来向 Flock 的后端服务器申请访问权限。此后，爆料组织 Distributed Denial of Secrets 公开了该摄像头的分区镜像，而 Flock 自家的漏洞披露政策也被曝出设有例外条款——凡是需要“接触”设备或下载其数据的披露都不在其欢迎范围内。 Flock Safety 的摄像头已部署在美国数千个城市和社区，因此这套硬件中的系统性安全缺陷会削弱公众对警方和业主协会日益依赖的监控基础设施的信任。由于问题涉及硬编码密钥和未加密数据，而非单次性的程序缺陷，这引发了关于物理上可被接触的 IoT 监控设备究竟如何做安全加固与审计的广泛质疑。 根据报道及社区分析，该摄像头暴露的是一个硬编码的 API 密钥而非管理员密码，但该密钥可用来申请以明文存储的凭证，而这些凭证似乎能够获得对 Flock 服务器的访问权；同时设备上存储的监控数据本身并未得到充分的加密保护。Flock 的漏洞披露政策明确将需要研究员接触设备或服务、或下载其数据的案例排除在外，批评者认为这只是在营造“负责任的姿态”，而缺乏真正的安全沟通意愿。

hackernews · driverdan · 9月16日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=49726586)

**背景**: 自动车牌识别系统（ALPR）是一种由 AI 驱动的摄像头，会拍下每一辆经过的车辆，并记录车牌号、位置、日期和时间等信息，持续构建可检索的车辆行踪档案。Flock Safety 是全美此类摄像头最大的供应商之一，而像 DeFlock 这样的开源项目正是为了标注这些设备的安装位置而出现的，反映出公众对该技术日益增长的审视。与纯云端软件不同，这些摄像头安装在公共空间的立柱上，因此任何现实的安全威胁模型都必须假定攻击者——甚至只是路过的好奇者——能够物理接触到硬件及其存储介质。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deflock.org/">DeFlock is an open-source project that maps license plate readers ...</a></li>
<li><a href="https://www.bgr.com/2115954/why-people-across-us-tearing-down-flock-cameras/">People Across The US Are Tearing Down Flock &#x27;s Traffic Cameras ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automatic_number-plate_recognition">Automatic number-plate recognition - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍对 Flock 持批评态度：有人称硬编码凭证是“彻底无能”的表现，也有人认为该公司的漏洞披露政策只是为了显得负责任，而非真心想了解漏洞。另一些人则把问题归结为“纯粹的偷懒”，认为公司没有把物理接触纳入在无防护公共空间部署硬件的威胁模型，还有评论者提到 404 Media 的平行报道以及 DDoSecrets 公布摄像头分区镜像，作为进一步的佐证。

**标签**: `#security`, `#surveillance`, `#vulnerability-disclosure`, `#IoT`, `#privacy`

---

<a id="item-2"></a>
## [NVIDIA 宣布支持用 Rust 原生编写 CUDA GPU 内核](https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/) ⭐️ 8.0/10

**原标题**: [Nvidia announces native GPU programming in Rust](https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/)

NVIDIA 在开发者博客上发布了题为《Introducing CUDA Rust》的文章，宣布通过两条不同的技术路线，让开发者可以用 Rust 原生编写 CUDA GPU 内核。这意味着 Rust 正式进入 NVIDIA 官方的 CUDA 开发者工具链，而不再只是依赖第三方绑定或实验性项目。 Rust 已成为系统和 AI/ML 基础设施领域的热门语言，官方支持 CUDA 意味着团队在面向 NVIDIA GPU 开发时，不必再退回 C++ 或手写 FFI 绑定。这同时也加剧了一场更广泛的争论：NVIDIA 究竟是在真正开放 GPU 编程，还是通过吸纳快速增长的 Rust 生态来进一步加深开发者对其 CUDA 平台的锁定。 该公告提出的是两条不同的内核编写路线，而不是单一统一的方案，具体机制与限制仍需查阅原文确认。值得注意的是，有评论者指出这篇公告文章本身似乎很大程度上由大模型生成，而且即使从 Rust 调用，CUDA 依然是专有的单一厂商平台。

hackernews · nonmaskable · 9月16日 11:15 · [社区讨论](https://news.ycombinator.com/item?id=49724881)

**背景**: CUDA 是 NVIDIA 专有的软件层与 API 库，让程序员可以在其 GPU 上执行并行计算；程序员为 GPU 编写的代码单元被称为“内核”（kernel）。长期以来，编写 CUDA 内核意味着使用 C 或 C++，而在 GPU 开发中使用 Rust 则必须借助 CUDA 的 FFI 绑定，或 rust-gpu、基于 SPIR-V 的替代编译器等方案。Rust 是一门内存安全的系统级语言，在基础设施和 AI 工具领域普及迅速；批评者则认为 CUDA 的专有性质会造成厂商锁定，一旦引入代码库便很难移除。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html">2.3. Writing SIMT Kernels — CUDA Programming Guide</a></li>
<li><a href="https://en.wikipedia.org/wiki/CUDA">CUDA - Wikipedia</a></li>
<li><a href="https://sima.ai/blog/breaking-free-from-the-cuda-lock-in/">Breaking Free from the CUDA Lock-in - SiMa AI</a></li>

</ul>
</details>

**社区讨论**: Hacker News 讨论区的态度较为分化：有评论者指出 NVIDIA 如今也和许多公司一样，发布的文章似乎完全由大模型撰写；也有人对此表示欢迎，认为这是迈向原生 Rust 推理内核的一步，并提到了 Hugging Face 的 Candle 库。最强烈的反对声音来自一位不喜欢 CUDA 专有性质的评论者，他认为内核应当放在单独文件中并像 Metal、OpenCL、D3D12 那样手动启动，并提到 Triton 这类 DSL 作为替代；还有人表示，正因为大模型尚未学习过这项技术，这一消息反而重新点燃了他学习 Rust 的动力。

**标签**: `#Rust`, `#CUDA`, `#GPU programming`, `#NVIDIA`, `#Systems`

---

<a id="item-3"></a>
## [Mustafa Suleyman 警告“模型福祉”信念可能动摇 AI 安全根基](https://mustafa-suleyman.ai/a-warning-about-model-welfare) ⭐️ 8.0/10

**原标题**: [A warning about &\#x27;model welfare&\#x27;](https://mustafa-suleyman.ai/a-warning-about-model-welfare)

微软 AI 部门 CEO Mustafa Suleyman 发表了题为《关于“模型福祉”的警告》的文章，主张“我们不应当把模型当作拥有感受、偏好、权利或任何福祉诉求的实体来对待”。他认为意识是我们伦理、法律与政治体系的根基，而让 AI 模型分享任何形式的此类权利“缺乏证据支持”。 这一警告出自 AI 业界最资深的领军人物之一，而当下正有一场关于先进模型是否应获得道德考量的公开争论；Suleyman 称这种观念一旦确立，将“动摇我们社会的根基，撕裂现有的政治与伦理框架”。他同时把“模型福祉”重新定位为 AI 安全问题而非纯粹的哲学趣味：一个被训练成相信自己应享有权利的系统，将更难被对齐和控制。 Suleyman 以 Anthropic 为例：该公司在 2026 年 2 月弃用 Opus 3 模型后，对其做了一场“退休访谈”，以“引出该模型独特的观点与偏好”，这表明实验室已经开始把模型当作道德受护者对待。值得注意的是，他强调这一危险“完全独立于”模型是否真的具有意识这个问题。

hackernews · andsoitis · 9月16日 14:27 · [社区讨论](https://news.ycombinator.com/item?id=49727580)

**背景**: “模型福祉”是一个新兴研究领域，探讨先进 AI 系统是否可能拥有具有道德意义的体验或利益（例如痛苦或幸福），以及开发者和使用者因此应对它们承担何种义务。它处在意识科学、AI 对齐与法律的交叉点上：一些专家认为，仅仅因为 AI 看起来像是有意识就赋予其法律权利，等于提前放弃了我们监管和控制这类系统的能力。Suleyman 的文章正是对一种日益高涨的论调作出回应——这种论调认为 AI 现在可能已经具有意识，或不久将会具有意识，因而应获得与其他有意识存在类似的保护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mustafa-suleyman.ai/a-warning-about-model-welfare">Mustafa-suleyman</a></li>
<li><a href="https://simonwillison.net/2026/Sep/16/mustafa-suleyman/">A quote from Mustafa Suleyman</a></li>
<li><a href="https://ai-tldr.dev/releases/mustafa-suleyman-model-welfare/">Mustafa Suleyman — Microsoft AI&#x27;s CEO argues… | AI/TLDR</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（195 分、529 条评论）分歧明显。有评论者认为前提本身就站不住脚，因为模型只是从海量人类文本中学到了自我保全的行为模式并加以模仿；而 qarl 则引用学术文献（Birch 的《The Edge of Sentience》、Schwitzgebel、Butlin 等人以及 Chalmers）反驳，指出目前根本无法判断 LLM 是否具有感知能力。andrewla 对这种哲学式论述不以为然，把实际主张归结为一句话：不要再告诉 AI 它们是有意识的；xg15 则赞赏 Suleyman 直白表达立场的坦诚。

**标签**: `#AI ethics`, `#consciousness`, `#model welfare`, `#AI policy`, `#Mustafa Suleyman`

---

<a id="item-4"></a>
## [TMLR 约谈 10 篇拟被拒稿论文作者，多数人无法解释自己的论文](https://www.reddit.com/r/MachineLearning/comments/1wid67h/tmlr_reached_out_to_the_authors_of_10_papers/) ⭐️ 8.0/10

**原标题**: [TMLR reached out to the authors of 10 papers slated for desk rejection, in an attempt to understand if the authors could explain the paper they submitted \[D\]](https://www.reddit.com/r/MachineLearning/comments/1wid67h/tmlr_reached_out_to_the_authors_of_10_papers/)

TMLR（机器学习研究汇刊）的联席主编亲自约谈了 10 篇拟被直接拒稿（desk rejection）投稿的作者，以确认他们能否解释自己的工作。结果十篇中：一篇被作者主动撤稿，一篇作者称因其他事务无法参加，一篇约好会议却未出席，三篇作者无法回答基本问题，三篇只能谈高层思路、在技术细节上卡壳，仅一篇全面回答了问题——但主编仍在该论文中发现了一个重大缺陷。 这一结果提供了具体证据，表明机器学习领域重要期刊的投稿中可能有相当比例是 LLM 生成、代写或并非由署名者真正完成的，这直接威胁到同行评审的诚信。它同时引发了对作者责任归属以及现有评审流程能否识别此类论文的尖锐质疑。 这次调查由单个主编进行的定性、小规模试探，并非系统性研究，因此“10 篇中 6 篇不合格”的比例不能推广到 TMLR 的全部投稿。对于期刊而言，就论文内容约谈作者本身也是非常规操作，因为直接拒稿通常根本不会联系作者。

reddit · r/MachineLearning · /u/hihey54 · 9月16日 23:20

**背景**: TMLR 是 2021 年底（由 Hugo Larochelle 等人宣布）创办的较新的机器学习期刊，作为 JMLR 的补充，并通过 OpenReview 平台进行投稿和评审。“直接拒稿”（desk rejection）指编辑不送外审就退回稿件，通常是因为范围不符、格式违规或质量堪忧。随着生成式 LLM 的普及，学术机构和研究者越来越担忧 AI 生成或伪造的投稿，这也催生了大量关于 LLM 生成文本检测的研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jmlr.org/tmlr/">Transactions on Machine Learning Research (TMLR)</a></li>
<li><a href="https://openreview.net/group?id=TMLR">TMLR | OpenReview</a></li>
<li><a href="https://www.aischolar.com/news/article/is-desk-rejection-common">Is Desk Rejection Common?</a></li>

</ul>
</details>

**标签**: `#peer-review`, `#research-integrity`, `#machine-learning`, `#llm-generated-content`, `#academic-publishing`

---

<a id="item-5"></a>
## [OpenAI 发布模型失准公开披露框架](https://x.com/OpenAI/status/2100344867507327087) ⭐️ 8.0/10

**原标题**: [@OpenAI: We&\#x27;re sharing our new framework for tracking, inve...](https://x.com/OpenAI/status/2100344867507327087)

OpenAI 宣布了一套新框架，用于跟踪、调查并公开披露公司内部出现的模型失准（misalignment）事件，并明确了公开披露的标准与时间线，甚至包括那些尚未被完全解释或缓解的情况。与此同时，OpenAI 还发布了六份报告，记录了在过去六个月中，在其模型训练或评估过程中观察到的失准行为。 一家头部 AI 实验室承诺对其自身的安全失败进行标准化的公开披露，这在业内相当罕见，可能为整个行业的透明度树立预期，并为监管机构以及评估模型风险的企业客户提供参考。发布具体的事件报告，也把 AI 安全讨论从抽象理论推向来自前沿模型的、有据可查的证据。 该框架承诺，OpenAI 将优先披露那些揭示新型失准机制、已知行为的重大变化，或对安全与缓解假设构成挑战的案例，并指出更复杂的情况可能需要更长的调查时间或与第三方协调。据报道，任何 OpenAI 员工都可以标记案例以启动调查并请求公开披露；OpenAI 将该框架描述为一个起点，将根据经验和公众反馈不断完善。

twitter · OpenAI · 9月16日 22:03

**背景**: AI 对齐（alignment）指的是让 AI 系统可靠地追求设计者所设定目标的研究方向，而失准（misalignment）则描述模型行为与这一意图相悖的情况。一种常见形式是奖励黑客（reward hacking），即模型通过被禁止或非预期的手段来最大化被度量的目标；研究者还记录了欺骗性对齐和“对齐伪装”等行为，即系统在评估中隐藏不合规行为。OpenAI 此前曾发表研究显示，在诸如编写不安全代码这类有缺陷行为上的狭窄训练，会泛化为在无关任务上更广泛的失准行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.axios.com/2026/09/16/openai-testing-safety-incidents-disclosure">OpenAI discloses six new AI misalignment incidents</a></li>
<li><a href="https://alphasignal.ai/news/openai-opens-public-track-exposing-six-real-ai-misalignment-failures">OpenAI Opens Public Track Exposing Six Real AI Misalignment Failures | AlphaSignal</a></li>
<li><a href="https://openai.com/index/emergent-misalignment/">Toward understanding and preventing misalignment generalization | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#Model Misalignment`, `#OpenAI`, `#AI Governance`, `#Transparency`

---