# Importing Modules
import request 
from tkinter import *
from pil import image, imageTk 
url='rickandmortyapi.com/api/character/?page=1'
response=request.get(url)
json_res=response.json()
print(json_res)
json_res_results=json('results')
print('json res_results')
for obj in json res_results:
    name = obj ('name')
print(name)
class character 
def_init_(self , name , gender , speices orgin, status , image)
self.name=name
self.gender 
self.species=species
self.orgin=orgin
self.status=status 