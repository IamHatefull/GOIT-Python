from datetime import datetime, timedelta

def congratulate(users):
    pres_time = datetime.now()
    #counting start and end of varifiable week which starts from present saturday and ends at next friday
    week_start = pres_time + timedelta(days = 5 - pres_time.weekday())
    week_end = week_start + timedelta(days = 7)

    congrat_list = []
    monday_list = []
    thuesday_list = []
    wednesday_list = []
    thursday_list = []
    friday_list = []

    for dicts in users:
        for name, birthday in dicts.items():
            if week_start.month <= birthday.month <= week_end.month and week_start.day <= birthday.day <= week_end.day:
             
                if birthday.weekday() == 5 or birthday.weekday() == 6 or birthday.weekday() == 0:
                    monday_list.append(name)
                if birthday.weekday() == 1:
                    thuesday_list.append(name)
                if birthday.weekday() == 2:
                    wednesday_list.append(name)
                if birthday.weekday() == 3:
                    thursday_list.append(name)
                if birthday.weekday() == 4:
                    friday_list.append(name)
            
            else:
                continue

    #i could just print without congrat_list, but i want to save info
    congrat_list.append('Monday: ' + ', '.join(monday_list))
    congrat_list.append('Thuesday: ' + ', '.join(thuesday_list))
    congrat_list.append('Wednesday: ' + ', '.join(wednesday_list))
    congrat_list.append('Thursday: ' + ', '.join(thursday_list))
    congrat_list.append('Friday: ' + ', '.join(friday_list))

    for i in congrat_list:
        print(i)


#______________
users = [{'Jim': datetime(year = 2021, month = 5, day = 16),'John': datetime(year = 2021, month = 5, day = 16)}, \
         {'Jason': datetime(year = 2021, month = 5, day = 18),'J': datetime(year = 2021, month = 5, day = 21)}]

congratulate(users)
