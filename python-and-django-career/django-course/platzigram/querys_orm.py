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

pu = User.objects.filter(email__endswith='@platzi.com').update(is_admin=True)


