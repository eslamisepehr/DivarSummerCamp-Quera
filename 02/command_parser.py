from floor import Floor_Type


class Command_Parser():

    def is_finished(self, command):
        if command == "end":
            return True

        return False

    # input:    <timestamp> request_desk <username> <floor_type> <duration>
    # output:   username, floor_type, time_range
    def request_desk_command_parser(self, command):
        command = command.split()

        start_time = int(command[0])
        end_time = start_time + int(command[4])

        return command[2], Floor_Type(command[3]), range(start_time, end_time)
