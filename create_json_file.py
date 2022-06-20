import json

#Write content to the file

my_dic={"Name":"Vikas","Skill":["Python","Salary","$2500"]}
of=open("file.json","w")
json.dump(my_dic,of,indent=5) # write to json file
of.close()

#Read the content from the file

fo=open("file.json","r")
print(json.load(fo))

