# create a data class so that we can use it in the program
class CryptoDataClass():
    def __init__(self, name='', price='0', main_price=0, volume_price=0, fall_change=0, rise_change=0, all_time_high=0, liquidity=0):
        # initialise
        self.name = name
        self.price = price
        self.main_price = main_price
        self.volume_price = volume_price
        self.fall_change = fall_change
        self.rise_change = rise_change
        self.all_time_high = all_time_high
        self.liquidity = liquidity
        
    def __str__(self):
        return str(self.__dict__)