import random

def saludo() -> str:
    print("🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧 \n   Welcome Player \n🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧")

def election(user)-> str:
    if user == 1:
        user = "🪨"
    elif user == 2:
        user = "📃"
    elif user == 3:
        user = "✂️"
    return user

def resultado(pc, player1) -> str:
    if player1 == pc:
        result = "You Tied"
    elif (
        (player1 == "🪨" and pc == "📃")
        or (player1 == "📃" and pc == "✂️")
        or (player1 == "✂️" and pc == "🪨")
    ):
        result = "You Lost😭"
    elif (
        (player1 == "🪨" and pc == "✂️")
        or (player1 == "📃" and pc == "🪨")
        or (player1 == "✂️" and pc == "📃")
    ):
        result = "You Won🎉"
    else:
        result="Opción Incorrecta"
    return result

def game() -> str:
    saludo()
    options = ["🪨", "📃", "✂️"]
    pc = random.choice(options)
    player1 = election(user=int(input("Choose \n1.🪨\n2.📃\n3.✂️\n")))
    return resultado(pc, player1)

print(game())
