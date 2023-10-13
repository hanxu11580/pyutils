import json



if __name__ == '__main__':
    dict = {
        'name':'Bob',
        'age':18
    }
    
    json_path = './Json/data.json'
    
    try:
        with open(json_path, 'w', encoding='utf-8') as fs:
            json.dump(dict, fs)
    except Exception as e:
        print(e)
        
    try:
        with open(json_path, 'r', encoding='utf-8') as fs:
            new_dict = json.load(fs)
            print(new_dict)
    except Exception as e:
        print(e)
        
    