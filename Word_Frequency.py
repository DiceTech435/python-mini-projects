from collections import Counter
from operator import itemgetter

# Word Frequency / Most occured words
sentence = "This project demonstrates key Object-Oriented Programming (OOP) principles with practical examples. The goal is to provide a clear reference for concepts like classes, inheritance, abstraction, int…" \
           "This project demonstrates the implementation of a Dark Mode and Light Mode theme switcher in a web application using Laravel Mix and SASS. The goal is to enhance user experience by allowing seamles…" \
           "This project implements a simple yet powerful like/unlike system that allows users to interact with posts dynamically. It focuses on database-driven functionality, AJAX for real-time updates, and a…"

shop = sentence.split()
words = Counter(shop)
top = words.most_common(3)
print(top)


# Sorting Items
users = [
    {"Fname": "Jesse", "Lname": "Kandi"},
    {"Fname": "Sam", "Lname": "Joe"},
    {"Fname": "Tom", "Lname": "Andrew"},
    {"Fname": "Tom", "Lname": "King"},
    {"Fname": "Tom", "Lname": "English"}
]

for i in sorted(users, key=itemgetter("Fname")):
    print(i)

print("------------------------------------")
for i in sorted(users, key=itemgetter("Fname", "Lname")):
    print(i)