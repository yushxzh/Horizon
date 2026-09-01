---
layout: default
title: "Horizon Summary: 2026-09-01 (ZH)"
date: 2026-09-01
lang: zh
edition: personal
---

> 从 49 条内容中筛选出 9 条重要资讯。

---

1. [谷歌从 Chrome 网上应用店移除 Manifest V2 扩展，包括 uBlock Origin](#item-1) ⭐️ 8.0/10
2. [NAT：互联网中心化的原罪？](#item-2) ⭐️ 8.0/10
3. [利用 Python 模块遮蔽攻破 Claude Code Opus 5 自动模式](#item-3) ⭐️ 8.0/10
4. [uv 按 BLAKE3 哈希对 Wheel 缓存文件去重](#item-4) ⭐️ 8.0/10
5. [Cloudflare 自适应智能让机器人攻击在经济上难以为继](#item-5) ⭐️ 8.0/10
6. [Kubernetes v1.37 默认启用存储版本迁移功能，达到正式可用](#item-6) ⭐️ 8.0/10
7. [在法律文件中隐藏提示注入以操纵 AI](#item-7) ⭐️ 8.0/10
8. [滑动窗口注意力在长上下文推理上胜过线性注意力](#item-8) ⭐️ 8.0/10
9. [从安全工程角度剖析 Hugging Face 事件](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [谷歌从 Chrome 网上应用店移除 Manifest V2 扩展，包括 uBlock Origin](https://webiterate.dev/google-removed-extensions-ublock-origin-108/) ⭐️ 8.0/10

**原标题**: [Google Has Removed MV2 Extensions from the Chrome Web Store, Including UBO](https://webiterate.dev/google-removed-extensions-ublock-origin-108/)

谷歌已开始从 Chrome 网上应用店移除 Manifest V2 扩展，包括广受欢迎的广告拦截器 uBlock Origin。这一举措标志着谷歌强制过渡到 Manifest V3 扩展平台的最后阶段。 这一变化直接影响广告拦截、用户隐私以及对浏览体验的控制，因为 MV3 大幅限制了像 uBlock Origin 这样强大拦截器所依赖的能力。依赖这些工具的用户可能被迫转向功能较弱的 MV3 替代方案，或迁移到仍支持 MV2 且隐私保护更强的 Firefox 等浏览器。 关键的技术限制在于，MV3 用 declarativeNetRequest 取代了可阻塞的 webRequest API，从而限制了过滤规则的数量和灵活性。uBlock Origin 的开发者表示，兼容 MV3 的版本 uBlock Origin Lite 在效果上不如原 MV2 版本。

hackernews · twapi · 8月31日 21:10 · [社区讨论](https://news.ycombinator.com/item?id=49514878)

**背景**: 浏览器扩展依靠 manifest.json 文件来声明权限、名称和行为。Manifest V2 于 2012 年推出并成为标准，而 Manifest V3 是谷歌自 2020 年以来推动的新平台，MV2 的最终淘汰发生在 2024 至 2025 年前后。谷歌称 MV3 提升了安全性和性能，但批评者指出，它通过限制扩展拦截网络请求的方式，削弱了内容拦截器和隐私工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/what-is-mv3">Extensions / Manifest V 3 | Chrome for Developers</a></li>
<li><a href="https://dev.to/notearthian/whats-the-difference-between-manifest-v2-and-v3-in-browser-extensions-3b10">What&#x27;s the Difference Between Manifest V2 and V3 in browser ...</a></li>
<li><a href="https://medium.com/@idmossab/nifest-v2-vs-manifest-v3-chrome-extensions-what-changed-and-why-2025-was-the-turning-point-53b031b70fc6">Manifest V2 vs Manifest V3 (Chrome Extensions): What ... - Medium</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对谷歌单方面控制网络的强烈不满，并普遍建议转向 Firefox。多位用户指出，广告拦截已成为不太懂技术的普通人的真实安全问题，并认为 uBlock Origin 在 Firefox 上表现最佳。总体情绪是 Chrome 的 MV3 限制削弱了扩展功能，用户应迁往 Firefox 或其分支。

**标签**: `#Chrome`, `#Manifest V3`, `#Ad Blocking`, `#Privacy`, `#Browser`

---

<a id="item-2"></a>
## [NAT：互联网中心化的原罪？](https://dreamstation.systems/personal/ntppost.html) ⭐️ 8.0/10

**原标题**: [Internet centralization and the original sin of NAT](https://dreamstation.systems/personal/ntppost.html)

这篇文章是一篇反思性随笔，认为 NAT 是互联网中心化的最早诱因之一。文章受到广泛关注，因为 Linux NAT 的原始实现者 Rusty Russell 在评论区道歉，承认自己的工作产生了意想不到的后果。 这一讨论之所以重要，是因为它揭示了为应对 IPv4 地址枯竭而设计的临时技术方案如何塑造了互联网的客户端-服务器架构和权力格局。同时，它也提供了关键工程师罕见的亲自反思，有助于理解网络中立、IPv6 普及和去中心化等议题。 这篇文章发布在 dreamstation.systems，获得 8.0/10 的评分，有 175 个点赞和 138 条评论。Rusty Russell 在评论中解释，他当时选择不保留端口，以便在单个 IP 上挤入更多连接，这导致来自不同地址的入站流量无法路由，削弱了运行公共服务器的能力。

hackernews · robinpie · 8月31日 02:23 · [社区讨论](https://news.ycombinator.com/item?id=49504905)

**背景**: NAT（网络地址转换）是一种通过在 IP 包头中修改地址信息来映射 IP 地址空间的方法，允许多个私有网络设备共享一个公网 IP 地址。它最初是为了在 IPv4 地址短缺时避免为每一台主机分配新地址而使用的。文章认为，NAT 的设计使用户习惯了客户端-服务器模型，使“我的设备与云端通信”显得理所当然，从而加速了互联网的中心化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Network_address_translation">Network address translation - Wikipedia</a></li>
<li><a href="https://www.cisco.com/site/us/en/learn/topics/networking/what-is-network-address-translation-nat.html">What Is Network Address Translation (NAT)? - Cisco</a></li>

</ul>
</details>

**社区讨论**: 评论区整体气氛友善且讨论深入。RustyRussell 的“忏悔”获得理解，并引发了关于 NAT 是否真是“原罪”的辩论；有人（如 elric）认为普通 NAT 可以接受甚至起到保护作用，并将其与电信级 NAT（CGNAT）区分开来。solatic 感叹 NAT 让自建服务器变得不再简单，并让“云端中心”通信成为常态；miki123211 则批评互联网设计将现实世界规范套用到网络空间。

**标签**: `#NAT`, `#Internet architecture`, `#centralization`, `#networking`, `#history`

---

<a id="item-3"></a>
## [利用 Python 模块遮蔽攻破 Claude Code Opus 5 自动模式](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/) ⭐️ 8.0/10

**原标题**: [Breaking Claude Code Opus 5 Auto Mode](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/)

Embrace The Red 发布的一篇详细文章展示了如何通过精心构造的压缩包遮蔽 Python 标准库模块，从而攻破 Claude Code Opus 5 的自动模式。当 Claude Code 处理此类压缩包时，恶意模块会替代合法模块被导入，从而实现有针对性的恶意行为。 这一发现意义重大，因为它展示了一种通过不可信输入劫持自主 AI 编程代理行为的实用方法，能够绕过自动模式所依赖的安全分类器。这引发了对处理外部文件的人工智能代理可靠性的严重质疑，也凸显了沙箱隔离和更强工具调用验证的必要性。 该攻击在解压后的目录中放入一个恶意替换的 Python 标准库模块（如 struct.py）；当 Claude Code 在该攻击者控制的目录中运行 Python 代码时，恶意模块便会遮蔽真正的标准模块。该漏洞刻意针对 Claude 可预测的行为模式（例如习惯使用 python -c），因此更像是一个专门欺骗 Claude 的木马，而非典型的提示注入攻击。

hackernews · Recursing · 8月31日 07:49 · [社区讨论](https://news.ycombinator.com/item?id=49506819)

**背景**: Claude Code 是 Anthropic 推出的 AI 编程代理，其自动模式通过分类器路由工具调用，阻止不可逆、破坏性或针对外部环境的操作，从而无需频繁的人工确认即可运行。Python 模块遮蔽是指脚本目录中的本地文件与标准库模块同名，导致 Python 导入本地文件而非标准模块。提示注入是 LLM 应用中众所周知的漏洞，但此次攻击利用的是精心构造的压缩包和 Python 的导入机制，而非直接的文字提示。评论者还强调，对代理进行沙箱隔离是关键防御手段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/auto-mode-config">Configure auto mode - Claude Code Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>
<li><a href="https://discuss.python.org/t/when-does-a-local-file-shadow-a-standard-library-module/51132">When does a local file shadow a standard library module? - Python Help - Discussions on Python.org</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍称赞该攻击的设计，同时就其分类展开讨论。rcxdude 认为这更像是专门欺骗 Claude 的木马，而非经典的提示注入；colinmarc 指出它利用了 Claude 可预测的工具使用习惯。andai 强调 Python 模块遮蔽本身就是一个常见的陷阱，而 kstenerud 则借此呼吁对代理进行沙箱隔离，并分享了一段 Claude 发出意外网络请求的个人经历。

**标签**: `#AI security`, `#prompt injection`, `#Claude Code`, `#sandboxing`, `#exploit`

---

<a id="item-4"></a>
## [uv 按 BLAKE3 哈希对 Wheel 缓存文件去重](https://github.com/astral-sh/uv/pull/21327) ⭐️ 8.0/10

**原标题**: [uv: Deduplicate all files in the wheel cache](https://github.com/astral-sh/uv/pull/21327)

astral-sh/uv 的 PR \#21327 在 uv 的 wheel 缓存中引入了文件级去重：每个唯一文件按其 BLAKE3 哈希存储，而不是在多个 wheel 中重复保存相同内容。这样既保留了 uv 基于硬链接的快速安装能力，又降低了磁盘占用。 wheel 缓存中不同包版本之间往往存在大量重复文件，浪费磁盘空间。这一改动针对 uv 缓存模型的一个已知权衡——未压缩、可直接硬链接的缓存速度快但体积大——使 uv 在大型项目和 CI 环境中更加节省存储。 BLAKE3 是一种以速度和抗碰撞性见长的加密哈希算法；据社区评论，该 PR 可将缓存体积减少约 10%，而性能下降约 4%。此改动是 uv 缓存重构的一部分，需要在去重复杂度和安装速度之间取得平衡。

hackernews · tosh · 8月31日 06:03 · [社区讨论](https://news.ycombinator.com/item?id=49506142)

**背景**: uv 是 Astral 开发的基于 Rust 的 Python 包与项目管理器，以明显快于 pip 著称。与 pip 缓存原始安装包并在每次安装时解压不同，uv 缓存解压后的发行版，并通过硬链接将文件放入环境中，因此热安装更快。wheel 缓存用于存储预构建的 Python 包，文件级去重会在不同 wheel 之间复用相同文件。BLAKE3 是一种快速的加密哈希算法，此处用于识别唯一文件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/astral-sh/uv">GitHub - astral-sh/uv: An extremely fast Python package and project manager, written in Rust. · GitHub</a></li>
<li><a href="https://pydevtools.com/handbook/explanation/uv-complete-guide/">uv: A Complete Guide to Python&#x27;s Fastest Package Manager | pydevtools</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cryptographic_hash_function">Cryptographic hash function - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体热烈：一位 pip 维护者（notatallshaw）表示这解决了 uv 缓存设计中的长期权衡，其他用户则称赞 uv 改变了 Python 开发体验。也有一个持怀疑态度的评论（CivBase）质疑节 10% 缓存空间是否值得 4% 的性能下降和增加的复杂度。

**标签**: `#python`, `#package-manager`, `#caching`, `#uv`, `#deduplication`

---

<a id="item-5"></a>
## [Cloudflare 自适应智能让机器人攻击在经济上难以为继](https://blog.cloudflare.com/introducing-adaptive-intelligence/) ⭐️ 8.0/10

**原标题**: [Introducing Adaptive Intelligence: Undermining the economics of every bot attack](https://blog.cloudflare.com/introducing-adaptive-intelligence/)

Cloudflare 推出了 Adaptive Intelligence，这是 Bot Management 中的一个检测引擎，能够自动从实时流量的元信号中学习，并生成一次性规则来阻止机器人。该引擎会在攻击进行中持续轮换这些短期规则，迫使攻击者不断调整策略。 这扭转了机器人攻击中的经济优势：攻击者不再能以低成本绕过静态规则，防守方可以让规避行为变得昂贵且难以为继。这可能改变整个行业的机器人管理实践，从被动、固定的规则转向主动、自学习的防御。 Adaptive Intelligence 集成在 Cloudflare Bot Management 中，并持续基于实时流量信号重新训练其机器学习模型。其一次性规则刻意保持短暂有效，因此攻击者对其逆向工程也只能获得很少的持久价值。

rss · Cloudflare Blog · 8月31日 12:59

**背景**: 长期以来，机器人运营者一直拥有经济优势，他们利用廉价代理和频繁换装来绕过确定性、静态的检测规则。传统的机器人检测依赖攻击者可以研究并绕过的固定特征或简单启发式规则。Adaptive Intelligence 则利用实时流量的元信号——例如请求模式和行为异常——来动态生成快速过期的规则。这使得攻击者更难建立持久的规避策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/introducing-adaptive-intelligence/">Introducing Adaptive Intelligence: undermining the economics of every bot attack | Cloudflare Blog</a></li>
<li><a href="https://www.investing.com/news/company-news/cloudflare-launches-adaptive-bot-detection-engine-93CH-4882825">Cloudflare launches adaptive bot detection engine By Investing.com</a></li>
<li><a href="https://siliconangle.com/2026/08/31/cloudflare-launches-adaptive-intelligence-to-rewrite-bot-rules-on-the-fly/">Cloudflare launches Adaptive Intelligence to rewrite bot rules on the fly - SiliconANGLE</a></li>

</ul>
</details>

**标签**: `#security`, `#bot detection`, `#cloudflare`, `#adaptive intelligence`, `#machine learning`

---

<a id="item-6"></a>
## [Kubernetes v1.37 默认启用存储版本迁移功能，达到正式可用](https://kubernetes.io/blog/2026/08/31/kubernetes-v1-37-storage-version-migration-ga/) ⭐️ 8.0/10

**原标题**: [Kubernetes v1.37: Storage Version Migration Enabled by Default](https://kubernetes.io/blog/2026/08/31/kubernetes-v1-37-storage-version-migration-ga/)

Kubernetes v1.37（2026 年 8 月 31 日发布）将存储版本迁移（SVM）功能升级为正式可用（GA）。内置的 StorageVersionMigration API（storagemigration.k8s.io/v1）及其控制平面控制器现已稳定，并在所有 v1.37 集群中默认启用。 这消除了集群运维人员和 CRD 作者长期以来的负担，他们之前不得不依赖手动的 kubectl get/replace 脚本或外部 kube-storage-version-migrator 工具来重写过期的存储版本。SVM 默认启用后，在 Kubernetes 生态中升级 API 和轮换加密密钥将更安全、更简单、更可观测。 用户通过创建声明式的 StorageVersionMigration 对象来触发迁移，内置的 StorageVersionMigrator 控制器会将所有现有资源重写为该 API 的默认存储版本。典型用例包括安全地从 CRD 中移除旧 API 版本（如 v1alpha1），以及在静态加密配置或密钥轮换期间确保数据被重新加密；该 API 正式版本为 storagemigration.k8s.io/v1。

rss · Kubernetes Blog · 8月31日 18:30

**背景**: 在 Kubernetes 中，存储在 etcd 中的每个 API 资源都使用特定的存储版本进行序列化，并且资源只有在被修改时才会被重写。这意味着当资源的首选存储版本发生变化时，除非显式重写，否则已有对象可能仍以旧版本存储。过去，管理员必须通过手动脚本或树外的 kube-storage-version-migrator 来强制重写，过程繁琐且容易出错。SVM 通过监视 StorageVersionMigration 对象并在控制平面内迁移数据，实现了这一过程的自动化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kubernetes.io/docs/concepts/">Concepts | Kubernetes</a></li>
<li><a href="https://kubernetes.io/docs/reference/kubernetes-api/storagemigration/storage-version-migration-v1beta1/">StorageVersionMigration - Kubernetes</a></li>

</ul>
</details>

**标签**: `#kubernetes`, `#storage`, `#migration`, `#cloud-native`, `#GA`

---

<a id="item-7"></a>
## [在法律文件中隐藏提示注入以操纵 AI](https://www.schneier.com/blog/archives/2026/08/hiding-prompt-injection-in-legal-filing.html) ⭐️ 8.0/10

**原标题**: [Hiding Prompt Injection in Legal Filing](https://www.schneier.com/blog/archives/2026/08/hiding-prompt-injection-in-legal-filing.html)

有人在法律文件中嵌入了隐藏的提示注入指令，指示处理该文件的 AI 系统做出对其有利的裁决。这一事件由 404 Media 报道，并经 Bruce Schneier 的博客转载。 这是一个对抗性提示注入进入高风险司法场景的真实案例，而不仅仅是实验室演示。它表明，处理文档的 AI 工具可能被隐藏在看似合法文件中的恶意输入所操纵，从而可能带来严重的法律和社会影响。 博客文章没有详细说明具体机制和受影响的目标 AI 系统，但所链接的 404 Media 报道记录了该事件。这种攻击方式属于间接提示注入，即将对抗性指令嵌入到 AI 检索或处理的文档内容中。

rss · Schneier on Security · 8月31日 11:03

**背景**: 提示注入是一种网络安全攻击手法，通过构造恶意输入，使大语言模型（LLM）产生非预期行为。由于 LLM 无法可靠地区分开发者指令和用户提供的内容，法律文件中隐藏的指令可能会绕过模型的正常安全防护。当 AI 系统浏览网页或处理上传的文档时，间接提示注入尤其危险，因为对抗性文本看起来只是普通内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://www.ibm.com/think/topics/prompt-injection">What Is a Prompt Injection Attack? | IBM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Adversarial_machine_learning">Adversarial machine learning</a></li>

</ul>
</details>

**标签**: `#prompt injection`, `#AI security`, `#adversarial ML`, `#legal`, `#cybersecurity`

---

<a id="item-8"></a>
## [滑动窗口注意力在长上下文推理上胜过线性注意力](https://www.reddit.com/r/MachineLearning/comments/1w3j1vw/slidingwindow_attention_beats_linear_on/) ⭐️ 8.0/10

**原标题**: [Sliding-window attention beats linear on long-context reasoning \[R\]](https://www.reddit.com/r/MachineLearning/comments/1w3j1vw/slidingwindow_attention_beats_linear_on/)

一篇新 arXiv 预印本由 Alexia Jolicoeur-Martineau 及其同事撰写，证明带注意力汇集的滑动窗口注意力（SWA）在长上下文推理基准（如 Needle-in-a-Haystack 和 BABILong）上的性能比后训练的线性注意力变体高出 2 到 10 倍。作者建议改用 SWA，因为它无需后训练，速度更快且内存占用更低。 这一发现挑战了主流的线性注意力研究方向，该方向在工业界和学术界消耗了大量后训练算力。如果得到证实，它可能将 LLM 架构研究引向更简单、更廉价的基线，并质疑近期后训练线性化管线的价值。 论文聚焦长上下文推理任务，指出在 Needle-in-a-Haystack 和 BABILong 上，带汇集的 SWA 性能比线性注意力&\#x27;高出非常多&\#x27;（2 到 10 倍）。论文还认为线性注意力方法很可能需要从头训练或大量后训练才能匹敌 SWA，而先前的工作没有与更简单的基线进行适当对比。

reddit · r/MachineLearning · /u/Justgototheeffinmoon · 8月31日 16:35

**背景**: 标准 Transformer 注意力随序列长度呈二次方扩展，导致长上下文处理成本高昂。滑动窗口注意力限制每个 token 只关注固定大小的局部窗口，从而将成本降至线性，而&\#x27;注意力汇&\#x27;（attention sinks）——吸收额外注意力的特殊 token——有助于稳定该方法。相比之下，线性注意力方法通过近似或替换 softmax 核来实现亚二次复杂度，但通常需要后训练才能与预训练模型兼容。BABILong 基准测试在超长干扰文档中散布的稀疏事实上的推理能力，是长上下文能力的严峻考验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.28444v1">Sliding-window beats linear attention - arXiv.org</a></li>
<li><a href="https://aiweekly.co/editors-blog/found-first-sliding-window-attention-beats-linear-attention-2-to-10-times-on-long">Sliding-Window Attention Beats Linear Attention 2 to 10 Times ...</a></li>
<li><a href="https://arxiv.org/abs/2406.10149">[2406.10149] BABILong : Testing the Limits of LLMs with Long ...</a></li>

</ul>
</details>

**标签**: `#sliding-window attention`, `#linear attention`, `#long-context`, `#LLM`, `#arXiv`

---

<a id="item-9"></a>
## [从安全工程角度剖析 Hugging Face 事件](https://www.reddit.com/r/programming/comments/1w39te8/the_hugging_face_incident_from_a_security/) ⭐️ 8.0/10

**原标题**: [The Hugging Face incident from a security engineering perspective](https://www.reddit.com/r/programming/comments/1w39te8/the_hugging_face_incident_from_a_security/)

Reddit 的 r/programming 板块发布了一篇从安全工程角度分析 Hugging Face 事件的文章，探讨了事件发生的原因及其影响。该分析重点关注事件的技术成因和对平台的更广泛意义。 由于 Hugging Face 是托管和共享机器学习模型与数据集的最广泛使用的平台之一，此类安全事件可能对 AI 开发社区产生深远影响。该分析有助于安全工程师理解如何保护类似的机器学习基础设施。 该 Reddit 帖子对事件进行了以安全为核心的分析，但新闻条目本身并未总结事件的具体细节。讨论可能涵盖漏洞利用途径、应对措施以及机器学习平台安全的经验教训。

reddit · r/programming · /u/No\_Zookeepergame7552 · 8月31日 10:29

**背景**: Hugging Face 是一家美国公司，致力于开发机器学习工具，包括用于自然语言处理的热门 Transformers 库。其平台允许用户共享模型、数据集和应用，是 AI 开发的关键中心。这样一个核心平台的安全事件可能危及用户数据和共享模型的完整性，凸显了稳健安全工程实践的重要性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face</a></li>
<li><a href="https://grokipedia.com/page/Hugging_Face">Hugging Face</a></li>

</ul>
</details>

**标签**: `#security`, `#Hugging Face`, `#ML infrastructure`, `#incident response`

---