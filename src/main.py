from mpi4py import MPI
import time
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

total_iterations = 100_000_000

local_iterations = total_iterations // size
local_count_inside_circle = 0

t0 = time.time()

for i in range(local_iterations):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    distance = x**2 + y**2
    if distance <= 1:
        local_count_inside_circle += 1

total_count_inside_circle = comm.reduce(local_count_inside_circle, op=MPI.SUM, root=0)

t1 = time.time()

if rank == 0:
    pi_estimate = 4 * total_count_inside_circle / total_iterations
    print(f"Estimativa de Pi: {pi_estimate:.6f}")
    print(f"Tempo de execução: {t1 - t0:.3f}s")
    print(f"Número de processos: {size}")
