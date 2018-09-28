#intro
print("Knarr...")
print("Gnissel...")
print("...")
print("...")
print("...")
print("BAAAM!")
print("Dörren gick igen bakom dig - du som bara skulle kika in i det här övergivna gamla huset.")
print("(Så här i efterhand var det kanske inte en jättebra idé.)")
print("Du befinner dig i en mörk hall. Sikten är ungefär en och en halv meter framåt, och du kan se en smal trappa framför dig. Till vänster om den går en mörk, smal korridor längre in i huset.")
print("Du utvärderar dina val och kommer fram till att du antingen kan försöka öppna dörren, gå upp för trappan eller undersöka korridoren.")

current_position = 1

#första valet
while current_position == 1:
    first_room = input("Vad tänker du göra? ")
    #händelser för första valet
    def first_choice(input):
        if "dörr" or "bakåt" or "öppna" or "ut" in first_room:
            current_position = 1
            print(current_position)
        elif "korridor" or "vänster" in first_room:
            current_position = 2
            print(current_position)
        elif "trapp" or "höger" in first_room:
            current_position = 3
            print(current_position)
        return current_position

    first_choice(input)

    if current_position == 1:
        print("Du försöker öppna dörren, men den har gått i baklås.")
    if current_position != 1:
        break

if current_position == 2:
    print("Du går in i korridoren.")
    print(meh)
