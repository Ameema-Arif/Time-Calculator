def add_time(start, duration, *weekday):
    start_time = start.split()
    time = start_time[0].partition(":")
    s_hour = int(time[0])
    s_min = int(time[2])
    noon_id = start_time[1]
    duration = duration.partition(":")
    d_hour = int(duration[0])
    d_min = int(duration[2])
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days = 0 

#d_hour can be any number
#d_min can be a whole number less than 60
#s_hour should count from 1 to 12 and after 12 it should return to 1
#s_min should count from 00 to 59 and whenever it passes 59 it should increment s_hour too
#noon_id whenever changes from PM to AM day should change too
#noon_id whenever changes from AM to PM day should not change
#s_hour whenever passes 12 noon_id should change
#3:30 PM, 10:40

    for hour in range(0, d_hour+1):
        if s_hour == 12:
            s_hour = 1
            continue
            
        if hour == 0:
            s_hour += 0
        else:
            s_hour += 1
            if s_hour == 12:
                if noon_id == "PM":
                    noon_id = "AM"
                    days += 1
                else:
                    noon_id = "PM"
        
        
    for minute in range(1, d_min+1):
        if s_min == 59:
                s_hour += 1
                if s_hour == 12:
                    if noon_id == "PM":
                        noon_id = "AM"
                        days += 1
                    else:
                        noon_id = "PM"
                s_min = 00
                continue
                
        else:
            s_min += 1

    if weekday:
        weekday = list(weekday)
        weekday = weekday[0]
        for dayname in week:
            if dayname.lower() == str(weekday).lower():
                day = week.index(dayname)
                break
            else:
                continue
            
        for count in range(0, days+1):
            if count == 0:
                day += 0
                continue
            if day == 6:
                day = 0
            else:
                
                day += 1

        if days == 0:
            new_time = str(s_hour) + ":" + str(s_min).rjust(2, "0") + " " + noon_id + "," + " " + week[day]
        elif days == 1:
            new_time = str(s_hour) + ":" + str(s_min).rjust(2, "0") + " " + noon_id + "," + " " + week[day] + " (next day)"
        else:
            new_time = str(s_hour) + ":" + str(s_min).rjust(2, "0") + " " + noon_id + "," + " " + week[day] + " (" + str(days) + " days later)"
            
    else:
        if days == 0:
            new_time = str(s_hour) + ":" + str(s_min).rjust(2, "0") + " " + noon_id
        elif days == 1:
            new_time = str(s_hour) + ":" + str(s_min).rjust(2, "0") + " " + noon_id + " (next day)"
        else:
            new_time = str(s_hour) + ":" + str(s_min).rjust(2, "0") + " " + noon_id + " (" + str(days) + " days later)"
    return(new_time)
            


    
