from datetime import datetime, date

#1
now = datetime.now()

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()


#2
current_date_format = now.strftime(f"%m/%d/%Y, %H:%M:%S")

#3
date_format_time = datetime.strptime("5 December, 2019", f"%d %B, %Y")

#4
next_year = date(year = 2026, month = 1, day = 1)
current_year = date(year = year, month = month, day = day)
print(next_year - current_year)

#5
get_that_year = datetime.strptime("1 January 1970", f"%d %B %Y")
that_year = date(year = get_that_year.year,  month = get_that_year.month, day = get_that_year.day)
print(current_year - that_year)

#6

""" 
######################### The instruction #########################
6. Think, what can you use the datetime module for? Examples:
    o Time series analysis
    o To get a timestamp of any activities in an application
    o Adding posts on a blog

"""