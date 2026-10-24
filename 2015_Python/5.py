def is_word_nice_old(word):
    disallowed_strings = ["ab", "cd", "pq", "xy"]
    vowels = ["a", "e", "i", "o", "u"]
    disallowed_check = True
    repeat_check = False
    vowels_check = False
    vowels_count = 0
    last_letter = ""
    for c in word:
        pair = last_letter + c
        if last_letter and pair in disallowed_strings:
            disallowed_check = False
            break
        if c == last_letter:
            repeat_check = True
        if c in vowels:
            vowels_count += 1
        if vowels_count == 3:
            vowels_check = True

        last_letter = c

    return disallowed_check and repeat_check and vowels_check

def is_word_nice_new(word):
    inbetween_check = False
    repeat_check = False
    last_letter = ""
    for i, c in enumerate(word):
        if i + 2 < len(word) and c == word[i + 2]:
            inbetween_check = True

        pair = last_letter + c
        if last_letter and pair in word[i + 1:]:
            repeat_check = True

        if inbetween_check and repeat_check:
            return True
        last_letter = c
    return False

nice_counter = 0

with open('./inputs/5.txt', 'r') as words:
    for word in words:
        #if is_word_nice_old(word):
        #    nice_counter += 1
        if is_word_nice_new(word):
            nice_counter += 1

print("Number of nice words: " + str(nice_counter))