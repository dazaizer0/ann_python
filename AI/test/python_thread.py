import threading

def FIRST():
    for i in range(1, 6):
        print(f'1/{i}')

def SECOND():
    for i in range(1, 6):
        print(f'2/{i}')


thread1 = threading.Thread(target=FIRST)
thread12 = threading.Thread(target=SECOND)

thread1.start()
thread12.start()

thread1.join()
thread12.join()

print("FINISH")
