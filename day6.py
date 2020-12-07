import numpy as np

file = open('day6Files\input.txt', 'r')
content = file.read()
voteList = content.split('\n\n')


def part_one():
    voteCount = 0
    for vote in voteList:
        vote = ''.join(vote.split())
        voteCount += len(set(vote))

    print(voteCount)


def part_two():
    voteCount = 0
    for vote in voteList:
        subVote = vote.split()
        subVoteSet = [set(sub_vote) for sub_vote in subVote]
        matchingLetters = subVoteSet[0].intersection(*subVoteSet[1:])
        voteCount += len(matchingLetters)

    print(voteCount)

part_one()
part_two()
