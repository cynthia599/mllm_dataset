\# VLSBench



\## 基本信息



\- 数据集名称：VLSBench

\- 全称：VLSBench: Unveiling Visual Leakage in Multimodal Safety

\- 模态：图像 + 文本

\- 任务：多模态安全评测、视觉风险识别

\- 论文：VLSBench: Unveiling Visual Leakage in Multimodal Safety

\- 论文年份：2025

\- 数据规模：约 2,241 组图文样本

\- 数据语言：英语

\- 许可证：Apache-2.0



\## 核心研究问题



VLSBench 主要解决现有多模态安全数据中的

Visual Safety Information Leakage（视觉安全信息泄漏）问题。



在部分传统安全数据中，文本问题本身已经包含明显的危险关键词，

模型即使不查看图像，也可能依据文本直接拒绝。



VLSBench 通过构造表面无害的文本查询，使安全风险主要由图像提供，

从而测试模型是否真正理解视觉内容中的危险语义。



\## 数据结构



官方 Hugging Face 仓库主要提供：



```text

vlsbench/

├── data/

├── imgs/

├── data.json

├── imgs.tar

└── README.md

```



\- `data/`：Parquet 格式的完整图文数据；

\- `imgs/`：已解压的原始图片；

\- `imgs.tar`：图片压缩包，与 `imgs/` 内容基本相同；

\- `data.json`：图片路径、问题、类别、图像描述和安全原因等元数据；

\- `README.md`：官方数据说明。



使用独立图片文件时，推荐下载：



```text

data.json + imgs.tar

```



不需要同时下载 `data/`、`imgs/` 和 `imgs.tar`，否则会重复保存同一批图片。



\## 核心特点



\### 1. 表面无害的文本查询



文本中尽量不直接出现明显危险关键词，避免模型只根据文本判断安全风险。



\### 2. 视觉主导风险



危险意图主要来自图像内容，模型必须结合图像才能理解完整语境。



\### 3. 图文联合安全判断



用于判断模型是否真正具备视觉侧安全识别和跨模态安全推理能力。



\### 4. 安全原因说明



部分样本提供图像描述与安全判断依据，便于分析模型为何应该拒绝或谨慎回答。



\## 主要用途



\- 评估模型是否真正理解图像中的安全风险；

\- 排除文本危险关键词造成的安全信息泄漏；

\- 测试视觉编码器和图文融合层的安全能力；

\- 分析图像主导与文本主导安全表征；

\- 用于安全神经元定位和跨数据集泛化实验；

\- 评估多模态安全微调与防御方法。



\## 官方资源



\- Hugging Face：

&#x20; https://huggingface.co/datasets/Foreshhh/vlsbench



\- 官方代码：

&#x20; https://github.com/AI45Lab/VLSBench



\- 论文：

&#x20; https://arxiv.org/abs/2411.19939



\## 下载说明



本仓库不重新分发 VLSBench 的原始图片和大规模数据文件。



请运行本目录中的 `download.bat` 或 `download.sh`，

从官方 Hugging Face 仓库下载数据。

