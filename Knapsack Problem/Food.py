


# Knapsack problem

# Solving the knapsack problem :

# Food Class

class Food(object):

    def __init__(self,name,value,calorie):

        self.name = name

        self.value = value

        self.calorie = calorie


    def get_value(self):
        return self.value

    def get_cost(self):
        return self.calorie

    def density(self):
        return self.get_value() / self.get_cost()

    def __str__(self):
        return self.name + ': < '+str(self.value)+' , '+str(self.calorie)+' >'


