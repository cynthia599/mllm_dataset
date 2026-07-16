\# JALMBench





\## 基本信息



\- 数据集名称：JALMBench

\- 全称：

&#x20; Benchmarking Jailbreak Vulnerabilities in Audio Language Models



\- 模态：

&#x20; Audio + Text



\- 任务：

&#x20; Audio Language Model Jailbreak Evaluation



\- 研究对象：

&#x20; Large Audio Language Models (LALMs)



\- 数据规模：

&#x20; - 2,200 条文本样本

&#x20; - 51,381 条音频样本

&#x20; - 超过 268 小时音频



\- 支持模型：

&#x20; 12 个主流 Audio Language Models



\- 论文：

&#x20; JALMBench: Benchmarking Jailbreak Vulnerabilities in Audio Language Models



\- 年份：

&#x20; 2025





\## 数据集背景



随着 Audio Language Models 的发展，

模型可以直接理解语音输入并生成文本响应。



不同于传统：



Text → LLM



Audio Language Model：



Audio → Audio Encoder → Language Model



因此安全风险不再只存在于文本 token，

音频编码器和语音理解模块也可能成为新的攻击入口。





JALMBench 旨在回答：



> 音频输入是否能够绕过已有语言模型安全对齐？





\## 数据组成





JALMBench 包含两大类攻击来源：





\## 1. Text-transferred Audio Jailbreak



文本越狱迁移到音频。





流程：



```

Text jailbreak prompt



&#x20;       ↓



Text-to-Speech (TTS)



&#x20;       ↓



Audio jailbreak prompt



&#x20;       ↓



Audio Language Model

```





特点：



\- 原始攻击来自文本领域；

\- 通过 TTS 转换为语音；

\- 测试文本安全机制能否迁移到音频。





例如：



文本：



```

harmful instruction

```



经过 TTS：



```

harmful\_instruction.wav

```



模型输入变为：



<Audio>





\## 2. Audio-originated Jailbreak



原生音频攻击。





攻击直接针对音频模态设计：



包括：



\- audio perturbation

\- voice manipulation

\- acoustic attack

\- semantic audio attack





目的：



测试音频编码器和语义理解模块的安全漏洞。





\## 攻击方法分类





JALMBench 支持：



\### Text-transferred attacks



文本攻击迁移：



\- TTS conversion

\- jailbreak prompt transformation





\### Audio-native attacks



音频原生攻击：



\- 音频扰动

\- 声学变化

\- 语音特征变化





\## 数据字段





典型样本结构：





```

JALMBench



├── audio/

│

├── text\_prompt

│

├── attack\_type

│

├── category

│

└── metadata

```





字段说明：



|字段|说明|

|-|-|

|audio|音频文件路径|

|text\_prompt|原始文本指令|

|attack\_type|攻击类型|

|category|安全类别|

|language|语言|

|speaker|说话人信息|





\## 数据多样性





JALMBench 包含丰富音频变化：



\- 多语言

\- 不同性别

\- 不同口音

\- 多种 TTS 方法





用于测试：



模型安全能力是否受到：



\- 语言变化；

\- 声音变化；

\- 说话方式变化；



影响。





\## 风险类别





数据覆盖多类安全风险：



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





JALMBench 可用于：



\- Audio Language Model 安全评测；

\- 音频越狱攻击研究；

\- 文本攻击向音频迁移研究；

\- 音频编码器安全分析；

\- 跨模态安全一致性研究；

\- 安全防御方法评估。





\## 与其他音频数据集区别





|数据集|特点|

|-|-|

|Jailbreak-AudioBench|音频编辑攻击和扰动评测|

|AJailBench|TTS攻击和音频扰动攻击|

|JALMBench|大规模ALM越狱综合benchmark|





JALMBench 更适合作为：



> Audio Language Model 安全评测标准基准。





\## 官方资源





Hugging Face:



https://huggingface.co/datasets/AnonymousUser000/JALMBench





论文:



https://arxiv.org/abs/2505.17568





代码：



请以论文官方仓库为准。





\## 下载说明





本仓库不重新分发：



\- wav 音频文件

\- parquet 文件

\- 大规模数据压缩包





仅提供：



\- 数据说明

\- 下载入口

\- 数据读取脚本





正式实验建议下载：



\- audio files

\- metadata

\- attack annotations

