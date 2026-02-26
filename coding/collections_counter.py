from collections import defaultdict


def anagrama(words):
    groups = defaultdict(list)
    for word in words:
        lst_words = list(word)
        lst_words.sort()
        anagrams = str(lst_words)
        groups[anagrams].append(word)

    return list(groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = anagrama(words)
print(result)
