import random
# گرفتن ورودی از کازبر
while True :
    total_participants = int(input("number of participants:"))
    winners = int(input("number of winners:"))
                       
    if total_participants < winners :
         print("Error: Participants must exceed the number of winners.please enter again.\n")
    else:
        break
        
# ساخت لیست شرکت کننده ها
phone_numbers = []
pre = "09"
for i in range(total_participants):
    numbers = random.randint(100_000_000, 999_999_999)
    full_number = f'{pre}{numbers}'
    phone_numbers.append(full_number)

winners = random.sample(phone_numbers ,winners)

# نمایش برنده ها
stars = '***'
for number, phone in enumerate(winners, start:= 1) :
    first_4_digits = phone[:4]
    last_3_numbers = phone[-3:]

    print(f'winner number {number}: {phone[:4]} {stars} {phone[-3:]}')