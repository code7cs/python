grades = ['a', 'b', 'c', 'f', 'c', 'f', 'a']


def remove_failed(grade):
    return grade != 'f'


# filter
print(list(filter(remove_failed, grades)))


# normal
filter_grade = []
for grade in grades:
    if grade != 'f':
        filter_grade.append(grade)
print (filter_grade)

# comprehension
print ([grade for grade in grades if grade != 'f' ])
