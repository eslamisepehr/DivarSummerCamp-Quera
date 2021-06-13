from building import Building
from command_parser import Command_Parser
from floor import Floor_Type

building = Building()

number_of_floors, special_floor_entrance_price = map(int, input().split())

building.add_entrance_price(Floor_Type.Free, 0)
building.add_entrance_price(Floor_Type.Special, special_floor_entrance_price)

for i in range(number_of_floors):
    number_of_desks, floor_type = input().split()
    building.add_floors_with_desks(Floor_Type(floor_type), int(number_of_desks))

command_parser = Command_Parser()

outputs = []
while True:
    command = input()
    if command_parser.is_finished(command):
        break

    username, floor_type, time_range = command_parser.request_desk_command_parser(command)
    response = building.request_desk(username, floor_type, time_range)
    outputs.append(response)

print("\n".join(outputs))
