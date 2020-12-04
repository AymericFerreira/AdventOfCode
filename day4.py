import string


file = open('day4Files\input.txt', 'r')
content = file.read()
commandList = content.split('\n\n')

numberOfValidPassport = 0


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


def remove_suffix(text, suffix):
    if text.endswith(suffix):
        return text[:-len(suffix)]
    return text


for passportTest in commandList:
    if "hcl:" in passportTest and "ecl:" in passportTest and "hgt:" in passportTest and "byr:" in passportTest \
            and "pid:" in passportTest and "eyr:" in passportTest and "iyr:" in passportTest:
        value = 0
        passportEntries = passportTest.split()
        for entry in passportEntries:
            if "hcl:" in entry:
                entry = remove_prefix(entry, "hcl:")
                if entry[0] == "#":
                    entry = entry[1:]
                    if all(c in string.hexdigits for c in entry):
                        value += 1
            elif "byr:" in entry:
                entry = remove_prefix(entry, "byr:")
                if 1920 <= int(entry) <= 2002:
                    value += 1
            elif "iyr:" in entry:
                entry = remove_prefix(entry, "iyr:")
                if 2010 <= int(entry) <= 2020:
                    value += 1
            elif "eyr:" in entry:
                entry = remove_prefix(entry, "eyr:")
                if 2020 <= int(entry) <= 2030:
                    value += 1
            elif "hgt:" in entry:
                entry = remove_prefix(entry, "hgt:")
                if "cm" in entry:
                    entry = remove_suffix(entry, "cm")
                    if 150 <= int(entry) <= 193:
                        value += 1
                elif "in" in entry:
                    entry = remove_suffix(entry, "in")
                    if 59 <= int(entry) <= 76:
                        value += 1
            elif "ecl:" in entry:
                entry = remove_prefix(entry, "ecl:")
                if entry in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    value += 1
            elif "pid:" in entry:
                entry = remove_prefix(entry, "pid:")
                if len(entry) == 9:
                    value += 1
        if value == 7:
            numberOfValidPassport += 1

print(numberOfValidPassport)