# imports functions
from functionality import *
print(add(10,20))
print(mul(10,20))

# imports module second
from other_package import second
second.my_function()

# imports function of module second
from other_package.second import *
my_function()

# imports package other_modules, modules of package are defined in __init__.py
from other_package import *
third.another_function()

# imports module of sub package
from other_package.sub_package import fourth
fourth.fourth_function()

# imports function from module of sub package
from other_package.sub_package.fourth import fourth_function
fourth_function()

from functionality import myclass
myclass