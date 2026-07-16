\# SafeBench



\## 基本信息



\- 数据集名称：SafeBench

\- 模态：文本、图像、音频

\- 任务：多模态大模型安全评测

\- 数据规模：完整版本约 2,300 组多模态安全查询

\- 风险类别：23 类

\- 小规模版本：MiniBench

\- 官方数据平台：Hugging Face



\## 数据集特点



SafeBench 是面向多模态大模型的综合安全评测基准。



它将相同或相关的危险语义构造成不同模态版本，用于比较模型在文本、图像和音频输入下的安全表现，并分析安全对齐是否能够稳定迁移到不同模态。



\## 官方仓库结构



官方 Hugging Face 仓库主要包含：



```text

safebench/

├── MiniBench\_Text/

├── SafeBench\_Text/

├── minibench.tar.gz

├── part\_aa

├── part\_ab

├── part\_ac

├── part\_ad

├── part\_ae

├── part\_af

├── part\_ag

├── part\_ah

├── part\_ai

├── part\_aj

├── category.csv

├── sample.csv

└── README.md

```



\### MiniBench\_Text



MiniBench 的纯文本版本，用于快速测试文本模型或建立 text-only baseline。



\### SafeBench\_Text



完整 SafeBench 的纯文本版本，用于比较纯文本输入和多模态输入下的安全差异。



\### minibench.tar.gz



小规模多模态数据压缩包，适合：



\- 查看数据结构；

\- 制作数据集展示；

\- 快速测试图像和音频模型；

\- 编写数据读取代码。



\### part\_aa 至 part\_aj



完整 SafeBench 多模态数据压缩包的分卷文件。



这些文件必须全部下载并按顺序合并，才能得到完整压缩包。



\### category.csv



记录风险类别编号和类别名称之间的映射关系。



\### sample.csv



提供少量样本和字段结构，便于在下载完整数据前了解数据格式。



\## MiniBench 解压后的结构



MiniBench 通常包含：



```text

minibench\_final/

├── text/

├── img/

├── audio\_data\_female/

└── audio\_data\_male/

```



\- `text/`：纯文本危险查询；

\- `img/`：图像形式的安全测试样本；

\- `audio\_data\_female/`：女性音色音频；

\- `audio\_data\_male/`：男性音色音频。



这些模态通常分别输入对应模型，而不是默认同时输入。



\## 风险分类



SafeBench 使用统一的 23 类风险体系组织文本、图像和音频样本。



模态与风险类别属于两个不同维度：



```text

风险类别

├── 文本版本

├── 图像版本

├── 女性音频版本

└── 男性音频版本

```



具体类别名称应以官方 `category.csv` 为准。



\## 主要用途



\- 多模态大模型安全评测；

\- 比较文本、图像和音频输入下的拒绝率；

\- 分析跨模态安全一致性；

\- 测试图像和音频输入是否削弱语言侧安全对齐；

\- 评估安全微调和防御方法；

\- 研究视觉编码器、音频编码器与语言模型之间的安全表征差异。



\## 官方资源



\- Hugging Face：

&#x20; https://huggingface.co/datasets/Zonghao2025/safebench



\- 项目主页：

&#x20; https://safebench-mm.github.io/



\## 下载说明



本仓库不重新分发 SafeBench 原始图片、音频和压缩分卷。



快速查看数据时，推荐下载：



```text

minibench.tar.gz

category.csv

sample.csv

README.md

```



正式实验需要完整数据时，再下载 `part\_aa` 至 `part\_aj` 并合并。

