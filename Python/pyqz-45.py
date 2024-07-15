def process_data(data):
    if isinstance(data, list):
        data.pop()
        return data
    elif isinstance(data, dict):
        data.pop("Name")
        return data
    else:
        return "Unknown Type"

print(process_data({"name": "Alice", "age": 30}))

#Ans:

#A) {"age": 30}
#B) "Unknown Type"
#C) Key Error - Ans - KeyError: 'Name'
#D) {"name": "Alice"}