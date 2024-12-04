blog_posts = ["", "The coolest math functions in python", "", "How to make HTTP requests in Pyhton", " A tutorial about data"]

for post in blog_posts:
    if post == "":
        continue
else:
    print(post)

print("---------------------------------------")

myString = ("This is my string")

for char in myString:
    print(char)

print("---------------------------------------")


for x in range(0,10):
    print(x)


print("---------------------------------------")

person = {'Namme': 'Karen Hall', 'Age':42, 'Gender': 'Female'}

for key in person:
    print(key, ':', person[key])

print("---------------------------------------")
print("Dictonaries, not list")
print("---------------------------------------")



blog_posts = {"Python": ["The coolest math functions in python", "How to make HTTP requests in Pyhton", " A tutorial about data"], "Javascript": ["Namespace in Javascript","Loops and booleans in Javascript"]}
for category in blog_posts:
     print("Posts about", category)
     for post in blog_posts[category]:
         print(post)
