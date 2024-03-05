def count_vowels(word):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in word if char in vowels)
test_word = input('Enter your word ')
vowel_count = count_vowels(test_word)
print(vowel_count)
