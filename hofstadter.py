# Hofstadter's Law: It always takes longer than you expect, even when you take into account Hofstadter's Law.
# Austin Z. Henley, 2021
# http://www.austinhenley.com/

import sys

# Display error and abort.
def abort(msg):
    sys.exit("Error: " + msg)

class Line:
    def __init__(self, text):
        self.index = 0
        self.tokens = []
        self.text = text
        self.tokenize()

    def tokenize(self):
        while self.index < len(self.text):
            if self.index > 0 and not self.text[self.index].isspace():  # Expect a space between tokens.
               abort("Unexpected token.")
            t = self.nextToken()
            if t is not None:
                self.tokens.append(t)

    # Gets next token. The 8 legal commands are: # ? ! @ + "regex" https://url.com/ /filepath.txt 
    def nextToken(self):
        length = len(self.text)
        # Skip all leading whitespace.
        while self.index < length and self.text[self.index].isspace():
            self.index += 1
        start = self.index

        if self.index == length:
            return None

        # Stdin/stdout.
        if self.text[self.index] == '#':
            self.index += 1
            return ('#', '#')

        # Equal to, not equal to, swap, or concatenate.
        elif self.text[self.index] in ['?', '!', '@', '+']:
            self.index += 1
            while self.index < length and self.text[self.index].isdigit():
                self.index += 1
            if self.index+1 == start:    # Must be one digit after the symbol.
                abort(f"Expected number after {self.text[start]}.")
            return (self.text[start], self.text[start+1:self.index])

        # Regex.
        elif self.text[self.index] == '"':
            pass

        # URL.
        elif self.text.startswith("http"):
            pass

        # File path.
        else:
            pass


# TODO: Handle file opening exceptions.
with open(sys.argv[1]) as f:
    rawlines = f.readlines()
