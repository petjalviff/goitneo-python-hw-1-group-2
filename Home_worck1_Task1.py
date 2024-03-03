from datetime import datetime

users=[
    # {"name": "Bill Gates", "birthday": datetime(1960, 2, 29)},
    {"name": "Vasyl Petryshyn", "birthday": datetime(1984, 2, 28)},
    {"name": "Oleg Bratko", "birthday": datetime(1991, 2, 27)},
    {"name": "Iryna Kulyk", "birthday": datetime(1988, 3, 1)},
    {"name": "Ivanna Kvitka", "birthday": datetime(1989, 3, 2)},
    {"name": "Petro Antonovych", "birthday": datetime(2003, 3, 3)},
    {"name": "Roman Roman", "birthday": datetime(1987, 3, 4)},
    {"name": "Ivan Novus", "birthday": datetime(1989, 3, 5)},
    {"name": "Sas Gares", "birthday": datetime(1956, 3, 6)},
    {"name": "Iryna Gates", "birthday": datetime(1956, 3, 7)},
    {"name": "Olena Petryshyn", "birthday": datetime(1984, 3, 8)},
    {"name": "Genja Bratko", "birthday": datetime(1991, 3, 9)},
    {"name": "Igor Kulyk", "birthday": datetime(1988, 3, 10)},
    {"name": "Roma Kvitka", "birthday": datetime(1989, 3, 11)},
    {"name": "Anna Antonovych", "birthday": datetime(2003, 3, 12)},
]



def get_birthdays_per_week(users):
        
    today=datetime.today()
    today=today.date()
    print("Today is ",today)
    
    # Створюємо список словників на тиждень в якому будуть відображатись всі іменинники
    dict_week={ 
            "Monday":[],
            "Tuesday":[],
            "Wednesday":[],
            "Thursday":[],
            "Friday":[],
            }
    for user in users:
        name=user["name"]
        birthday=user["birthday"].date()
        birthday_this_year=birthday.replace(year=today.year)
        print("")
        print(name)
        # print(birthday)
        # print(birthday_this_year)
        if birthday_this_year<today:
            birthday_this_year=birthday.replace(year=today.year+1)
        print(birthday_this_year)

        day_today=today.weekday()
        print("day_today -",day_today)
        delta_days=((birthday_this_year-today).days)
        print("delta_days -", delta_days)

        if delta_days<7:
            day_week=delta_days+day_today
            print("day_week 1-", day_week)
            if day_week>6:
                day_week=delta_days+day_today-7
                print("day_week 2-", day_week)

            if day_week==0:
                dict_week["Monday"].append(name)
            elif day_week==1:
                dict_week["Tuesday"].append(name)
            elif day_week==2:
                dict_week["Wednesday"].append(name)
            elif day_week==3:
                dict_week["Thursday"].append(name)
            elif day_week==4:
                dict_week["Friday"].append(name)
            elif day_week==5:
                dict_week["Monday"].append(name)
            elif day_week==6:
                dict_week["Monday"].append(name)


        for day_dict, people in dict_week.items():
            print(f"{day_dict}: {people}")
    return dict_week    


print(get_birthdays_per_week(users))