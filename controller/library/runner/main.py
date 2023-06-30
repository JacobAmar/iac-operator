import subprocess, os,re
def run_command(command):
    process = subprocess.run(command,universal_newlines=True,capture_output=True)
    try:
       process.check_returncode()
       return process.stdout
    except Exception:
        print("terraform command has failed, exiting")
        print(process.stderr)

def terraform_init():
    process = run_command(["terraform","init","-input=false","-no-color"])
    print(process)

def terraform_plan():
    process = run_command(["terraform","plan","-input=false","-no-color"])
    # using regex to capture terraform changes
    result = re.search("Plan:\s(\d).*(\d)\sto\schange.*(\d)\sto\sdestroy",process)
    to_add = result.group(1)
    to_change = result.group(2)
    to_destroy = result.group(3)
    print([to_add,to_change,to_destroy])

def main():
    os.chdir("../../../terraform")
    #terraform_init()
    terraform_plan()

main()