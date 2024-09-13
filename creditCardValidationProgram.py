# Credit Card Validation Program
#Test Credit Card Account Numbers(get numbers here for testing, check it online)

sumOddDdigits = 0
sumEvenDdigits = 0
total = 0

# 1. Remove any '-' or ' ' and revert the numbers
cardNumber = input("Enter a credit card number: ")
cardNumber = cardNumber.replace("-", "")
cardNumber = cardNumber.replace(" ", "")
cardNumber = cardNumber[::-1]

# 2. Add all digits in the odd places from right to left
for x in cardNumber[::2]:
    sumOddDdigits += int(x)

# 3. Double every second digit from right to left, if result is a two-digit number, add the two-digit number together to get a single digit.
for x in cardNumber[1::2]:
    x = int(x) * 2
    if x >= 10:
        sumEvenDdigits += (1 + (x % 10))
    else:
        sumEvenDdigits += x

# 4. Sum the totals of step 2 & 3
total = sumOddDdigits + sumEvenDdigits

# 5. If sum is divisible by 10, the credit card number is valid
if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")