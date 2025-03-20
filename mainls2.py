def count_vowels(s):
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = sum(1 for char in s if char in vowels)

    for i, char in enumerate(s):
        if char.lower() == 'y':
            if (i == 0 or s[i - 1].lower() not in vowels) and (i == len(s) - 1 or s[i + 1].lower() not in vowels):
                count += 1

    return count
