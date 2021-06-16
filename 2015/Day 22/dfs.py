import copy
# Spell Class
class Effect:
    def __repr__(s):
        return f"{s.__class__.__name__}: {s.Turns} Turns"
    def __init__(s, Cost, World, Turns = 0):
        World.Casts.append(s.__class__.__name__)
        s.Effects = World.Effects
        s.Player = World.Player
        s.Boss = World.Boss
        if Turns:
            s.Effects.append(s)
        s.Player.Mana -= s.Cost
        World.Spent += Cost
        s.Turns = Turns
    def StartTurn(s):
        s.Turns -= 1
        return s.Turns
    def EndEffect(s):
        pass
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
class Player:
    def __init__(s, HP, Mana):
        s.HP, s.Mana = HP, Mana
        s.Armor = 0
    def __repr__(s):
        return f"[Player] HP: {s.HP}, Mana: {s.Mana}, Armor: {s.Armor}"

class Boss:
    def __init__(s, HP, Damage):
        s.HP, s.Damage = HP, Damage
    def __repr__(s):
        return f"[Boss] HP: {s.HP}, Damage: {s.Damage}"
# Compact State
class World:
    def __init__(s, Player, Boss):
        s.Casts, s.Effects = [], []
        s.Player, s.Boss = Player, Boss
        s.Cast, s.Spent = True, 0
    def __repr__(s):
        return "\n".join(map(repr, [s.Player, s.Boss, s.Effects]))
    def CastOptions(s):
        Active = [type(x) for x in s.Effects]
        return [Spell for Spell in (Recharge, Poison, Shield, Drain, Missile)
            if Spell not in Active and Spell.Cost <= s.Player.Mana]
    def ExecuteTurns(s, Delta = 0):
        if s.Cast:
            s.Player.HP -= Delta
        if s.Player.HP <= 0:
            return
        for Eff in (*s.Effects,):
            if not Eff.StartTurn():
                s.Effects.remove(Eff)
                Eff.EndEffect()
        if s.Boss.HP <= 0:
            World.Least = min(World.Least, s.Spent)
            return print(World.Least)
        if s.Cast:
            for Opt in s.CastOptions():
                Opt(Alt := copy.deepcopy(s))
                if Alt.Boss.HP > 0 and Alt.Spent < World.Least:
                    Alt.Cast = not s.Cast
                    Alt.ExecuteTurns(Delta)
        else:
            s.Player.HP -= max(1, s.Boss.Damage -
                s.Player.Armor); s.Cast = not s.Cast
            s.ExecuteTurns(Delta)
# Outside Logic
Ex1_P, Ex1_B = Player(50, 500), Boss(71, 10)

World.Least = 2500
World(Ex1_P, Ex1_B).ExecuteTurns()
print("Silver:", World.Least)

World.Least = 5000
World(Ex1_P, Ex1_B).ExecuteTurns(1)
print("Gold:", World.Least)
