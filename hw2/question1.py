# Ozan Yetkin | 1908227
# Write a recursive function that generates a list of all anagrams of a given string.

def anagrams_of(s):
	# Define the base case which is basically a string with a single character
    if len(s) <= 1:
        # Return the list containing the string itself if it is the base case
        return [s]
    else:
        # If it is not the base case, initialize an empty list that would contain anagrams
        anagrams = []
        # Iterate over the already found incomplete anagrams recursively by calling the function itself by trimming the last character
        for anagram in anagrams_of(s[:-1]):
            # Iterate again with the length of the string in recursion to slice the anagram and insert the last character in different positions
            for i in range(len(s)):
                # Slice the anagram in recursion into two parts by [i:] and [:i] and insert the last character of string in between
                anagrams.append(anagram[i:] + s[-1] + anagram[:i])
        # Return the anagrams list that will inevitably call anagrams_of(s[:-1]) until a single character remains
        return anagrams

# Test should return the list of all anagrams
print(anagrams_of("po"))
print(anagrams_of("pot"))
print(anagrams_of("pots"))