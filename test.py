
# List of lists
cars_list = [[1,'Honda','red'], [2,'Toyota','white'], [3,'Mazda','blue']]
# Output dictionary
cars_dict = {}
 
# Convert to dictionary
for key, car, color in cars_list:
    cars_dict[key] = [car, color]
 
# Print to see output
print (cars_dict)
print (cars_dict[1])