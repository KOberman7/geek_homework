import time


class TrafficLight:
    __color_r = 'red'
    __color_y = 'yellow'
    __color_g = 'green'

    def __init__(self):
        print('TrafficLight is on')

        self.__color_r = 'red'
        print(self.__color_r)
        time.sleep(7)

        self.__color_y = 'yellow'
        print(self.__color_y)
        time.sleep(2)

        self.__color_g = 'green'
        print(self.__color_g)
        time.sleep(10)

        self.__color_y = 'yellow'
        print(self.__color_y)
        time.sleep(2)

TL_1 = TrafficLight()
TL_1.__init__()

