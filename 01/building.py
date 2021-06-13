from floor import Floor


class Building:
    floors = []

    def __init__(self):
        self.floors = []

    def add_floors_with_desks(self, number_of_desks):
        last_floor_id = self.floors[-1].id if len(self.floors) else 0
        floor = Floor(last_floor_id + 1)
        floor.add_desks(number_of_desks)
        self.floors.append(floor)

    def request_desk(self, username, time_range):
        for floor in self.floors:
            desk_id = floor.request_desk(username, time_range)
            if desk_id is not None:
                return f"{username} got desk {floor.id}-{desk_id}"

        return f"no desk available"

    def display_floors_with_desks(self):
        for floor in self.floors:
            print(floor)
            floor.display_desks()

    def __str__(self):
        return f"BUILDING-> Number of Floors: {len(self.floors)}"
