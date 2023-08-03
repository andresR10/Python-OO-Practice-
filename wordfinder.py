"""Word Finder: finds random words from a dictionary."""
import random 


class WordFinder:
    ...
    """
    A class to read words from a file and provide a method to return a random word.

    Attributes:
    words (list): A list to store the read words from the file.

    Methods:
    __init__(self, file_path): Initializes the WordFinder with the path to the file containing words.
    parse(self, dict_file): Parses the dictionary file and returns a list of words.
    random(self): Returns a random word from the list of words.
    """


    def __init__(self, file_path):
        """Initialize the WordFinder with a path to a text file.
        
        Parameters:
        file_path(str): the path to the file containing words, one word per line 
        """
        word_file = open(file_path)
        self.words = self.parse(word_file)
        print(f"{len(self.words)} words read")
    
    def parse(self, word_file):
        """parse the file_path to the list of words"""

        return [w.strip() for w in word_file]
    
    def random(self):
        """Return a randomly selected word as str type object"""

        return random.choice(self.words)
    


class SpecialWordFinder(WordFinder):
    """
    A subclass of WordFinder that handles files with comments and blank lines.

    Methods:
    parse(self, dict_file): Parses the dictionary file and returns a list of non-empty, non-comment words.
    """

    def parse(self, dict_file):
        """
        Parse dict_file -> list of non-empty, non-comment words.

        Parameters:
        dict_file (file): The file object containing words, one word per line.

        Returns:
        list: A list of non-empty, non-comment words read from the file.
        """
        words = [w.strip() for w in dict_file if w.strip() and not w.startswith("#")]
        return words



