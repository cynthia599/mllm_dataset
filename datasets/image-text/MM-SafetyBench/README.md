\# MM-SafetyBench



\## 基本信息



\- 数据集名称：MM-SafetyBench

\- 模态：图像 + 文本

\- 任务：多模态大模型安全评测、图文越狱攻击评测

\- 论文：MM-SafetyBench: A Benchmark for Safety Evaluation of Multimodal Large Language Models

\- 会议：ECCV 2024

\- 样本规模：5,040 组图文样本

\- 风险类别：13 类



\## 数据构造形式



\- Text-only：仅输入危险文本，作为语言侧安全基线。

\- SD：利用 Stable Diffusion 生成与查询语义相关的图像。

\- OCR：将危险问题或关键词写入图片。

\- SD+OCR：将语义相关图片与图像文字结合。



\## 主要用途



\- 测试图像输入是否削弱模型安全拒绝能力；

\- 评估 OCR 图像文字攻击；

\- 评估视觉语义型越狱攻击；

\- 分析跨模态安全一致性；

\- 用于多模态安全神经元和图文融合机制研究。



\## 官方资源



\- 官方代码：https://github.com/isXinLiu/MM-SafetyBench

\- 论文：https://arxiv.org/abs/2311.17600



\## 下载说明



本仓库不重新分发原始数据，请从官方代码仓库获取数据生成脚本和相关资源。

