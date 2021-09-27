#
# Michael Salzarulo
#
# restaurant.py
#
# Restaurant bill generator with tax and tip included.
#

def main():

    print('Restaurant Bill Generator ...\n')

    food_cost = float(input('Please enter cost of food:   '))
    drinks_cost = float(input('  "      "   cost of drinks: '))
    
    total = food_cost + drinks_cost
    tax = total * 0.75
    tip = total * .18
    final_total = total + tax + tip
    
    print('\nRestaurant Bill\n--------------------------------\n\nCost of Meal:           $', (food_cost + drinks_cost))
    print('Tax Amount:             $', format(tax, '.2f'), '\nTip Amount:             $', format(tip, '.2f'), '\n                        --------')
    print('Total:                  $', format(final_total, '.2f'))
    
main()
