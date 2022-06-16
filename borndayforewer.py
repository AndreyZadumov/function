import random

def game():
    Musk = 'назовите дату рождения Илона Маска '
    Bezos = 'назовите дату рождения Джеффа Безоса '
    Gates = 'назовите дату рождения Билла Гейтса '
    Jobs = 'назовите дату рождения Стива Джопса '
    Korolev = 'назовите дату рождения Сергея Королева '
    Pushkin = 'назовите дату рождения Александра Пушкина '
    Lenin = 'назовите дату рождения Владимира Ленина '
    Stalin = 'назовите дату рождения Иосифа Сталина '
    Vysotsky = 'назовите дату рождения Владимира Высоцкого '
    Gagarin = 'назовите дату рождения Юрия Гагарина '

    Musk_answer = "28.06.1971"
    Bezos_answer = "12.01.1964"
    Gates_answer = "28.10.1955"
    Jobs_answer = "24.02.1955"
    Korolev_answer = "12.01.1907"
    Pushkin_answer = "16.05.1799"
    Lenin_answer = "22.04.1870"
    Stalin_answer = "09.12.1879"
    Vysotsky_answer = "25.12.1938"
    Gagarin_answer = "09.03.1934"

    people = [Musk, Bezos, Gates, Jobs, Korolev, Pushkin, Lenin, Stalin, Vysotsky, Gagarin]
    people_answer = [Musk_answer, Bezos_answer, Gates_answer, Jobs_answer, Korolev_answer, Pushkin_answer, Lenin_answer,
                     Stalin_answer, Vysotsky_answer, Gagarin_answer]

    right = 0
    wrong = 0

    for i in range(5):
        idx = random.randint(0, 9)
        answer = input(people[idx])
        if answer != people_answer[idx]:
            wrong += 1
            print('неверно')
        else:
            right += 1
    print('Ваши результаты: ')
    print('количество правильных ответов', right)
    print('количество ошибок', wrong)

game()
question = str(input('Играем еще раз? '))
while question == 'да':
    game()
    question = str(input('Играем еще раз? '))
print('до скорого')