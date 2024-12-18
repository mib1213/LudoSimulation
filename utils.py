positions = [0, 0, 0, 0]
index = 0
dice = 1

def moving_figure(positions, dice, index):
    #needed parameters: positions, dice, index

    """Here the function will later be explained."""

    if (positions[index] + dice) <= 44:
        positions[index] += dice

        #Determine wether a figure has to get kicked out

        for x in positions:

            if x == index:
                
                continue

            diff = abs(positions[index] - x)

            modulo_index = positions[index] % diff
            modulo_x = positions[x] % diff

            floor_division_index = positions[index] // diff
            floor_division_x = positions[x] // diff

            if modulo_index == modulo_x:
                if abs(floor_division_index - floor_division_x) == modulo_index:
                    positions[x] = 0




    