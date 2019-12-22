class Car:

    def __init__(self, speed, color, name, is_police, show_speed):

        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)
        self.show_speed = show_speed

    def go(self):
        print('Машина едет')

    def stop(self):
        print('Машина остановилась')

    def TownCar(Car):
        print(
            f'Speed - {self.speed}, color - {self.color}, name - {self.name},Speed now - {self.show_speed}, police? {self.is_police}.')

        if show_speed > 60:
            print('To fast!')

    def SportCar(Car):

        print(
            f'Speed - {self.speed}, color - {self.color}, name - {self.name},Speed now - {self.show_speed}, police? {self.is_police}.')

    def WorkCar(Car):

        print(
            f'Speed - {self.speed}, color - {self.color}, name - {self.name},Speed now - {self.show_speed}, police? {self.is_police}.')

        if show_speed > 40:
            print('To fast!')

    def PoliceCar(Car):

        print(f'Speed - {self.speed}, color - {self.color}, name - {self.name},Speed now - {self.show_speed}, police? {self.is_police}.')


c = Car
Car.speed(60, 'Black', 'Tayota', False, 100)
Car.go(50)
Car.stop(0)


#TownCar = Car(0, 'yello', 'Priora', 65, False)
#S_Car = SportCar(120, 'Red', 'Lambo', 70, False)
#W_Car = WorkCar(35, 'gray', 'Gazelle',35, False)
#P_Car = PoliceCar(200, 'hakky', 'Police', 80, True)
