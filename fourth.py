from math import sqrt
from itertools import count, islice

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(n**0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

sentence = input("Waiting for words: ")
words = sentence.split()
for word in words:
    word_sum = 0
    if word.isalpha():
        for letter in word:
            value = ord(letter)
            if value > 96:
                word_sum += value - 96
            else:
                word_sum += value - 38
        if is_prime(word_sum):
            print("Word {} is prime, value {}".format(word,word_sum))
        else:
            print("Word {} is not prime, value {}".format(word,word_sum))
    else:
        print("Invalid word, skipping")
            
