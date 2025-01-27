from Этап2_Финальное_Бурнос_Дмитрий.add_titles_loop import content_count
status=[]
for i in content_count:
    temp_status = input("введите статус заметки"+ str(i) + "готова/готовится/отложена")
    # цикл для проверки статуса и дальнейшее его преобразование в читаемый формат
    while temp_status not in ("готова","готовится","отложена","1","2","3"):
        temp_status = input("статус может быть готова/готовится/отложена или числа 1/2/3 соответственно")
    if temp_status =="1":
        temp_status="готова"
    elif temp_status =="2":
        temp_status="готовится"
    elif temp_status == "3":
        temp_status = "отложена"
    status.append(temp_status)

print(status)