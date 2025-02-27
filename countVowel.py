print("Count vowel in the word")

word = input("Count the vowel in the word ")

splitByVowel =  list(word)

totalVowels = splitByVowel.count('a')+splitByVowel.count('e')+splitByVowel.count('i')+splitByVowel.count('o')+splitByVowel.count('u')

print(totalVowels)