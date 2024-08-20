import io
class WordsFinder:
    def __init__(self, *file_names):
        list_of_names = []
        for file_name in file_names:
            list_of_names.append(file_name)
        self.file_names = list_of_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    translation_table = str.maketrans('', '', ',.=!?;:-')
                    line = line.translate(translation_table)
                    words += line.split()
                all_words[file_name] = list(words)
        return all_words


    def find(self, word):
        word = word.lower()
        found_positions = {}
        for file_name, words in self.get_all_words().items():
            position = words.index(word)
            found_positions[file_name] = position + 1
        return found_positions

    def count(self, word):
        counts = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            counts[file_name] = words.count(word)
        return counts


# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
# print(finder1.get_all_words())
# print(finder1.find('Child'))
# print(finder1.count('Child'))

# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words())  # Все слова
# print(finder2.find('TEXT'))  # 3 слово по счёту
# print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
