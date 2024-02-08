#Question 1: FizzBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#Question 2: Fibonacci Sequence
def fibonacci(n):
    fibo_sequence = [0, 1]
    while fibo_sequence[-1] + fibo_sequence[-2] <= n:
        fibo_sequence.append(fibo_sequence[-1] + fibo_sequence[-2])
    return fibo_sequence

print(fibonacci(100))

#Question 3: Power of Two
def is_power_of_two(n):
    return n != 0 and (n & (n - 1)) == 0

print(is_power_of_two(8)) # returns True
print(is_power_of_two(6)) # returns False

#Question 4: Capitalize Words
def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

print(capitalize_words("hello")) # returns "hello"
print(capitalize_words("i love coding")) # returns "I Love coding"

#Question 5: Reverse Integer
def reverse_integer(n):
    sign = -1 if n < 0 else 1
    reversed_n = int(str(abs(n))[::-1]) * sign
    return reversed_n

print(reverse_integer(300)) 
print(reverse_integer(-20)) 
print(reverse_integer(-35)) 
print(reverse_integer(100))  

#Question 6: Count Vowels
def count_vowels(sentence):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hello, World!")) # returns 3

       
