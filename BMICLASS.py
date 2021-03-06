# Tony
# 6/29/2018
# This class is for BMI and has functions to return name age weight and height
#  and calculate bmi as well as the status of that bmi
class BMI:
    def __init__(self,name,age,weight,height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getWeight(self):
        return self.__weight
    def getHeight(self):
        return self.__height
    def getBMI(self):
        KILOGRAMS_PER_POUND = .453559237
        METERS_PER_INCH = .0254
        bmi = self.__weight*KILOGRAMS_PER_POUND/((self.__height*METERS_PER_INCH)**2)
        return round(bmi*100)/100
    def getStatus(self):
        bmi = self.getBMI()
        if bmi < 18.5:
            return "Under Weight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Over weight"
        else:
            return "Obese"

