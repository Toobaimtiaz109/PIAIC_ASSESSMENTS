#Question-1
#Simple Message
message:str = "Hello, This is my second python Assessment."
print(message)
#Question-2
#Simple Messages
message:str = "It is raining outside."
print(message)
message:str = "No, its sunny outside."
print(message)
#Question-3
#Personal Message
name:str = "Rishmail"
print(f"Hello {name} ,Would you like to go outside with me?")
#Question-4
#Name Cases
name1:str = "Zainab"
print(name1.upper())
print(name1.lower())
print(name1.title())
#Question-5
#Famous Quote
print('Robert Kiyosaki once said,"Losers quit when they fail,winners fail until they succeed".')
#Question-6
#Famous Quote 2
famous_person:str = "Albert Einstein"
message3:str = f'{famous_person} once said,"Education is what remains after one has forgotten what one has learned in school".'
print(message3)
#Question-7
#Stripping names     :-{means to remove something.}
name2:str = " \t \n Tooba \t \n"
print(f'Original:{name2}')
print(f'lstrip:{name2.lstrip()}')
print(f'Rstrip:{name2.rstrip()}')
print(f'Strip:{name2.strip()}')
#Question-8
#Variable sum
x = 5
y = 8
z = 4
print(x+y+z)
#Question-9
#Variable swap    :-{Swapping in programming refers to the process of exchanging the values of two variables.}
a:int = 10
b:int = 8
print("Before Swap: ")
print(f"a={a}")
print(f"b={b}")
a,b = b,a
print("After Swap: ")
print(f"a={a}")
print(f"b={b}")
#Question-10
#Favourite Color
favouritecolor:str = "Yellow"
print(f"My favourite color is {favouritecolor}.")
mycolor:str = favouritecolor
print(f"{mycolor} is my favourite color.")
#Question-11
#Changing pet name
pet_name:str = "Buddy"
pet_name:str = "Max"
print(f"New pet name is: ")
#Question-12
#Observing name error
#sunshine:str = "SunShine"
#print(sunsine)
#Question-13
#Reassigning Score
score:int = 100
print(f"Original Score: {score}")
score:int = 50
print(f"After Reassigning Score: {score}")
#Question-14
#City name
city:str = "Lahore"
print(city)
#Question-15
#Tittle case
text:str = "python programming"
print(f"Text in tittlecase: {text.title()}")
#Question-16
#Lowercase conversation
mixedcase:str = "PytHon ProGramMing"
print(f"Text in lowercase: {mixedcase.lower()}")
#Question-17
#Uppercase conversation
mixedcases:str = "Python Programming"
print(f"Text in uppercase: {mixedcases.upper()}")
#Question-18
#Current temperature
temperature:int = 25
print(f"The current temperature is {temperature} degrees.")
#Question-19
#Printing a poem
poem:str = "Our life is like,\na thorny rose\nNot perfect,\nbut beautiful."
print(poem)