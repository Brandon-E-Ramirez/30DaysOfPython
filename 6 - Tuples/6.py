# Exercises: Level 1

#     Create an empty tuple
empty_tuple = ();

#     Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sis = ("Blanca", "Lesli"); 
bro = ("Juan", "Giovanni", "Jesus");


#     Join brothers and sisters tuples and assign it to siblings
siblings = sis + bro;
#     How many siblings do you have?
print(len(siblings));

#     Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ("Felipe", "Maria");
print(family_members)
# Exercises: Level 2

#     Unpack siblings and parents from family_members
siblings = family_members[0:5];
parents = family_members[5:];

print(siblings)
print(parents)

#     Create fruits, vegetables and animal products tuples. Join the three tuples and assign it 
# to a variable called food_stuff_tp.
fruits = ("Apple", "Banana", "Orange");
vegetables = ("Carrot", "Potato", "Tomato");
animal_products = ("Cat", "Dog", "Lion");
food_stuff_tp = fruits + vegetables + animal_products;
#     Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp);
#     Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = food_stuff_tp[int(len(food_stuff_tp)/2)];
print(middle);
#     Slice out the first three items and the last three items from food_staff_lt list
extra = food_stuff_lt[0:3] + food_stuff_lt[-3:];
print(extra);
#     Delete the food_staff_tp tuple completely
del food_stuff_tp
#     Check if an item exists in tuple:
vg_companies = ('Sony', 'Nintendo', 'Id', 'Valve', 'Microsoft');
nin = 'Nintendo' in vg_companies
print(nin)


#     nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')


#     Check if 'Estonia' is a nordic country

#     Check if 'Iceland' is a nordic country