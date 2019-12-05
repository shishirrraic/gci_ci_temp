from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

print("now =", now)
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time is =", dt_string)
print("date and time is it is it=", dt_string)
