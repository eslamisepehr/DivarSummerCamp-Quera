from building import Building
from command_parser import Command_Parser
from floor import Floor_Type

building = Building()

command_parser = Command_Parser()

# Features
number_of_features = int(input())
features_price = command_parser.desk_features_command_parser(input())
building.add_desk_features_price(features_price)

# Add floors
number_of_floors, special_floor_entrance_price = map(int, input().split())

building.add_entrance_price(Floor_Type.Free, 0)
building.add_entrance_price(Floor_Type.Special, special_floor_entrance_price)

for i in range(number_of_floors):
    number_of_desks, floor_type = input().split()
    desks_features = input().split()
    building.add_floors_with_desks(Floor_Type(floor_type), desks_features)

# Processing
outputs = []
while True:
    command = input()
    if command_parser.is_finished(command):
        break

    response = ""

    if command_parser.is_request_desk_command(command):
        username, floor_type, time_range = command_parser.request_desk_command_parser(command)
        response = building.request_desk(username, floor_type, time_range)
    elif command_parser.is_reserve_desk_command(command):
        username, time_range, features = command_parser.reserve_desk_command_parser(command)
        response = building.reserve_desk(username, time_range, features)
    elif command_parser.is_reserve_multiple_desks_command(command):
        username, time_range, number_of_desks = command_parser.reserve_multiple_desks_command_parser(command)
        response = building.reserve_multiple_desks(username, time_range, number_of_desks)

    outputs.append(response)

print("\n".join(outputs))
