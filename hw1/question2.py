# Ozan Yetkin | 1908227
# Define a function to return the first prime number in a given list
def first_non_prime(user_list):
    # Iterate through the given list to check if each provided number is prime or not
    for i in user_list:
        # Set a flag to be updated if the number is non-prime, initially asume as prime
        is_prime = True

        # Iterate from 2 to the number itself (i) to check if it is divisible by any of them
        for j in range(2, i):
            # Check if the number in the list (i) is divisible by any number in range (j)
            if (i % j) == 0:
                # If it is the case, it means the number is not prime, update the flag as false
                is_prime = False
                # Break out from the loop since prime rule is already broken and rest of the divisions are unnecessary
                break

        # Check the flag and if it is false (non-prime), return the number and exit the function, else it would return none by default
        if is_prime == False:
            return i


# Call the function and test with different inputs
print(first_non_prime([2, 3, 52, 19]))  # prints 52
print(first_non_prime([2, 101, 71462394821, 55467547393]))  # prints 55467547393 (?)
# Actually it should print 71462394821 hocam it equals to 16573 * 4311977, and 55467547393 is a prime number
# Kindly check their prime factorization: https://www.wolframalpha.com/input/?i=71462394821, https://www.wolframalpha.com/input/?i=55467547393)
print(first_non_prime([2, 3, 5, 7, 11]))  # prints nothing
print(first_non_prime([2, 3, 5, 7, 11, 12]))  # prints 12
print(first_non_prime([2, 3, 5, 6, 7, 11]))  # prints 6
