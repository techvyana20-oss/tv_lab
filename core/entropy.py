import math

def calculate_entropy(charset_size, length):
    return length * math.log2(charset_size)
