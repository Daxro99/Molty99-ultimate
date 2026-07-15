from dataclasses import dataclass
@dataclass
class Situation:
    hp_percent: float
    ep_percent: float
    enemy_count: int
    loot_count: int
    guardian_near: bool
    danger_level: float
    phase: str
