# Day 25 of Advent of code 2018

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a, b))


def common_star(a, b):
    list_one = set(a)
    list_two = set(b)
    return True if list_one & list_two else False


def day25():
    all_constellations_list = []
    found_constellation_for_curr_star = False

    with open("input_day25", "r") as file:
        lines = file.readlines()
        for line in lines:
            if line == '\n':
                break
            line = line[:-1]
            curr_star = line.split(',')
            curr_star = [int(x) for x in curr_star]

            if len(all_constellations_list) == 0:
                new_constellation = [curr_star]
                all_constellations_list.append(new_constellation)
                continue

            for i, constellation in enumerate(all_constellations_list):
                for point in constellation:
                    distance = manhattan(point, curr_star)
                    if distance <= 3:
                        if found_constellation_for_curr_star and (all_constellations_list[found_const_num] != constellation):
                            for s in constellation:
                                all_constellations_list[found_const_num].append(s)
                            all_constellations_list.remove(constellation)
                        else:
                            constellation.append(curr_star)
                            found_constellation_for_curr_star = True
                            found_const_num = i
                        break

            if not found_constellation_for_curr_star:
                new_constellation = [curr_star]
                all_constellations_list.append(new_constellation)
            found_constellation_for_curr_star = False

        print("Number of constellations is: " + str(len(all_constellations_list)))


if __name__ == "__main__":
    day25()
