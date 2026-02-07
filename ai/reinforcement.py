import random

# Basic reinforcement memory
strategy_memory = {}

def choose_strategy(account_id):
    """
    Choose posting strategy based on previous rewards.
    """
    if account_id not in strategy_memory:
        strategy_memory[account_id] = {
            "thread": 0,
            "single": 0,
            "question": 0
        }

    strategies = strategy_memory[account_id]

    # Pick highest rewarded strategy
    best = max(strategies, key=strategies.get)

    # Add exploration (20% random)
    if random.random() < 0.2:
        return random.choice(list(strategies.keys()))

    return best


def reward_strategy(account_id, strategy, reward_score):
    """
    Reward strategy based on performance score.
    """
    if account_id not in strategy_memory:
        return

    strategy_memory[account_id][strategy] += reward_score
