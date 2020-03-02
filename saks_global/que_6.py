
import itertools
#This itertools library use for return combination what we need  
class FindTheThreeElementsSumEqualToZero:
      
  def get_all_three_combination_with_sum_zero(self, number_list=None):
    # Here I have created list to append, three element combination equal to zero
    sum_zero_combination = []
    data = itertools.combinations(number_list, 3)

    for item in data:
      # Here I have check sum of the combination
      sum_value = sum(item)
      if sum_value==0:
        # the combination sum equal to zero then append before we created list
        sum_zero_combination.append(item)
    return sum_zero_combination

# here I have testing given sample  
input_number_list = [-25, -10, -7, -3, 2, 4, 8, 10] 
object_name = FindTheThreeElementsSumEqualToZero()
return_list = object_name.get_all_three_combination_with_sum_zero(input_number_list)

print (return_list)
# output
# [(-10, 2, 8), (-7, -3, 10)]