# Ozan Yetkin | 1908227
# Define a function that takes two string inputs to count substrings
def substring_count(first, second):
    # Initialize a count to count substring occurences
    count = 0

    # Iterate using the length of the first string to search through all of it
    for i in range(len(first)):
        # Slice the first string using i and the length of the second string to search all substrings that are same length with the second

        # Use (i) as start of slicing and (len(second) + i) as end to shift substrings with same length (len(second)) as iteration continues
        # Check if the sliced substring within iteration is same with the second string
        if second == first[i : len(second) + i]:
            # If it is the case, increment count by one
            count += 1

    # Return the count of given substring occurences
    return count


# Call the function and test it with different inputs
print(substring_count("lifeforlifeforlifeforlife", "life"))  # returns 4
print(substring_count("lifeforlifeforlifeforlife", "lifeforlife"))  # returns 3
