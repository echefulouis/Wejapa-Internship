#Quiz: Calculate
#In this quiz you're going to do some calculations for a tiler. Two parts of a floor need tiling. One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. Tiles come in packages of 6.

#1. How many tiles are needed?
#2. You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?




# Fill this in with an expression that calculates how many tiles7 are needed.
first_floor=9*7
second_floor=5*7
total_tiles_used=first_floor+second_floor
print("Total tiles needed",total_tiles_used)

# Fill this in with an expression that calculates how many tiles will be left over.
total_tiles_bought=17*6
print('Total tiles remaining',(total_tiles_bought-total_tiles_used))