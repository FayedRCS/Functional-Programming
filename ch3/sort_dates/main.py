def sort_dates(dates):


    #Nested function so that it's easier to see what index splits into year/month/day

    
    dates = sorted(dates, key=year_month_day) #key= could be replaced with 'lambda x : (x.split("-")[2], x.split("-")[0], x.split("-")[1])'

    return dates

def year_month_day(dates):
    year = dates.split("-")[2]
    month = dates.split("-")[0]
    day = dates.split("-")[1]
    return year, month, day
    