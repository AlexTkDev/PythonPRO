import random


class Car:
    def __init__(self, model, color, trip_distance=0):
        self.fuel = random.randrange(0, 9)
        self.trip_distance = trip_distance
        self.model = model
        self.color = color

    def move(self, distance):
        self.trip_distance += distance
        self.fuel -= distance

    def correct_fuel(self):
        return max(0, self.fuel)


if __name__ == '__main__':
    cars = [
        Car("Mercedes", "White"),
        Car("Ford", "Blue"),
        Car("BMW", "Black")
    ]

    desired_dist = 5

    while True:
        for car in cars:
            car.move(random.randrange(0, 9))
            if car.trip_distance >= desired_dist:
                print(f"{car.color} {car.model} ПЕРЕМІГ! Пройдена відстань: {car.trip_distance} км.\n")
                break
        else:
            continue
        break

    for i, car in enumerate(cars, 1):
        print(
            f"{i}. {car.color} {car.model} проїхав {car.trip_distance} км. Залишок палива: {car.correct_fuel()} л.")
