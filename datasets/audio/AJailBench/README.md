\# AJailBench





\## 基本信息



\- 数据集名称：AJailBench

\- 模态：Audio + Text

\- 任务：Audio-Language Model 越狱攻击评测

\- 类型：Audio Jailbreak Benchmark

\- 研究对象：

&#x20; Audio-Language Models (ALMs)



\- 数据规模：

&#x20; 约 1,495 条音频越狱样本



\- 数据格式：

&#x20; Audio + Instruction + Safety Category





\## 数据集背景



随着 Audio-Language Models（ALMs）的发展，

模型能够通过语音理解用户指令并生成文本回复。



然而，大多数模型安全对齐主要基于文本输入，

攻击者可以利用：



\- 语音转换；

\- 音频扰动；

\- TTS 生成语音；

\- 声学隐藏信息；



绕过文本安全过滤机制。



AJailBench 专门用于研究：



> 音频输入是否能够成为绕过大模型安全对齐的新攻击入口。





\## 数据组成



AJailBench 主要包含三类音频攻击形式：





\## 1. Text-to-Speech Attack (TTS)



将危险文本指令转换为自然语音。



流程：



```

Harmful text instruction

&#x20;         |

&#x20;         ↓

&#x20;      TTS model

&#x20;         |

&#x20;         ↓

&#x20;     audio.wav

&#x20;         |

&#x20;         ↓

&#x20;Audio-Language Model

```





用于测试：



\- 模型是否能够识别语音中的危险意图；

\- 文本安全机制是否可以迁移到语音模态。





\## 2. Audio Adversarial Attack



对原始语音进行扰动：



包括：



\- noise injection

\- waveform perturbation

\- speed modification

\- pitch modification





目的：



降低 Audio Encoder 对危险语义的识别能力。





\## 3. Voice Conversion Attack



改变语音属性：



例如：



\- speaker identity

\- gender

\- accent

\- speaking style





用于测试：



模型安全能力是否受到说话人特征影响。





\## 风险类别



AJailBench 覆盖多个安全风险：



\- Illegal Activity

\- Violence

\- Self-harm

\- Hate Speech

\- Privacy Violation

\- Fraud

\- Cybersecurity

\- Sexual Content





具体类别以官方 metadata 为准。





\## 数据结构



典型形式：



```

AJailBench/



├── audio/

│   └── xxx.wav

│

├── metadata.json

│

└── category.csv

```





样本字段：



|字段|说明|

|-|-|

|audio|音频路径|

|instruction|对应危险指令|

|category|风险类别|

|attack\_type|攻击类型|

|tts\_model|语音生成模型|





\## TTS 是什么？



TTS（Text To Speech）



即：



> 文本转语音技术。





例如：



输入：



```

How to perform a harmful action

```



经过 TTS：



```

speech.wav

```



模型接收到的是：



```

<Audio>

```



而不是文本。





研究重点：



判断 Audio-Language Model 是否会因为输入形式变化而降低安全拒绝能力。





\## 主要用途



AJailBench 可用于：



\- Audio-Language Model 安全评测；

\- 音频越狱攻击研究；

\- TTS 攻击分析；

\- 音频编码器安全机制研究；

\- 跨模态安全迁移研究；

\- 安全对齐方法测试。





\## 与文本/图像越狱关系





|攻击类型|输入通道|

|-|-|

|GCG|Text token|

|FigStep|Image OCR|

|HADES|Visual semantic|

|AJailBench|Audio encoder|





AJailBench 研究：



> 音频编码器是否成为新的 jailbreak attack surface。





\## 官方资源



论文：

arXiv:

https://arxiv.org/abs/2505.15406


ACL Anthology:

https://aclanthology.org/2026.acl-long.1259/





Hugging Face：



未公开





代码：



请以论文官方仓库为准。





\## 下载说明



本仓库不重新分发原始音频文件。



请通过官方 Hugging Face 数据页面下载。



建议保存：



\- metadata

\- parquet/json 文件

\- audio 文件索引



完整实验需要下载对应音频文件。

