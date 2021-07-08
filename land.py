
class Land:
    """  """
    def __init__(self):
        self.coordinate_of_person = {}

    def add_person(self, person, coordinate):
        self.coordinate_of_person[person] = coordinate

    def move_person(self, person):
        delta_x, delta_y = person.walk()
        actual_coordinate = self.coordinate_of_person[person]
        new_coordinate = actual_coordinate.move(delta_x, delta_y)

        self.coordinate_of_person[person] = new_coordinate

    def get_coordinate(self, person):
        return self.coordinate_of_person[person]
