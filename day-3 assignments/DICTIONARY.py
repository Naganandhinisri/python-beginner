def filter_dictionaries(dictionaries):
    for dictionary in dictionaries:
        if dictionary['result'] == "pass":
            print(dictionary['name'])


filter_dictionaries([{'id': 1, 'result': "pass", 'name': 'Ramesh'},
                     {'id': 2, 'result': "pass", 'name': 'Suresh'},
                     {'id': 3, 'result': "fail", 'name': 'Alex'}])
