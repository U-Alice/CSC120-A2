class Computer:
    # unique identifier for the computer
    id: int
    # year the computer was made
    year_made: int
    # price of the computer
    price : int
    # operating system installed on the computer
    operating_system: str
    # description of the computer
    description: str
    # other attributes
    processor_type: str
    hard_drive_capacity: int
    memory: int

    # Constructor
    def __init__(self, id: int, year_made: int, price: int, operating_system: str, description: str, processor_type: str, hard_drive_capacity: int, memory: int):
        self.id = id
        self.year_made = year_made
        self.price = price
        self.operating_system = operating_system
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory

    def __str__(self):
        return f'Item ID: {self.id} : {{"description": "{self.description}", "processor_type": "{self.processor_type}", "hard_drive_capacity": {self.hard_drive_capacity}, "memory": {self.memory}, "operating_system": "{self.operating_system}", "year_made": {self.year_made}, "price": {self.price}}}'
    # Method refurbish, updates the OS and price of the computer
    def refurbish(self, new_os: str):
        if int(self.year_made) < 2000:
            self.price = 0 # too old to sell, donation only
        elif int(self.year_made) < 2012:
            self.price = 250 # heavily-discounted price on machines 10+ years old
        elif int(self.year_made) < 2018:
            self.price = 550 # discounted price on machines 4-to-10 year old machines
        else:
            self.price = 1000 # recent stuff
        if new_os is not None:
            self.operating_system = new_os # update details after installing new OS