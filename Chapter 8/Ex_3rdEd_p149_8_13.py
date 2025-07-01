def build_profile(first, last, **user_info):
 """Build a dictionary containing everything we know about a user."""
 user_info['first_name'] = first.title()
 user_info['last_name'] = last.title()
 return user_info

user_profile = build_profile('welile', 'zambodla', gender='male', height='170cm', weight='68kg')
print(user_profile)