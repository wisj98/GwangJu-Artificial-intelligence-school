count = 0
for i in range(int(input())):
    already = []
    word = input()
    for j in range(len(word)):
        if word[j] not in already: already.append(word[j])
        elif word[j] in already and word[j-1] == word[j]: pass
        else: