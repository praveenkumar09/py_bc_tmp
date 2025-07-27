class Vehicle:
    def __init__(self, starting_top_speed=100):
        self.top_speed = starting_top_speed
        self.__warnings = []
        self.passengers = []

    def __repr__(self):
        return 'Top speed : {}, Warnings : {}'.format(self.top_speed, self.__warnings)

    def drive(self):
        print(' I am driving but certainly not faster than {}'.format(self.top_speed))

    def add_warning(self, warnings_str):
        if len(warnings_str) > 0:
            self.__warnings.append(warnings_str)

    def get_warnings(self):
        return self.__warnings