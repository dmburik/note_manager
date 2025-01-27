from datetime import date
notes=[]
answer_yes = ["y","yes","Y","YES","Yes","да","ДА","Д","д"]
answer_no = ["нет","н","НЕТ","Нет","Н","N","NO","n","No"]
def create_multiply_notes():#функция для ввода названий дат имен и тд
    list_of_notes=[]
    number_of_notes = 0
    note_name=input("введите название заметки")
    note_name_lst=[]
    while len(note_name) == 0:
        print("название заметки не может быть пустым")
        note_name = input("введите название заметки")
    note_name_lst.append(note_name)
    number_of_notes+=1
    username= input("введите ваше имя")
    content = input("введите описание заметки")
    def status_check():
        temp_status = input("введите статус заметки" + str(number_of_notes) + "готова/готовится/отложена")
        # цикл для проверки статуса и дальнейшее его преобразование в читаемый формат
        while temp_status not in ("готова", "готовится", "отложена", "1", "2", "3"):
            temp_status = input("статус может быть готова/готовится/отложена или числа 1/2/3 соответственно")
        if temp_status == "1":
            temp_status = "готова"
        elif temp_status == "2":
            temp_status = "готовится"
        elif temp_status == "3":
            temp_status = "отложена"
        return temp_status
    status=status_check()

    created_date = input("введите дату создания заметки в формате 00.00.0000")
    def check_date_new(dat):#функция проверки дат
        check_issue_date2 =dat
        local_issue_date = 0
        while local_issue_date == 0:
            try:
                local_issue_date = date(int(check_issue_date2[6:11]), int(check_issue_date2[3:5]),
                                        int(check_issue_date2[0:2]))
            except ValueError:
                try:
                    local_issue_date = date(int(check_issue_date2[0:4]), int(check_issue_date2[5:7]),
                                            int(check_issue_date2[8:10]))
                except ValueError:
                    print("не корректный формат даты / не существующая дата")
                    check_issue_date2 = input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")
        return local_issue_date
    created_date=check_date_new(created_date)
    issue_date = input("введите дату предполагаемого окончания заметки в формате 00.00.0000")
    issue_date=check_date_new(issue_date)
    voc_name={"ID:":str(number_of_notes),"Имя:": username,"название заметки:":note_name,"Описание:":content,"Статус:":status,
    "Дата создания:":str(created_date),"Дедлайн":str(issue_date)}
    list_of_notes.append(voc_name)
    yes_no_answer=input("хотите добавить еще заметку?Y/N")
    while yes_no_answer not in answer_no:
        if yes_no_answer in answer_yes:
            note_name = input("введите название заметки")
            while note_name in note_name_lst:#проверка повторяющегося значения
                print("такое название заметки уже существует")
                note_name=input("введите название заметки")
                while len(note_name)==0:#проверка пустого значения
                    print("название заметки не может быть пустым")
                    note_name = input("введите название заметки")
            note_name_lst.append(note_name)
            username = input("введите ваше имя")
            content = input("введите описание заметки")
            status=status_check()
            created_date = input("введите дату создания заметки в формате 00.00.0000")
            created_date = check_date_new(created_date)
            issue_date = input("введите дату предполагаемого окончания заметки в формате 00.00.0000")
            issue_date = check_date_new(issue_date)
            number_of_notes += 1
            voc_name = {"ID:": str(number_of_notes),"Имя:": username, "название заметки:": note_name, "Описание:": content, "Статус:": status,
                        "Дата создания:": str(created_date), "Дедлайн": str(issue_date)}
            list_of_notes.append(voc_name)
            yes_no_answer = input("хотите добавить еще заметку?Y/N")
        else:
            print("на вопрос можно ответить толькоY/N(да/нет)")
            yes_no_answer = input("хотите добавить еще заметку?Y/N")
    return number_of_notes,list_of_notes
number_of_notes,list_of_notes=create_multiply_notes()
def print_notes(number_of_notes):#функция для печати списка
    for i in range(number_of_notes):
        iter_list=iter(list_of_notes[i])
        for l in iter_list:
            print(l+list_of_notes[i][l])
print_notes(number_of_notes)
def delete_multiply_notes():#функция для удаления заметок
    number_after_del = number_of_notes
    yes_no_answer=input("Хотите удалить какую то заметку?Y/N")
    while yes_no_answer not in  answer_no:
        if yes_no_answer in answer_yes:

            inp_for_del = input("введите название заметки или имя пользователя для удаления")
            list_of_index=[]
            for i in range(len(list_of_notes)):
                if inp_for_del == list_of_notes[i]["Имя:"]:
                    list_of_index.append(i)
                elif inp_for_del == list_of_notes[i]["название заметки:"]:
                    yes_no_answer2 = input(
                        f"вы уверены что хотите удалить заметку {list_of_notes[i]["название заметки:"]}? Y/N?")
                    while yes_no_answer2 not in answer_no:
                        if yes_no_answer2 in answer_yes:
                            list_of_notes.pop(i)
                        else:
                            print("на вопрос можно ответить толькоY/N(да/нет)")
                            yes_no_answer2 = input(
                                f"вы уверены что хотите удалить заметку{list_of_notes[i]["название заметки:"]}? Y/N?")
                    break
            if len(list_of_index)>1:
                yes_no_answer2 = input(f'в списке {len(list_of_index)} заметки созданных {inp_for_del}, удалить все? Y/N?')
                while yes_no_answer2 not in answer_no:
                    if yes_no_answer2 in answer_yes:
                        for i in list_of_index:
                            list_of_notes.pop(i)
                            number_after_del -= 1
                    else:
                        print("на вопрос можно ответить толькоY/N(да/нет)")
                        yes_no_answer2 = input(
                            f'в списке {len(list_of_index)} заметки созданных {inp_for_del}, удалить все? Y/N?')
                if yes_no_answer2 in answer_no:
                    for i in list_of_index:
                        print(list_of_notes[i])
                    inp_for_del=input("введите название заметки из указанных выше для удаления")
                    index_for_del = -5
                    for i in list_of_index:
                        if inp_for_del == list_of_notes[i]["название заметки:"]:
                           index_for_del=i
                    if index_for_del !=-5:
                        list_of_notes.pop(index_for_del)
                        number_after_del -= 1
                    else:
                        print(f"названия заметки: {inp_for_del} - в списке не найдено")
        else:
            print("на вопрос можно ответить толькоY/N(да/нет)")
            yes_no_answer = input("хотите удалить заметку?Y/N")
            continue
        yes_no_answer = input("Хотите удалить какую то еще заметку?Y/N")

    return list_of_notes,number_after_del
list_of_notes,number_of_notes=delete_multiply_notes()
print_notes(number_of_notes)

