class TemperatureApp :
 @staticmethod
 def convert_cel_to_far():
    try:
        print("Enter a temperature in degrees C :")
        temp = float(input())
        # F = C * 9/5 + 32
        res_f = temp * 9 / 5 + 32
        res_f = round(res_f, 2)
        print(f"{temp} degrees C = {res_f} degrees F")
    except ValueError:
        print("Invalid input. Please enter numeric values")

 @staticmethod
 def convert_far_to_cel() :

    try:
        print("Enter a temperature in degrees F :")
        temp = float(input())
        # C = (F - 32) * 5/9
        res_c = (temp - 32) * 5 / 9
        res_c = round(res_c, 2)
        print(f"{temp} degrees F = {res_c} degrees C")
    except ValueError:
        print("Invalid input. Please enter numeric values")

TemperatureApp.convert_far_to_cel()
TemperatureApp.convert_cel_to_far()