# Frontier Math Agent

An agentic research assistant for frontier mathematics.

## Vision
This project explores how AI agents can assist mathematical research by:
- retrieving relevant literature,
- proposing conjectures,
- testing examples and counterexamples,
- performing symbolic and numeric experiments,
- checking assumptions in proof sketches,
- and maintaining a reproducible research log.

## Core Goals
- Assist, not replace, mathematical reasoning
- Make research workflows more reproducible
- Separate speculation from verified results
- Build evaluation benchmarks for mathematical research assistance

## Current Capabilities
- Literature-aware reasoning
- Symbolic computation workflows
- Numeric experiment pipelines
- Conjecture decomposition
- Proof-sketch verification
- Counterexample search

## Project Status
Early-stage research prototype.

## Repository Structure
See `docs/architecture.md` and `docs/roadmap.md`.

## Quick Start
```bash
git clone https://github.com/your-username/frontier-math-agent.git
cd frontier-math-agent
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -m src.frontier_math_agent.main
