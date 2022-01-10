import json
import pathlib


class Location(object):
    def __init__(self, latitude, longitude):
        self.lat = latitude
        self.lng = longitude

    
class PointOfInterest(object):
    def __init__(self, id, title, shortDescription, description, year, category, images, district, location):
        self.id = id
        self.title = title
        self.shortDescription = shortDescription
        self.description = description
        self.year = year
        self.category = category
        self.images = images
        self.district = district
        self.location = location


INCREMENT = 0.01

defaultLocation = Location(49.826524, 10.742834)
latitudeModification = defaultLocation
latitudeLocations = []
latitudeLocations.append(latitudeModification)

locations = []

## generate list of Locations
# 100 locations latitude
for i in range(100):
    latitudeModification.lat = latitudeModification.lat + INCREMENT
    latitudeLocations.append(Location(latitudeModification.lat, defaultLocation.lng))

# respectively 100 locations longitude
for location in latitudeLocations:
    columns = []
    columns.append(location)

    for i in range(100):
        location.lng = location.lng + INCREMENT
        columns.append(Location(location.lat, location.lng))

    locations.append(columns)
        
flatListLocations = [item for sublist in locations for item in sublist]


# generate respective list of PointOfInterest
pointsOfInterest =  []
for i, location in enumerate(flatListLocations):
    pointsOfInterest.append(PointOfInterest(
        i,
        "title-" + str(i),
        "shortDescription-" + str(i),
        "DescriptionDescription DescriptionDescription -" + str(i),
        "2000",
        "category",
        [],
        "district",
        location
    ))


# write data to JSON file
jsonString = json.dumps(pointsOfInterest, default=lambda x: x.__dict__)
path = pathlib.Path(__file__).parent.resolve()
print(str(path))

with open(str(path) +'/poi.json', 'w+') as text_file:
    text_file.write(jsonString)