import os

bash_command = "cd netology/sysadm-homeworks/devops-netology", "git status"
result_os = os.popen(' && ' .join(bash_command)).read()
for result in result_os.split('\n'):
        if result.find('modified') != -1:
                    prepare_result = result.replace('\tmodified:   ','' )
                    print(prepare_result)
# Checking modified files in a git repository
