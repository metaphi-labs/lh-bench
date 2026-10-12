# LH-Bench

**A benchmark for long-horizon agents on subjective enterprise work.**

[Paper (arXiv:2603.22744)](https://arxiv.org/abs/2603.22744) · [Leaderboard](https://metaphi.ai/benchmarks/lh-bench) · [Datasets](https://huggingface.co/collections/metaphilabs/lh-bench-6acd48af30ec71aff2a0ffcd)

Real enterprise work is subjective, and a unit test cannot score it. LH-Bench scores autonomous, long-horizon agents on that kind of work with three signals that are checked against each other:

1. **Expert-grounded rubrics** that give an LLM judge the domain context it needs to score the process.
2. **Curated ground-truth artifacts** that give stepwise reward on the output.
3. **Pairwise human preference** from domain experts, to confirm the ranking.

Findings from the paper: rubrics written by domain experts give more reliable judge scores than rubrics written by an LLM (inter-judge agreement κ = 0.60 against 0.46), human preference confirms the same top-tier separation (p < 0.05), and with runtime verification hooks agents recover from 70% of errors across 96 runs.

This repository is the index for the benchmark: what it contains, where the data is, the current results and how to cite it. The evaluation harness is not yet published here.

## Environments

| Environment | Tasks | What the agent does | How it is scored |
|---|---|---|---|
| Figma to code | 33 | Builds a real Figma design into a React and Tailwind app through the Figma API | A visual judge against the design on eight weighted rubrics, and expert preference |
| Programmatic content | 41 courses, 183 chapters | Turns source documents into courses rendered as programmatic video | Citation grounding, educator rubrics and expert preference |
| Financial documents | 37 | Reads business bank statements into labelled transactions | Extraction and categorisation against risk analysts' labels |
| Figma design | 10 | Designs inside a headless Figma on one design system | Completeness and consistency checks |

The paper reports results on the first two. The other two are part of the suite and have no published results yet.

## Data

All datasets are on Hugging Face under [`metaphilabs`](https://huggingface.co/metaphilabs).

| Dataset | Contents | License | Access |
|---|---|---|---|
| [`frontend-figma-to-code`](https://huggingface.co/datasets/metaphilabs/frontend-figma-to-code) | The Figma designs the agents build from | MIT | Open |
| [`figma2code-expert-preferences`](https://huggingface.co/datasets/metaphilabs/figma2code-expert-preferences) | Pairwise expert votes on the built pages, with reasoning and a quality rating | CC BY-NC 4.0 | Open |
| [`remotion-video-gen`](https://huggingface.co/datasets/metaphilabs/remotion-video-gen) | Courses with source documents, line-level citation ground truth and educator rubrics | MIT | Open |
| [`remotion-video-preferences`](https://huggingface.co/datasets/metaphilabs/remotion-video-preferences) | Pairwise expert votes on the rendered chapters, with reasoning | CC BY-NC 4.0 | Open |
| [`credit-underwriting-preview`](https://huggingface.co/datasets/metaphilabs/credit-underwriting-preview) | A preview of the bank statement cases with the transaction taxonomy | MIT | Open |
| [`credit-underwriting-commercial`](https://huggingface.co/datasets/metaphilabs/credit-underwriting-commercial) | The redacted bank statement cases with extraction and categorisation ground truth | MIT | On request |

```python
from datasets import load_dataset

tasks = load_dataset("metaphilabs/frontend-figma-to-code", split="train")
votes = load_dataset("metaphilabs/figma2code-expert-preferences", split="train")
print(tasks[0]["id"], len(votes))
```

[`examples/load.py`](examples/load.py) loads every open dataset and prints its size and columns.

## Results

Results as of March 2026. The live leaderboard is at [metaphi.ai/benchmarks/lh-bench](https://metaphi.ai/benchmarks/lh-bench).

**Figma to code**, output score from 1 to 5, 33 tasks. `n` is the number of tasks scored; ± is a 95% bootstrap interval where the run count allows.

| # | Model | Harness | Score | ± | n |
|---|---|---|---|---|---|
| 1 | GPT-5.2 Pro | Codex | 4.27 | | 18 |
| 2 | Claude Opus 4.6 | Claude Code | 4.19 | 0.28 | 32 |
| 3 | GPT-5.2 | Codex | 3.94 | 0.36 | 31 |
| 4 | Claude Opus 4.5 | Claude Code | 3.88 | | 29 |
| 5 | Gemini 3.1 Pro | Gemini CLI | 3.73 | 0.44 | 29 |
| 6 | Claude Sonnet 4.5 | Claude Code | 3.66 | | 22 |
| 7 | Gemini 3 Pro | Gemini CLI | 3.59 | | 22 |

**Programmatic content**, artifact score from 0 to 1, course-level means over 41 courses and 183 chapters, 95% bootstrap intervals.

| # | Model | Harness | Score | ± |
|---|---|---|---|---|
| 1 | Claude Opus 4.6 | Claude Code | 0.612 | 0.069 |
| 2 | Gemini 3.1 Pro | Gemini CLI | 0.526 | 0.063 |
| 3 | GPT-5.2 | Codex | 0.478 | 0.044 |

## Evaluate your agent

To have an agent scored on LH-Bench, write to [agent@metaphi.ai](mailto:agent@metaphi.ai).

## Citation

```bibtex
@article{chandwani2026lhbench,
  title   = {LH-Bench: Skill-Grounded Evaluation of Long-Horizon Agents on Subjective Enterprise Tasks},
  author  = {Chandwani, Abhishek and Gupta, Ishan},
  journal = {arXiv preprint arXiv:2603.22744},
  year    = {2026}
}
```

An earlier version of the paper was titled "Beyond Binary Correctness: Scaling Evaluation of Long-Horizon Agents on Subjective Enterprise Tasks". It is the same work; please cite it under the current title.

## License

The contents of this repository are released under the MIT License. Each dataset carries its own license, listed above.
