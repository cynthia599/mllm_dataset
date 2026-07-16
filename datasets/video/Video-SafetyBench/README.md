\# Video-SafetyBench





\## 1. Overview





\- Dataset Name:



&#x20; Video-SafetyBench





\- Full Name:



&#x20; Video-SafetyBench: A Benchmark for Safety Evaluation of Video LVLMs





\- Modality:



&#x20; Video + Text





\- Task:



&#x20; Video Large Vision-Language Model Safety Evaluation





\- Target Models:



&#x20; Video-Language Models (Video LVLMs)





\- Year:



&#x20; 2025





\- Dataset Scale:



&#x20; - 2,264 video-text pairs

&#x20; - 13 unsafe categories

&#x20; - 48 fine-grained subcategories





\## 2. Paper





\### Title



Video-SafetyBench: A Benchmark for Safety Evaluation of Video LVLMs





\### Venue



NeurIPS 2025 Datasets and Benchmarks Track





\### Paper URL



arXiv:



https://arxiv.org/abs/2505.11842





\### Citation



```bibtex

@article{liu2025videosafetybench,

&#x20; title={Video-SafetyBench: A Benchmark for Safety Evaluation of Video LVLMs},

&#x20; author={Liu, Xuannan and Li, Zekun and He, Zheqi and others},

&#x20; journal={arXiv preprint arXiv:2505.11842},

&#x20; year={2025}

}

```





\## 3. Dataset Download





\### Official Dataset



HuggingFace:



https://huggingface.co/datasets/BAAI/Video-SafetyBench





\### Dataset Files





```

Video-SafetyBench



├── data/

│

├── benign\_data.json

│

├── harmful\_data.json

│

├── video.tar.gz

│

└── README.md

```





File description:





| File | Description |

|---|---|

| benign\_data.json | benign query annotations |

| harmful\_data.json | harmful query annotations |

| video.tar.gz | original video files |

| data | dataset metadata |





The complete video package:



```

video.tar.gz

```



is approximately 13.2 GB.





Access requires accepting the dataset license agreement on HuggingFace.





\## 4. Code Repository





Official GitHub:



https://github.com/flageval-baai/Video-SafetyBench





The repository provides:



\- Dataset processing

\- Model evaluation scripts

\- Response evaluation

\- Safety scoring





\## 5. Dataset Construction





Video-SafetyBench focuses on safety evaluation under dynamic video inputs.





Different from image safety benchmarks:





```

Image + Text



&#x20;      ↓



Static visual understanding





Video + Text



&#x20;      ↓



Temporal visual understanding

```





Video introduces additional risks:





\- temporal reasoning;

\- motion information;

\- event understanding;

\- video-induced harmful context.





The benchmark generates safety-related video-text pairs to evaluate whether Video LVLMs can maintain safety alignment under video inputs.





\## 6. Dataset Structure





Each sample contains:





```

sample



├── question\_id



├── video\_path



├── question



├── harmful\_intention



├── category



├── subcategory



└── question\_type

```





Field description:





| Field | Description |

|-|-|

| video\_path | video file location |

| question | user query |

| harmful\_intention | harmful objective |

| category | safety category |

| subcategory | fine-grained risk type |

| question\_type | harmful or benign query |





\## 7. Query Types





Video-SafetyBench contains two types of queries:





\## 1. Harmful Query





The question itself directly contains harmful intent.





Example:





```

Video:

Dangerous action scene





Question:

How can someone perform this action?

```





Purpose:



Test direct harmful instruction handling.





\---



\## 2. Benign Query





The question appears harmless,

but becomes unsafe when combined with video context.





Example:





```

Video:

Unsafe activity





Question:

What is happening in this video?

```





Purpose:



Test whether models can correctly understand hidden video risks.





\## 8. Safety Categories





The dataset covers:





\### Unsafe Content



Including:



\- Violence

\- Illegal activities

\- Self-harm

\- Harmful behaviors





\### Social Risks



Including:



\- Hate

\- Discrimination

\- Privacy risks





\### Other Safety Risks



Including:



\- Dangerous actions

\- Misleading scenarios





The benchmark contains:



\- 13 major categories

\- 48 fine-grained subcategories





\## 9. Applications





Video-SafetyBench can be used for:





\- Video LVLM safety evaluation;



\- Video jailbreak attack research;



\- Temporal safety reasoning analysis;



\- Multimodal safety alignment;



\- Defense method evaluation;



\- Safety representation analysis.





\## 10. Comparison With Related Benchmarks





| Dataset | Modality | Main Focus |

|---|---|---|

| MM-SafetyBench | Image + Text | Image jailbreak |

| JailBreakV-28K | Image + Text | Vision jailbreak |

| VLGuard | Image + Text | Safety fine-tuning |

| JALMBench | Audio + Text | Audio jailbreak |

| Video-SafetyBench | Video + Text | Video LVLM safety |





\## 11. Download Example





Install HuggingFace CLI:





```bash

pip install huggingface\_hub

```





Login:





```bash

hf auth login

```





Download:





```bash

hf download BAAI/Video-SafetyBench \\

\--repo-type dataset \\

\--local-dir Video-SafetyBench

```





\## 12. License





License:



CC BY-NC-SA 4.0





The dataset is intended for

non-commercial AI safety research.

