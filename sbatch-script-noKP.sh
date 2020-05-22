#! /bin/bash


#SBATCH --job-name="KPTest"
#SBATCH --mail-type=ALL
#SBATCH --mail-user=Cansin.Sapmaz@city.ac.uk
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --output kpep32040-%J.output
#SBATCH --error kpep32040-%J.err
#SBATCH --gres=gpu:1
#SBATCH --partition=normal



module load cuda/10.0
module add python/intel

python3 main.py --dataset celebKP --light true --iteration 10000 --save_freq 10000 --print_freq 10000 --result_dir noKP --trainkp False --with_kp False --kpep 0 && python3 main.py --dataset celebKP --light true --iteration 20000 --save_freq 10000 --print_freq 10000 --result_dir noKP --trainkp False --with_kp False --kpep 0 --resume True && python3 main.py --dataset celebKP --light true --iteration 30000 --save_freq 10000 --print_freq 10000 --result_dir noKP --trainkp False --with_kp False --kpep 0 --resume True && python3 main.py --dataset celebKP --light true --iteration 40000 --save_freq 10000 --print_freq 10000 --result_dir noKP --trainkp False --with_kp False --kpep 0 --resume True && python3 main.py --dataset celebKP --light true --iteration 50000 --save_freq 10000 --print_freq 10000 --result_dir noKP --trainkp False --with_kp False --kpep 0 --resume True
