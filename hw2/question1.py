# Ozan Yetkin | 1908227
# Write a recursive function that generates a list of all anagrams of a given string.

def anagrams_of(s):
	# Define the base case which is basically an empty string
    if len(s) == 0:
        return []
    else:
        anagrams = anagrams_of(s[:-1])
        for i in range(len(s)):
            anagrams.append(s[i:] + s[i])
        return anagrams

# Test should return the list of all anagrams
print(anagrams_of("po"))