import time

def from_json(json_obj):
    if '__class__' in json_obj:
        if json_obj['__class__'] == 'time.asctime':
            return time.strptime(json_obj['__value__'])
        if json_obj['__class__'] == 'bytes':
            return bytes(json_obj['__value__'])
    return json_obj