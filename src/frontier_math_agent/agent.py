from .config import Settings


class FrontierMathAgent:
    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or Settings()

    def describe(self) -> str:
        return (
            "Planner, Retriever, Experiment, Verifier, and Research Log "
            "agents orchestrated for mathematical research workflows."
        )
