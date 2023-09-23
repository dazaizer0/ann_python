import lib_rs as rs
import time

start = time.time()

for i in range(41):
    print(f'{i} - {rs.fib(i)}')

end = time.time()
print(f'time: {end - start}')
