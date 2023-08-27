yourstring = ""
while len(yourstring) <= 1:
    yourstring = input('Type a string you wish to replace with a specific character: ')
    
character = input('what character? ')
length = input("what length do you want the new string to be?(press 'DF' to select the original length of your string.)\n")
#while isinstance(length, int) == False:
#    length = input("what length do you want the new string to be?(press 'DF' to select the original length of your string.)\n")

if length == "Df" or length == "dF" or length == "Df" or length == "df":
    length = int(len(yourstring))
counter = 0
if length != "DF" or length != "dF" or length != "Df" or length != "df":
    while len(character) != 1:
        character = input("Please type only ONE character: ")
print("Here is your new string: ", end="")
for i in range(length):
    print(character, end="")
    counter+=1
print("\nNumber of characters in your string:", counter)
