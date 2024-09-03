import math

def shift(string, key):
    # only lowercase will be shifted, should be an easy fix though

    output = ""
    
    for char in string:
        if(ord('z') < ord(char) or ord(char) < ord('a')):
            output += char
            continue

        output += chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
        # first convert to number, and subtract number of a
        # this way if char='a' then num=0, char='z' num=25
        # add the key to the number, and modulus 26 so it wraps around
        # then add the number of a back and convert to a character again

    return output

character_frequency = [
    0.079, # A
    0.014, # B
    0.027, # C
    0.041, # D
    0.122, # E
    0.021, # F
    0.019, # G
    0.059, # H
    0.068, # I
    0.002, # J
    0.008, # K
    0.039, # L
    0.023, # M
    0.065, # N
    0.072, # O
    0.018, # P
    0.001, # Q
    0.058, # R
    0.061, # S
    0.088, # T
    0.027, # U
    0.010, # V
    0.023, # W
    0.002, # X
    0.019, # Y
    0.010  # Z
    ]

def get_frequency(string):
    # get the character frequency of a string
    counts = [0] * 26
    total = 0
    for char in string:
        if(ord('a') <= ord(char) <= ord('z')):
            counts[ord(char) - ord('a')] += 1
            total += 1
    
    frequencies = []

    for count in counts:
        frequencies.append(count / total)

    return frequencies 
    


def decrypt_square_error(string):
    # decrypt by minimizing the square error of the frequency
    # returns key to shift by

    min_error = math.inf
    key = -1

    for i in range(26):
        encrypted = shift(string, i)
        frequency = get_frequency(encrypted)
        square_error = 0

        for j, prob in enumerate(frequency):
            diff = character_frequency[j] - prob
            square_error += diff ** 2
        if min_error > square_error:
            min_error = square_error
            key = i
    return key



secret_message = "my favorite fruit is apples"
key = 12

encrypted = shift(secret_message, key)

decrypted_key = decrypt_square_error(encrypted)
decrypted_final = shift(encrypted, decrypted_key)

print(decrypted_final)