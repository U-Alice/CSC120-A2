from typing import Dict
from computer import Computer
class ResaleShop:
    # inventory is the dictionary mapping item IDs to Computer objects
    inventory: dict[int, Computer]
    # next_id is the next available ID for a new computer
    next_id: int   

    # Constructor 
    def __init__(self):
        self.inventory = {}
        self.next_id = 0
    
    # Method buy, adds a computer to inventory and returns its ID
    def buy(self, computer: Computer) -> int:
        computer.id = self.next_id
        self.inventory[self.next_id] = computer
        self.next_id += 1
        return computer.id
    
    # Method sell, removes a computer from inventory by its ID
    def sell(self, item_id: int):
        if item_id in self.inventory:
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
            print("Thank you for shopping with us!\n")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    # Method print_inventory, prints all computers in inventory
    def print_inventory(self):
        if self.inventory:
            for item_id, computer in self.inventory.items():
                print(computer)
        else:
            print("No inventory to display.")

    # Method refurbish, updates the OS and price of a computer by its ID
    def refurbish(self, item_id: int, new_os: str | None = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id]
            computer.refurbish(new_os)
        else:
            print("Item", item_id, "not found. Cannot refurbish.")

    # Method update_price, updates the price of a computer by its ID
    def update_price(self, item_id: int, new_price: int):
        if item_id in self.inventory:
            self.inventory[item_id].price = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")
    
def main():

    shop = ResaleShop()
    
    computer = Computer(
        id=0,
        year_made=2013,
        price=1500,
        operating_system="macOS Big Sur",
        description="Mac Pro (Late 2013)",
        processor_type="3.5 GHc 6-Core Intel Xeon E5",
        hard_drive_capacity=1024,
        memory=64
    )

    computer_2 = Computer(
        id=0,
        year_made=2013,
        price=1500,
        operating_system="macOS Big Sur",
        description="Mac Pro (Late 2013)",
        processor_type="3.5 GHc 6-Core Intel Xeon E5",
        hard_drive_capacity=1024,
        memory=64
    )

    # Print a little banner
    print("-" * 21)
    print("ALICE's COMPUTER RESALE STORE")
    print("-" * 21)

    # Adding to resale store
    print("Adding to inventory...")
    computer_id = shop.buy(computer)
    computer2_id = shop.buy(computer_2)
    # print("Done.\n")

    # Checking inventory
    print("\n Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

    # Refurbishing
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    shop.refurbish(computer_id, new_OS)
    print("Done.\n")

    print("\nChecking inventory...")
    shop.print_inventory()
    print("Done.\n")

    # Updating price
    print("Updating price of Item ID:", computer_id, "to 2000")
    shop.update_price(computer_id, 2000)  

    # Checking inventory
    print("\nChecking inventory...")
    shop.print_inventory()
    print("Done.\n")

    #Trying to sell an item not in inventory
    shop.sell(42)

    # Selling the computer
    shop.sell(computer_id)

    # Checking inventory
    print("\nChecking inventory...")
    shop.print_inventory()
    print("Done.\n")

if __name__ == "__main__": main()