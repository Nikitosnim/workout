HELP="""
help - напечатать справку по программе.
add - добавить задачу в список(название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""



f=True
while f:
      c=input("Введи команду: ")

      if c == "help":
            print(HELP)
      elif c=="show":
            print(today,tomorrow,other)
      elif c=="add":
            q=input("Введите название задачи")
            w=input("Дата выполнения задачи")
            if w=="Сегодня":
                 today .append(q)
            elif w=="Завтра":
                 tomorrow .append(q)
            else:
                  other.append(q)
      elif c=='exite':
            print("Спасибо за использование! До свидания!")
            break
      else:
            print("Неизвестная команда")
