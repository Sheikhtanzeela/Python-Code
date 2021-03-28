# Python OOP

# INSTANCE VARIABLES

# I V should be unique to each instance
class Employee:

    raise_amount = 1.04
    num_of_emps = 0
    
    def __init__(self,first,last,pay):
       self.first = first
       self.last = last
       self.pay = pay
       self.email = first + '_' + last + '@company.com'

       Employee.num_of_emps += 1

       
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod 
    def set_raise_amt(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last,pay = emp_str.split('-')
        return cls(first , last, pay)


    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User',90000)


import datetime
my_date = datetime.date(2016,7,11)
print(Employee.is_workday(my_date))

emp_str_1 = 'John-Doe-50000'
emp_str_1 = 'Harr-Doe-90000'
emp_str_1 = 'Poert-sam-70000'

new_emp_1 = Employee.from_string(emp_str_1) 

#print(new_emp_1.email)
#print(new_emp_1.pay)


Employee.set_raise_amt(1.05)

#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)






print(Employee.num_of_emps)

#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)

#Employee.raise_amount = 1.05
#emp_1.raise_amount= 1.05

#print(emp_1.__dict__)
#print(Employee.__dict__)





#print(emp_1)
#print(emp_2)


#print(emp_1.email)
#print(emp_2.email)


#print(Employee.fullname(emp_1))


#print( emp_1.fullname())
#print( emp_2.fullname())


# CLASS VARIABLES

# class variables are the variables that are shared among all the
# instances of class
