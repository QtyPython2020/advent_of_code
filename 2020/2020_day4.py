# -*- coding: utf-8 -*-
"""
@author: QtyPython2020

"""
import re

def _parse_passport(batch):
    """

    """
    passports = []
    passport = {}
    for line in batch:
        if len(line) == 1:
            passports.append(passport)
            passport = {}
            continue
        elements = list(map(lambda x:{x[0]:x[1]},
                            map(lambda x:x.split(":"),
                                line.strip("\n").split())))
        for element in elements:
            passport.update(element)
    else:
        passports.append(passport)
    return passports

def part1(batch_file) -> int:
    """
    In your batch file, how many passports are valid?
    """
    valid = 0
    passports = _parse_passport(batch_file)
    for pass_ in passports:
        if len([k for k in pass_.keys() if k != "cid"])==7:
            valid += 1
    return valid



def part2(batch_file):
    """
    In your batch file, how many passports are valid?
    """
    valid = 0
    passports = _parse_passport(batch_file)
    for pass_ in passports:
        sufficient_fields = len([k for k in pass_.keys() if k != "cid"]) == 7
        valid_birthyear = 1920 <= int(pass_.get("byr",0)) <= 2002
        valid_issue_year = 2010 <= int(pass_.get("iyr",0)) <= 2020
        valid_expiration_year = 2020 <= int(pass_.get("eyr",0)) <= 2030
        height = pass_.get("hgt","")
        valid_height = (height.endswith("cm") and 150 <= int(height[:-2]) <= 193) \
            or (height.endswith("in") and 59 <= int(height[:-2]) <= 76)
        valid_hair_color = bool(re.match("#[0-9a-f]{6}",
                                         pass_.get("hcl","")))
        valid_eye_color = pass_.get("ecl","") in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        valid_pid = len(pass_.get("pid","")) == 9 and pass_.get("pid","").isnumeric()
        valid += all([sufficient_fields,
                      valid_birthyear,
                      valid_issue_year,
                      valid_expiration_year,
                      valid_height,
                      valid_hair_color,
                      valid_eye_color,
                      valid_pid])
    return valid

if __name__ == "__main__":
    with open("input_2020_4.txt") as file:
        instructions = file.readlines()
    print(part1(instructions))
    print(part2(instructions))
