import copy, queue, dataclasses
# Spell Class
class Effect:
    def __repr__(s):
        return f"{s.__class__.__name__}: {s.Turns} Turns"
    def __init__(s, Cost, World, Turns = 0):
        s.Boss, s.Turns = World.Boss, Turns
        s.Effects = World.Effects
        s.Player = World.Player
        if Turns:
            s.Effects[type(s)] = s
        s.Player.Mana -= s.Cost
        World.Spent += Cost
    def StartTurn(s):
        s.Turns -= 1
        return s.Turns
    def EndEffect(s):
        del s.Effects[type(s)]
# Children
class Missile(Effect):
    def __init__(s, World):
        super().__init__(s.Cost, World)
        s.Boss.HP -= 4
    Cost = 53
class Drain(Effect):
    def __init__(s, World):
        super().__init__(s.Cost, World)
        s.Player.HP += 2
        s.Boss.HP -= 2
    Cost = 73
class Shield(Effect):
    def __init__(s, World):
        super().__init__(s.Cost, World, 6)
        s.Player.Armor += 7
    def EndEffect(s):
        super().EndEffect()
        s.Player.Armor -= 7
    Cost = 113
class Poison(Effect):
    def __init__(s, World):
        super().__init__(s.Cost, World, 6)
    def StartTurn(s):
        s.Boss.HP -= 3
        return super().StartTurn()
    Cost = 173
class Recharge(Effect):
    def __init__(s, World):
        super().__init__(s.Cost, World, 5)
    def StartTurn(s):
        s.Player.Mana += 101
        return super().StartTurn()
    Cost = 229
# Entities
@dataclasses.dataclass
class Player:
    def __repr__(s):
        return f"[Player] HP: {s.HP}, Mana: {s.Mana}, Armor: {s.Armor}"
    HP: int; Mana: int; Armor: int = 0
@dataclasses.dataclass
class Boss:
    def __repr__(s):
        return f"[Boss] HP: {s.HP}, Damage: {s.Damage}"
    HP: int; Damage: int
Spells = Effect.__subclasses__()
# Compact State
class World:
    def __init__(s, Player, Boss):
        s.Cast, s.Spent, s.Effects = True, 0, {}
        s.Player, s.Boss = Player, Boss
    def __repr__(s):
        return "\n".join(map(repr, [s.Player, s.Boss, s.Effects]))
    def __lt__(s, o):
        return s.Boss.HP * s.Spent < o.Boss.HP * o.Spent
    def CastOptions(s):
        return filter(lambda x: x not in s.Effects
            and x.Cost <= s.Player.Mana, Spells)
    def ExecuteTurn(s, Delta = 0):
        Copies = []
        if s.Cast:
            s.Player.HP -= Delta
        if s.Player.HP <= 0:
            return Copies
        for Active in (*s.Effects.values(),):
            if not Active.StartTurn():
                Active.EndEffect()
        if s.Boss.HP <= 0:
            World.Least = s.Spent
            return s.Spent
        if s.Cast:
            for Opt in s.CastOptions():
                Opt(Alt := copy.deepcopy(s))
                if Alt.Spent < World.Least:
                    Alt.Cast = not s.Cast
                    Copies.append(Alt)
        else:
            s.Player.HP -= max(1, s.Boss.Damage -
                s.Player.Armor); s.Cast = not s.Cast
            if s.Player.HP > 0:
                Copies.append(s)
        return Copies
# A* Like Search
def A_Search(Delta = 0):
    World.Least, Q = 5000, queue.PriorityQueue()
    Q.put(World(Player(50, 500), Boss(71, 10)))
    while isinstance(Value := Q.get().ExecuteTurn
        (Delta), list): [*map(Q.put, Value)]
    return Value
# Run Problem
print("Silver:", A_Search())
print("Gold:", A_Search(1))
