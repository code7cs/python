# def greet(name, time):
#     print(f'Good {time} {name}, hope you are well')
#
#
# greet('Hanfan', 'morning')
#
#
# def area(radius):
#     return 3.142 * radius * radius
#
#
# def vol(area, length):
#     print(area * length)
#
#
# radius = int(input("enter a radius: "))
# length = int(input("enter a length: "))
#
# vol(area(radius), length)

#
# myname = 'james'
#
# def print_myname():
#     global myname
#     myname = 'hanfan'
#     print("the name inside the functino is", myname)
#
# print_myname()
# print("the name outside the function is", myname)


# person = dict(name='hanfan', age='22', height='6ft')
# print(person)


def belt_counts(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'there are {num} {belt} belts')


hanfan_belts = {}

while True:
    hanfan_name = input("enter a name:")
    hanfan_belt = input("enter a belt color:")
    hanfan_belts[hanfan_name] = hanfan_belt

    if (input("enter another? (y/n)") == 'y'):
        continue
    else:
        break

#
# def hanfan_intro(dictionary):
#     for key, val in dictionary.items():
#         print(f'I am {key}, and I am a {val} belt')

# hanfan_intro(hanfan_blets)
belt_counts(hanfan_belts)
