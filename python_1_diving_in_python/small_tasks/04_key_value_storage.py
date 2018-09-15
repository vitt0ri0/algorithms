import argparse
import os
import tempfile
import json

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--value")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

# read from file, check if file exists
try:
    with open(storage_path, 'r') as f:
        file_string = f.read()
        if file_string:
            storage = json.loads(file_string)
        else:
            storage = {}
except FileNotFoundError:
    storage = {}

# get Key, Value easy readable
key = args.key
value = args.value

# if we have Value, then update the storage
if value:
    storage_values = storage.get(key)
    if storage_values:
        if value not in storage_values:
            storage_values.append(value)
            storage[key] = storage_values
    else:
        storage[key] = [value]

# if we doesn't have Value, then read the Key and print it
else:
    storage_values = storage.get(key)
    if storage_values:
        print(*storage_values, sep=", ")
    else:
        print(storage_values)

# write to file
with open(storage_path, 'w') as f:
    f.write(json.dumps(storage))
