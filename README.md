# Projeto HPC - Estimação de Pi com Monte Carlo

## Visão Geral
    Este projeto implementa o método de Monte Carlo para estimar o valor de Pi (π). A simulação envolve a geração de um grande número de pontos aleatórios dentro de um quadrado unitário e a contagem de quantos desses pontos caem dentro de um círculo inscrito. A partir da proporção, é possível estimar o valor de π. O objetivo principal é demonstrar e medir a escalabilidade de um ambiente de Computação de Alto Desempenho (HPC), explorando o paralelismo com MPI (Message Passing Interface) em Python, utilizando a biblioteca mpi4py.

## Requisitos
    1. Python 3.10 ou superior
    2. Biblioteca mpi4py
    3. Uma implementação MPI (como o MS-MPI para Windows ou OpenMPI para Linux/macOS)
    4. Ambiente de agendamento de jobs SLURM (necessário para execução no cluster Santos Dumont)

## Como Rodar (Local)
    Para testar a aplicação na sua máquina, siga os passos abaixo. Certifique-se de que a sua implementação MPI e a biblioteca mpi4py estão instaladas e configuradas corretamente.
        # Navegue até a pasta raiz do projeto
            cd projeto-hpc
        # Torne o script executável
            chmod +x scripts/run_local.sh
        # Execute o script com 4 processos. Você pode ajustar o número.
            bash scripts/run_local.sh

## Como Rodar (Santos Dumont)
    Para submeter o job no supercomputador, você usará o agendador SLURM.

    1. Copie os arquivos do projeto para o nó de acesso do Santos Dumont e prepare os dados temporários em /scratch.
    2. Compile ou prepare o ambiente executando o script de build.
        bash scripts/build.sh
    3. Submeta o job SLURM usando o script job_cpu.slurm
        sbatch scripts/job_cpu.slurm

## Estrutura
O projeto está organizado na seguinte estrutura de diretórios:
    1. src/: Contém o código-fonte principal (main.py).
        scripts/: Contém os scripts para automação, como run_local.sh e job_cpu.slurm.
    2.env/: Contém o arquivo requirements.txt com as dependências do     
        projeto.
    3.results/: Contém os logs e saídas da execução do job, conforme      
        configurado no script SLURM.

