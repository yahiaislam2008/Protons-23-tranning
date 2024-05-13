import datetime as dt
birthdate_year=int(input("enter your birthdate year:"))
birthdate_month=int(input("enter your birthdate month:"))
birthdate_day=int(input("enter your birthdate day:"))
today=dt.datetime.now()
birthday=dt.datetime(birthdate_year,birthdate_month,birthdate_day)
age_years=int((today  -  birthday).days)/365.25
print("you are", age_years ,"years old")
if(age_years>20):
    print("youuu are tooooo ooold")
else:
    print("babay shark doo-doo-doo-doo")
    