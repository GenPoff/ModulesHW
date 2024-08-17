def custom_write(file_name, strings):
    with open(file_name, 'w', encoding='utf-8') as f:
        strings_positions = {}
        for i, string in enumerate(strings):
            f.write(string + '\n')
            position = f.tell()
            strings_positions[(i + 1, position)] = string
    return strings_positions

# Пример использования функции
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)