import re

inp_imm = """3578 units each with 3874 hit points (immune to radiation) with an attack that does 10 bludgeoning damage at initiative 17
865 units each with 10940 hit points (weak to bludgeoning, cold) with an attack that does 94 cold damage at initiative 19
3088 units each with 14516 hit points (immune to cold) with an attack that does 32 bludgeoning damage at initiative 4
2119 units each with 6577 hit points (immune to slashing, fire; weak to cold) with an attack that does 22 bludgeoning damage at initiative 6
90 units each with 2089 hit points (immune to bludgeoning) with an attack that does 213 cold damage at initiative 14
1341 units each with 4768 hit points (immune to bludgeoning, radiation, cold) with an attack that does 34 bludgeoning damage at initiative 1
2846 units each with 5321 hit points (immune to cold) with an attack that does 17 cold damage at initiative 13
4727 units each with 7721 hit points (weak to radiation) with an attack that does 15 fire damage at initiative 10
1113 units each with 11891 hit points (immune to cold; weak to fire) with an attack that does 80 fire damage at initiative 18
887 units each with 5712 hit points (weak to bludgeoning) with an attack that does 55 slashing damage at initiative 15"""

inp_infection = """3689 units each with 32043 hit points (weak to cold, fire; immune to slashing) with an attack that does 16 cold damage at initiative 7
33 units each with 10879 hit points (weak to slashing) with an attack that does 588 slashing damage at initiative 12
2026 units each with 49122 hit points (weak to bludgeoning) with an attack that does 46 fire damage at initiative 16
7199 units each with 9010 hit points (immune to radiation, bludgeoning; weak to slashing) with an attack that does 2 slashing damage at initiative 8
2321 units each with 35348 hit points (weak to cold) with an attack that does 29 radiation damage at initiative 20
484 units each with 21952 hit points with an attack that does 84 radiation damage at initiative 9
2531 units each with 24340 hit points with an attack that does 18 fire damage at initiative 3
54 units each with 31919 hit points (immune to bludgeoning, cold) with an attack that does 1178 radiation damage at initiative 5
1137 units each with 8211 hit points (immune to slashing, radiation, bludgeoning; weak to cold) with an attack that does 14 bludgeoning damage at initiative 11
2804 units each with 17948 hit points with an attack that does 11 radiation damage at initiative 2"""

class group:
	def __init__(self, n, hp_each, weaknesses, immunities, atk_dmg, atk_type, initiative, team):
		self.n = n
		self.hp_each = hp_each
		self.weaknesses = weaknesses
		self.immunities = immunities
		self.atk_dmg = atk_dmg
		self.atk_type = atk_type
		self.initiative = initiative
		self.team = team
	def __repr__(self):
		return 'group({!r})'.format(self.__dict__)
	@property
	def eff_power(self):
		return max(self.n, 0) * self.atk_dmg

	def dmg_to(self, other):
		return self.eff_power * (0 if self.atk_type in other.immunities else 2 if self.atk_type in other.weaknesses else 1)
def parse(st, team, boost=0):
	res = []
	for i in st.split('\n'):
		g = re.match(r'(\d+) units each with (\d+) hit points (?:\((.*?)\) )?with an attack that does (\d+) (\S+) damage at initiative (\d+)', i)
		n = int(g.group(1))
		hp = int(g.group(2))
		weaknesses = set()
		immunities = set()
		wi = g.group(3)
		if wi is not None:
			for cmp in wi.split('; '):
				if cmp.startswith('immune to '):
					immunities |= set(cmp[len('immune to '):].split(', '))
				elif cmp.startswith('weak to '):
					weaknesses |= set(cmp[len('weak to '):].split(', '))
		dmg = int(g.group(4))
		typ = g.group(5)
		initiative = int(g.group(6))
		res.append(group(n, hp, weaknesses, immunities, dmg + boost, typ, initiative, team))
	return res

def get_team(s):
	if s is None: return 'stalemate'
	for i in s:
		return i.team
def run_combat(imm_inp, inf_inp, boost=0):
	immune_system = set(parse(imm_inp, 'immune', boost))
	infection = set(parse(inf_inp, 'infection'))
	while immune_system and infection:
		potential_combatants = immune_system | infection
		attacking = {}
		for combatant in sorted(immune_system | infection, key=lambda x: (x.eff_power, x.initiative), reverse=True):
			try:
				s = max((x for x in potential_combatants if x.team != combatant.team and combatant.dmg_to(x) != 0), key=lambda x: (combatant.dmg_to(x), x.eff_power, x.initiative))
			except ValueError as e:
				attacking[combatant] = None
				continue
			potential_combatants.remove(s)
			attacking[combatant] = s
		did_damage = False
		for combatant in sorted(immune_system | infection, key=lambda x: x.initiative, reverse=True):
			if combatant.n <= 0:
				continue
			atk = attacking[combatant]
			if atk is None: continue
			dmg = combatant.dmg_to(atk)
			n_dead = dmg // atk.hp_each
			if n_dead > 0: did_damage = True
			atk.n -= n_dead
			if atk.n <= 0:
				immune_system -= {atk}
				infection -= {atk}

		if not did_damage: return None
		print('NEW ROUND')
		print('values', *sorted(map(lambda x: x.n, immune_system | infection)))
	winner = max(immune_system, infection, key=len)
	return winner

run_combat(inp_imm, inp_infection)

winner = run_combat(inp_imm, inp_infection)
print('Part 1:', sum(x.n for x in winner))

boost_min = 0
boost_max = 1
while get_team(run_combat(inp_imm, inp_infection, boost_max)) != 'immune':
	boost_max *= 2
	#print(boost_max)

import math
while boost_min != boost_max:
	pow = (boost_min + boost_max) // 2
	cr = run_combat(inp_imm, inp_infection, pow)
	res = get_team(cr)
	if res != 'immune':
		boost_min = math.ceil((boost_min + boost_max) / 2)
	else:
		boost_max = pow
	#print(boost_min, boost_max)
print('Boost:', boost_max)
print('Part 2:', sum(x.n for x in run_combat(inp_imm, inp_infection, boost_max)))
