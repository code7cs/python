class Planet:

    shape = 'round'

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

    @classmethod
    def commons(cls):
        return f'All planets have {cls.shape} because of gravity'

    @staticmethod
    def spin(speed='2000 miles per hour'):
        return f'The planet spins and spins at {speed}'


# create a new instance of this class
hf = Planet('Hanfan', 200, 5.5, 'Hanfan system')

print (f'Name is: {hf.name}')
print (f'Radius is: {hf.radius}')
print (f'Gravity is: {hf.gravity}')

# orbit() is instance method, which is only has to be from the instance
print (hf.orbit())
print (Planet.shape)

# commons() is class method, can be accessed by Planet (can be used on the class itself)
print (Planet.commons())
print (hf.commons())

# spin() is static method, can be accessed by Planet (can be used on the class itself)
print (Planet.spin('a very high speed'))
print (hf.spin('a very high speed'))
