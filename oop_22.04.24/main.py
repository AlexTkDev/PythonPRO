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
        return 0 if self.fuel < 0 else self.fuel


if __name__ == '__main__':
    car1 = Car("Mercedes", "White")
    car2 = Car("Ford", "Blue")
    car3 = Car("BMW", "Black")

    desired_dist = 5
    race_dist = 0

    while race_dist < desired_dist:
        car1.move(random.randrange(0, 9))
        car2.move(random.randrange(0, 9))
        car3.move(random.randrange(0, 9))

        if car1.trip_distance >= desired_dist:
            print(f"{car1.color} {car1.model} ПЕРЕМІГ! Пройдена відстань: {car1.trip_distance} км.\n")
            break
        elif car2.trip_distance >= desired_dist:
            print(f"{car2.color} {car2.model} ПЕРЕМІГ! Пройдена відстань: {car2.trip_distance} км.\n")
            break
        elif car3.trip_distance >= desired_dist:
            print(f"{car3.color} {car3.model} ПЕРЕМІГ! Пройдена відстань: {car3.trip_distance} км.\n")
            break

    print(f"1. {car1.color} {car1.model} проїхав {car1.trip_distance} км. Залишок палива: {car1.correct_fuel()} л.")
    print(f"2. {car2.color} {car2.model} проїхав {car2.trip_distance} км. Залишок палива: {car2.correct_fuel()} л.")
    print(f"3. {car3.color} {car3.model} проїхав {car3.trip_distance} км. Залишок палива: {car3.correct_fuel()} л.")
