
from coordinate import Coordinate
from walking import walking
from land import Land


def walking_simulation(steps, number_of_attemps, type_of_person):
    """  """
    person = type_of_person(name="Sergio")
    origin = Coordinate(0, 0)
    distances = []

    for _ in range(number_of_attemps):
        land = Land()
        land.add_person(person, origin)
        simulation = walking(land, person, steps)
        distances.append(round(simulation, 1))

    return distances
