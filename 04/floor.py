from desk import Desk
import enum


class Floor_Type(enum.Enum):
    Free = "free"
    Special = "special"


class Floor_Entrance_Price:
    entrance_prices = []

    def __init__(self):
        self.entrance_prices = []

    def get_price(self, floor_type):
        for type, value in self.entrance_prices:
            if type == floor_type:
                return value

    def add(self, floor_type, value):
        index = self.__is_exists(floor_type)
        if index is not None:
            self.__change_value(index, value)
        else:
            self.entrance_prices.append([floor_type, value])

    def __is_exists(self, floor_type):
        for i in range(len(self.entrance_prices)):
            if self.entrance_prices[i][0] == floor_type:
                return i

        return None

    def __change_value(self, index, value):
        self.entrance_prices[index][1] = value


class Floor:
    id = None
    desks = []
    type = None

    def __init__(self, id, type):
        self.id = id
        self.type = type
        self.desks = []

    def add_desks_by_features(self, desks_features):
        last_desk_id = self.desks[-1].id if len(self.desks) else 0
        for i in range(len(desks_features)):
            desk = Desk(last_desk_id + 1 + i, desks_features[i])
            self.desks.append(desk)

    def request_desk(self, owner, time_range, features):
        for desk in self.desks:
            desk_id, desk_features = desk.request(owner, time_range, features)
            if desk_id is not None:
                return desk_id, desk_features

        return None, None

    def display_desks(self):
        for desk in self.desks:
            print("\t", desk)

    def __str__(self):
        return f"FLOOR-> Id: {self.id} - Type: {self.type} - Number of Desks: {len(self.desks)}"
