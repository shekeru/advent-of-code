import re

inp_imm = """17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3"""

inp_infection = """801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4"""

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
		return self.n * self.atk_dmg

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
		print('immune_system', *map(lambda x: x.n, immune_system))
		print('infection', *map(lambda x: x.n, infection))
	winner = max(immune_system, infection, key=len)
	return winner

winner = run_combat(inp_imm, inp_infection)
print('Part 1:', sum(x.n for x in winner))

boost_min = 0
boost_max = 1
while get_team(run_combat(inp_imm, inp_infection, boost_max)) != 'immune':
	boost_max *= 2
	#print(boost_max)

run_combat(inp_imm, inp_infection, 1570)

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
