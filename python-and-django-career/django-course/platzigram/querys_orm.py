from posts.models import User

user = User.objects.get(email='freddier@platzi.com')
print(user)

# error email doesn't exists
#user = User.objects.get(email='freddy@platzi.com')

platzi_users = User.objects.filter(email__endswith='@platzi.com')
print(platzi_users)

users = User.objects.all()
print(users)

# error return at 4 (get admits 1 result)
# platzi_users = User.objects.get(email__endswith='@platzi.com')

platzi_users = User.objects.filter(email__endswith='@platzi.com')

for u in platzi_users:
    print(u.email, ':', u.is_admin)

platzi_users = User.objects.filter(email__endswith='@platzi.com').update(is_admin=True)

platzi_users = User.objects.filter(email__endswith='@platzi.com')
for u in platzi_users:
    print(u.email, ':', u.is_admin)


# use auth django
from django.contrib.auth.models import User
u = User.objects.create_user(username='yesika', password='admin123')
u.password
# >>> 'pbkdf2_sha256$180000$UVZBVWdfHsgd$VZWxPalxWT1JfckT7SVrhRUI24iEZJ5ZQ1MmbTLl5Qg='
# pass key derivation function sha256 con 180 mil iteracion y el secret_key de la app



