class Luhn:
    def __init__(self, card_num):
        self.card_num = list(self.number_list(card_num))

    def valid(self):
        card_num_temp = self.card_num # Make temporary copy

        for i in range(len(card_num_temp)-1, -1, -2):
            ## Go backwards through card_num_temp, looking at
            ## every other number x and converting it to (x*2)%9
            card_num_temp[i] = ( card_num_temp[i] * 2 ) % 9
        # card_num is valid (True) if the sum of converted
        # numbers mod 10 equals 0
        return sum(card_num_temp) % 10 == 0

    def number_list(self, card_num):
        """Turn card number into a generator of numbers"""
        for char in card_num:
            if char.isnumeric():
                yield char
