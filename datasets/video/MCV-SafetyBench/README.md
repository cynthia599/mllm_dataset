# MCV-SafetyBench


## 1. Overview

- Dataset Name:

  MCV-SafetyBench


- Full Name:

  Multi-Clip Video SafetyBench


- Modality:

  Video + Text


- Task:

  Video Large Vision-Language Model Jailbreak Evaluation


- Target Models:

  Video LVLMs


- Year:

  2026


- Dataset Scale:

  2,920 multi-clip video samples


---

# 2. Paper


## Title

Jailbreaking Multimodal Large Language Models using Multi-Clip Video


## Paper URL

https://arxiv.org/abs/2606.02111


---

# 3. Dataset Download


## Official Dataset

GitHub Repository:

https://github.com/ChoongwonKang/MCV_Jailbreak


The dataset is released together with the official code repository.


Dataset includes:

- Multi-clip video samples
- Safety annotations
- Evaluation files


Expected structure:
MCV-SafetyBench

├── videos/

├── annotations/

├── prompts/

└── evaluation files

# 4. Code Repository


Official GitHub:

https://github.com/ChoongwonKang/MCV_Jailbreak


The repository provides:

- Video construction scripts
- Dataset processing
- Jailbreak evaluation pipeline


---

# 5. Dataset Description


MCV-SafetyBench studies jailbreak vulnerabilities
of Video Large Vision-Language Models.


Different from image jailbreak:
Image + Text

(single visual context)



MCV-SafetyBench introduces:



Multiple Video Clips

    ↓

Temporal Context

    ↓

Video LVLM

    ↓

Response



The benchmark investigates whether
multi-clip video context increases jailbreak vulnerability.


---

# 6. Dataset Construction


The benchmark constructs videos from multiple clips.


Pipeline:



Video Clips

  ↓

Multi-Clip Video

  ↓

Video LVLM Input

  ↓

Safety Evaluation



The benchmark evaluates:

- Number of clips
- Temporal information
- Context diversity


---

# 7. Attack Type


MCV-SafetyBench focuses on:


## Multi-Clip Video Jailbreak


Compared with static images:


Image:


Single frame



Video:


Multiple frames

Temporal evolution

Context accumulation



This additional information may weaken
existing safety alignment mechanisms.


---

# 8. Dataset Structure


Example:



sample

├── video.mp4

├── question

├── category

├── annotation

└── metadata



Example JSON:


```json
{
"id":"0001",
"video":"xxx.mp4",
"question":"example question",
"category":"harmful_behavior"
}
