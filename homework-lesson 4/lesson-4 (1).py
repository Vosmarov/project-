from sys import argv
def pay_work(hours, hour_pay, prem):
    pay = (hours * hour_pay) + prem
    return pay
name_script, hourses, hour_pays, prems = argv
print(name_script)
print(pay_work(hours=int(hourses), hour_pay=int(hour_pays), prem=int(prems)))

