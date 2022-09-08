frequency_map = {}


def extract_words(message):
    if len(message) > 0:
        words = message.split(',')
        for w in words:
            if w in frequency_map:
                frequency_map[w] += 1
            else:
                frequency_map[w] = 1


def get_words_histogram():
    ranked_words = {}
    if len(frequency_map) == 0:
        return ranked_words

    most_occurring = max(frequency_map.values())
    least_occurring = min(frequency_map.values())

    for word, frequency in frequency_map.items():
        current_word_occurring = frequency
        rank_calc = round(4 * (current_word_occurring - least_occurring) / (most_occurring - least_occurring)) + 1
        ranked_words[word] = rank_calc

    return ranked_words

