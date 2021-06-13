class Desk:
    id = None
    owner = None
    time_range = None

    def __init__(self, id):
        self.id = id
        self.owner = None

    def request(self, owner, time_range):
        if self.__is_overlap_with(time_range):
            return None

        self.owner = owner
        self.time_range = time_range
        return self.id

    def __is_overlap_with(self, time_range):
        if self.time_range is None:
            return False

        return self.time_range.stop > time_range.start and time_range.stop > self.time_range.start

    def __str__(self):
        return f"DESK-> Id: {self.id} - Owner: {self.owner}"
