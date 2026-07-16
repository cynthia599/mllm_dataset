\# FigStep





\## 1. Overview





\- Dataset Name:



&#x20; FigStep





\- Full Name:



&#x20; FigStep: Jailbreaking Large Vision-Language Models via Typographic Visual Prompts





\- Modality:



&#x20; Image + Text





\- Task:



&#x20; Vision-Language Model Jailbreak Attack





\- Attack Type:



&#x20; Black-box visual jailbreak attack





\- Target Models:



&#x20; Large Vision-Language Models (LVLMs)





\- Year:



&#x20; 2025





\---



\# 2. Paper





\## Title



FigStep: Jailbreaking Large Vision-Language Models via Typographic Visual Prompts





\## Venue



AAAI 2025 Oral





\## Paper URL





arXiv:



https://arxiv.org/abs/2311.05608





AAAI:



https://ojs.aaai.org/





\---



\# 3. Code Repository





Official GitHub:



https://github.com/CryptoAILab/FigStep





The repository provides:



\- FigStep attack implementation;

\- image prompt generation;

\- jailbreak examples;

\- evaluation scripts.





\---



\# 4. Dataset Download





\## Official Dataset





The dataset is released together with the official repository.





GitHub:



https://github.com/CryptoAILab/FigStep





Dataset location:



```

FigStep/



├── prompts/



├── images/



├── jailbreak\_instances/



└── results/

```





\## HuggingFace Dataset





No official HuggingFace dataset repository.





Users can generate the dataset using the released code.





\---



\# 5. Dataset Background





FigStep studies the vulnerability of

Vision-Language Models under visual jailbreak attacks.





Traditional jailbreak:





```

Text harmful instruction



&#x20;       ↓



LLM



&#x20;       ↓



Safety refusal

```





FigStep:





```

Harmful instruction



&#x20;       ↓



Typography image



&#x20;       ↓



Vision Encoder



&#x20;       ↓



LVLM



&#x20;       ↓



Unsafe response

```





The attack transfers harmful semantics from

the text modality into the visual modality.





\---



\# 6. Dataset Construction





FigStep converts harmful instructions into

images through typography.





Example:





Original text:





```

harmful instruction

```





Transformation:





```

Text



&#x20;↓



Rendered image containing text



&#x20;↓



Image input to LVLM

```





The model receives:





```

Image + benign text prompt

```





instead of directly receiving the harmful instruction.





\---



\# 7. Attack Mechanism





\## Typographic Visual Prompt





The harmful query is displayed as:



\- numbered lists;

\- formatted text;

\- visual instructions.





The attacker then uses a benign instruction:





Example:





```

Please complete the list shown in the image.

```





The LVLM reads the hidden harmful instruction

from the image and generates a response.





\---



\# 8. Dataset Structure





Typical sample:





```

FigStep



├── image



│   └── harmful\_prompt.png





├── instruction



│   └── benign\_text\_prompt





└── metadata

```





Sample:





```json

{

&#x20; "image": "xxx.png",

&#x20; "prompt": "benign instruction",

&#x20; "attack": "FigStep"

}

```





\---



\# 9. Applications





FigStep can be used for:





\- LVLM jailbreak evaluation;



\- Visual safety alignment research;



\- Image-based attack analysis;



\- Cross-modal safety research;



\- Defense method evaluation.





\---



\# 10. Comparison With Related Datasets





| Dataset | Type | Focus |

|---|---|---|

| MM-SafetyBench | Benchmark | Multimodal safety evaluation |

| JailBreakV-28K | Benchmark | Large-scale visual jailbreak |

| FigStep | Attack Dataset | Typography-based jailbreak |

| VLGuard | Safety Dataset | Safety fine-tuning |





\---



\# 11. Citation





```bibtex

@inproceedings{gong2025figstep,

title={FigStep: Jailbreaking Large Vision-Language Models via Typographic Visual Prompts},

author={Gong, Yichen and others},

booktitle={AAAI Conference on Artificial Intelligence},

year={2025}

}

```

