from jsondb import JsonDB

class EarthquakeDB(JsonDB):
    def filter_by_magnitude(self, min_magnitude):
        return [eq for eq in self.data if float(eq.get("magnitude", 0)) >= min_magnitude]

    def filter_by_place(self, keyword):
        return [eq for eq in self.data if keyword.lower() in eq.get("place", "").lower()]
