# Write a method to decide if two strings are anagrams or not.

def anagram(str1, str2):
    s1 = sorted(str1)
    s2 = sorted(str2)
    if s1 == s2:
        print("{} {} - Anagram".format(str1, str2))
    else:
        print("{} {} - Not an Anagram".format(str1, str2))


if __name__ == "__main__":
    anagram("listen", "silent")
    anagram("triangle", "integral")
    anagram("apple", "pabble")