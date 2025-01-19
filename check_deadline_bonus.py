from datetime import date, datetime

# вывод даты в обратной последовательности(День - Месяц - Год)
current_date=date.today()
print(current_date)
date_for_print=current_date.strftime('%d-%m-%Y')
print ("Текущая дата : "+ date_for_print)
# запрос даты от пользователя с дальнейшей конвертацией
check_issue_date = input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")
check_year_date=check_issue_date
check_lenth_date=check_issue_date
answer_yes = ["y","yes","Y","YES","Yes","да","ДА","Д","д"]
answer_no = ["нет","н","НЕТ","Нет","Н","N","NO","n","No"]

jan=('январь',"января","янв","jan","january")
feb=('feb',"february","февраль","февраля","фев")
mar=("march","mar","март","мар","марта")
apr=("apr","april","апр","апрель","апреля")
may=("may","май","мая")
jun=("jun","june","июнь","июня","июн")
jul=("jul","july","июль","июля","июл")
aug=("aug","august","август","авг","августа")
sep=('sep',"september","сен","сент","сентябрь","сентября")
octo=('oct',"october","окт","октябрь","октября")
nov=("nov","november","ноя","нояб","ноябрь","ноября")
dec=("dec","december","дек","декабрь","декабря")
month=[jan,feb,mar,apr,may,jun,jul,aug,sep,octo,nov,dec]

def check_month_and_days():
    check_lenth_date=check_issue_date
    #if
    for i in range  ( 0 ,len(check_lenth_date)-1):
        sepa = [' ', ',', '.', '/', '-', ';', ':']
        if check_lenth_date[i] in sepa:
            first_sep=i
            break
        else:
            i+=1
    for l in range (first_sep+1,len(check_lenth_date)-1):
        sepa = [' ', ',', '.', '/', '-', ';', ':']
        if check_lenth_date[l] in sepa:
            second_sep=l
            break
        else:
            l+=1
    if    first_sep ==1:
        while not check_lenth_date[0].isdigit():
            print("в дате могут быть только'1' и цифры")
            check_lenth_date = input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")
        day_count="0"+check_lenth_date[0]
    elif     first_sep==2:
        while not check_lenth_date[0:1].isdigit():
            print("в дате могут быть только'2' и цифры")
            check_lenth_date = input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")
        day_count=check_lenth_date[0]+check_lenth_date[1]
    else:
        print("не корректо задана дата" )
    print(day_count)
    if second_sep == 3 and first_sep == 1:
        while not check_lenth_date[2].isdigit():
            print("в дате могут быть только'3' и цифры")
            check_lenth_date = input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")
        month_count = "0" + check_lenth_date[2]
    elif second_sep == 4 and first_sep == 1:
        while not check_lenth_date[2:3].isdigit():
            print("в дате могут быть только'4' и цифры")
            check_lenth_date = input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")
        month_count = check_lenth_date[2]+check_lenth_date[3]
    elif second_sep == 4 and first_sep == 2 :
        while not check_lenth_date[3].isdigit():
            print("в дате могут быть только'6' и цифры")
            check_lenth_date = input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")
        month_count = "0"+ check_lenth_date[3]
    elif second_sep == 5 and first_sep == 2 :
        while not check_lenth_date[3:4].isdigit():
# данная проверка не нужна при отсутствии названий месяцев в 2 и менее символов
 #          for l in range(0, 12):
  #             if check_lenth_date[first_sep + 1: second_sep] in month[l][0:10]:
   #                month_count = "0" + str(l + 1)
    #               print(month_count)
     #              break
      #         else:
      #             l+=1
     #              if l==13:
    # при наличии названий в 2 символа следующие 2 строки уходят в блок else
            print("в дате могут быть только'7' и цифры")
            check_lenth_date = input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")
        month_count = check_lenth_date [3]+check_lenth_date[4]
    else:
        for l in range(0,12):
            if check_lenth_date[first_sep+1 : second_sep] in month[l][0:10]:
                month_count="0"+str(l+1)
                print(month_count)
                break
            else:
                l+=1
                if l ==12:
                    print("не правильный формат даты")
                    print(check_lenth_date[first_sep+1:second_sep])
    return day_count,month_count,check_lenth_date

