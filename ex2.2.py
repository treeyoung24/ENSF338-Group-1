with open("C:/University/VSCode/ENSF338/Lab01/pg2701.txt", "r", encoding="utf-8") as textfile:
    textfile.seek(915) # starts from chapter 1
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'] 
    vowel_amt = 0
    word_amt = 0
    textarray = textfile.readlines()

    for lines in textarray:

        linelist = list(lines)
        for char in linelist:
            if char in vowel_list:
                vowel_amt += 1

        word = lines.split()

        for i in word:
            word_amt += 1


avg_vowels = (vowel_amt / word_amt)
    
print('There are an average of', avg_vowels, 'vowels in this file.')