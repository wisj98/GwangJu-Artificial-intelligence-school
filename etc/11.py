from collections import deque
def solution(begin, target, words: list):
    dic = {}
    words.append(begin)
    if target not in words:
        return 0
    for i in range(len(words)):
        son = []
        for j in range(len(words)):
            checker = 0
            for x in range(len(words[i])):
                if words[i][x] == words[j][x]:
                    checker += 1
            if checker + 1 == len(words[i]):
                son.append(words[j])
        dic[words[i]] = son
    return bfs(dic, begin, target)

def bfs(graph, start, target):
    visited = set()
    now = [start]
    visit = graph[start]
    root = 0
    while visit:
        for i in now:
            for c in graph[i]:
                print(i)
                if c == target:
                    return root
                if c not in visited:
                    visited.add(c)
                    now.append(c)
            


print(solution("hit", "cog",["hot", "dot", "dog", "lot", "log", "cog"]))