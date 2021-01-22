
def encryptor(message):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    key = int('0b11', base=0)
    # sentence = input(': ')
    new_sentence = ''
    for char in message:
        if char in alpha:
            new_index = alpha.index(char) + key
            if new_index > 25:
                new_char = alpha[new_index % len(alpha)]
            else:
                new_char = alpha[new_index]
            new_sentence += new_char
        elif char.isupper():
            new_index = alpha.index(char.lower()) + key
            if new_index > 25:
                new_char = alpha[new_index % len(alpha)].upper()
            else:
                new_char = alpha[new_index].upper()
            new_sentence += new_char
        else:
            new_sentence += char

    return new_sentence


if __name__ == '__main__':
    print(encryptor('Level 1	Beginner means someone who has just gone through an introductory'
                    'Python course. He can solve some problems with 1 or 2 Python'
                    'classes or functions. Normally, the answers could directly be found in the textbooks.'.upper()))
