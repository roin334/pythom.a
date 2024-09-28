import random

numbers = [i for i in range(1, 42)]


user_ticket = [3,7,10,11,17,29]
while len(user_ticket) < 6:
    try:
        num = int(input("Choose a number between 1-42: "))
        if num < 1 or num > 42:
            print("The number must be between 1-42.")
        elif num in user_ticket:
            print("You have already selected this number, try another one.")
        else:
            user_ticket.append(num)
    except ValueError:
        print("Please enter a valid number.")


drawn_numbers = random.sample(numbers, 6)


matching_numbers = len(set(user_ticket).intersection(drawn_numbers))


if matching_numbers == 0 or matching_numbers == 1:
    print("Your ticket did not win.")
elif 1 < matching_numbers < 4:
    print("You won between 100-1000 GEL.")
elif 4 <= matching_numbers < 6:
    print("You won between 1000-5000 GEL.")
else:
    print("You've won the jackpot!")

print(f"Your ticket: {user_ticket}")
print(f"Numbers drawn: {drawn_numbers}")
print(f"Number of matches: {matching_numbers}")