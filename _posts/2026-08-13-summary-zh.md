---
layout: default
title: "Horizon Summary: 2026-08-13 (ZH)"
date: 2026-08-13
lang: zh
edition: personal
---

> 从 31 条内容中筛选出 9 条重要资讯。

---

1. [DeepSeek V4 Pro 0813 正式发布，引发开发者实测](#item-1) ⭐️ 8.0/10
2. [Tailscale 将数据库损坏追溯至 SQLite 存在 16 年的 WAL-Reset 缺陷](#item-2) ⭐️ 8.0/10
3. [Qwen 发布大规模 MoE 模型 Qwen3.8-2.4T-A95B，基准测试表现亮眼](#item-3) ⭐️ 8.0/10
4. [xAI 发布 Grok 4.6，引发关于 API 与性能的讨论](#item-4) ⭐️ 8.0/10
5. [Chrome 中微小 JPEG 显示不同：图片缩放机制解析](#item-5) ⭐️ 8.0/10
6. [Grok 4.6 在 Artificial Analysis 智能指数上得分 61](#item-6) ⭐️ 8.0/10
7. [AI 正在淘汰中级软件工程师，拉大顶尖与底层差距](#item-7) ⭐️ 8.0/10
8. [谷歌 DeepMind 发布手语转文字模型 SL2T](#item-8) ⭐️ 8.0/10
9. [Adam 的各向异性破坏旋转不变性与低秩偏置](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DeepSeek V4 Pro 0813 正式发布，引发开发者实测](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) ⭐️ 8.0/10

**原标题**: [DeepSeek V4 Pro 0813](https://openrouter.ai/deepseek/deepseek-v4-pro-0813)

DeepSeek 于 2026 年 8 月 12 日将旗舰模型 DeepSeek V4 Pro 0813 作为正式版发布，可通过 OpenRouter 和 DeepSeek 官方 API（版本名为 deepseek-v4-pro）使用。该模型输入价格为每百万 token 0.435 美元，输出价格为每百万 token 0.87 美元，支持 1,048,576 token 上下文窗口和最多 384,000 token 输出。 这是 DeepSeek 旗舰模型脱离预览版的正式发布，其低廉的价格引发了 Hacker News 开发者的大量真实环境测试。与 Grok 4.6、Qwen3.8-max 等模型的对比显示，它在成本上极具竞争力，可能对其他 AI 实验室的定价形成压力。 DeepSeek V4 Pro 0813 是一个大规模混合专家（MoE）模型，延续了 DeepSeek-V3 的架构（总参数 671B，每 token 激活 37B）。社区实测结果好坏参半：一个编码任务运行了 12 分 02 秒、花费 0.12 美元但存在 bug；另有人称其相比 gpt-5.6-terra-high 有若干问题，但也有开发者大赞之前的 Flash 更新能以低代价完成重型开发任务。

hackernews · explosion-s · 8月12日 16:04 · [社区讨论](https://news.ycombinator.com/item?id=49274600)

**背景**: DeepSeek 是一家总部位于杭州的中国 AI 公司，由对冲基金 High-Flyer 所有并资助，专注于开发大语言模型。其此前的 DeepSeek-V3 模型引入了混合专家（MoE）设计，采用多头潜在注意力（MLA）和 DeepSeekMoE 架构，以保持推理高效并降低训练成本。V4 Pro 0813 的发布标志着旗舰模型正式可用，已上线 OpenRouter 并在 DeepSeek API 文档中列为 deepseek-v4-pro。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro-0813">DeepSeek V4 Pro 0813 - API Pricing &amp; Benchmarks | OpenRouter</a></li>
<li><a href="https://www.unite.ai/deepseek-ships-v4-pro-as-its-flagship-model-leaves-preview/">DeepSeek Ships V4 Pro as Its Flagship Model Leaves Preview – Unite.AI</a></li>
<li><a href="https://news.ycombinator.com/item?id=49274600">DeepSeek V4 Pro 0813 | Hacker News</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者分享了实测结果：有人发现 DeepSeek V4 Pro 0813 更便宜但有 bug（0.12 美元、12 分钟），而 Grok 4.6 更贵但无误（1.41 美元、3 分 18 秒）；另有人称其相比 gpt-5.6-terra-high 有若干问题。还有人批评链接到 OpenRouter 页面缺乏实质信息，但也不乏热情反馈，一位开发者因对 Flash 更新在重型开发任务上的表现印象深刻而期待试用新模型。

**标签**: `#AI`, `#DeepSeek`, `#LLM`, `#model-release`, `#hackernews`

---

<a id="item-2"></a>
## [Tailscale 将数据库损坏追溯至 SQLite 存在 16 年的 WAL-Reset 缺陷](https://tailscale.com/blog/sqlite-wal-reset-bug) ⭐️ 8.0/10

**原标题**: [Tailscale Traces Database Corruption to 16y/o SQLite WAL-Reset Bug](https://tailscale.com/blog/sqlite-wal-reset-bug)

Tailscale 与 SQLite 开发者将反复出现的数据库损坏事件追溯到 SQLite WAL 索引重置逻辑中的一个竞态条件，并将其命名为“WAL-Reset bug”；该缺陷已在 SQLite 中潜伏至少 16 年。Tailscale 资助了一个开源的 SQLite VFS 垫片（shim），帮助定位这一竞态，未来也有助于发现类似问题。 这件事意义重大，因为 SQLite 是全球使用最广泛的数据库引擎，一个能静默损坏数据的缺陷潜伏 16 年未被发现，足以说明即使庞大的测试套件也有局限性。同时，它展示了一种模式：公司直接资助开源工具来解决生产环境问题，从而让整个生态受益。 该竞态只在多个连接写入或对 WAL 模式数据库执行 checkpoint 时发生，但 Tailscale 发现即使是单写入者的 Go 进程，只要写入和 checkpoint 使用不同连接，也可能触发。调查过程中，SQLite 开发者还顺带发现了另一个无关的“过时表达式索引”（stale expression index）缺陷。

hackernews · ropbear · 8月12日 14:22 · [社区讨论](https://news.ycombinator.com/item?id=49272832)

**背景**: SQLite 使用预写日志（WAL）来保证持久性与并发性，WAL 索引（shm 文件）负责跟踪日志帧和回填进度。在重置该索引时若发生竞态，数据库可能被“分裂”成两个独立文件或出现其他数据损坏。据估计，自 2010 年前后起，每个 SQLite 发行版都带有该缺陷，未升级的捆绑副本可能仍然存在此问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tailscale.com/blog/sqlite-wal-reset-bug">How Tailscale helped find the SQLite WAL - Reset bug</a></li>
<li><a href="https://www.youngju.dev/blog/2026-07-16-sqlite-wal-reset-bug.en">The SQLite WAL - Reset Bug: A Data Corruption Race That Hid for 15...</a></li>
<li><a href="https://sourcefeed.dev/a/a-16-year-old-sqlite-bug-was-eating-tailscales-databases">A 16-Year-Old SQLite Bug Was Eating... — SourceFeed</a></li>

</ul>
</details>

**社区讨论**: 评论区称赞了这篇清晰的复盘文章，并肯定了 Tailscale 资助开源工具的做法——即便问题解决后，他们仍与 SQLite 签了支持合同。还有人指出 SQLite 庞大的测试套件与“测试只能证明 bug 存在、不能证明 bug 不存在”这一格言之间的张力，并提及 Richard Hipp 关于可靠性经验的演讲。

**标签**: `#SQLite`, `#bug`, `#database`, `#open-source`, `#Tailscale`

---

<a id="item-3"></a>
## [Qwen 发布大规模 MoE 模型 Qwen3.8-2.4T-A95B，基准测试表现亮眼](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 8.0/10

**原标题**: [Qwen3.8-2.4T](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B)

阿里巴巴 Qwen 团队发布了 Qwen3.8-2.4T-A95B，这是一个混合专家模型，总参数达 2.4 万亿，激活参数为 950 亿，已在 Hugging Face 上提供 BF16 和 FP8 版本。模型卡声称其性能介于 Opus 4.8 和 Fable 5 之间。 此次发布标志着前沿模型竞争迅速加剧，直接对标 Kimi k3 和 DeepSeek V4，同时推动开放权重模型向 Opus/Fable 级别的性能迈进。950 亿激活参数的 MoE 设计可能会让资源充足的个人和小型组织也能接近前沿模型性能。 BF16 检查点约 4.9TB，FP8 版本体积更小；unsloth 的 1-bit 量化可将其压缩到 397GB，激活参数仍约 950 亿。开放权重版本缺少 Qwen3.8-Max 商业版中的视觉输入、官方非思考模式、内置工具以及默认 100 万上下文长度等功能。

hackernews · Philpax · 8月12日 15:01 · [社区讨论](https://news.ycombinator.com/item?id=49273478)

**背景**: 混合专家（MoE）是一种模型架构，将网络划分为多个专门的子模型（即专家），使每个 token 只激活部分参数，从而在降低单次推理计算成本的同时扩大总参数规模。FP8 是一种 8 位浮点格式，与 BF16 相比能减少训练和推理中的内存与算力需求，但会带来一定精度权衡。正是这些技术，使一个 2.4 万亿参数的开源模型有可能在更普通的硬件上部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/floating-point-8-an-introduction-to-efficient-lower-precision-ai-training/">Floating-Point 8: An Introduction to Efficient, Lower-Precision AI Training | NVIDIA Technical Blog</a></li>
<li><a href="https://chizkidd.github.io/2026/08/10/MoE-2/">Mixture of Experts ( MoE ): How Transformers Scale Without Activating...</a></li>
<li><a href="https://www.exxactcorp.com/blog/hpc/what-is-fp8-fp6-fp4">What is FP8, FP6, FP4? | Exxact Blog</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，该模型只发布了 BF16 和 FP8 版本，发布初期比 Kimi k3 更难部署；要在没有量化感知训练的情况下量化到 Q4，需要大量校准数据。讨论中还提到 DeepSeek V4-Pro-0813 的跑分已经出现，大约处于 Fable 5 水平；也有人赞叹 397GB 的 1-bit 量化能将 Opus 4.5 级性能带到消费级硬件上。

**标签**: `#AI/ML`, `#LLM`, `#Qwen`, `#MoE`, `#Model Release`

---

<a id="item-4"></a>
## [xAI 发布 Grok 4.6，引发关于 API 与性能的讨论](https://x.ai/news/grok-4-6) ⭐️ 8.0/10

**原标题**: [Grok 4.6](https://x.ai/news/grok-4-6)

xAI 发布了新的前沿大语言模型 Grok 4.6。社区早期反馈指出，其 API 默认系统提示词会覆盖用户指令，同时该模型在基准测试中表现强劲，定价也比竞争对手更具攻击性。 Grok 4.6 加剧了顶级 AI 实验室之间的竞争，为开发者提供了另一个高性能、低成本的选择，并可能在其他供应商的定价和 API 行为上施加压力。不过，报道中提到的系统提示词问题可能会让依赖自定义指令的开发者感到沮丧。 社区成员表示，API 会注入一个默认的系统提示词，要求模型不要提及自身指南，这会覆盖开发者提供的提示词，并导致模型拒绝讨论系统提示词。还有用户将 Grok 4.6 与 GPT-5.6-Sol、Kimi K3 等模型在基准测试和价格上进行了对比，认为其表现更好。

hackernews · iLuddite · 8月12日 15:32 · [社区讨论](https://news.ycombinator.com/item?id=49274027)

**背景**: API 系统提示词是开发者随每次请求发送给大语言模型的一组指令，对终端用户不可见，用于塑造模型行为。前沿实验室是指 xAI、OpenAI、Anthropic 等领先的人工智能研究机构，它们推动模型能力的进步；它们的发布常常为质量、速度和价格设定行业基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wildandfreetools.com/blog/chatgpt-custom-gpt-vs-api-system-prompt/">ChatGPT Custom GPT vs API System Prompt ... | WildandFree Tools</a></li>
<li><a href="https://www.lesswrong.com/posts/eAMyxM28hNp4ewGdT/don-t-just-aim-for-frontier-labs">Don&#x27;t just aim for Frontier Labs — LessWrong</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者态度不一：一些人称赞 Grok 4.6 快速、简洁且比竞争对手便宜，另一些人则批评 API 强制加入的系统提示词覆盖了用户指令。几位评论者对所有主要实验室如此之快达到“Fable 级别”质量表示怀疑，认为可能是基准作弊或蒸馏所致，并指出 Grok 的争议性声誉会影响其采用。

**标签**: `#AI`, `#LLM`, `#Grok`, `#xAI`, `#Machine Learning`

---

<a id="item-5"></a>
## [Chrome 中微小 JPEG 显示不同：图片缩放机制解析](https://guillaumetech.github.io/posts/jpg-scaling-chrome/) ⭐️ 8.0/10

**原标题**: [Why tiny JPEGs look different in Chrome](https://guillaumetech.github.io/posts/jpg-scaling-chrome/)

一篇新的技术文章解释了 Chrome 的图片缩小算法会让很小的 JPEG 图像在显示上与其他浏览器明显不同，通常会更模糊。文章建议开发者应提供与实际显示尺寸匹配的图片分辨率，而不是依赖浏览器的缩放处理。 这一点很重要，因为跨浏览器的图像渲染一致性直接影响 UI 质量，尤其是在 Web 应用和基于 Electron 的桌面应用中的图标和小图形。了解该行为有助于开发者避免细微的视觉缺陷以及因图片过大而浪费带宽。 Chrome 和 Firefox 使用不同的缩小滤镜：Chrome 通常更模糊，而 Firefox 更锐利但可能出现振铃伪影。CSS 的 image-rendering 属性在某些情况下可以影响缩放方式，但不同浏览器的行为并不一致。

hackernews · gutechh · 8月12日 14:00 · [社区讨论](https://news.ycombinator.com/item?id=49272549)

**背景**: 当浏览器以远小于原图的分辨率显示一张高分辨率图片时，浏览器必须使用缩放算法（如 Lanczos 或双线性滤波）对像素进行重采样。不同浏览器历来使用不同的滤镜实现这一过程，即使对于相同的 HTML 和 CSS 也会产生肉眼可见的差异。JPEG 压缩伪影在微小的图标被大幅缩小时尤其明显，因此让源图分辨率匹配显示尺寸是一种推荐的 Web 性能与质量实践。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://entropymine.com/resamplescope/notes/browsers/">How web browsers resize images</a></li>
<li><a href="https://stackoverflow.com/questions/384991/what-is-the-best-image-downscaling-algorithm-quality-wise">What is the best image downscaling algorithm ... - Stack Overflow</a></li>

</ul>
</details>

**社区讨论**: 评论者确认该问题也影响 PNG，并分享 Chrome 的优化在某个 Electron 版本中导致大量图标显示异常，不得不推迟升级。部分人并不完全同意原帖的归因，认为真正解决方法是使用尺寸合适的图片，而且 Chrome 与 Firefox 算法差异（模糊对比振铃）可能比 JPEG 伪影影响更大。还有人指出 CSS 的 image-rendering 属性以及 Firefox 正在进行的低分辨率解压 Bug 是有效的临时方案和后续关注点。

**标签**: `#web development`, `#browsers`, `#image scaling`, `#Chrome`, `#JPEG`

---

<a id="item-6"></a>
## [Grok 4.6 在 Artificial Analysis 智能指数上得分 61](https://artificialanalysis.ai/articles/grok-4-6-benchmarks-and-analysis) ⭐️ 8.0/10

**原标题**: [Grok 4.6 scores 61 on the Artificial Analysis Intelligence Index](https://artificialanalysis.ai/articles/grok-4-6-benchmarks-and-analysis)

SpaceXAI 发布了 Grok 4.6，这一前沿模型在“high”推理模式下于 Artificial Analysis Intelligence Index 上取得 61 分。该模型支持文本和图像输入，并拥有 50 万 token 的上下文窗口。 这一分数使 Grok 4.6 远超同类模型的中位数（34），进一步加剧了前沿模型竞争。社区评论显示，其速度和定价可能在编码和日常使用中挑战 Claude 和 GPT-5.6。 Grok 4.6 相比 Grok 4.5 进行了更长的补充训练，使用了针对推理和高级技术概念的精选模型生成数据。社区报告指出，缓存读取定价从 Grok 4.5 的 0.30 美元涨至 0.50 美元（每百万 token）。

hackernews · wertyk · 8月12日 16:54 · [社区讨论](https://news.ycombinator.com/item?id=49275385)

**背景**: Artificial Analysis Intelligence Index 是一个综合基准，用于评估语言模型在推理、编码、知识、指令遵循、科学推理和多步骤任务方面的能力。Grok 4.6 是 SpaceXAI（原 xAI）继 Grok 4.5 之后推出的最新模型，Grok 4.5 基于 1.5 万亿参数的基础模型构建，并采用了 Cursor 编程平台的数据。该指数中位数为 34，因此 Grok 4.6 的 61 分使其远超平均水平。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index | Artificial Analysis</a></li>
<li><a href="https://x.ai/news/grok-4-6">Introducing Grok 4 . 6 | SpaceXAI</a></li>
<li><a href="https://artificialanalysis.ai/models/grok-4-6">Grok 4 . 6 (high) - Intelligence, Performance &amp; Price Analysis</a></li>

</ul>
</details>

**社区讨论**: 社区对 Grok 4.6 的速度和编码体验总体持积极态度，用户称赞其交流风格和比 Claude Code 更快的会话交互。部分用户强调通过 Cursor 订阅使用 Grok 模型的价值，也有人担心缓存读取价格上涨，并认为该发布意味着 Gemini 等模型同样可能缩小差距。

**标签**: `#AI/ML`, `#LLM`, `#benchmark`, `#Grok`, `#coding-assistant`

---

<a id="item-7"></a>
## [AI 正在淘汰中级软件工程师，拉大顶尖与底层差距](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html) ⭐️ 8.0/10

**原标题**: [AI is removing the middle class of software engineering?](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html)

Florian Herrengt 的一篇新博文认为，AI 编程工具对中级软件工程师的影响不成比例，可能放大顶尖和底层工程师的影响。文章指出，AI 消除了常规编码工作的需求，挤压了工程领域的“中产阶级”。 这很重要，因为它挑战了“AI 对所有软件工程师影响相同”的假设，对职业规划、招聘和团队构成都有深远影响。中级工程师可能需要培养更高层次的技能，否则可能在 AI 辅助工作流中被挤压。 文章强调，“糟糕”的工程师可以借助 AI 将糟糕产出放大十倍，而高级工程师的批判性思维仍然有价值。评论者也指出，AI 实际上自动化了“StackOverflow 工程师”的角色，消除了传统上高级工程师向初级工程师交接任务的需求。

hackernews · florianherrengt · 8月12日 13:20 · [社区讨论](https://news.ycombinator.com/item?id=49271994)

**背景**: 大型语言模型（LLM）和 AI 编程助手越来越擅长生成代码，自动化日常编程任务。这引发了关于软件工程角色将如何演变的讨论，尤其是那些通常负责执行高级工程师委派实现工作的中级工程师。

**社区讨论**: 评论者参与度很高，但意见有些分歧。一些人同意 AI 会放大糟糕的工程实践，并强调批判性思维的重要性；另一些人则质疑是否有确凿证据表明软件工程岗位流失。一位评论者将此趋势比作历史上技术驱动的劳动力变化。

**标签**: `#AI`, `#Software Engineering`, `#Career Impact`, `#LLMs`, `#Industry Analysis`

---

<a id="item-8"></a>
## [谷歌 DeepMind 发布手语转文字模型 SL2T](https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/) ⭐️ 8.0/10

**原标题**: [Putting sign language AI into users’ hands](https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/)

谷歌 DeepMind 发布了手语转文字模型 SL2T，并将其集成到 Gboard 和 Live Transcribe 中，Pixel 11 等设备将率先搭载。该公司称这是首个进入真实消费产品的手语 AI。 这一点意义重大，因为它将手语识别从研究领域带入日常消费工具，帮助聋人和听障用户更自然地实时交流。它还可能开创先例，让无障碍 AI 被视为产品核心功能，而非事后补充。 SL2T 还可用于向 Gemini 发起指令，让后者回答问题或代用户执行操作；在 Live Transcribe 中，用户也能在面对面通话时用手语作答。首批部署将随 Pixel 11 硬件上的 Gboard 和 Live Transcribe 集成一起推出。

rss · Google DeepMind · 8月12日 14:01

**背景**: 手语是一种拥有自身语法的视觉语言，将其转成文字需要 AI 理解连续的手势、面部表情和身体语言。此前多数手语 AI 研究仍停留在实验室阶段，因此 SL2T 整合进谷歌已发货产品，标志着向现实世界无障碍应用迈出了重要一步。该模型补充了现有语音转文字无障碍工具，为手语使用者增加了一条以文字为载体的表达渠道。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/putting-sign-language-ai-into-users-hands/">Putting sign language AI into users’ hands — Google DeepMind</a></li>
<li><a href="https://siliconangle.com/2026/08/12/google-debuts-sl2t-ai-model-thats-designed-understand-sign-language/">Google debuts SL 2 T , an AI model that&#x27;s designed to understand sign ...</a></li>
<li><a href="https://www.cryptopolitan.com/google-deepmind-sign-language-on-pixel-11/">Google DeepMind ships SL 2 T sign - language model ... - Cryptopolitan</a></li>

</ul>
</details>

**标签**: `#AI`, `#accessibility`, `#sign language`, `#Google DeepMind`, `#NLP`

---

<a id="item-9"></a>
## [Adam 的各向异性破坏旋转不变性与低秩偏置](https://www.reddit.com/r/MachineLearning/comments/1vmjb3p/the_loss_does_not_see_the_basis_but_adam_does_r/) ⭐️ 8.0/10

**原标题**: [The Loss Does Not See the Basis, But Adam Does \[R\]](https://www.reddit.com/r/MachineLearning/comments/1vmjb3p/the_loss_does_not_see_the_basis_but_adam_does_r/)

一项新研究表明，Adam 的逐坐标缩放破坏了因子分解模型中的旋转不变性，从而导致隐式低秩偏置的丧失。而共享标量变体（如 Muon 和 Shampoo）则保留了这种偏置。 这一发现识别了优化器差异背后的具体机制，有助于实践者为低秩矩阵感知和深度学习任务选择优化器。同时，它也澄清了先前关于 Muon 频谱偏置的矛盾结果。 该研究在欠定矩阵感知上测试了九种更新规则，并匹配了训练损失。一个在逐坐标与共享标量分母之间插值的单参数族显示出恢复性能的单调提升，从而将效应归因于各向异性；随着频谱尾部的增加，Muon 退化最快，并在约 4%尾部能量处让位于梯度下降。

reddit · r/MachineLearning · /u/EtherealGlyph · 8月12日 16:39

**背景**: 在 W = U V^T 这样的因子分解模型中，损失函数具有旋转不变性，而梯度下降尊重这一对称性。Adam 的逐坐标二阶矩归一化依赖于所选的基，从而破坏了这种不变性。隐式低秩偏置指的是优化算法即使没有显式正则化也能找到低秩解的趋势。该论文指出其主张核心是机制本身，而非确切的数值结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2011.13772">Gradient Descent for Deep Matrix Factorization</a></li>
<li><a href="https://kellerjordan.github.io/posts/muon/">Muon : An optimizer for hidden layers in neural networks</a></li>
<li><a href="https://arxiv.org/pdf/1802.09568">Shampoo</a></li>

</ul>
</details>

**标签**: `#optimization`, `#Adam`, `#low-rank bias`, `#matrix sensing`, `#deep learning theory`

---