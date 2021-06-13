from desk import Desk


class Floor:
    id = None
    desks = []

    def __init__(self, id):
        self.id = id
        self.desks = []

    def add_desks(self, number_of_desk):
        last_desk_id = self.desks[-1].id if len(self.desks) else 0
        for id in range(last_desk_id, number_of_desk):
            desk = Desk(id + 1)
            self.desks.append(desk)

    def request_desk(self, owner, time_range):
        for desk in self.desks:
            desk_id = desk.request(owner, time_range)
            if desk_id is not None:
                return desk_id

        return None

    def display_desks(self):
        for desk in self.desks:
            print("\t", desk)

    def __str__(self):
        return f"FLOOR-> Id: {self.id} - Number of Desks: {len(self.desks)}"
