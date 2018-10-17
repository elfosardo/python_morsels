import re


def count_words(phrase):
    phrase_list = []
    phrase_dict = {}
    phrase_tuple = phrase.lower().split()

    for word in phrase_tuple:
        if re.search(r'[^a-z]', word[0]):
            word = word.lstrip(word[0])
        if re.search(r'[^a-z]', word[-1]):
            word = word.rstrip(word[-1])
        phrase_list.append(word)

    for word in phrase_list:
        phrase_dict[word] = phrase_list.count(word)

    return phrase_dict


if __name__ == '__main__':
    print(count_words("oh what a day what a lovely day"))
    print(count_words("Oh what a day what a lovely day"))
    print(count_words("Oh what a day, what a lovely day!"))
