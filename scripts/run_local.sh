#!/usr/bin/env bash

# O comando "set -e" garante que o script irá parar se houver algum erro
set -e

# Este é o comando para rodar o seu programa MPI.
# O "-np 4" indica que você quer usar 4 processos (ranks) para a execução.
# Você pode ajustar esse número para testar o desempenho com diferentes
# quantidades de processos.
echo "Executando o projeto de Monte Carlo com 4 processos..."
mpirun -np 4 python3 ../src/main.py