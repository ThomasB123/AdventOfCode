infile = open('04input.txt','r')
count = 0
fields = []
check = {}
for line in infile:
    if line == '\n':
        for i in range(len(fields)):
            name,value = fields[i].split('\n')[0].split(':')
            check[name] = value
        if len(check) == 8 or len(check) == 7 and 'cid' not in check:
            byr = 1920 <= int(check['byr']) <= 2002
            iyr = 2010 <= int(check['iyr']) <= 2020
            eyr = 2020 <= int(check['eyr']) <= 2030
            if check['hgt'][-2:] == 'cm': hgt = 150 <= int(check['hgt'][:-2]) <= 193
            elif check['hgt'][-2:] == 'in': hgt = 59 <= int(check['hgt'][:-2]) <= 76
            else: hgt = 0
            hcl = len(check['hcl']) == 7 and check['hcl'][0] == '#'
            for x in check['hcl'][1:]:
                if x not in '0123456789abcdef': hcl = 0
            ecl = check['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth'] and len(check['ecl']) == 3
            pid = len(check['pid']) == 9
            for x in check['pid']:
                if x not in '0123456789': pid = 0
            count += byr and iyr and eyr and hgt and hcl and ecl and pid
        fields = []
        check = {}
    else:
        fields.extend(line.split())
print(count)