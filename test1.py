# from coordTransform_utils import Geocoding
import coordTransform_utils as util

lng = 118.07400059168339
lat = 36.845435015941064

result2 = util.bd09_to_gcj02(lng, lat)
result5 = util.bd09_to_wgs84(lng, lat)

print('bd09_to_gcj02 bd09_to_wgs84')
print(result2, result5)
