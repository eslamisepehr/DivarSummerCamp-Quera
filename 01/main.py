from building import Building
from command_parser import Command_Parser

building = Building()

number_of_floors = int(input())
for i in range(number_of_floors):
    number_of_desks = int(input())
    building.add_floors_with_desks(number_of_desks)

command_parser = Command_Parser()

outputs = []
while True:
    command = input()
    if command_parser.is_finished(command):
        break

    username, time_range = command_parser.request_desk_command_parser(command)
    response = building.request_desk(username, time_range)
    outputs.append(response)

print("\n".join(outputs))
