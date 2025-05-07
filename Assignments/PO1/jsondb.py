import json
import os

class JsonDB:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = []
        self._load_data()

    def _load_data(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = []

    def _save_data(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f, indent=4)

    def create(self, record):
        self.data.append(record)
        self._save_data()
        return len(self.data) - 1

    def read(self, filters=None):
        if not filters:
            return self.data
        return [record for record in self.data if all(record.get(k) == v for k, v in filters.items())]

    def update(self, index, new_record):
        if 0 <= index < len(self.data):
            self.data[index] = new_record
            self._save_data()
        else:
            raise IndexError("Invalid record index")

    def delete(self, index):
        if 0 <= index < len(self.data):
            del self.data[index]
            self._save_data()
        else:
            raise IndexError("Invalid record index")
