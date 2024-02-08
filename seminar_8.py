from typing import List
def read_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print('файла нет. Сначала введите данные\n')
        return []

def show_data(data: list):
    for line in data:
        print(line)

def save_data(file):
    print('Введите данные контакта:')
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{first_name}, {last_name}, {patronymic}, {phone_number}\n')

def search_data(contacts: List[str]):
    search_str = input('Введите фамилию для поиска: ')
    founded = []
    for contact in contacts:
        if search_str.lower() in contact.split(', ')[1].lower():
            founded.append(contact)
    return founded

def copy_data(file):
    num_lines = int(input("Выберите какую строку сохранить в другом файле: "))
    name_file = input("Введите название файла для копирования: ")
    with open(file, 'r') as file1:
        lines = file1.readlines()
    try:
        with open(name_file, 'a') as file2:
            if num_lines <= len(lines):
                file2.write(lines[num_lines-1])
            else:
                print("Ошибка: в исходном файле нет строки с таким номером.")
    except FileNotFoundError:
        print("Создание файла...")
        with open(name_file, 'w') as file2:
            if num_lines <= len(lines) or num_lines == len(lines):
                file2.write(lines[num_lines-1])
            else:
                print("Ошибка: в исходном файле нет строки с таким номером.")

def main():
    file_name = 'phone_book.txt'
    flag = True
    while flag:
        print('0 - выход')
        print('1 - запись в файл')
        print('2 - показать записи')
        print('3 - найти запись')
        print('4 - скопировать данные')
        answer = input('Выберите действие: ')
        if answer == '0':
            flag = False
        elif answer == '1':
            save_data(file_name)
        elif answer == '2':
            data = read_file(file_name)
            show_data(data)
        elif answer == '3':
            data = read_file(file_name)
            founded_data = search_data(data)
            show_data(founded_data)
        elif answer == '4':
            copy_data(file_name)

if __name__ == '__main__':
    main()
