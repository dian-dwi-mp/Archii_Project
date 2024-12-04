import subprocess

def execute_task(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except Exception as e:
        print(f"Error executing task: {e}")

def open_application(app_name):
    try:
        subprocess.run(["xdg-open", app_name], check=True)
    except Exception as e:
        print(f"Error opening application: {e}")

