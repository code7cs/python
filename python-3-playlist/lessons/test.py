from classes import Planet

naboo = Planet('Naboo', 500, 8.8, 'Naboo system')
print (f'Name is: {naboo.name}')
print (f'Radius is: {naboo.radius}')
print (f'Gravity is: {naboo.gravity}')
print (naboo.spin('a very high speed'))
