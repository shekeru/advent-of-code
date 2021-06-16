import copy
# Generic Spell
class Effect:
    def __init__(s, Cost, World, Turns = 0):
        s.World, s.Turns = World, Turns
        if Turns:
            s.World['Effects'][type(s)] = s
        World['PlayerMana'] -= Cost
        World['SpentMana'] += Cost
    def StartTurn(s):
        s.Turns -= 1
        return s.Turns
    def EndEffect(s):
        del s.World['Effects'][type(s)]
# Spell Classes
class Missile(Effect):
    def __init__(s, World):
        super().__init__(s.Cost, World)
        World['BossHp'] -= 4
    Cost = 53
class Drain(Effect):
    def __init__(s, World):
        super().__init__(s.Cost, World)
        s.World['PlayerHp'] += 2
        s.World['BossHp'] -= 2
    Cost = 73
class Shield(Effect):
    def __init__(s, World):
        super().__init__(s.Cost, World, 6)
        s.World['PlayerArmor'] += 7
    def EndEffect(s):
        super().EndEffect()
        s.World['PlayerArmor'] -= 7
    Cost = 113
class Poison(Effect):
    def __init__(s, World):
        super().__init__(s.Cost, World, 6)
    def StartTurn(s):
        s.World['BossHp'] -= 3
        return super().StartTurn()
    Cost = 173
class Recharge(Effect):
    def __init__(s, World):
        super().__init__(s.Cost, World, 5)
    def StartTurn(s):
        s.World['PlayerMana'] += 101
        return super().StartTurn()
    Cost = 229
Spells = Effect.__subclasses__()
# Functions
def CastOptions(World):
    return tuple(Spell for Spell in Spells if Spell not
        in World['Effects'] and Spell.Cost <= World['PlayerMana'])
def RunDFS(World, Delta = 0):
    global Least
    if World['CastTurn']:
        World['PlayerHp'] -= Delta
    if World['PlayerHp'] <= 0:
        return
    for Active in (*World['Effects'].values(), ):
        if not Active.StartTurn():
            Active.EndEffect()
    if World['BossHp'] <= 0:
        return (Least := World['SpentMana'])
    if World['CastTurn']:
        for Opt in CastOptions(World):
            Opt(Alt := copy.deepcopy(World))
            if Alt['SpentMana'] < Least:
                Alt['CastTurn'] = not World['CastTurn']
                RunDFS(Alt, Delta)
    else:
        World['PlayerHp'] -= max(1, World['BossDmg'] - World['PlayerArmor'])
        World['CastTurn'] = not World['CastTurn']
        RunDFS(World, Delta)
    return Least
# Game State
State = {
    'BossHp': 71,
    'BossDmg': 10,
    'PlayerHp': 50,
    'PlayerMana': 500,
    'PlayerArmor': 0,
    'CastTurn': True,
    'SpentMana': 0,
    'Effects': {},
}
# Run Problem
Least = 7500
print("Silver:", RunDFS(State))

Least = 7500
print("Gold:", RunDFS(State, 1))
