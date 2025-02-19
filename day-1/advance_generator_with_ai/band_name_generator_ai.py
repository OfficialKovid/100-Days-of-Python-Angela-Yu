from langchain_ollama import OllamaLLM
import ast

model = OllamaLLM(model = "llama3.2:1b")

city = input("Enter the name of city you where you grow up? \n")
pet_name = input("Enter the name of your pet?\n")


input = f"""
You are a band name generator. Give me 5 band name suggestions. Try to relate or use the information I give you. You can also add some creativity from your side. But the name should be related to my information.

Info about me:
- I was born in "{city}" (a city).
- My pet's name is "{pet_name}".

Output **MUST** be a valid pythonlist Example:
["name1", "name2", "name3", "name4", "name5"]

Do not include anything else in your response. Just return the python list.
"""

result = model.invoke(input)
print(f"\n Raw result {result}")
try:
    band_names = ast.literal_eval(result)
except Exception as e:
    band_names = None
    print(f"{e} is the error")


print("Band Names could be: ")
if band_names is not None:
    for idx,name in enumerate(band_names):
        print(f"{idx+1} {name}")
else:
    print("Sorry we're facing some issues, please try after some time.")