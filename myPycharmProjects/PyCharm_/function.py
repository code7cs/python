# def get_formatted_name(first_name, last_name, middle_name=' '):
#     """return full name"""
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
#
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)
#
#
# print("---------------------")
#
#
# def build_person(first_name, last_name, age=''):
#     """返回一个字典，其中包含有关一个人的信息"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
#
# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)
#

#
# def greet_users(names):
#
#     """向列表中的每位用户都发出简单的问候"""
#
#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)
#
#
# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)


# def print_models(unprinted_designs, completed_models):
#     """模拟打印每个设计，直到没有未打印的设计为止 打印每个设计后，都将其移到列表completed_models中"""
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         # 模拟根据设计制作3D打印模型的过程
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     """显示打印好的所有模型"""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
#
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)


# def make_pizza(size, *toppings):
#     # """打印顾客点的所有配料"""
#     """概述要制作的比萨"""
#     print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
#
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}

    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
