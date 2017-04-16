import sys
import pickle

class Mary(object):
    def __init__(self):
        self.notes = self.deserialize()
    
    def serialize(self):
        with open("messages.txt", "wb+") as f:
            pickle.dump(self.notes, f)

    def deserialize(self):
        notes = {}

        try:    
            with open("messages.txt", "rb+") as f:
                notes = pickle.load(f)
        except (EOFError, FileNotFoundError):
            pass

        return notes

    def add_note(self, note):
        self.notes.setdefault("Mary", [])
        self.notes["Mary"].append(note)

        
if __name__ == "__main__":

    mary = Mary()
    note = sys.argv[1]
    mary.add_note(note)
    mary.serialize()
    print(mary.notes)
