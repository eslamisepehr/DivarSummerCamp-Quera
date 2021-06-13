class Desk_Feature_Price:
    features_price = []

    def add(self, value):
        self.features_price.append(value)

    def multiple_add(self, values):
        self.features_price.extend(values)

    def get_price(self, index):
        return self.features_price[index]


class Desk:
    id = None
    owner = None
    time_ranges = []
    features = None

    def __init__(self, id, features):
        self.id = id
        self.features = features
        self.owner = None
        self.time_ranges = []

    def request(self, owner, time_range, features):
        if self.__is_overlap_with(time_range):
            return None, None

        if features is not None and self.features != features:
            return None, None

        self.owner = owner
        self.time_ranges.append(time_range)
        return self.id, self.features

    def is_request_available(self, time_range, features):
        if self.__is_overlap_with(time_range):
            return None, None

        if features is not None and self.features != features:
            return None, None

        return self.id, self.features


    def __is_overlap_with(self, time_range):
        for reserved_time_range in self.time_ranges:
            if reserved_time_range.stop > time_range.start and time_range.stop > reserved_time_range.start:
                return True

        return False

    def __str__(self):
        return f"DESK-> Id: {self.id} - Owner: {self.owner} - Features: {self.features}"
