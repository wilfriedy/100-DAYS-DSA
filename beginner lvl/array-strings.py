from typing import List
def oddString(words: List[str]) -> str:
    n = len(words)
    differences = []
    for i in range(n):
        temp = []
        for j in range(n-1):
            dif = ord(words[i][j+1]) - ord(words[i][j])
            temp.append(dif)

        differences.append(temp)

    print(differences.count(differences[2]))

    return differences

words = ["adc","wzy","abc"]
print(oddString(words))

