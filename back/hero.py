from dataclasses import dataclass
import math
from typing import List, Dict
import random


@dataclass
class Powerstats:
    intelligence: int
    strength: int
    speed: int
    durability: int
    power: int
    combat: int
    AS: int


@dataclass
class Biography:
    full_name: str
    alter_egos: str
    aliases: List[str]
    place_of_birth: str
    first_appearance: str
    publisher: str
    alignment: str


@dataclass
class Hero:
    id: int
    name: str
    powerstats: Powerstats
    alignment: str
    biography: Biography
    image: str


@dataclass
class HeroFull(Hero):
    isbuffed: bool
    hp: int
    fb: int
    actualStats: Powerstats


@dataclass
class Team:
    alignment: str
    heroes: List[HeroFull]


def calculate_hp(hero: Hero) -> float:
    powerstats = hero.powerstats
    durability = powerstats.durability
    strength = powerstats.strength
    power = powerstats.power
    AS = powerstats.AS
    return math.floor(
        (strength * 0.8 + durability * 0.7 + power) * (1 + AS / 10) / 2 + 100,
    )


def calculate_fb(hero: Hero, team_alignment: str) -> float:
    if team_alignment == hero.alignment or hero.alignment == "neutral":
        return 1 + random.randint(0, 9)
    else:
        return round(1 / (1 + random.randint(0, 9)), 2)


def parse_hero(hero: Hero, team_alignment: str) -> HeroFull:
    powerstats = hero.powerstats
    AS = powerstats.AS
    transformed_stats = Powerstats(**vars(powerstats))
    hp = calculate_hp(hero)
    fb = calculate_fb(hero, team_alignment)
    isbuffed = is_alignment_match(team_alignment, hero.alignment)
    for key in vars(transformed_stats):
        if key != "AS":
            setattr(
                transformed_stats,
                key,
                math.floor(
                    ((2 * getattr(transformed_stats, key) + AS) * fb) / 2
                ),
            )
    return HeroFull(
        **vars(hero),
        hp=hp,
        fb=fb,
        actualStats=transformed_stats,
        isbuffed=isbuffed,
    )


def get_team_alignment(heroes: List[HeroFull]) -> str:
    alignment_count: Dict[str, int] = {}
    for hero in heroes:
        if hero.alignment in alignment_count:
            alignment_count[hero.alignment] += 1
        else:
            alignment_count[hero.alignment] = 1
    return max(alignment_count, key=alignment_count.get)


def is_alignment_match(team_alignment: str, hero_alignment: str) -> bool:
    return team_alignment == hero_alignment or hero_alignment == "neutral"
