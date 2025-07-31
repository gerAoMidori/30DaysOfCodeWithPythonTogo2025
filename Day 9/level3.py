person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

def application_check(person):
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. {"He is married." if person['is_married'] else "He is not married."}")
    print(f"His address is {person['address']['street']}, {person['address']['zipcode']}.")
    if "skills" in person:
        print(f"He has skills and the middle skill is {person['skills'][len(person['skills']) // 2]}.")
        if 'Python' in person['skills']:
            print("He knows Python.")
        else:
            print("He doesn't know Python.")

        if set(person["skills"]) == {"JavaScript", "React"}:
            print('He is a front end developer'),
        elif set(person["skills"]) == {"Node", "MongoDB", "Python"}:
            print('He is a backend developer')
        elif set(person["skills"]) == {"React", "Node", "MongoDB"}:
            print('He is a fullstack developer')
        else:
            print("unknown title")
    
    else:
        print("He has no skills.")

application_check(person)