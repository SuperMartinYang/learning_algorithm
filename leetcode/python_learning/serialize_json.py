import json
import tool_kit.serialize_json_solver
import time
entry = {
    'time': time.strptime('Thu Sep 21 20:00:14 2017')
}


with open('serial.json', mode='w', encoding='utf-8') as json_file:
    json.dump(entry, json_file, default=tool_kit.serialize_json_solver.to_json)

