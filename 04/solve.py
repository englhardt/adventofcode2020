import re

def check1(passports):
    ans = 0
    req_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for p in passports:
        ans += all(x in p for x in req_keys)
    return ans

def check2(passports):
    ans = 0
    req_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for p in passports:
        valid = True
        valid &= all(x in p for x in req_keys)
        valid &= valid and 1920 <= int(p['byr']) <= 2002
        valid &= valid and 2010 <= int(p['iyr']) <= 2020
        valid &= valid and 2020 <= int(p['eyr']) <= 2030
        valid &= valid and ('cm' in p['hgt'] or 'in' in p['hgt'])
        if valid and 'cm' in p['hgt']:
            valid &= valid and 150 <= int(p['hgt'][:-2]) <= 193
        if valid and 'in' in p['hgt']:
            valid &= valid and 59 <= int(p['hgt'][:-2]) <= 76
        valid &= valid and re.match('#[0-9a-f]{6}', p['hcl']) is not None
        valid &= valid and p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        valid &= valid and re.match('^[0-9]{9}$', p['pid']) is not None
        ans += valid
    return ans

d = open("input.txt").read().strip().split('\n\n')
passports = [dict(x.split(':') for x in re.split('\s', p)) for p in d]
print(check1(passports))
print(check2(passports))
