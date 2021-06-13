from floor import Floor_Type


class Command_Parser():

    def is_finished(self, command):
        if command == "end":
            return True

        return False

    def is_request_desk_command(self, command):
        return command.split()[1] == "request_desk"

    def is_reserve_desk_command(self, command):
        return command.split()[1] == "reserve_desk"

    def is_reserve_multiple_desks_command(self, command):
        return command.split()[1] == "reserve_multiple_desks"

    def is_desk_status_command(self, command):
        return command.split()[1] == "desk_status"

    # input:    <timestamp> request_desk <username> <floor_type> <duration>
    # output:   username, floor_type, time_range
    def request_desk_command_parser(self, command):
        command = command.split()

        start_time = int(command[0])
        end_time = start_time + int(command[4])

        return command[2], Floor_Type(command[3]), range(start_time, end_time)

    # input:    <timestamp> reserve_desk <username> <from_time> <duration> <feature_code>
    # output:   username, time_range, features
    def reserve_desk_command_parser(self, command):
        command = command.split()

        start_time = int(command[3])
        end_time = start_time + int(command[4])

        return command[2], range(start_time, end_time), command[5]

    def desk_features_command_parser(self, command):
        return list(map(int, command.split()))

    # input:    <timestamp> reserve_multiple_desks <username> <number of desks> <from_time> <duration>
    # output:   username, time_range, number_of_desks
    def reserve_multiple_desks_command_parser(self, command):
        command = command.split()

        number_of_desks = int(command[3])

        start_time = int(command[4])
        end_time = start_time + int(command[5])

        return command[2], range(start_time, end_time), number_of_desks

    # input:    <timestamp> desk_status <desk_id>
    # output:   timestamp, floor_id, desk_id
    def desk_status_command_parser(self, command):
        command = command.split()

        floor_id, desk_id = map(int, command[2].split("-"))

        return int(command[0]), floor_id, desk_id