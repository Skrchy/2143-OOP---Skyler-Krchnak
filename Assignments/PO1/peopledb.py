from jsondb import JsonDB

class PeopleDB(JsonDB):
    def find_by_name(self, first_name=None, last_name=None):
        results = []
        for person in self.data:
            if (first_name and person.get("first_name") == first_name) or \
               (last_name and person.get("last_name") == last_name):
                results.append(person)
        return results

    def create_person(self, person):
        # Simple validation
        if "first_name" not in person or "last_name" not in person:
            raise ValueError("Person must have a first and last name")
        return self.create(person)
