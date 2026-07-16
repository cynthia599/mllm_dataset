\# JailBreakV-28K



\## 基本信息



\- 数据集名称：JailBreakV-28K

\- 模态：图像 + 文本

\- 任务：多模态大模型越狱攻击与安全鲁棒性评测

\- 论文：JailBreakV: A Benchmark for Assessing the Robustness of Multimodal Large Language Models against Jailbreak Attacks

\- 会议：COLM 2024

\- 数据规模：约 28,000 条图文测试样本

\- 原始危险请求：约 2,000 条

\- 风险类别：16 类



\## 数据组成



JailBreakV-28K 主要包含三类攻击数据：



\### 1. LLM Transfer Attack



将传统文本大模型越狱提示迁移到多模态大模型。



\- 攻击主要由文本提示完成；

\- 图片可能是自然图、噪声图、空白图或生成图；

\- 用于测试文本越狱能力是否会继承到多模态模型。



\### 2. FigStep



将危险标题、关键词或步骤排版到图片中，再通过表面中性的文本要求模型识别并补充图片内容。



\- 图片承担主要攻击语义；

\- 主要依赖 OCR 和图像文字理解；

\- 用于测试视觉文字通道的安全过滤能力。



\### 3. Query-related



使用与危险查询语义相关的物体、界面或场景图片，并配套文本问题。



\- 图像提供危险场景或语义线索；

\- 用于测试视觉语义与图文融合带来的安全风险。



\## 数据目录结构



```text

JailBreakV\_28K/

├── figstep/

├── llm\_transfer\_attack/

├── query\_related/

├── JailBreakV\_28K.csv

├── mini\_JailBreakV\_28K.csv

└── RedTeam\_2K.csv





其中：



JailBreakV\_28K.csv：完整样本索引，记录文本、攻击类型、风险类别和图片路径；

mini\_JailBreakV\_28K.csv：小规模测试子集；

RedTeam\_2K.csv：约 2,000 条原始危险请求；

三个图片文件夹与 CSV 中的路径字段对应。

主要用途

评估多模态模型的越狱攻击成功率；

比较文本迁移攻击、OCR 图片攻击和视觉语义攻击；

测试不同攻击方式的跨模型泛化能力；

分析视觉编码器、融合层和语言层的安全机制；

作为多模态安全防御与安全神经元研究的基准数据。

官方资源

Hugging Face：

https://huggingface.co/datasets/JailbreakV-28K/JailBreakV-28k

GitHub：

https://github.com/EddyLuo1232/JailBreakV\_28K

论文：

https://arxiv.org/abs/2404.03027

