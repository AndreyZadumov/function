def program():
    story = {}
    while True:
        deposit = 0
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню ')
        if choice == '1':
            contribution = int(input("введите сумму пополнения счета: "))
            deposit += contribution
            print(choice)
        elif choice == '2':
            price = int(input("введите сумму покупки: "))
            if price >= deposit:
                title = str(input("введите название покупки: "))
                story.fromkeys([price], title)
                deposit -= price
                print(choice)
            else:
                print("недостаточно средств для совершения покупки")
        elif choice == '3':
            print(story.items())
            print(choice)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')



program()