def duplicates(string):
    return len([ch for ch in set(string.lower()) if string.lower().count(ch) > 1])

# найти кол-во дублирующихся букв
def letters(string):
    repeating_letters = []
    duplicate_letters = []
    res = 0
    for letter in string:
        if letter in repeating_letters and letter not in duplicate_letters:
            res += 1
            duplicate_letters.append(letter)
        else:
            repeating_letters.append(letter)
    return res



