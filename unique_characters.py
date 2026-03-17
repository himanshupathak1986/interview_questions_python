# Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?

def unique_characters(input):
    print(input)
    set_input = set(input)
    print(set_input)
    
    if len(set_input)== len(input):
        print("All characters are unique")
    else:
        print("Characters are not unique")

if __name__ == "__main__":
    unique_characters("abcde")
    unique_characters("this is a string")