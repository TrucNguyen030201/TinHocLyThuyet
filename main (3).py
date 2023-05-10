
class VendingMachine:
    def __init__(self, items, prices):
        self.items = items
        self.prices = prices
        self.states = ["start", 
                       "accept_coin", 
                       "select_item", 
                       "dispense_item",
                       "paid"]
        self.current_state = "start"
        self.total_money = 0
        self.selected_item = None

    def coin(self, amount):
        if self.current_state == "accept_coin":
            self.total_money += amount
            print(f"Accepted {amount} cents. Total: {self.total_money} cents")
            if self.total_money >= min(self.prices.values()):
                self.current_state = "select_item"
                print("Please select an item")
            else:
                print(f"The amount is not enough. Please add")
        else:
            print("Invalid operation in current state")



    def select(self, item):
        if self.current_state == "paid":
            self.current_state = "select_item"
        if self.current_state == "select_item" and item in self.items and self.total_money > 0:
            self.selected_item = item
            self.current_state = "dispense_item"
            print(f"Selected {item}. Price: {self.prices[item]} cents")
        
        elif self.total_money == 0:
            print("You must add your money because you have been returned before")
        elif self.current_state == "dispense_item":
            print("The product has not previously been paid for")
        else:
            print("Invalid operation in current state")
            
    def dispense(self):
        if self.current_state == "dispense_item" and self.selected_item is not None:
            if self.total_money >= self.prices[self.selected_item]:
                print(f"Dispensing {self.selected_item}")
                self.total_money -= self.prices[self.selected_item]
                print(f"Total: {self.total_money} cents")
                self.current_state = "paid"
                self.selected_item = None
                print("Keep buying or get your money back")
                
            else:
                self.current_state = "select_item"
                print("Not enough money")
                print(f"Total: {self.total_money} cents")
        else:
            print("No products available to pay for yet")

    def cancel(self):
        if self.current_state == "select_item":
            print("No item selected")
            print(f"Returned the excess Total: {self.total_money} cents")
            self.total_money = 0
        elif self.current_state == "paid":
            print("Products have been paid ")
            print(f"Returned the excess Total: {self.total_money} cents")
            self.total_money = 0
        elif self.current_state == "dispense_item":
            print("Products haven't been paid ")
            print(f"Returned the excess Total: {self.total_money} cents")
            self.total_money = 0
        else:
            print("Invalid operation in current state")
        

    def run(self):
        print("  Welcome to the vending machine!")
        print("    -------------------------")
        print("    |  Product   |   Price  |")
        print("    |            |          |")
        print("    |  7up       |   14     |")
        print("    |  Coca      |   13     |")
        print("    |  Coke      |   11     |")
        print("    |  Pepsi     |   12     |")
        print("    -------------------------")
        print("|Coin|Select|Despense|Cancel|Quit|\n")
        print("Please enter the amount")
        while True:
            acct = "not_hbrt"
            action = input("> ")
            if action == "quit" and acct != "hb_rt":
                print(f"Returned the excess Total: {self.total_money} cents")
                break
            elif action == "quit":
                break
            elif action == "help":
                print("Commands: coin <amount>, select <item>, dispense, cancel, quit")
            elif action.startswith("coin"):
                amount = int(action.split()[1])
                self.current_state = "accept_coin"
                self.coin(amount)
            elif action.startswith("select"):
                item = action.split()[1]
                self.select(item)
            elif action == "dispense":
                self.dispense()
            elif action == "cancel":
                acct = "hb_rt"
                self.cancel()
            else:
                print("Invalid command")
                

vending_machine = VendingMachine(items={"Coke": 10, "Pepsi": 10, "Coca": 10, "7up": 10}, prices={"Coke": 11, "Pepsi": 12, "Coca": 13, "7up": 14})
vending_machine.run()