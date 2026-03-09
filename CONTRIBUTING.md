# Contributing to Jazzy AI Models

## Running the Research Spider

```bash
python3 research_spider.py
```

This will generate:
- `README.md` - Research report
- `models_database.json` - Full model database

## Adding New Search Queries

Edit `research_spider.py` and add to the `search_queries` list.

## Model Categories

- Neuromorphic: Brain-inspired, spiking neural networks
- Reasoning: Chain-of-thought, o1-style models
- Code Specialists: Programming-focused models
- Multimodal: Vision + language models
- Tiny Powerhouses: 1-3B parameter models
- Experimental: Research/alpha/beta models
