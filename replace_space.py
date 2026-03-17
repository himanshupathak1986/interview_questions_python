# Write a method to replace all spaces in a string with ‘%20’.

def replace_space(input):
    print(input)
    str = input.replace(" ", "%20")
    print(str)
    
if __name__ == "__main__":
    replace_space("This is a string with spaces")