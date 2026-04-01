from .agent import FrontierMathAgent


def main() -> None:
    agent = FrontierMathAgent()
    print(agent.describe())


if __name__ == "__main__":
    main()
