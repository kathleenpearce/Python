proseString = """
Hi Best Friend,


Just writing to tell you that I've quit that dumb job at OCCUPATION and I've decided to finally start working at NEWCOMPANY. I know you might think that place is quite ADJECTIVEONE but I've always been interested and passionate about PLURAL_NOUN, and NEWCOMPANY are the people that specialize in that. I know I will end up being the best ADJECTIVETWO that I can be!

I'll see you at HOLIDAY!

Love,

NAME"""


newProseString = proseString

userInput = input("Please provide the best job in the world")
newProseString = proseString.replace("OCCUPATION", userInput)



userInput = input("Please provide the worst company in the world")
newProseString = proseString.replace("NEWCOMPANY", userInput)

userInput = input("Please provide and adjective")
newProseString = proseString.replace("ADJECTIVEONE", userInput)

userInput = input("Please provide a different adjective")
newProseString = proseString.replace("ADJECTIVETWO", userInput)

userInput = input("Please provide a plural noun")
newProseString = proseString.replace("PLURAL_NOUN, userInput")

userInput = input("Please provide an obscure holiday")
newProseString = proseString.replace("HOLIDAY", userInput)


print)newProseString