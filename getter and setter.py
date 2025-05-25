'''
Getter -> Getter in python are the method that is used to access the values of an objects properties
they are used to return the value of a specific property,and are typically define using the @property decorator.'''
class Myclass:
    def __init__(self,value):
        self._value=value
    def show(self):
        print(f"The value is:{self._value}")
        # Getters 
    @property
    def ten_value(self):
        return 10*self._value
    '''Setters-> It is importent to note that the getters do not take any arguments and we can't set the value through getter method
    For that we need setter method which can be added by decorating method with @property_name.setter
'''
        # Setters
    @ten_value.setter
    def ten_value(self,new_value):
        self._value=new_value/10
obj = Myclass(10)
obj.ten_value=67
print(obj.ten_value)
obj.show()