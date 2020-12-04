Fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
Ps = [{k: v for [k, v] in [x.split(':') for x in p.split()]}
    for p in open('input.txt').read().split("\n\n")]
from string import *

def Validate(O):
    return (1920 <= int(O['byr']) <= 2002) \
        and (2010 <= int(O['iyr']) <= 2020) \
        and (2020 <= int(O['eyr']) <= 2030) \
        and ((O['hgt'][-2:] == 'cm' and 150 <=
            int(O['hgt'][:-2]) <= 193) or (O['hgt'][-2:] ==
                'in' and 59 <= int(O['hgt'][:-2]) <= 76)) \
        and O['hcl'][0] == "#" and 7 == len(O['hcl']) \
        and all(c in string.hexdigits for c in O['hcl'][1:]) \
        and O['ecl'] in ('amb','blu','brn','gry','grn','hzl','oth') \
        and len(O['pid']) == 9 and all(c in string.digits for c in O['pid'])

print("Silver:", len(T1 := [p for p in Ps if sum \
    ([1 for k in Fields if k in p]) == 7]))
print("Gold:", len([p for p in T1 if Validate(p)]))
