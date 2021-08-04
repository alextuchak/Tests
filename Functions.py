documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people(doc_number):
    id = 0
    for keys in documents:
        if doc_number == keys.get('number'):
            print(f'Документ с номером {doc_number} принадлежит {keys["name"]}')
            break
        id += 1
        if id == len(documents):
            print(f'Документа с номером {doc_number} нет в каталоге документов.')


def shelf(doc_number):
    id = 0
    for keys in directories:
        if doc_number in directories.get(keys):
            return keys
        id += 1
        if id == len(directories):
            return None


def list(documents):
    for dicts in documents:
        for keys in dicts:
            print(f'{dicts[keys]}', end=' ')
        print()


def add(user_input_type, user_input_number, user_input_name, user_input_shelf):
    # user_input_type = input('Введите тип документа:')
    # user_input_number = input('Введите номер документа:')
    # user_input_name = input('Введите имя и фамилию владельца документа:')
    # user_input_shelf = input('Введите номер полки на которой разместится документ:')
    temp_dict = {"type": user_input_type,
                 "number": user_input_number,
                 "name": user_input_name
                 }
    documents.append(temp_dict)
    id = 0
    for keys in directories.keys():
        if user_input_shelf == keys:
            directories.get(keys).append(user_input_number)
            return user_input_shelf
        id += 1
        if id == len(directories):
            print('Полки с таким номером не существует')


def delete(user_input_number):
    # user_input_number = input('Введите номер докуменат который необходимо удалить')
    id = 0
    for keys in documents:
        if user_input_number == keys.get('number'):
            documents.pop(id)
            break
        id += 1
        if id == len(documents):
            print(f'Документа с номером {user_input_number} нет в каталоге документов.')
    for keys in directories.keys():
        if user_input_number in directories.get(keys):
            directories.get(keys).remove(user_input_number)
            return True
        id += 1
        if id == len(directories):
            print(f'Документа с номером {user_input_number} нет в каталоге документов.')


def move(directories):
    user_input_number = input('Введите номер докуменат который необходимо переместить')
    id = 0
    id_list = 0
    for keys in directories:
        if user_input_number in directories.get(keys):
            user_input_shelf = int(input(
                'Введите номер полки куда необходимо переместить документ'))
            if user_input_shelf <= len(directories):
                directories.get(str(user_input_shelf)).append(
                    directories.get(keys).pop(directories.get(keys).index(user_input_number)))
                break
            else:
                print('Полки с таким номером не существует')
                break
        id += 1
        if id == len(directories):
            print(f'Документа с номером {user_input_number} нет в каталоге документов.')


def add_shelf(directories):
    print(f'Текущий каталог состоит из {len(directories)} полок')
    user_input_shelf = input('Введите номер новой полки:')
    id = 0
    for shelf in directories.keys():
        id += 1
        if user_input_shelf in directories.keys():
            print('Полка с таким номером уже существует!')
            break
        elif id == len(directories):
            directories.update({user_input_shelf: []})
            print(directories)
            break

#
# def main():
#     while True:
#         user_input = input('Введите кооманду. Для вызова справки введите help:')
#         if user_input == 'help':
#             return (f'Программа реализует следующие функции при вводе команд:\n',
#                     f'p - поиск владельца по номеру документа\n',
#                     f's - поис местонахождения документа по его номеру\n',
#                     f'l - выводит список всех хранящихся документов\n',
#                     f'a - добавляет новый документ в каталог\n',
#                     f'd - удаляет документ из каталога и полки\n',
#                     f'm - перемещает докумен с указанным номером на указанную полку\n',
#                     f'as - добавляет новую полку\n',
#                     f'quit - для выхода из программы\n',)
#         elif user_input == 'p':
#             doc_number = input('Введите номер документа:')
#             people(doc_number)
#         elif user_input == 's':
#             doc_number = input('Введите номер документа:')
#             shelf(doc_number)
#         elif user_input == 'l':
#             list(documents)
#         elif user_input == 'a':
#             add(documents, directories)
#         elif user_input == 'd':
#             delete(documents, directories)
#         elif user_input == 'm':
#             move(directories)
#         elif user_input == 'as':
#             add_shelf(directories)
#         elif user_input == 'quit':
#             print('До свидания')
#             break
#
#
# main()
