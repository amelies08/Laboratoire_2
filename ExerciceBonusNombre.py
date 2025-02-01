reponse = 34
reponse = int(reponse)

print("Devine le nombre entre 1 et 100.")
guess = input()
guess = int(guess)

while guess != reponse :
    if guess > reponse :
        print("le nombre est trop grand")
        guess = input()
        guess = int(guess)
    if guess < reponse :
        print("le nombre est trop petit")
        guess = input()
        guess = int(guess)
else:
    print("bravo!")
