# Frontier Math Agent

A multi-agent research assistant for frontier mathematics.

## Why this project
Frontier mathematics needs more than a single chatbot loop. This project uses a small set of specialized agents that can decompose problems, retrieve prior work, run experiments, and verify reasoning while maintaining a reproducible research log.

## Architecture (MVP)
The initial design uses five cooperating roles:

1. **Planner agent** – decomposes a research question into tractable subproblems.
2. **Retriever agent** – gathers papers, definitions, known results, and examples.
3. **Experiment agent** – runs symbolic and numerical experiments.
4. **Verifier agent** – checks derivations, assumptions, and edge cases.
5. **Research log agent** – records what was tried, what failed, and what remains open.

This is intentionally structured as a multi-role system rather than a monolithic assistant.

## Suggested stack
- Python
- OpenAI Agents SDK or LangGraph
- SymPy
- NumPy / SciPy
- Jupyter notebooks
- pytest
- (later) Lean / Isabelle integration

## MVP priorities
Before formal proof integration, the highest-value capabilities are:
- retrieving prior work,
- testing conjectures,
- generating examples and counterexamples,
- tracking assumptions,
- summarizing promising directions.

## Project status
Early-stage scaffold and architecture baseline.

## Repository layout
```text
frontier-math-agent/
├── README.md
├── LICENSE
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── .env.example
├── docs/
├── src/frontier_math_agent/
├── notebooks/
├── tests/
├── data/
└── .github/
```

## Quick start
```bash
git clone https://github.com/your-username/frontier-math-agent.git
cd frontier-math-agent
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -m src.frontier_math_agent.main
```

## Documentation
Use the docs folder for design artifacts:
- `docs/vision.md`
- `docs/architecture.md`
- `docs/roadmap.md`
- `docs/benchmark_plan.md`
- `docs/safety_and_limits.md`

If documentation grows significantly, move long-form material to a repository wiki and keep the README focused on purpose and usage.
