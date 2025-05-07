from peopledb import PeopleDB
from meteoritedb import MeteoriteDB
from earthquakedb import EarthquakeDB

def main():
    # Working with PeopleDB
    pdb = PeopleDB("people.json")
    new_id = pdb.create_person({"first_name": "Alice", "last_name": "Johnson", "city": "Seattle"})
    found = pdb.find_by_name(first_name="Teresa")
    print("Found people:", found)

    # Working with MeteoriteDB
    mdb = MeteoriteDB("meteorites.json")
    heavy = mdb.find_heaviest_meteorites()
    print("Top meteorites by mass:", heavy)

    range_hits = mdb.find_by_year_range(1900, 1960)
    print("Meteorites from 1900–1960:", range_hits)

    # Working with EarthquakeDB
    edb = EarthquakeDB("earthquakes.json")
    strong_eqs = edb.filter_by_magnitude(5.0)
    print("Strong earthquakes (≥5.0):", strong_eqs)

    in_california = edb.filter_by_place("california")
    print("Earthquakes in California:", in_california)

if __name__ == "__main__":
    main()
