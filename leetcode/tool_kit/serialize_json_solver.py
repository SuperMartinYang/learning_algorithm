import time

def to_json(python_obj):
    if isinstance(python_obj, time.struct_time):
        return {'__class__':'time.asctime',
                '__value__':time.asctime(python_obj)}
    if isinstance(python_obj, bytes):
        return {'__class__': 'bytes',
                '__value__':list(python_obj)}
    return python_obj