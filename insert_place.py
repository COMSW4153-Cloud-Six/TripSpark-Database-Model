
from db_config import get_connection

def insert_place(poi, city, country, currency, latitude, longitude, rating,
    description, spending, budget, vibes, activities, food,
    best_season, trip_days, nearest_airport, transport,
    accessibility, direction):

    cnx = None
    cursor = None
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        #insert_query = "INSERT INTO catalog (name , country , currency , lat , lon , rating_avg , description , vibe , budget , poi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        #cursor.execute(insert_query, (name , country , currency , lat , lon , rating_avg , description , vibe , budget , poi))
        
        insert_query = "INSERT INTO catalog (poi, city, country, currency, latitude, longitude, rating, description, spending, budget, vibes, activities, food, best_season,trip_days, nearest_airport, transport, accessibility, direction) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(insert_query, (poi.lower(), city.lower(), country.lower(), currency.lower(), latitude, longitude, rating,
            description.lower(), spending.lower(), budget, vibes.lower(), activities.lower(), food.lower(),
            best_season.lower(), trip_days, nearest_airport.lower(), transport.lower(),
            accessibility.lower(), direction))
        
        cnx.commit()

        print(f"Location '{poi}' inserted successfully.")

    except Exception as err:
        print(f"Error: {err}")

    finally:
        if cursor:
            try:
                cursor.close()
            except Exception:
                pass

        if cnx and cnx.is_connected():
            try:
                cnx.close()
                print("MySQL connection closed.")
            except Exception:
                pass

