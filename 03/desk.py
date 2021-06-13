class Desk:
    id = None
    owner = None
    time_ranges = []

    def __init__(self, id):
        self.id = id
        self.owner = None
        self.time_ranges = []

    def request(self, owner, time_range):
        if self.__is_overlap_with(time_range):
            return None

        self.owner = owner
        self.time_ranges.append(time_range)
        return self.id

    def __is_overlap_with(self, time_range):
        for reserved_time_range in self.time_ranges:
            if reserved_time_range.stop > time_range.start and time_range.stop > reserved_time_range.start:
                return True

        return False

    def __str__(self):
        return f"DESK-> Id: {self.id} - Owner: {self.owner}"
