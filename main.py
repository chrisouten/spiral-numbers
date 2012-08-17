import math
import sys

def main():
    spiral_number = None
    
    #Keep getting input until they give us the correct input or exit
    while spiral_number is None:
        #Get the input, check if they want to quit 
        input = raw_input("Please enter a number to spiral (q to quit): ")
        if input.strip().lower() == 'q':
            sys.exit()
            
        #For formatting purposes we need to see how many digits this number is
        justify_spaces = len(input.strip())
        try:
            spiral_number = int(input)
        except ValueError:
            print "You must enter a positive integer value"
    
    #Get the size of the array needed for the spiral
    array_size = int(math.ceil(math.sqrt(spiral_number + 1))) + 1
    #Get the starting position for the zero
    starting_position = array_size / 2
    
    #Set up a list of directions with x,y change values
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    #We always go left first so set the active direction to left
    active_direction = 0
    #So this is a mapping for active direction to the next direction to go
    # i.e. left goes down, down goes right, right goes up, up goes left
    direction_check_empty = {0:1, 1:2, 2:3, 3:0}
    
    #Set up a empty list and initialize our 2d array
    spiral = []
    for x in range(array_size):
        row = []
        for y in range(array_size):
            #Adding some empty spaces that are formatted
            row.append(''.join([' ' for space in range(justify_spaces)]))
        spiral.append(row)

    # Get our start going    
    x,y = starting_position, starting_position
    # We justify the number for formatting
    spiral[x][y] = ('%d' % 0).rjust(justify_spaces)
    
    # Start our trek around the spiral
    x = x + directions[active_direction][0]
    y = y + directions[active_direction][1]
    
    for val in range(1,spiral_number + 1):
        spiral[x][y] = ('%d' % val).rjust(justify_spaces)
        
        # Get the location for checking to see if we need to change directions
        x2 = x + directions[direction_check_empty[active_direction]][0]
        y2 = y + directions[direction_check_empty[active_direction]][1]
        
        # Check to see if its blank
        # if it's blank we change the active direction, set up the x,y
        # otherwise we keep on going with the current direction
        if not spiral[x2][y2].strip():
            x = x2
            y = y2
            if active_direction == 3:
                active_direction = 0
            else:
                active_direction = active_direction + 1
        else:
            x = x + directions[active_direction][0]
            y = y + directions[active_direction][1]
        
    # Now it's time to print our spiral
    for a in spiral:
        print ' '.join(a)
        
        

if __name__ == '__main__':
    main()