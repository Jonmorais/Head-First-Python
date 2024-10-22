import pprint

people = {
    'Ford': {
        'Name': 'Ford Prefect',
        'Gender': 'Male',
        'Occupation': 'Researcher',
        'Home Planet': 'Betelgeuse Seven'
    },
    'Arthur': {
        'Name': 'Arthur Dent',
        'Gender': 'Male',
        'Occupation': 'Sandwich-Maker',
        'Home Planet': 'Earth'
    },
    'Trillian': {
        'Name': 'Tricia McMillan',
        'Gender': 'Female',
        'Occupation': 'Mathematician',
        'Home Planet': 'Earth'
    },
    'Robot': {
        'Name': 'Marvin',
        'Gender': 'Unknown',
        'Occupation': 'Paranoid Android',
        'Home Planet': 'Unknown'
    }
}

pprint.pprint(people)
# print(people['Arthur']['Occupation']) -> Sandwich-Maker
