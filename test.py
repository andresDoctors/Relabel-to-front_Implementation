import subprocess
import os

def run(cmd):

    if(os.name == 'nt'):
        completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    else:
        completed = subprocess.run(["bash", "-c", cmd], capture_output=True)

    return completed

if __name__ == '__main__':

    for i in range(1, 5 + 1):
        cmd = f'python ./source/main.py ./test-in/test{i}.in > ./test-out/test{i}.out'
        print(f'cmd:"{cmd}"')
        command_info = run(cmd)
        if command_info.returncode != 0:
            print(f"An error occured:\n{command_info.stderr}")
        else:
            print(f"ommand executed successfully:\n{command_info.stdout}")

    print("-------------------------")
