import threading

def pierwsza_petla():
    for i in range(1, 6):
        print(f'Wątek 1: Iteracja {i}')

def druga_petla():
    for i in range(1, 6):
        print(f'Wątek 2: Iteracja {i}')


watek1 = threading.Thread(target=pierwsza_petla)
watek2 = threading.Thread(target=druga_petla)

watek1.start()
watek2.start()

watek1.join()
watek2.join()

print("Program zakończony.")
