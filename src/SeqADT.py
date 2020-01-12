## @file SeqADT.py
#  @title SeqADT
#  @author Jame Tran
#  @date Feb.16, 2019


## @brief Creates an abstract data type that creates a sequence and provides
#  methods to access sequence.
class SeqADT:
    ## @brief Method to initialize sequence
    #  @param1 Takes in a list s
    def __init__(self, s):
        self.s = s
        self.i = 0

    ## @brief Method to return sequence to start
    def start(self):
        self.i = 0

    ## @brief Method to advance to next value in sequence
    #  @details Returns the current value, than moves index up by one. raises
    #  exception if we move past the end of sequence
    #  @return Returns current SeqADT value
    def next(self):
        if self.i >= len(self.s):
            raise StopIteration
        self.out = self.s[self.i]
        self.i = self.i + 1
        return self.out

    ## @brief Method to check whether we reached the end of the sequence
    #  @details Checks whether index is greater or equal to len(SeqADT). If it
    #  is, we reached the end of the sequence
    # @return boolean of whether or not we reached the end
    def end(self):
        if self.i >= len(self.s):
            return True
        else:
            return False
