from collections import Counter
from random import choice

Advantage = Counter(advantage=1, threat=-1)
Blank = Counter()
Dark = Counter(dark=1)
Dispair = Counter(dispair=1, success=-1)
Failure = Counter(failure=1, success=-1)
Light = Counter(light=1)
Success = Counter(success=1)
Threat = Counter(threat=1, advantage=-1)
Triumph = Counter(triumph=1)

Difficulty = (
    Blank, Failure, Failure + Failure, Threat, Threat,
    Threat, Threat + Threat, Threat + Failure,
)
Ability = (
    Blank, Success, Success, Success + Success, Advantage,
    Advantage, Advantage + Success, Advantage + Advantage
)
Boost = (
    Blank, Blank, Advantage + Advantage, Advantage, Success + Advantage, Success
)
Setback = (
    Blank, Blank, Failure, Failure, Threat, Threat
)
Proficiency = (
    Blank, Success, Success, Success + Success, Success + Success, Advantage,
    Success + Advantage, Success + Advantage, Success + Advantage,
    Advantage + Advantage, Advantage + Advantage, Triumph
)
Challenge = (
    Blank, Failure, Failure, Failure + Failure, Failure + Failure, Threat,
    Threat, Failure + Threat, Failure + Threat, Threat + Threat,
    Threat + Threat, Dispair
)
Force = (
    Dark, Dark, Dark, Dark, Dark, Dark, Dark + Dark,
    Light, Light, Light + Light, Light + Light, Light + Light
)


def roll(
    boost=0,
    setback=0,
    ability=0,
    difficulty=0,
    proficiency=0,
    challenge=0,
    force=0
):
    boost = sum((choice(Boost) for _ in range(boost)), Blank)
    setback = sum((choice(Setback) for _ in range(setback)), Blank)
    ability = sum((choice(Ability) for _ in range(ability)), Blank)
    difficulty = sum((choice(Difficulty) for _ in range(difficulty)), Blank)
    proficiency = sum((choice(Proficiency) for _ in range(proficiency)), Blank)
    challenge = sum((choice(Challenge) for _ in range(challenge)), Blank)
    force = sum((choice(Force) for _ in range(force)), Blank)
    return (
        boost + setback + ability + difficulty
        + proficiency + challenge + force
    )


if __name__ == '__main__':
    print roll(proficiency=4, challenge=4)