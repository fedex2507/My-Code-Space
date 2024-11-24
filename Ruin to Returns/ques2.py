# Function to convert a decimal number to binary with precision k_prec
def decimalToBinary(num, k_prec):
    binary = ""  # Initialize binary string
    Integral = int(num)  # Extract the integral part of the number
    fractional = num - Integral  # Calculate the fractional part

    # Convert the integral part to binary
    while Integral:
        rem = Integral % 2  # Find remainder when dividing by 2
        binary += str(rem)  # Append remainder to the binary string
        Integral //= 2  # Divide the integral part by 2

    binary = binary[::-1]  # Reverse the binary string to get the correct order
    binary += '.'  # Add the decimal point for the fractional part

    # Convert the fractional part to binary with k_prec bits of precision
    while k_prec:
        fractional *= 2  # Multiply the fractional part by 2
        fract_bit = int(fractional)  # Extract the bit (0 or 1)

        if fract_bit == 1:  # If the bit is 1
            fractional -= fract_bit  # Subtract 1 from the fractional part
            binary += '1'  # Append '1' to the binary string
        else:  # If the bit is 0
            binary += '0'  # Append '0' to the binary string
        k_prec -= 1  # Decrement precision counter

    return binary  # Return the binary representation

# Function to calculate the probability of winning the game
def win_probability(p, q, k, N):
    binary_value = decimalToBinary(k / N, 100)  # Get binary representation of k/N with 100 bits of precision

    if k == 0:  # If k is 0, the probability is 0
        return 0
    elif k >= N:  # If k is greater than or equal to N, the probability is 1
        return 1
    prob = 0  # Initialize the answer to 1
    # Iterate through the binary representation from the 99th to the 1st bit
    for i in range(99, 0, -1):
        if binary_value[i] == '1':  # If the current bit is '1'
            prob = p + q * prob  # Update ans using p and q
        else:  # If the current bit is '0'
            prob = p * prob  # Update ans using only p
    return prob  # Return the final probability

# Function to calculate the expected game duration
def game_duration(p, q, k, N):
    binary_value = decimalToBinary(k / N, 100)  # Get binary representation of k/N with 100 bits of precision

    if k == 0 or k >= N:  # If k is 0 or k is greater than or equal to N, duration is 0
        return 0
    expected_duration = 0  # Initialize the answer to 0
    # Iterate through the binary representation from the 99th to the 1st bit
    j = 99
    while j >=0 :
        if binary_value[j] == '1':
            break
        j -= 1
    for i in range(j, 0, -1):
        if binary_value[i] == '1':  # If the current bit is '1'
            expected_duration = 1 + q * expected_duration  # Update ans using 1 and q
        else:  # If the current bit is '0'
            expected_duration = 1 + p * expected_duration  # Update ans using 1 and p
    return expected_duration  # Return the expected game duration
