import lib_rs as rs
import time

start = time.time()

rs.fib_to(43)

end = time.time()
print(f'time: {end - start}')
