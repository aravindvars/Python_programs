import subprocess

def run_terminal_command(commands):
    for command in commands:
      try:
          subprocess.run(command, shell=True, check=True)
      except subprocess.CalledProcessError as e:
          print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}")
      except FileNotFoundError:
          print("Command not found. Please make sure the command is installed.")

if __name__ == "__main__":
    command_to_execute = "date", "ls -lt", "if ( -d Hello ) then echo 'Folder exists' else echo 'No Folder fi"  # Replace this with the command you want to run in the terminal
    run_terminal_command(command_to_execute)