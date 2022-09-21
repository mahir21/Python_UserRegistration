#Building a basic sign in and sign up page using python data

print("sign up user form data")
UserName = input('Enter UserName')
Password = input('Enter Password')

print("Enter Account Details")
UserName2 = input('Enter UserName2')
Password2  = input('Enter Password')

if( (UserName == UserName2)  & (Password == Password2)):
  print('User Has Succesfully Login')
else:
  print('User Denied Access Try Again')
