import random


# class Car:
#     def __init__(self, model, color, trip_distance=0):
#         self.fuel = random.randrange(0, 9)
#         self.trip_distance = trip_distance
#         self.model = model
#         self.color = color
#
#     def move(self, distance):
#         self.trip_distance += distance
#         self.fuel -= distance
#
#     def correct_fuel(self):
#         return max(0, self.fuel)
#
#
# if __name__ == '__main__':
#     cars = [
#         Car("Mercedes", "White"),
#         Car("Ford", "Blue"),
#         Car("BMW", "Black")
#     ]
#
#     desired_dist = 5
#
#     while True:
#         for car in cars:
#             car.move(random.randrange(0, 9))
#             if car.trip_distance >= desired_dist:
#                 print(f"{car.color} {car.model} ПЕРЕМІГ! Пройдена відстань: {car.trip_distance} км.\n")
#                 break
#         else:
#             continue
#         break
#
#     for i, car in enumerate(cars, 1):
#         print(
#             f"{i}. {car.color} {car.model} проїхав {car.trip_distance} км. Залишок палива: {car.correct_fuel()} л.")

# or

class Car:
    def __init__(self, model: str, color: str):
        self.fuel = random.randrange(0, 9)
        self.trip_distance = random.randrange(0, 9)
        self.model = model
        self.color = color

    def move(self) -> None:
        distance = random.randrange(0, 9)
        move_distance = min(distance, self.fuel)
        self.trip_distance += move_distance
        self.fuel -= move_distance

    def __repr__(self) -> str:
        return f"<{self.model}: fuel={self.fuel} distance={self.trip_distance}>"


MODEL_COLOR = [("DODGE", "RED"), ("CHEVROLET", "YELLOW"), ("FORD", "ORANGE")]
cars = [Car(model=model, color=color) for model, color in MODEL_COLOR]

desired_dist = random.randrange(3, 9)

winner = None
while not winner:
    for car in cars:
        if car.fuel > 0:
            car.move()
            if car.trip_distance >= desired_dist:
                winner = car
                print(f"Winner is {winner.model} with distance {winner.trip_distance}")
                break

for car in cars:
    print(car)
