from jsondb import JsonDB

class MeteoriteDB(JsonDB):
    def find_by_year_range(self, start_year, end_year):
        return [m for m in self.data if "year" in m and start_year <= int(m["year"]) <= end_year]

    def find_heaviest_meteorites(self, top_n=5):
        filtered = [m for m in self.data if "mass" in m]
        sorted_meteorites = sorted(filtered, key=lambda x: float(x["mass"]), reverse=True)
        return sorted_meteorites[:top_n]
