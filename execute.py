import subprocess
import os
from sys import argv


def run(cmd):

    if(os.name == 'nt'):
        command_info = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    else:
        command_info = subprocess.run(["bash", "-c", cmd], capture_output=True)

    return command_info

def give_output(command_info):

    if command_info.returncode != 0:
        print(f"An error occured:\n{command_info.stderr}")
    else:
        print(f"command executed successfully:\n{command_info.stdout}")

    print("-------------------------")

def execute():

    if(len(argv) == 2 and argv[1] == 'test'):
        for filename in os.listdir('./in'):

            cmd = f'python ./source/main.py ./in/{filename} > ./out/{filename}.out'
            command_info = run(cmd)
            give_output(command_info)

    elif(len(argv) == 1):
        for i in range(1, 5 + 1):

            cmd = f'python ./source/main.py ./test-in/test{i}.in > ./test-out/test{i}.out'
            command_info = run(cmd)
            give_output(command_info)


if __name__ == '__main__':
    execute()
