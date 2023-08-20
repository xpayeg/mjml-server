import os

file_name = "app.yaml"
repo_name = os.getenv('REPO_NAME') 

file = open(file_name, "r")

data = file.read()
file.close()

data = data.replace("REPO_NAME", repo_name)

file = open(file_name, "w")
file.write(data)
file.flush()
file.close()
