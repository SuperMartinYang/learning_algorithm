import tool_kit.unserialize_json_solver
import json

with open('serial.json', mode='r', encoding='utf-8') as json_file:
    entry = json.load(json_file, object_hook=tool_kit.unserialize_json_solver.from_json)
