import math
import requests


def calc_distance(lat1, lon1, lat2, lon2):
	lat1 = math.radians(lat1)
	lon1 = math.radians(lon1)
	lat2 = math.radians(lat2)
	lon2 = math.radians(lon2)

	h = math.sin( (lat2 - lat1) / 2 ) ** 2 + \
		math.cos( lat1 ) * \
		math.cos( lat2 ) * \
		math.sin( (lon2 - lon1) / 2 ) ** 2

	return 6372.8 * 2 * math.asin( math.sqrt(h) )


def get_distance(meteor):
    return meteor.get('distance', math.inf)

# my_location = ( 53.1682, 50.4494 ) # My location based in google maps
my_location = ( 29.424122, -98.493628 ) 
meteorite_api = 'https://data.nasa.gov/resource/gh4g-9sfh.json'

print("Catching API")
meteor_response = requests.get(meteorite_api)
meteor_data     = meteor_response.json()
print("Status code: " + str(meteor_response.status_code) )

for meteor in meteor_data:
    if not ('reclat' in meteor and 'reclong' in meteor): continue
    meteor['distance'] = calc_distance( float(meteor['reclat']),
                                        float(meteor['reclong']),
                                        my_location[0],
                                        my_location[1] )

meteor_data.sort( key = get_distance )

print("1 Per Line: ...")
for close_ten in meteor_data[0:10]:
    print( close_ten ) 