def check_year():
    check_year_date=check_issue_date
    for i in range(0, len(check_year_date)+1):
        sepa = [' ', ',', '.', '/', '-', ';', ':']
        if check_year_date[i] in sepa:
            first_sep = i
            break
        else:
            i += 1

    for l in range(first_sep + 1, len(check_year_date) ):
        sepa = [' ', ',', '.', '/', '-', ';', ':']
        if check_year_date[l] in sepa:
            second_sep = l
            break
        else:
            l += 1

    while  not check_year_date[second_sep+1:20].isdigit() :
        print("в дате могут быть только'8' и цифры")
        check_year_date=input("введите дату дэдлайна в формате ДД-ММ-ГГГГ")

    if int(check_year_date[second_sep+1:20]) > 1991:
        year_check2 = check_year_date[second_sep+1:20]
    elif 100 <= int(check_year_date[second_sep+1:20]) <= 1991:
        yes_no_question = input(
            "ваш год меньше года создания python вы уверены что правильно указали год? введите Y/N")
        i = 0
        while i == 0:
            if yes_no_question in answer_yes:
                year_check2 = check_year_date[second_sep+1:20]
                i += 1
            elif yes_no_question in answer_no:
                year_check2 = input("введите правильный год в формате ГГГГ")
                while int(year_check2) < 1991:
                    year_check2 = input("введите правильный год в формате ГГГГ")
                i += 1
            else:
                print("на вопрос можно ответь только 'Y'(да) или 'N'(нет)")
                while yes_no_question in answer_yes or yes_no_question in answer_no:
                    yes_no_question = input(
                        "ваш год меньше года создания python вы уверены что правильно указали год? введите Y/N")
    elif int(check_year_date[second_sep+1:20]) < 100:
        yes_no_question = input(
            'вы ввели ' + check_year_date[second_sep+1:20] + " , вы имели ввиду 20" + check_year_date[second_sep+1:20] + '? Y/N')
        i = 0
        while i == 0:
            if yes_no_question in answer_yes:
                year_check2 = '20' + check_year_date[second_sep+1:20]
                i += 1
                #print(yes_no_question)
            elif yes_no_question in answer_no:
                year_check2 = input("введите дату 4мя цифрами в формате ГГГГ")
                while int(year_check2) <= 1991:
                    yes_no_question_2 = input(
                        "ваш год меньше года создания python вы уверены что правильно указали год? введите Y/N")
                    n = 0
                    while n == 0:
                        if yes_no_question_2 in answer_yes:
                            year_check2 = check_year_date[second_sep+1:20]
                            n += 1
                        elif yes_no_question_2 in answer_no:
                            year_check2 = input("введите правильный год в формате ГГГГ")
                            while int(year_check2) <= 1991:
                                year_check2 = input("введите правильный год в формате ГГГГ")
                            n += 1
                        else:
                            while yes_no_question_2 not in answer_yes and yes_no_question_2 not in answer_no:
                                print("на вопрос можно ответь только 'Y'(да) или 'N'(нет)")
                                yes_no_question_2 = input(
                                    "ваш год меньше года создания python вы уверены что правильно указали год? введите Y/N")
            else:
                 while yes_no_question not in answer_yes and yes_no_question not in answer_no:
                    print("на вопрос можно ответь только 'Y'(да) или 'N'(нет)")
                    yes_no_question = input(
                        'вы ввели ' + check_year_date[second_sep+1:20] + " , вы имели ввиду 20" + check_year_date[second_sep+1:9] + '? Y/N')
            i+=1
    else:
        print("формат года введен не верно")
        year_check2=input("введите год 4мя цифрами в формате ГГГГ")
    print(year_check2)
    return year_check2
check_month_and_days()
inp_day,inp_month,inp_date=check_month_and_days()
 #while inp_date!=check_issue_date:
  #  check_month_and_days()
  #  inp_day,inp_month,inp_date=check_month_and_days()
  #  check_year()

inp_year=check_year()
def check_days():
    days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31]
    if days_in_month[int(inp_month)-1]>=int(inp_day):
        issue_date=inp_year+"-"+inp_month+"-"+inp_day
        print (issue_date)
    elif int(inp_month)==2 and int(inp_day) == 29 and int(inp_year)%4==0:
        issue_date = inp_year + "-" + inp_month + "-" + inp_day
        print(issue_date)
    else:
        print("в месяце"+inp_month+" - "+days_in_month[inp_month-1]+"дней")
check_days()