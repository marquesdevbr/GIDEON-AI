from brain.brain import Brain

brain = Brain()
brain.initialize()

while True:
    text = input("Você: ")

    if text.lower() in ["sair", "exit"]:
        break

    resposta = brain.process(text)

    print(f"GIDEON: {resposta}")