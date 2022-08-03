import json
import logging
import os

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def parse_user(output_file, *input_files):
    results={}
    key="name"

    def find_key(json_dict):
        try: 
            if json_dict[key] not in  results:
                results[json_dict[key]]=json_dict
        except KeyError: 
            pass 

    for item in input_files:
        try:
            with open(item, 'r') as file:
                data=json.load(file, object_hook=find_key)
        except FileNotFoundError:
            logging.error(f"File {item} doesn't exist") 

    with open(output_file, "w") as file:
        data = json.dump(list(results.values()), file, indent=4)


file1=os.path.dirname(__file__) + "\\files\\user1.json"
file2=os.path.dirname(__file__) + "\\files\\user2.json"
file3=os.path.dirname(__file__) + "\\files\\user3.json"

parse_user(file3, file1, file2)
