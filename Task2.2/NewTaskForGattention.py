print("_______________________")
def count_linesTask1(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print("Файл не найден. Попробуйте вести название ещё раз, если не поможет создайте новый файл.")

file_name = input("Введите имя файла: ")
num_lines = count_linesTask1(file_name)
print(f"Строк в файле на данный момент: {num_lines}")
print("_______________________")


def count_studentsTask2():
    try:
        with open("grades.txt", 'r') as file:
            students = file.readlines()
            count = 0
            for student in students:
                data = student.strip().split()
                if len(data) == 4 and all(int(grade) >= 65 for grade in data[1:]):
                    count += 1
            return count
    except FileNotFoundError:
        print("Файл не найден")

num_students = count_studentsTask2()
print(f"Количество студентов, сдавших все три теста: {num_students}")
print("_______________________")

def count_LongWordsTask3():
    with open('words.txt', 'r') as file:
        words = file.read().split()

    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]

    for word in longest_words:
        print(word)
        print("_______________________")
count_LongWordsTask3()

from collections import Counter

def most_recurring_wordTask4():
    try:
        with open("file.txt", 'r') as file:
            words = file.read().split()
            word_counts = Counter(words)
            most_common = word_counts.most_common(1)
            return most_common[0][0]
    except FileNotFoundError:
        print("Файл не найден")

common_word = most_recurring_wordTask4()
print(f"Самое часто встречающееся слово это: {common_word}")
print("_______________________")


def find_differencesTask5(file1_name, file2_name):
    try:
        with open(file1_name, 'r') as file1, open(file2_name, 'r') as file2:
            lines1 = file1.readlines()
            lines2 = file2.readlines()

            for i in range(len(lines1)):
                if lines1[i] != lines2[i]:
                    print(f"Строка {i + 1}:")
                    print("Файл 1:", lines1[i].strip())
                    print("Файл 2:", lines2[i].strip())
    except FileNotFoundError:
        print("Файл не найден")


file1_name = input("Введите имя первого файла: ")
file2_name = input("Введите имя второго файла: ")

find_differencesTask5(file1_name, file2_name)

print("_______________________")



