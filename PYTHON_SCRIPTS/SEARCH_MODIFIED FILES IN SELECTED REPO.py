import os

host = str(input("Введите путь к Git-репозиторию для проверки файлов на модификацию: "))
bash_command =  "cd " + host, "git status"
result_os = os.popen(' && ' .join(bash_command)).read()
for result in result_os.split('\n'):
            if result.find('modified') != -1:
                                    prepare_result = result.replace('\tmodified:   ','' )
                                    print(host+ '/' + prepare_result)
#MODIFIED FILES IN SELECTED REPO