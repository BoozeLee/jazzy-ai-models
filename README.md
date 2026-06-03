# Jazzy AI Models

A lightweight Hugging Face research crawler for discovering under-the-radar AI models. The project ranks models by popularity signals, capability tags, and practical local-development value, then produces a markdown report for model selection and experimentation.

## What It Demonstrates

- Python data collection against public model metadata.
- Simple ranking heuristics for "hidden gem" model discovery.
- Practical model scouting across multimodal, reasoning, code, tiny, and experimental categories.
- A small, readable automation script that can be adapted for portfolio research or internal tooling.

## Stack

- **Language:** Python 3
- **HTTP:** `requests`
- **Output:** generated markdown research report

## Files

```text
research_spider.py      # Crawls and ranks model metadata
requirements.txt        # Runtime dependencies
README.md               # Project overview and usage
```

## Local Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python research_spider.py
```

The script writes its findings as markdown so the output can be reviewed, committed, or copied into a deeper research workflow.

## Validation

```bash
python -m py_compile research_spider.py
python research_spider.py
```

If the Hugging Face API changes or rate-limits requests, rerun with a smaller query set before treating the output as final research.

## Status

Portfolio research utility. The repository is public to show small-tool automation, AI model discovery workflow design, and clean Python scripting.
