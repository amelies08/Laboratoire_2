reponse = 34
reponse = int(reponse)
tentative = 1

print("Devine le nombre entre 1 et 100.")
print("nombre de tentatives : ", tentative)
guess = input()
guess = int(guess)

while guess != reponse :
    if guess > reponse :
        print("le nombre est trop grand")
        guess = input()
        guess = int(guess)
        tentative = tentative + 1
        print("nombre de tentatives : ", tentative)
    if guess < reponse :
        print("le nombre est trop petit")
        guess = input()
        guess = int(guess)
        tentative = tentative + 1
        print("nombre de tentatives : ", tentative)
else:
    print("bravo!")
