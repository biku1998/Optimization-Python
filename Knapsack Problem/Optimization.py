
# importing the Food Module
from Food import Food

# this module will build menu using the Food class
def build_menu(names = [] , values = [] , calories = []):
        """ This Method Will build Food Menu using the Food module
        
        Param : name  : Food name list,
                values  : value list 
                calories : list of food calories

        returns : A Menu Prepared from the food Provided
        """
        menu  = list()
        for i in range(len(values)):

            menu.append(Food(names[i],values[i],calories[i]))


        return menu

# implementing the greedy algo :

def greedy(items , maxCost , keyFunction):
    """
    param : 
        items : food menu 
        maxCost : my max cost to get the items
        keyFunction  :  this Funtion Will tell you what good
        means in knapsack problem.
    """
    # items is list offcourse 
    # now creating a copy of items 

    itemsCopy = sorted(items , key = keyFunction, reverse = True)

    result = list()

    totalValue , totalCost = 0.0 , 0.0

    for i in range(len(itemsCopy)):

        if(totalCost + itemsCopy[i].get_cost()) <= maxCost:
            result.append(itemsCopy[i])

            totalCost += itemsCopy[i].get_cost()
            totalValue += itemsCopy[i].get_value()

    return result , totalValue

def testGreedy(items, constraint, keyFunction):
    # this function will test the grredy module
    taken , val = greedy(items,constraint,keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print('   ',item)


def testGreedys(foods,maxUnits):
    # This module will test testGreedy Module

    print('Use Greedy by Value to allocate ',maxUnits,'calories')

    testGreedy(foods,maxUnits,Food.get_value)

    print('\nUse Greedy by cost to allocate ',maxUnits,'calories')

    testGreedy(foods,maxUnits,lambda x : 1/Food.get_cost(x))
    # testGreedy(foods,maxUnits,lambda x : Food.get_cost(x))


    print('\nUse Greedy by density to allocate ',maxUnits,'calories')

    testGreedy(foods,maxUnits,Food.density)



# main Function 
def main():
    # main function code
    names = ['wine', 'beer', 'pizza', 'burger', 'fries','cola', 'apple', 'donut', 'cake']
    values = [89,90,95,100,90,79,50,10]
    calories = [123,154,258,354,365,150,95,195]
    foods = build_menu(names,values,calories)
    testGreedys(foods,750)

# calling the main function when the code will run 
if __name__  ==  "__main__":

    main()
