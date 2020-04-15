from datetime import date

users = [
    {
        'email': 'cvander@platzi.com',
        'first_name': 'Christian',
        'last_name': 'Van der Henst',
        'password': '1234567',
        'is_admin': True,
    },
    {
        'email': 'freddier@platzi.com',
        'first_name': 'Freddy',
        'last_name': 'Vega',
        'password': '987654321',        
    },
    {
        'email': 'yesica@platzi.com',
        'first_name': 'Yesica',
        'last_name': 'Cortes',
        'password': 'qwerty',
        'birthdate': date(1990, 12, 19),
    },
    {
        'email': 'pablo@platzi.com',
        'first_name': 'Pablo',
        'last_name': 'Trinidad',
        'password': 'msicomputer',
        'is_admin': True,
        'birthdate': date(1981, 11, 6),
        'bio': 'The path of the rigtheous man is beset on all sides by the iniquities of the selfish and the ',
    },
]

from posts.models import User

for user in users:
    obj = User(**user)
    obj.save()
    print(obj.pk, ':', obj.email)