import time 

tempo = input("Digite o tempo (em segundos): ")

if tempo.isdigit():
    tempo = int(tempo)

else:
    print("Entrada Inválida!")
    quit()

while tempo != 0:
    minuts, seconds = divmod(tempo, 60)
    timer = "{:02d}:{:02d}".format(minuts, seconds)
    print(timer, end= "\r")
    time.sleep(1)
    tempo = tempo - 1

print("TEMPO ACABOU!")