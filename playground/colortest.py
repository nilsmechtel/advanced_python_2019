
def find_black_spots(list_of_intensities):

    min_value = 0
    list_of_black_spots = []
    for pos, element in enumerate(list_of_intensities):
        if pos == 0:
            continue
        if pos == len(list_of_intensities) - 1:
            continue
        if sum(list_of_intensities[pos - 1]) > sum(element) < sum(list_of_intensities[pos + 1]):
            list_of_black_spots.append(pos)
    return list_of_black_spots
