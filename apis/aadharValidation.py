# Python3 program to validate
# Aadhaar number using regex.
import re


# Function to validate Aadhaar
# number.
def isValidAadhaarNumber(str):
    # Regex to check valid
    # Aadhaar number.
    regex = ("^[2-9]{1}[0-9]{3}" +
             "[0-9]{4}[0-9]{4}$")

    # Compile the ReGex
    p = re.compile(regex)

    # If the string is empty
    # return false
    if (str == None):
        return False

    # Return if the string
    # matched the ReGex
    if (re.search(p, str)):
        return True
    else:
        return False


# Driver code

# Test Case 1:
str1 = "409605065235"
print("str1",isValidAadhaarNumber(str1))

# Test Case 2:
str2 = "4675 9834 6012 8"
print(isValidAadhaarNumber(str2))

# Test Case 3:
str3 = "0175 9834 6012"
print(isValidAadhaarNumber(str3))

# Test Case 4:
str4 = "3675 98AF 60#2"
print(isValidAadhaarNumber(str4))

# Test Case 5:
str5 = "417598346012"
print(isValidAadhaarNumber(str5))

# This code is contributed by avanitrachhadiya2155
