# Write a python programme that accepts all lowercase  strings to uppercase

def response(text):
    z = text.upper()
    print(z)

text = "I love coding"
response(text)

#Write a python function that counts all the vowels and consonats.

def count(val):
    vov = 0
    con = 0
    for i in range(len(val)):
        if val[i] in ['a','e','i','o','u']:
            vov = vov+1
        else:
            con = con + 1

    print("Count of vowels is ",vov)
    print("Count of consonant is ",con)

x = "Education"
count(x)


#Write a python function that accepts the radius of circle as 
# parameter and returns the radius of the circle.

def area(radius):
    area = 3.14*radius*radius
    return area

radius = int(input("4")) 
print(area(radius))



