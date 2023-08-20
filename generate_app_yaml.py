import os

file_name = "app.yaml"
branch_name = os.getenv('BRANCH_NAME') 

file = open(file_name, "r")

data = file.read()
file.close()

data = data.replace("BRANCH_NAME", branch_name)

file = open(file_name, "w")
file.write(data)
file.flush()
file.close()
