
from coordinate import Coordinate
from land import Land


def walking(land, person, steps):
    """  """
    beginning = land.get_coordinate(person)

    for _ in range(steps):
        land.move_person(person)

    return beginning.distance(land.get_coordinate(person))
