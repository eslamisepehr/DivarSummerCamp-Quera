class Command_Parser():

    def is_finished(self, command):
        if command == "end":
            return True

        return False

    # input:    <timestamp> request_desk <username> <duration>
    # output:   username, time_range
    def request_desk_command_parser(self, command):
        command = command.split()

        start_time = int(command[0])
        end_time = start_time + int(command[3])

        return command[2], range(start_time, end_time)
