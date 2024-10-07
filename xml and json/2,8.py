import json 
data = {"name": "San",
         "age": 18, 
         "city": "Ha Noi",
         "company":"Dev luxury"}
json_data = json.dumps(data)
print(json_data)