
from walking_simulation import walking_simulation
from person import TraditionalPerson
from graph import graph


def main(walking_distance, number_of_attemps, type_of_person):
    """  """
    average_distance_x_walk = []

    for steps in walking_distance:

        distances = walking_simulation(steps, number_of_attemps, type_of_person)
        average_distance = round(sum(distances) / len(distances), 4)
        max_distance = max(distances)
        min_distance = min(distances)
        average_distance_x_walk.append(average_distance)

        print(f"\n{type_of_person.__name__} random walking of {steps} steps")
        print(f"Middle distance = {average_distance}")
        print(f"Max distance = {max_distance}")
        print(f"Min distance = {min_distance}")

    graph(walking_distance, average_distance_x_walk)


if __name__ == "__main__":
    walking_distance = [10, 100, 1000, 100000]
    number_of_attemps = 100

    main(walking_distance, number_of_attemps, TraditionalPerson)
