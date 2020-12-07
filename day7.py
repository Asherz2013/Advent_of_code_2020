# Import Regex
import re

# A dict with all bags that should contain other bags
policies = dict()
# A set of all bags
allbags = set()

def read_input(f):
    f=open(f, "r")
    return f.read().split('\n')

def can_hold_shiny_gold(bag):
    if bag not in policies:
        return False
    if 'shiny gold' in policies[bag]:
        return True
    # if it's not directly in this policy, it could be in a child policy
    return any([can_hold_shiny_gold(child) for child in policies[bag]])

def amount_of_child_bags(bag):
    if bag not in policies:
        return 0
    # good old recursion
    return sum([ int(child[1])*(1+amount_of_child_bags(child[0])) for child in policies[bag].items()])

def solve(f, part="A"):
    policies_strings = read_input(f)

    #Parse all policies
    for pol in policies_strings:
        parent = re.findall(r"^([a-z\s?]+) bags?",pol.split("contain")[0])
        child = re.findall(r"([0-9]+)\s+([a-z]+\s+[a-z]+)",pol.split("contain")[1])

        # add child policies for this bag to the dict, and add parent to set
        if len(child) > 0:
            policies.update({parent[0]: {c[1] : c[0] for c in child}})
        allbags.add(parent[0])

    if part == "A":
        return sum([ 1 if can_hold_shiny_gold(bag) else 0 for bag in allbags])
    return amount_of_child_bags('shiny gold')

print(f'Part A: {solve("Advent_of_code_2020/day7.txt")}, Part B: {solve("Advent_of_code_2020/day7.txt", part="B")}')