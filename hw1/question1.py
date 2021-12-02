# Ozan Yetkin | 1908227
# Define the function that takes two input strings for anagram check
def is_anagram(str1, str2):
    # Inform the user if provided inputs are not strings
    if type(str1) != type("a string") or type(str2) != type("a string"):
        return "Please provide string for both inputs"
    else:
        # Convert the strings into lowercase and get rid of spaces
        str1 = str1.lower().replace(" ", "")
        str2 = str2.lower().replace(" ", "")

        # Initialize a count that will count the same letters in str1 and str2
        count = 0
        # Iterate through the first string to process its letters one by one
        for s in str1:
            # Check if the letter is included in str2
            if s in str2:
                # If it is the case, increment the counter
                count += 1

        # Check if strings without spaces and the count are in same length
        if len(str1) == len(str2) and count == len(str2):
            # If it is the case, it means we have anagrams, return True
            return True
        else:
            # If not, it means inputs are not anagrams, return False
            return False


# Call the function and test with different inputs
print(is_anagram(5, "car"))
print(is_anagram("asd", 3.2))
print(is_anagram("crampone", "car"))
print(is_anagram("cram", "carm"))
print(is_anagram("New York Times", "monkeys write"))
print(is_anagram("anagram", "nag a ram"))
print(is_anagram("Debit Card", "Bad Credit"))
print(is_anagram("Jim Morrison", "Mr Mojo Risin"))
