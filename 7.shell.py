import subprocess

def execute_command(command):
    try:
        result = subprocess.run(command, shell = True, check = True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Erro: ", e)

def process_redirection(command):
    parts = command.split(">")
    if len(parts) == 2:
        cmd, output_file = parts[0].strip(), parts[1].strip()
        with open(output_file, "w") as f:
            subprocess.run(cmd, shell = True, check = True, stdout = f)
    else:
        execute_command(command)

def shell():
    while True:
        user_input = input("& ")
        if user_input.lower() == "exit":
            break
        elif "|" in user_input:
            commands = user_input.split("|")
            p1 = subprocess.Popen(commands[0].strip().split(), stdout = subprocess.PIPE)
            p2 = subprocess.Popen(commands[1].strip().split(), stdout = p1.stdout) 
            p1.stdout.close()
            p2.communicate()
        elif ">" in user_input:
            command, _, output_file = user_input.partition(">")
            command = command.strip()
            output_file = output_file.strip()
            with open(output_file, "w") as f:
                subprocess.run(command, shell=True, check=True, stdout=f)
        elif "<" in user_input:
            command, _, input_file = user_input.partition("<")
            command = command.strip()
            input_file = input_file.strip()
            with open(input_file, "r") as f:
                subprocess.run(command, shell=True, check=True, stdin=f)    
        else:
            execute_command(user_input)
        

if __name__ == "__main__":
    shell()