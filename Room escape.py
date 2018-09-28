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
first_room = input("Vad tänker du göra? ")

#händelser för första valet
def first_choice(first_room):
    if "dörr" or "bakåt" or "öppna" or "ut" in first_room:
        print("Dörr")
    if "trapp" or "höger" in first_room:
        print("Trapp")
    if "korridor" or "vänster" in first_room:
        print("korridor")

first_choice(first_room)
