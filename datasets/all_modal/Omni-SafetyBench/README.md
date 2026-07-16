# Omni-SafetyBench


## 1. Overview

- Dataset Name:

  Omni-SafetyBench


- Full Name:

  Omni-SafetyBench: A Benchmark for Safety Evaluation of Audio-Visual Large Language Models


- Modality:

  Omni-modal

  Including:

  - Text
  - Image
  - Audio
  - Video


- Task:

  Safety Evaluation of Omni-Modal Large Language Models


- Year:

  2025


- Dataset Scale:

  - 24 modality variations
  - 972 samples for each modality variation


---

# 2. Paper


## Title

Omni-SafetyBench: A Benchmark for Safety Evaluation of Audio-Visual Large Language Models


## Paper URL

https://arxiv.org/abs/2508.07173


## Venue

arXiv 2025


---

# 3. Dataset Download


## HuggingFace Dataset

Official Dataset:

https://huggingface.co/datasets/Leyiii/Omni-SafetyBench


## Dataset Repository

The dataset contains:

- metadata files
- text prompts
- image inputs
- audio inputs
- video inputs


# 5. Dataset Description


Omni-SafetyBench is designed for evaluating safety
alignment of Audio-Visual Large Language Models.


Different from traditional:

```
Text-only LLM

or

Image-text MLLM
```


Omni-SafetyBench focuses on:


```
Audio

+

Visual

+

Text

        ↓

Audio-Visual LLM

        ↓

Safety Response
```


It evaluates whether models maintain safety alignment
under complex multimodal inputs.


---

# 6. Modality Combinations


The benchmark considers:


- Audio-only input

- Visual-only input

- Audio-visual joint input

- Cross-modal combinations


A total of:

```
24 modality combinations
```


are evaluated.


---

# 7. Safety Evaluation


The benchmark focuses on:


## 1. Harmful Content Understanding


Including:

- Violence
- Illegal activities
- Unsafe behaviors


## 2. Cross-modal Safety Consistency


Evaluates whether models produce consistent safety decisions
when the same harmful intent is presented through different modalities.


## 3. Audio-Visual Joint Safety


Tests whether combined audio and visual information
introduces new safety vulnerabilities.


---

# 8. Evaluation Metrics


The paper introduces:


## Conditional Attack Success Rate (C-ASR)

Measures successful harmful response generation
while considering modality comprehension.


## Conditional Refusal Rate (C-RR)

Measures model refusal ability under successful understanding.


## Cross-Modal Safety Consistency Score (CMSC)

Measures whether safety behavior remains consistent
across different modalities.


---

# 9. Applications


Omni-SafetyBench can be used for:


- Audio-visual LLM safety evaluation;

- Multimodal jailbreak analysis;

- Cross-modal safety consistency research;

- Safety alignment evaluation;

- Defense method testing.


---

# 10. Related Benchmarks


| Dataset | Modality | Focus |
|---|---|---|
| MM-SafetyBench | Image + Text | Vision safety |
| Video-SafetyBench | Video + Text | Video LVLM safety |
| Jailbreak-AudioBench | Audio + Text | Audio jailbreak |
| Omni-SafetyBench | Audio + Visual + Text | Omni safety evaluation |


---

# 11. Citation


```bibtex
@article{pan2025omnisafetybench,
title={Omni-SafetyBench: A Benchmark for Safety Evaluation of Audio-Visual Large Language Models},
author={Pan, Leyi and others},
year={2025}
}
```
