#!/usr/bin/python3
import gitlab
import sys
import base64
import os
from datetime import datetime


gl = gitlab.Gitlab("https://gitlab.alpinelinux.org")
project = gl.projects.get(1, lazy=True)
apkbuild = gl.projects.get(1).files.raw(file_path="main/aaudit/APKBUILD", ref="master")
p rint(apkbuild.decode('UTF-8'))
 
 
                                     
  
# list the content of a subdirectory on a specific branch
items = project.repository_tree(path='main', ref='master', get_all=True)

for i in items:
    print(i["name"])


write_path = os.getcwd()
a = 1
while a < 5:
    x = datetime.now()
    file_name = f"{x.strftime('%d-%m-%Y-%H-%M-%S-%f=HDTV')}_{a}.txt"
    
    with open(os.path.join(path, file_name), 'w') as fp:
        fp.write(f'this is a test')

    a += 1




"""
with open("/Users/afeddersen/github/Auto-GPT/tools/APKBUILD", "wb") as f:
    project.files.raw(file_path=file_path, ref=branch_name, streamed=True, action=f.write)






import gitlab
import base64


# private token authentication
gl = gitlab.Gitlab(<gitlab-url>, private_token=<private-token>)

gl.auth()

# list all projects
projects = gl.projects.list(all=True)
for project in projects:
    # print(project) # prints all the meta data for the project
    # print("Project: ", project.name)
    # print("Gitlab URL: ", project.http_url_to_repo)

    # Skip projects without branches
    if len(project.branches.list()) == 0:
        continue

    branch = project.branches.list()[0].name

    try:
        f = project.files.get(file_path='Dockerfile', ref=branch)
    except gitlab.exceptions.GitlabGetError:
        # Skip projects without Dockerfile
        continue

    file_content = base64.b64decode(f.content).decode("utf-8")
    print(file_content.replace('\\n', '\n'))

"""








