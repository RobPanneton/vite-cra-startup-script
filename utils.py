import subprocess

def run_subprocess(command, directory):
     subprocess.run(command, shell=True, check=True, cwd=directory, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )


