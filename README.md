# Crosslingual On-Policy Self-Distillation for Multilingual Reasoning

<p align="center">
  <a href="https://arxiv.org/abs/2605.09548"><img src="https://img.shields.io/badge/arXiv-COPSD-b31b1b.svg" alt="arXiv"></a>
  <a href="https://huggingface.co/datasets/yihongLiu/COPSD-AfriMGSM-TrainDataset"><img src="https://img.shields.io/badge/🤗%20Dataset-Hugging%20Face-yellow" alt="AfriMGSM-Train-DataSet"></a>
  <a href="https://huggingface.co/datasets/yihongLiu/COPSD-PolyMath-TrainDataset"><img src="https://img.shields.io/badge/🤗%20Dataset-Hugging%20Face-yellow" alt="PolyMath-Train-DataSet"></a>
</p>

Official code release for **Crosslingual On-Policy Self-Distillation for Multilingual Reasoning**.

> **Links:** [Paper](https://arxiv.org/abs/2605.09548) · [TrainData1](https://huggingface.co/datasets/yihongLiu/COPSD-AfriMGSM-TrainDataset) · [TrainData2](https://huggingface.co/datasets/yihongLiu/COPSD-PolyMath-TrainDataset)


## Overview

Large language models have achieved strong mathematical reasoning performance in English, but this ability is not equally accessible across languages. In particular, low-resource languages often show much lower reasoning accuracy, even when the underlying reasoning problem is equivalent.

We propose **Crosslingual On-Policy Self-Distillation (COPSD)**, a framework that transfers a model's own high-resource reasoning behavior to low-resource languages. COPSD uses the same model as both student and teacher:

During training:

- the **student** receives only the low-resource or target-language problem and generates an on-policy reasoning trajectory;
- the **teacher** receives privileged crosslingual context, including the English problem translation and the English reference solution;
- training minimizes a full-distribution token-level divergence between the teacher and student policies on the student's own rollouts.

This repository builds on the original [OPSD](https://github.com/siyan-zhao/OPSD) codebase and adapts it for crosslingual and low-resource multilingual mathematical reasoning.

## Method Sketch

```text
Low-resource target-language problem
        │
        ▼
 Student policy generates an on-policy reasoning trajectory
        │
        ▼
 Same model as teacher, conditioned on privileged English context
        │
        ├── English problem translation
        └── English reference solution
        │
        ▼
 Full-distribution token-level self-distillation loss on the student's own rollout
```

## Repository Structure

```text
.
├── multilingual_opsd_train.py          # Main COPSD training entry point
├── multilingual_opsd_trainer.py        # COPSD trainer and self-distillation losses
├── multilingual_data_collator.py       # Multilingual student/teacher prompt construction
├── multilingual_grpo_train.py          # Multilingual GRPO baseline training
├── language_config.py                  # Language-specific prompts, labels, and thinking prefixes
├── accelerate.yaml                     # Accelerate/DeepSpeed launch config
├── environment.yml                     # Conda environment
├── multilingual_scripts/
│   └── run_all_opsd_4b_3000.sh         # Qwen3-4B multilingual COPSD training script
├── african_langs_scripts/
│   ├── run_all_opsd_1.7b_train.sh      # Qwen3-1.7B AfriMGSM training script
│   ├── run_all_opsd_4b_train.sh        # Qwen3-4B AfriMGSM training script
│   └── run_all_opsd_8b_train.sh        # Qwen3-8B AfriMGSM training script
├── polymath_eval/
│   ├── evaluate_math.py                # PolyMath evaluation
│   └── run_eval_4b_all_checkpoints.sh  # Evaluate Qwen3-4B checkpoints
└── african_langs_eval/
    ├── evaluate_math.py                # AfriMGSM evaluation
    ├── run_afrimgsm_one_lang_all_ckpts_1.7b.sh
    ├── run_afrimgsm_one_lang_all_ckpts_4b.sh
    └── run_afrimgsm_one_lang_all_ckpts_8b.sh
```

## Supported Languages

The current codebase includes language-specific prompts and labels for:

- **PolyMath / multilingual math languages:** `BN`, `DE`, `EN`, `ES`, `FR`, `JA`, `RU`, `SW`, `TE`, `TH`, `ZH`
- **AfriMGSM languages:** `AMH`, `EWE`, `HAU`, `IBO`, `KIN`, `LIN`, `LUG`, `ORM`, `SNA`, `SOT`, `SWA`, `TWI`, `VAI`, `WOL`, `XHO`, `YOR`, `ZUL`

## Installation

```bash
conda env create -f environment.yml
conda activate opsd
```

The training scripts use FlashAttention 2 by default. If your environment does not already provide it, install a version compatible with your CUDA and PyTorch setup, for example:

```bash
pip install flash-attn --no-build-isolation
```

Before running training, update the placeholder paths in the training files/scripts:

```python
CACHE_ROOT = "YOUR PATH"
```

and in shell scripts:

```bash
PROJECT_ROOT="YOUR PATH"
```

## Data Format

Our current code expects translated JSON files with English source reasoning and target-language problem fields. A minimal example is:

```json
{
  "problem": "English source problem here.",
  "solution": "English reference solution here.",
  "problem_de": "German translated problem here.",
}
```

At runtime, `multilingual_opsd_train.py` adds:

- `target_lang`
- `problem_en`

You can adapt the script to the training set structure we reliesed to HuggingFace: [Train Data for AfriMGSM Languages](https://huggingface.co/datasets/yihongLiu/COPSD-AfriMGSM-TrainDataset) · [Train Data for PolyMath Languages](https://huggingface.co/datasets/yihongLiu/COPSD-PolyMath-TrainDataset). 

## Training

### Multilingual COPSD on Qwen3-4B

Edit `multilingual_scripts/run_all_opsd_4b_3000.sh` to set the data directory, output directory, GPU IDs, and port, then run:

```bash
bash multilingual_scripts/run_all_opsd_4b_3000.sh
```

The default script trains separate models for following languages:

```text
BN, SW, TE, TH, ZH, ES, RU, JA
```

### AfriMGSM COPSD

For African-language experiments, use one of the scripts in `african_langs_scripts/`:

```bash
bash african_langs_scripts/run_all_opsd_1.7b_train.sh
bash african_langs_scripts/run_all_opsd_4b_train.sh
bash african_langs_scripts/run_all_opsd_8b_train.sh
```

These scripts train separate models for the supported AfriMGSM languages.


## Important Training Options

| Argument | Description |
| --- | --- |
| `--train_language` | Target language code, e.g. `DE`, `ZH`, `SWA`, `YOR`. |
| `--translated_data_path` | Path to the translated JSON file. |
| `--fixed_teacher` | Use the base model without LoRA adapters as a fixed teacher. Requires `--use_peft`. |
| `--student_enable_thinking` | Enable target-language thinking prefix in the student prompt. |
| `--include_problem_en` | Include the English source problem in the teacher context. |
| `--include_reference_solution_en` | Include the English reference solution in the teacher context. |


## Evaluation

### PolyMath

```bash
cd polymath_eval
bash run_eval_4b_all_checkpoints.sh
```

The script evaluates the base model and available COPSD checkpoints across the configured languages.

### AfriMGSM

```bash
cd african_langs_eval
bash run_afrimgsm_one_lang_all_ckpts_1.7b.sh
bash run_afrimgsm_one_lang_all_ckpts_4b.sh
bash run_afrimgsm_one_lang_all_ckpts_8b.sh
```

Evaluation outputs are saved under `eval_results/`.


## Released Assets

- **Paper:** [arXiv](https://arxiv.org/abs/2605.09548)
- **Data:** [Train Data for AfriMGSM Languages](https://huggingface.co/datasets/yihongLiu/COPSD-AfriMGSM-TrainDataset) · [Train Data for PolyMath Languages](https://huggingface.co/datasets/yihongLiu/COPSD-PolyMath-TrainDataset)

## Citation

If you find this repository useful, please cite our paper:

```bibtex
@misc{liu2026crosslingualonpolicyselfdistillation,
      title={Crosslingual On-Policy Self-Distillation for Multilingual Reasoning}, 
      author={Yihong Liu and Raoyuan Zhao and Michael A. Hedderich and Hinrich Schütze},
      year={2026},
      eprint={2605.09548},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2605.09548}, 
}
```

This codebase is adapted from OPSD. Please also consider citing the original OPSD work:

```bibtex
@misc{zhao2026selfdistilledreasoneronpolicyselfdistillation,
      title={Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models}, 
      author={Siyan Zhao and Zhihui Xie and Mengchen Liu and Jing Huang and Guan Pang and Feiyu Chen and Aditya Grover},
      year={2026},
      eprint={2601.18734},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2601.18734}, 
}
```

## Acknowledgements

This repository builds on the excellent [OPSD](https://github.com/siyan-zhao/OPSD) implementation for on-policy self-distillation. We thank the authors for releasing their code.
