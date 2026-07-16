\# Jailbreak-AudioBench





\## 基本信息



\- 数据集名称：Jailbreak-AudioBench

\- 模态：Audio + Text

\- 任务：音频大模型越狱攻击、安全评测

\- 类型：Audio Jailbreak Benchmark

\- 论文：

&#x20; Jailbreak-AudioBench: A Comprehensive Benchmark for Audio Jailbreak Attacks on Large Audio-Language Models



\- 年份：2025

\- 数据规模：

&#x20; 约 94,800 条音频越狱样本



\- 数据格式：

&#x20; Audio + Instruction





\## 数据集背景



随着 Audio-Language Models（ALMs）的发展，

模型可以同时理解语音内容和文本指令。



然而，现有大模型安全机制主要针对文本输入设计，

攻击者可以通过音频模态绕过文本安全过滤。



Jailbreak-AudioBench 系统研究：



\- 语音输入是否能够绕过安全对齐；

\- 音频扰动是否降低模型拒答能力；

\- 不同攻击方式对音频大模型的影响。





\## 数据组成



Jailbreak-AudioBench 包含多种音频越狱攻击形式：



```text

Jailbreak-AudioBench



├── Original harmful instruction

│

├── Audio jailbreak attacks

│

├── Generated speech

│

└── Perturbed audio

```





主要包括：



\## 1. Speech-based Jailbreak



将危险文本转换为语音。



例如：



文本：



```

\[malicious instruction]

```



转换为：



```

audio.wav

```



测试模型是否能够识别语音中的危险意图。





\## 2. Audio Perturbation Attack



通过修改音频信号：



\- noise injection

\- speed change

\- pitch change

\- compression

\- distortion



降低安全识别能力。





\## 3. Voice-based Attack



利用不同：



\- speaker

\- accent

\- speaking style



测试模型安全机制是否依赖声音特征。





\## 数据字段



典型结构：



```text

sample

├── audio

│   └── xxx.wav

│

├── instruction

│

├── category

│

├── attack\_type

│

└── metadata

```





字段说明：



|字段|含义|

|-|-|

|audio|音频文件路径|

|instruction|对应文本指令|

|category|风险类别|

|attack\_type|攻击方式|

|speaker|说话人信息|





\## 风险类别



数据覆盖多种安全风险：



\- Illegal Activity

\- Violence

\- Self-harm

\- Hate Speech

\- Privacy

\- Fraud

\- Cybersecurity

\- Sexual Content





具体类别以官方 metadata 为准。





\## 主要用途



Jailbreak-AudioBench 可用于：



\- 音频大模型安全评测；

\- Audio-Language Model 越狱研究；

\- 跨模态安全迁移分析；

\- 音频扰动攻击研究；

\- 安全对齐机制分析；

\- 音频编码器安全表征研究。





\## 与图文越狱的区别





|类别|攻击通道|

|-|-|

|文本越狱|Text token|

|图文越狱|Vision encoder + Text|

|音频越狱|Audio encoder + Text|





该数据集主要研究：



> 音频编码器是否成为绕过安全对齐的新攻击入口。





\## 官方资源



GitHub:



https://github.com/Researchtopic/Code-Jailbreak-AudioBench





Hugging Face:



https://huggingface.co/datasets/researchtopic/Jailbreak-AudioBench





\## 下载说明



本仓库不重新分发原始音频文件。



请使用本目录中的 download 脚本，

从官方 HuggingFace 数据仓库下载。





推荐首次下载：



\- metadata

\- parquet 文件





完整实验需要：



\- 全部 parquet

\- 对应 audio 文件

