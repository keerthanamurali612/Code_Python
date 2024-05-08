
class laptop:
    def __init__(self,price,processor):
        self.price=price
        self.processor=processor
    
HP=laptop(50000,"AMD")
print(HP.price, HP.processor)
