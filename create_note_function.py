import datetime
from datetime import date

answer_yes = ["y","yes","Y","YES","Yes","да","ДА","Д","д"]
answer_no = ["нет","н","НЕТ","Нет","Н","N","NO","n","No"]
status_inp_varieties = ["1","2","3",'новая',"в процессе","выполнена"]
note_id=0
list_of_notes=[]# тут потому что потом пригодится(для проверки повторов)
def create_note():# функция для создания заметок
    loc_note_id=note_id
    username = input("Введите Ваше имя: ")
    title = input("Введите название заметки: ")
    while len(title)==0:
        print("название заметки не может быть пустым")
        title = input("Введите название заметки: ")
    content = input("Введите описание заметки: ")
    status = input("Выберите статус заметки 1 - новая; 2 - в процессе; 3 - выполнена")
    while status not in status_inp_varieties:# проверка статуса и перевод из числа в слова
        print("статус может быть только один из перечисленных")
        status = input("Выберите статус заметки 1 - новая; 2 - в процессе; 3 - выполнена")
    if status == "1":
        status = "новая"
    elif status == "2":
        status = "в процессе"
    elif status == "3":
        status="выполнена"
    created_date=date.today()
    issue_date = input("Введите дату дедлайна в формате ДД-ММ-ГГГГ(при пустом значении + неделя от текущей даты)")
    if len(issue_date)==0:
        issue_date=(created_date + datetime.timedelta(days=7)).strftime('%d-%m-%Y')

    else:
        local_issue_date= 0
        while local_issue_date == 0:# проверка даты
            try:
                local_issue_date=date(int(issue_date[6:11]),int(issue_date[3:5]),int(issue_date[0:2]))
            except ValueError:
                try:
                    local_issue_date = date(int(issue_date[0:4]), int(issue_date[5:7]),int(issue_date[8:10]))
                except ValueError:
                    print("не корректный формат даты / не существующая дата")
                    issue_date = input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")
        issue_date = local_issue_date.strftime('%d-%m-%Y')
    loc_note_id +=1
    created_date = date.today().strftime('%d-%m-%Y')
    dict_name = {"ID:": str(loc_note_id), "Имя: ": username, "название заметки: ": title, "Описание: ": content,
                "Статус: ": status,
                "Дата создания: ": str(created_date), "Дедлайн: ": str(issue_date)}
    list_of_notes.append(dict_name)

    return list_of_notes,loc_note_id
list_of_notes,note_id=create_note()
def print_notes():# функция для печати списка
    for i in range(note_id):
        iter_list=iter(list_of_notes[i])
        for l in iter_list:
            print(l+list_of_notes[i][l])
print_notes()