import csv
def top_n(dict_1,n=5):
    return sorted(dict_1.items(),key=lambda x:x[1],reverse=True)[:n]

def load_data(file_path: str) -> list[list[str]]:
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        return list(reader)

def aggregate(data,key_index,value_index):
    result = {}
    for row in data[1:]:
        key = row[key_index]
        value = row[value_index]
        result[key] = result.get(key,0) + float(value)
    return result