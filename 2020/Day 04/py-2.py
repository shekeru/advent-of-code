List = [{k: v for k, v in (x.split(':') for x in p.split())} for p in
    open('input.txt').read().split("\n\n")]; from re import match

Verify, Colors = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: match(r'^\d+(cm|in)$', x) and {
        'cm': lambda y: 150 <= y <= 193,
        'in': lambda y: 59 <= y <= 76,
    }[x[-2:]](int(x[:-2])),
    'hcl': lambda x: match(r'^#[0-9a-f]{6}$', x),
    'ecl': lambda x: x in Colors,
    'pid': lambda x: match(r'^[0-9]{9}$', x),
}, ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

print("Silver:", len(List := [x for x in List if all(k in x for k in Verify)]))
print("Gold:", len([x for x in List if all(Verify[k](x[k]) for k in Verify)]))
