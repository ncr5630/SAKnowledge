#given number list
number_list = [5, 8, -1, 2, 2, -7, 4, 0, -4]

# sorting the list 
number_list.sort() 

#print the given list after sort accending 
print("sorted list accending:",number_list)

#positive number list
positive_numbers=[]

for item in number_list:
  # check item value is positive or zero
  if item>=0:
    # append positive values to positive_numbers list
    positive_numbers.append(item)
# print positive number list
print("After remove negative values: ",positive_numbers)

