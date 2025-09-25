# src/main.py
from mpi4py import MPI
import time
import random

# Inicializa o MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Número total de iterações, será dividido entre os processos
total_iterations = 100_000_000

# Cada processo (rank) faz sua parte do trabalho
local_iterations = total_iterations // size
local_count_inside_circle = 0

t0 = time.time()

# Loop principal para a simulação de Monte Carlo
for i in range(local_iterations):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    distance = x**2 + y**2
    if distance <= 1:
        local_count_inside_circle += 1

# Soma os resultados de todos os processos no processo raiz (rank 0)
total_count_inside_circle = comm.reduce(local_count_inside_circle, op=MPI.SUM, root=0)

t1 = time.time()

# O processo raiz (rank 0) imprime o resultado
if rank == 0:
    pi_estimate = 4 * total_count_inside_circle / total_iterations
    print(f"Estimativa de Pi: {pi_estimate:.6f}")
    print(f"Tempo de execução: {t1 - t0:.3f}s")
    print(f"Número de processos: {size}")
    
# Importante: para garantir a comunicação e sincronização, todos os processos devem chegar
# a este ponto, mesmo que só o rank 0 imprima.