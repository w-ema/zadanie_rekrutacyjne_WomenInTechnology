def are_anagrams(s1, s2, s3):
    # definiuję funkcję tworzącą słownik znaków i ich powtórzeń występujących w łańcuchu
    def dict_of_characters(x):
        dict = {}
        for i in x:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        return dict
    # sprawdzam czy długość każdego z łańcuchów jest nie większa niż 5
    if all(len(s)<=5 for s in [s1, s2, s3]):
        #sprawdzam czy wprowadzone łańcuchy znaków się nie powtarzają
        if (s1!=s2 and s1!=s3 and s3!=s2):
            # sprawdzam czy wprowadzone dane są anagramami
            if (dict_of_characters(s1)==dict_of_characters(s2) and dict_of_characters(s1)==dict_of_characters(s3)):
                ans = True
            else:
                ans = False
        else:
            ans = print("Wprowadzone łańcuchy powtarzają się")
    else:
        ans = print("Maksymalna długość znaków w łańcuchu wynosi 5!")
    return ans