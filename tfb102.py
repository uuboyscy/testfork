class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.parkingslot = [big, medium, small]

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        car = carType
        if car == 1:
            if self.parkingslot[0] > 0:
                self.parkingslot[0] -= 1
                return True
            else:
                return False
        if car == 2:
            if self.parkingslot[1] > 0:
                self.parkingslot[1] -= 1
                return True
            else:
                return False
        if car == 3:
            if self.parkingslot[2] > 0:
                self.parkingslot[2] -= 1
                return True
            else:
                return False
