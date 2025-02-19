# Band name generator with AI

## How it works
- User will enter the city on which he grew up and the name of his pet.
- It uses local ai model to generate 5 names which are closely related to the input.


## How to run this
- Install Python if it's not installed.

- Install ollama if it's not installed.

- In terminal run (it is to install llama3.2 1 Billion parameter model You can download other similar models.)
    - `ollama pull llama3.2:1b ` 
- Get the files:
    - Clone the github repo & cd to the `advance_generator_with_ai` folder.
    or
    - Download `requirements.txt` & `band_name_generator_ai.py` files and save in a folder.

- Create a virtual environment.
    - `python -m venv venv`

- Activate the virtual environment
    - Windows:
        - `.\venv\Scripts\activate `
    - Linux, Mac:
        - ` source venv/bin/activate `
    - Git Bash in  Windows:
        - ` source venv/Scripts/activate `
- Install The required packages.
    - ` pip install -r requirements.txt `
    - or
    - `pip install langchain langchain-ollama ollama`

- If using llama3.2:1b:
    - In terminal run `python band_name_generator_ai.py `
- If using any other model eg: deepseek-r1:1.5b:
    - Inside band_name_generator_ai.py replace the name.
    - Put ` model = OllamaLLM(model = "deepseek-r1:1.5b")` instead of ` model = OllamaLLM(model = "llama3.2:1b")` 