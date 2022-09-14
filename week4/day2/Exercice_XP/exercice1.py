# Create a set called my_fav_numbers with all your favorites numbers.
my_fav_numbers = {1,2,3,4,5}
# Add two new numbers to the set.
my_fav_numbers.add(11)
my_fav_numbers.add(13)
my_fav_numbers.add(15)
print(my_fav_numbers)
# Remove the last number.
my_fav_numbers.remove(15)
print(my_fav_numbers)
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
friend_fav_numbers =  {'allasane','naouratou','hadama'}
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called
friend=friend_fav_numbers.union(my_fav_numbers)

print(friend)
