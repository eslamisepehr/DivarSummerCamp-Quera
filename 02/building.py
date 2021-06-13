from floor import Floor, Floor_Type, Floor_Entrance_Price


class Building:
    floors = []
    floor_entrance_price = None

    def __init__(self):
        self.floors = []
        self.floor_entrance_price = Floor_Entrance_Price()

    def add_floors_with_desks(self, floor_type, number_of_desks):
        last_floor_id = self.floors[-1].id if len(self.floors) else 0
        floor = Floor(last_floor_id + 1, floor_type)
        floor.add_desks(number_of_desks)
        self.floors.append(floor)

    def request_desk(self, username, floor_type, time_range):
        for floor in self.floors:
            if floor.type is not floor_type:
                continue

            desk_id = floor.request_desk(username, time_range)
            if desk_id is not None:
                result = f"{username} got desk {floor.id}-{desk_id}"

                if floor.type == Floor_Type.Special:
                    price = self.calculate_desk_price(floor.type)
                    result += f" for {price}"

                return result

        return f"no desk available"

    def add_entrance_price(self, floor_type, value):
        self.floor_entrance_price.add(floor_type, value)

    def calculate_desk_price(self, floor_type):
        return self.floor_entrance_price.get_price(floor_type)

    def display_floors_with_desks(self):
        for floor in self.floors:
            print(floor)
            floor.display_desks()

    def __str__(self):
        return f"BUILDING-> Number of Floors: {len(self.floors)}"
