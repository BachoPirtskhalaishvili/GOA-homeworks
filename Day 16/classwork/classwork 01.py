correct_pin = "1234"

entered_pin = ""

while entered_pin != correct_pin:

    entered_pin = input("შეიყვანეთ პინ კოდი: ")
    
    if entered_pin != correct_pin:
        print("არასწორი პინ კოდი, სცადეთ თავიდან!")

# თუ while ციკლიდან გამოვიდა, ე.ი. სწორია
print("წარმატებით შეხვედით სისტემაში!")