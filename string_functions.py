'''
def is_palindrome(s):
    # Remove whitespace and convert to lowercase for uniform comparison
    cleaned = s.replace(" ", "").lower()
    # Compare original cleaned string with its reverse slice [::-1]
    return cleaned == cleaned[::-1]

# Input & Function Call
text = input("Enter a string: ")
if is_palindrome(text):
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is NOT a palindrome.")
'''
'''
def count_characters(s):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    d_count = 0
    other_count = 0

    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
        elif char.isdigit():
            d_count += 1
        else:
            other_count += 1

    return v_count, c_count, d_count, other_count

# Input & Function Call
sentence = input("Enter a sentence: ")
v, c, d, o = count_characters(sentence)

print(f"Vowels: {v}")
print(f"Consonants: {c}")
print(f"Digits: {d}")
print(f"Special characters & spaces: {o}")
'''
def process_sentence(sentence):
    words = sentence.split()
    if not words:
        return "", ""

    # Reverse the order of words
    reversed_sentence = " ".join(words[::-1])

    # Find the longest word based on string length
    longest_word = max(words, key=len)

    return reversed_sentence, longest_word

# Input & Function Call
line = input("Enter a line of text: ")
rev_line, longest = process_sentence(line)

print(f"Reversed words : {rev_line}")
print(f"Longest word   : {longest}")