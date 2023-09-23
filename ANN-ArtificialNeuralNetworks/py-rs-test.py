import lib_rs as rs
import time

start = time.time()

rs.fib_to(10)

a = 345
b = 54647
print(rs.sum(a, b))

end = time.time()
print(f'time: {end - start}')