if __name__ == "__main__":
    '''location_data = {
        "name": ["New York City", "Seattle", "New York City"],
        "country": ["USA", "USA", "USA"],
        "currency": ["USD", "USD", "USD"],
        "lat":[40.712776, 37.774929, 51.507351],
        "lon":[-74.005974, -122.419418, -0.127758],
        "rating_avg":[4.3, 3.5, 4.6],
        "description":["Lively place", "Good place", "Awesome place"],
        "vibe":["Good", "Bad", "Bad"],
        "budget":["$200", "$200", "$200"],
        "poi":["Times Square", "Space Needle", "Central Park"]
    }

    for i in range(3):
        insert_place(location_data["name"][i] , location_data["country"][i] , location_data["currency"][i] , location_data["lat"][i] , location_data["lon"][i] , location_data["rating_avg"][i] , location_data["description"][i] , location_data["vibe"][i] , location_data["budget"][i] , location_data["poi"][i])
    '''


    locations = [
        (
            "Times Square", "New York City", "USA", "USD", 40.7580, -73.9855, 4.5,
            "Famous commercial intersection in Manhattan",
            "high", 200,
            "Urban,Modern,Nightlife",
            "Shopping,Photography,Walking Tours",
            "Street Food,Coffee,Local Cuisine",
            "summer", 2, "JFK", "walkable",
            "Crowded area with lots of walking",
            "https://www.google.com/maps/place/Times+Square/@40.7579747,-73.9881175,17z/data=!3m1!4b1!4m6!3m5!1s0x89c25855c6480299:0x55194ec5a1ae072e!8m2!3d40.7579747!4d-73.9855426!16zL20vMDdxZHI?entry=ttu&g_ep=EgoyMDI1MTExNy4wIKXMDSoASAFQAw%3D%3D"
        ),

        (
            "Central Park", "New York City", "USA", "USD", 40.7829, -73.9654, 4.8,
            "Large public park in Manhattan",
            "low", 50,
            "Relaxed,Nature,Urban",
            "Parks,Photography,Walking Tours",
            "Coffee,Street Food",
            "spring", 1, "JFK", "walkable",
            "Mostly flat trails",
            "https://www.google.com/maps/place/Central+Park/@40.7825547,-73.9681583,16z/data=!3m1!4b1!4m6!3m5!1s0x89c2589a018531e3:0xb9df1f7387a94119!8m2!3d40.7825547!4d-73.9655834!16zL20vMDljN3Y?entry=ttu&g_ep=EgoyMDI1MTExNy4wIKXMDSoASAFQAw%3D%3D"
        ),

        (
            "Space Needle", "Seattle", "USA", "USD", 47.6205, -122.3493, 4.6,
            "Iconic observation tower",
            "medium", 150,
            "Modern,Urban",
            "Architecture,Photography",
            "Fine Dining,Local Cuisine",
            "summer", 1, "SEA", "public_transit",
            "Elevator access available",
            "https://www.google.com/maps/place/Space+Needle/@47.6205063,-122.3518523,16z/data=!3m1!4b1!4m6!3m5!1s0x5490151f4ed5b7f9:0xdb2ba8689ed0920d!8m2!3d47.6205063!4d-122.3492774!16zL20vMDFrN3Y3?entry=ttu&g_ep=EgoyMDI1MTExNy4wIKXMDSoASAFQAw%3D%3D"
        ),

        (
            "Golden Gate Bridge", "San Francisco", "USA", "USD", 37.8199, -122.4783, 4.9,
            "Historic suspension bridge",
            "low", 0,
            "Historic,Urban,Nature",
            "Photography,Walking Tours",
            "Coffee,Street Food",
            "fall", 1, "SFO", "rideshare",
            "Windy but walkable",
            "https://www.google.com/maps/place/Golden+Gate+Bridge+Vista+Point/@37.8077867,-122.4855004,15z/data=!3m1!4b1!4m6!3m5!1s0x808586ec0636bb65:0xfd29c84f7e83d613!8m2!3d37.8077876!4d-122.4752007!16s%2Fg%2F1tpbc62h?entry=ttu&g_ep=EgoyMDI1MTExNy4wIKXMDSoASAFQAw%3D%3D"
        ),

        (
            "Statue of Liberty", "New York City", "USA", "USD", 40.6892, -74.0445, 4.7,
            "Symbol of American freedom",
            "medium", 120,
            "Historic,Cultural",
            "Museums,Photography",
            "Local Cuisine",
            "summer", 1, "JFK", "public_transit",
            "Ferry with stairs",
            "https://www.google.com/maps/place/Statue+of+Liberty/@40.6892494,-74.0470753,17z/data=!3m1!4b1!4m6!3m5!1s0x89c25090129c363d:0x40c6a5770d25022b!8m2!3d40.6892494!4d-74.0445004!16zL20vMDcycDg?entry=ttu&g_ep=EgoyMDI1MTExNy4wIKXMDSoASAFQAw%3D%3D"
        ),

        (
            "Hollywood Sign", "Los Angeles", "USA", "USD", 34.1341, -118.3215, 4.4,
            "Famous landmark in LA",
            "low", 0,
            "Urban,Modern",
            "Photography,Walking Tours",
            "Street Food",
            "spring", 1, "LAX", "car_rental",
            "Hiking trails available",
            "https://www.google.com/maps/place/Hollywood+Sign/@34.1340213,-118.3242515,17z/data=!3m1!4b1!4m6!3m5!1s0x80c2bf0a45505a7d:0xabb7acc626709843!8m2!3d34.1341151!4d-118.3215482!16zL20vMDUwY3R2?entry=ttu&g_ep=EgoyMDI1MTExNy4wIKXMDSoASAFQAw%3D%3D"
        ),

        (
            "Disneyland", "Anaheim", "USA", "USD", 33.8121, -117.9190, 4.8,
            "World-famous theme park",
            "high", 250,
            "Adventure,Modern",
            "Parks,Photography",
            "Brunch,Local Cuisine",
            "summer", 2, "SNA", "rideshare",
            "Wheelchair friendly",
            "https://www.google.com/maps/place/Disneyland+Park/@33.8120918,-117.9215491,17z/data=!3m1!4b1!4m6!3m5!1s0x80dcd7d12b3b5e6b:0x2ef62f8418225cfa!8m2!3d33.8120918!4d-117.9189742!16zL20vMDJmenM?entry=ttu&g_ep=EgoyMDI1MTExNy4wIKXMDSoASAFQAw%3D%3D"
        ),

        (
            "Grand Canyon", "Arizona", "USA", "USD", 36.0544, -112.1401, 4.9,
            "Massive canyon with scenic views",
            "low", 80,
            "Nature,Adventure",
            "Photography,Walking Tours",
            "Street Food",
            "spring", 2, "PHX", "car_rental",
            "Some steep areas",
            "https://www.google.com/maps/place/Grand+Canyon/@36.0997622,-112.1227843,15z/data=!3m1!4b1!4m6!3m5!1s0x80cc0654bd27e08d:0xb1c2554442d42e8d!8m2!3d36.0997631!4d-112.1124846!16zL20vMGNuczU?entry=ttu&g_ep=EgoyMDI1MTExNy4wIKXMDSoASAFQAw%3D%3D"
        ),

        (
            "Niagara Falls", "Ontario", "Canada", "CAD", 43.0962, -79.0377, 4.8,
            "Famous waterfall",
            "medium", 100,
            "Nature,Adventure",
            "Photography,Parks",
            "Local Cuisine",
            "summer", 1, "YYZ", "public_transit",
            "Slippery paths",
            "https://www.google.com/maps/place/Niagara+Falls,+ON,+Canada/@43.0538143,-79.2528424,11z/data=!3m1!4b1!4m6!3m5!1s0x89d3445eec824db9:0x46d2c56156bda288!8m2!3d43.0895577!4d-79.0849436!16zL20vMDE4bGNf?entry=ttu&g_ep=EgoyMDI1MTExNy4wIKXMDSoASAFQAw%3D%3D"
        ),

        (
            "CN Tower", "Toronto", "Canada", "CAD", 43.6426, -79.3871, 4.7,
            "Iconic observation tower",
            "medium", 130,
            "Modern,Urban",
            "Photography,Architecture",
            "Fine Dining",
            "fall", 1, "YYZ", "public_transit",
            "Elevator access",
            "https://www.google.com/maps/place/CN+Tower/@43.6425662,-79.3896317,17z/data=!3m2!4b1!5s0x882b34d819a55ff7:0xad7cf7bcaf4e239b!4m6!3m5!1s0x882b34d68bf33a9b:0x15edd8c4de1c7581!8m2!3d43.6425662!4d-79.3870568!16zL20vMDF0d3M?entry=ttu&g_ep=EgoyMDI1MTExNy4wIKXMDSoASAFQAw%3D%3D"
        ),

        (
            "Eiffel Tower", "Paris", "France", "EUR", 48.8584, 2.2945, 4.7,
            "Famous iron tower",
            "medium", 140,
            "Historic,Cultural,Romantic",
            "Photography,Architecture",
            "Bakeries,Fine Dining",
            "spring", 2, "CDG", "walkable",
            "Some stairs",
            "https://www.google.com/maps/place/Eiffel+Tower/@48.8583701,2.2919064,16z/data=!3m1!4b1!4m6!3m5!1s0x47e66e2964e34e2d:0x8ddca9ee380ef7e0!8m2!3d48.8583701!4d2.2944813!16zL20vMDJqODE?entry=ttu&g_ep=EgoyMDI1MTExNy4wIKXMDSoASAFQAw%3D%3D"
        ),

        (
            "Colosseum", "Rome", "Italy", "EUR", 41.8902, 12.4922, 4.7,
            "Ancient Roman gladiator arena",
            "medium", 110,
            "Historic,Cultural",
            "Museums,Photography",
            "Local Cuisine",
            "spring", 2, "FCO", "walkable",
            "Uneven stone paths",
            "https://www.google.com/maps/place/Colosseum/@41.8902102,12.489656,17z/data=!3m1!4b1!4m6!3m5!1s0x132f61b6532013ad:0x28f1c82e908503c4!8m2!3d41.8902102!4d12.4922309!16zL20vMGQ1cXg?entry=ttu&g_ep=EgoyMDI1MTExNy4wIKXMDSoASAFQAw%3D%3D"
        ),

        (
            "Big Ben", "London", "UK", "GBP", 51.5007, -0.1246, 4.6,
            "Historic clock tower",
            "low", 0,
            "Historic,Urban",
            "Photography,Walking Tours",
            "Coffee,Bakeries",
            "summer", 1, "LHR", "public_transit",
            "Flat pavement",
            "https://www.google.com/maps/place/Big+Ben/@51.5007292,-0.1272003,16z/data=!3m2!4b1!5s0x47d8e55e300273ad:0x64ade3f4995c75cd!4m6!3m5!1s0x487604c38c8cd1d9:0xb78f2474b9a45aa9!8m2!3d51.5007292!4d-0.1246254!16zL20vMDI2eWRj?entry=ttu&g_ep=EgoyMDI1MTExNy4wIKXMDSoASAFQAw%3D%3D"
        ),

        (
            "Dubai Mall", "Dubai", "UAE", "AED", 25.1972, 55.2744, 4.7,
            "Largest mall in the world",
            "high", 300,
            "Modern,Urban",
            "Shopping,Architecture",
            "Fine Dining,Brunch",
            "winter", 2, "DXB", "rideshare",
            "Wheelchair friendly",
            "https://www.google.com/maps/place/Dubai+Mall/@25.197438,55.276923,17z/data=!3m2!4b1!5s0x3e5f6829d585a26f:0xa2f9a6d6258c2d45!4m6!3m5!1s0x3e5f682829c85c07:0xa5eda9fb3c93b69d!8m2!3d25.1972295!4d55.279747!16zL20vMGJ4ZG40?entry=ttu&g_ep=EgoyMDI1MTExNy4wIKXMDSoASAFQAw%3D%3D"
        ),

        (
            "Mount Fuji", "Tokyo", "Japan", "JPY", 35.3606, 138.7274, 4.9,
            "Sacred mountain and volcano",
            "medium", 120,
            "Nature,Adventure,Cultural",
            "Photography,Hiking",
            "Local Cuisine",
            "fall", 2, "HND", "car_rental",
            "Rocky trails",
            "https://www.google.com/maps/place/Mount+Fuji/@35.3606246,138.7170637,15z/data=!3m1!4b1!4m6!3m5!1s0x6019629a42fdc899:0xa6a1fcc916f3a4df!8m2!3d35.3606255!4d138.7273634!16zL20vMGNrczA?entry=ttu&g_ep=EgoyMDI1MTExNy4wIKXMDSoASAFQAw%3D%3D"
        )
    ]

    for place in locations:
        insert_place(*place)


