import random


LOOT_CHANCE = 0.006
NO_SIMULATIONS = int(1e3)


def has_loot() -> bool:
    return random.random() < LOOT_CHANCE


def week_sequence(no_of_weeks: int) -> bool:
    return any([has_loot() for _ in range(no_of_weeks)])


if __name__ == "__main__":

    loot_count = 0
    for sequence_length in range(1, 13):
        for _ in range(NO_SIMULATIONS):
            if week_sequence(sequence_length):
                loot_count += 1
        print(f"{sequence_length}: {round(100*loot_count/NO_SIMULATIONS)}")
