import json
from datetime import datetime


class Diary:

    FILENAME = 'diary.json'
    entries = []

    def build_entries(self):
        return ''.join([f'{entry.get("created")}:\n{entry.get("description")}\n---\n' for entry in self.entries])

    def load(self):
        try:
            with open(self.FILENAME, 'r') as f:
                self.entries = json.loads(f.read())
        except FileNotFoundError:
            return []
    
    def save(self):
        with open(self.FILENAME, 'w') as f:
            f.write(json.dumps(self.entries))
    
    def add_entry(self, entry):
        self.entries.append(entry.serialize())


class Entry:
    def __init__(self, description):
        self.description = description
        self.created = datetime.now().strftime("%c")

    def serialize(self):
        return {
            "description": self.description,
            "created": self.created
        }
