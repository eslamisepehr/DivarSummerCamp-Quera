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

    # input:    <timestamp> request_desk <username> <floor_type> <duration>
    # output:   username, floor_type, time_range
    def request_desk_command_parser(self, command):
        command = command.split()

        start_time = int(command[0])
        end_time = start_time + int(command[4])

        return command[2], Floor_Type(command[3]), range(start_time, end_time)

    # input:    <timestamp> reserve_desk <username> <from_time> <duration>
    # output:   username, time_range
    def reserve_desk_command_parser(self, command):
        command = command.split()

        start_time = int(command[3])
        end_time = start_time + int(command[4])

        return command[2], range(start_time, end_time)
