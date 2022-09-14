from collections import Counter
from threading import Thread, Lock

mutex = Lock()

frequency_map = {}
top_five_words_ranked = {}


def extract_words(message):
    if len(message) > 0:
        words = message.split(',')
        for w in words:
            if w in frequency_map:
                frequency_map[w] += 1
            else:
                frequency_map[w] = 1


def get_top_five():
    return dict(Counter(frequency_map).most_common(5))  # O(nlogn)


def top_five_ranked():
    mutex.acquire()
    top_five_words = get_top_five()
    mutex.release()

    most_occurring = max(top_five_words.values())
    least_occurring = min(top_five_words.values())

    if most_occurring == least_occurring:
        for word in top_five_words:
            top_five_words_ranked[word] = 1
        return top_five_words_ranked

    for word, frequency in top_five_words.items():
        current_word_occurring = frequency
        rank_calc = round(4 * (current_word_occurring - least_occurring) / (most_occurring - least_occurring)) + 1
        top_five_words_ranked[word] = rank_calc

    result = dict(Counter(top_five_words_ranked).most_common())
    return result


def get_words_histogram():
    if len(frequency_map) == 0:
        return {}
    return top_five_ranked()
