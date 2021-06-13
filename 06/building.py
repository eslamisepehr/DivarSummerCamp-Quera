from floor import Floor, Floor_Type, Floor_Entrance_Price
from desk import Desk_Feature_Price


class Building:
    floors = []
    floor_entrance_price = None
    desk_features_price = None

    def __init__(self):
        self.floors = []
        self.floor_entrance_price = Floor_Entrance_Price()
        self.desk_features_price = Desk_Feature_Price()

    def add_floors_with_desks(self, floor_type, desks_features):
        last_floor_id = self.floors[-1].id if len(self.floors) else 0
        floor = Floor(last_floor_id + 1, floor_type)
        floor.add_desks_by_features(desks_features)
        self.floors.append(floor)

    def request_desk(self, username, floor_type, time_range):
        for floor in self.floors:
            if floor.type is not floor_type:
                continue

            desk_id, desk_features = floor.request_desk(username, time_range, None)
            if desk_id is not None:
                price = self.calculate_desk_price(floor.type, time_range, desk_features)
                result = f"{username} got desk {floor.id}-{desk_id} for {price}"

                return result

        return f"no desk available"

    def reserve_desk(self, username, time_range, features):
        for floor in self.floors:
            if floor.type is not Floor_Type.Special:
                continue

            desk_id, desk_features = floor.request_desk(username, time_range, features)
            if desk_id is not None:
                price = self.calculate_desk_price(floor.type, time_range, desk_features)
                result = f"{username} reserved desk {floor.id}-{desk_id} for {price}"

                return result

        return f"no desk available"

    def reserve_multiple_desks(self, username, time_range, number_of_desks):
        results = []

        for floor in self.floors:
            if floor.type is not Floor_Type.Special:
                continue

            available_desks = floor.get_available_desks(time_range, [])

            if len(available_desks) != number_of_desks:
                results = []
                continue

            for i in range(len(available_desks)):
                desk_id, desk_features = floor.request_specific_desk(available_desks[i], username, time_range, None)
                if desk_id is not None:
                    price = self.calculate_desk_price(floor.type, time_range, desk_features)
                    results.append([desk_id, price])

            break

        if len(results) == number_of_desks:
            total = 0
            result = f"{username} reserved desks "
            for i in range(len(results)):
                total += results[i][1]
                result += f"{floor.id}-{results[i][0]}"
                if len(result) > i:
                    result += " "

            result += f"for {total}"
            return result

        return f"not enough desks available"

    def get_desk_status_by_id(self, timestamp, floor_id, desk_id):
        for floor in self.floors:
            if floor.id != floor_id:
                continue

            return floor.get_desk_status(timestamp, desk_id)

        return "desk not found"

    def add_entrance_price(self, floor_type, value):
        self.floor_entrance_price.add(floor_type, value)

    def add_desk_features_price(self, values):
        self.desk_features_price.multiple_add(values)

    def calculate_desk_price(self, floor_type, time_range, desk_features):
        total = 0

        if desk_features is not None:
            for i in range(len(desk_features)):
                if desk_features[i] == "1":
                    total += self.desk_features_price.get_price(i)

        total *= self.calculate_duration(time_range)
        total += self.floor_entrance_price.get_price(floor_type)

        return total

    def calculate_duration(self, time_range):
        return time_range.stop - time_range.start

    def display_floors_with_desks(self):
        for floor in self.floors:
            print(floor)
            floor.display_desks()

    def __str__(self):
        return f"BUILDING-> Number of Floors: {len(self.floors)}"
