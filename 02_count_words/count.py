
import re
from collections import Counter


def count_words(phrase):
    """Return the number of times each word occurs in the phrase."""
    return Counter(re.findall(r"[\w'-]+", phrase.lower()))


if __name__ == '__main__':
    print(count_words("oh what a day what a lovely day"))
    print(count_words("Oh what a day what a lovely day"))
    print(count_words("Oh what a day, what a lovely day!"))
