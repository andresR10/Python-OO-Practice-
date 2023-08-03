"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start = 0):
        """Initializes SerialGenerator with a start number"""
        self.start = start
        self.current = start

    def __repr__(self):
        """shows more readable representation"""
        return f"<SerialGeneratorstart={self.start} current={self.current}>"
    
    def generate(self):
        """Generates next sequential number from the starting number and returns it"""
        self.current += 1
        return self.current 
    
    def reset(self):
        """Resets current value back to initial one"""
        self.current = self.start
    



