class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        try:
            # Make temporary copy
            card_num_temp = list(self.number_list(self.card_num))
        except ValueError:
            # card_num contains invalid characters
            return False

        for i in range(len(card_num_temp)-2, -1, -2):
            ## Go backwards through card_num_temp, looking at
            ## every other number
            # Multiply number by two
            card_num_temp[i] = card_num_temp[i] * 2

            if card_num_temp[i] > 9:
                # Number is now greater than 9, so subtract 9
                card_num_temp[i] -= 9
        # card_num is valid (True) if the sum of converted
        # numbers mod 10 equals 0
        return sum(card_num_temp) % 10 == 0

    def number_list(self, card_num):
        """Turn card number into a generator of numbers"""
        card_num = card_num.strip() # Remove any padding whitespace
        
        if len(card_num) < 2:
            # Strings of length 1 or less are not valid
            raise ValueError()

        for char in card_num:
            if char.isnumeric():
                # Char is valid
                yield int(char)
            elif char != ' ':
                # Char is definitely not a space or number
                raise ValueError()
