import os
import sys

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist

analytics_save_directory = 'results'
visualize = True
most_common_word_count = 10
words_excluded_from_most_common = [',', '.', 'a', 'az']


def setup_directory():
    if not os.path.exists(analytics_save_directory):
        os.makedirs(analytics_save_directory)


def read_verse_from_file() -> str:
    with open(verse_file_path, mode='r', encoding='utf-8') as verse_file:
        return verse_file.read()


def analyze_verse(verse_text: str) -> str:
    results = []
    results.append('A vers:')
    results.append(verse_text)
    results.append('--------------------------------')

    word_tokens = find_word_tokens(verse_text)
    results.append(f'Szavak száma: {str(len(word_tokens))}')
    results.append(f'Szavak: {word_tokens}')

    sentence_tokens = find_sentence_tokens(verse_text)
    results.append(f'Mondatok száma: {str(len(sentence_tokens))}')
    results.append(f'Mondatok:\n{'\n'.join(sentence_tokens)}')

    results.append('--------------------------------')

    most_common_words = find_word_frequencies(word_tokens, most_common_word_count)
    results.append(f'Leggyakoribb szavak:\n{'\n'.join(str(item) for item in most_common_words)})')

    return '\n\n'.join(results)


def find_word_tokens(verse_text: str):
    return word_tokenize(verse_text, language='hungarian')


def find_sentence_tokens(verse_text: str):
    return sent_tokenize(verse_text, language='hungarian')


def find_word_frequencies(word_tokens, n):
    freq = FreqDist(token.lower() for token in word_tokens)

    for ignored_word in words_excluded_from_most_common:
        freq.pop(ignored_word, 0)

    if visualize:
        freq.plot(n, title='Leggyakoribb szavak')
    return freq.most_common(n)


def save_results(results: str):
    save_path = os.path.join(analytics_save_directory, f'results_{verse_name}.txt')

    if os.path.exists(save_path):
        print(f'Results file {save_path} already exists, overriding.')
        os.remove(save_path)

    with open(save_path, mode='w', encoding='utf-8') as results_file:
        results_file.write(results)

    print(f'Analysis of {verse_name} saved to {save_path}')


if __name__=="__main__":
    if len(sys.argv) < 2:
        print('Használat: python analyze_verse.py <verse_name>')
        sys.exit(1)
    verse_name = sys.argv[1]
    verse_file_path = os.path.join('verses', f'{verse_name}.txt')

    setup_directory()
    verse_text = read_verse_from_file()
    results = analyze_verse(verse_text)
    save_results(results)