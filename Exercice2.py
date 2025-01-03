def are_anagrams(s1, s2):
    if len(s1) == len(s2):
        if sorted(s1) == sorted(s2):
            return True
    return False

print(are_anagrams("hey", "test"))  

