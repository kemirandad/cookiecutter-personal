import os
import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

packages_condition = "{{ cookiecutter.install_packages}}"
project_slug = "{{ cookiecutter.project_slug}}"
python_version = "{{ cookiecutter.python_version }}"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

if packages_condition.lower().strip() == 'Yes':
    subprocess.call(['conda','create','--name',project_slug,'python=',python_version])
    subprocess.call(['conda','env','create','--file','environment.yml'])

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")