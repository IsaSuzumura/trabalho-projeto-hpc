#!/bin/bash

#SBATCH --job-name=monte_carlo_pi
#SBATCH --output=results/%x_%j.out
#SBATCH --error=results/%x_%j.err
#SBATCH --time=00:10:00
#SBATCH --ntasks=16
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G

# Carregue os módulos necessários para o seu ambiente.
# No Santos Dumont, você precisará carregar o módulo do MPI e do Python.
# Este é um exemplo, os nomes exatos podem variar no cluster.
# #module load mpi python/3.10 

echo "Iniciando a execução em $(date)"

# Use o srun para executar seu programa MPI no cluster.
# O SLURM automaticamente gerenciará o número de tarefas (--ntasks)
# que você especificou acima.
srun python3 src/main.py

echo "Execução finalizada em $(date)"