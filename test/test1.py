# from coordTransform_utils import Geocoding
from ..coord import coordTransform_utils as util

# 测试

# lng = 118.07400059168339
# lat = 36.845435015941064

# result2 = util.bd09_to_gcj02(lng, lat)
# result5 = util.bd09_to_wgs84(lng, lat)

# print('bd09_to_gcj02 bd09_to_wgs84')
# print(result2, result5)

# map=(lng,lat)
# print(util.bd09_to_gcj02(map[0], map[1]))
# print(util.bd09_to_wgs84(map[0], map[1]))

# map=(117.984285,36.838225),(117.9901716,36.8352266),(117.9894317,36.8289983),(117.988405,36.8223416),(117.9879533,36.819215),(117.997927,36.8154),(118.011175,36.814325),(118.0155233,36.8139866),(118.032325,36.807435),(118.03691,36.8071766),(118.0410133,36.8066),(118.04741,36.805503),(118.05186,36.8047817),(118.0583528,36.8038639),(118.0630366,36.800075),(118.0599361,36.7999944),(118.05476,36.8006766),(118.05338,36.79935),(118.048527,36.784457),(118.0479333,36.7851139),(118.05368,36.799736),(118.054755,36.800603),(118.0599722,36.7999444),(118.0630544,36.8002472),(118.0594667,36.8038778),(118.052948,36.804863),(118.04717,36.805815),(118.04048,36.806918),(118.034888,36.80768),(118.031846,36.8078),(118.0143033,36.814305),(118.010195,36.8146333),(117.995221,36.81576),(117.9883083,36.8199667),(117.9890333,36.824215),(117.9900267,36.8309717),(117.9902967,36.8342267),(117.9822167,36.838595)

# print(map)
# print(map[10])

# map=(118.044817,36.835911),(118.029521,36.846764),(118.026973,36.84955),(118.01895,36.894216),(118.01837,36.89451),(118.026256,36.848796),(118.028718,36.84666),(118.043216,36.836273)
# map=(118.075888,36.807823),(118.047758,36.822142),(118.038021,36.829563),(118.01837,36.89451),(118.01895,36.894216),(118.038111,36.829576),(118.047929,36.822481),(118.075509,36.808257)
map=(118.03761,36.739733),(118.038591,36.743196),(118.044608,36.766138),(118.049502,36.786281),(118.049087,36.784881),(118.044683,36.767175),(118.038335,36.74322),(118.0373,36.73967)

for coord in map:
    # print(coord)
    # result = util.wgs84_to_bd09(coord[0], coord[1])
    result = util.wgs84_to_gcj02(coord[0], coord[1])
    print(result[0],result[1])


# print(len(map))
