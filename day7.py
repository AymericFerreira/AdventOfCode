import sys
import re

graph = {}
for line in open('day7Files\input.txt'):
    color = re.match('(.+?) bags', line).group(1)
    contains = re.findall('(\d+) (.+?) bag', line)
    graph[color] = contains


def has_shiny(color):
    if color == 'shiny gold':
        return True
    return any(has_shiny(c) for _, c in graph[color])


print(sum(has_shiny(c) for c in graph.keys()) - 1)


def count(bag_type):
    return 1 + sum(int(n) * count(c) for n, c in graph[bag_type])


print(count('shiny gold') - 1)
