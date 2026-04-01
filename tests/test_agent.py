from frontier_math_agent.agent import FrontierMathAgent


def test_agent_describe_mentions_planner() -> None:
    assert "Planner" in FrontierMathAgent().describe()
