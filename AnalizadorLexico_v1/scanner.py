from tokens import Token, TokenType

class EnglishScanner:
    def __init__(self, text) -> None:
        self.words = text.split()  # Divide el texto en palabras
        self.current_word = 0  # Índice de la palabra actual
        self.curr = None  # Palabra actual
        self.tokens = []  # Lista para almacenar tokens
        self.scan()
    
    def scan(self):
        while self.current_word < len(self.words):
            self.curr = self.words[self.current_word]
            if self.curr in ('\n', '\t', ' '):
                self.current_word += 1
            elif self.curr.isalpha():  # Verificar si la palabra es alfabética (para identificar tokens de palabras)
                token = self.assign_token(self.curr)
                self.tokens.append(token)
                self.current_word += 1
            else:
                raise Exception('Character not recognized')
    
    def assign_token(self, word):
        if word in ('the', 'a', 'an'):
            return Token(TokenType.ARTICLE, word)
        elif word in ('and', 'or', 'not'):
            return Token(TokenType.CONJUNCTION, word)
        elif word in ('I', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her'):
            return Token(TokenType.PRONOUN, word)
        elif word in ('quickly', 'often', 'very', 'always', 'really', 'too', 'here', 'now', 'almost', 'well'):
            return Token(TokenType.ADVERB, word)
        elif word in ('be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'see', 'take', 'is', 'are','was'):
            return Token(TokenType.VERB, word)     
        elif word in ('cat', 'dog', 'house', 'friend', 'car', 'book', 'city', 'family', 'money', 'time'):
            return Token(TokenType.NOUN, word)   
        elif word in ('happy', 'beautiful', 'big', 'red', 'good', 'old', 'small', 'green', 'young', 'long'):
            return Token(TokenType.ADJECTIVE, word)
        elif word in ('in', 'on', 'under', 'between', 'near', 'above', 'with', 'through', 'from', 'to'):
            return Token(TokenType.PREPOSITION, word)
        elif word in ('.', ',', '!', '?', ';', ':', '-', '\'', '(', ')'):
            return Token(TokenType.PUNCTUATION, word)
        else:
            return Token(TokenType.UNKNOW, word)
        
    
    def scanAll(self):
        return self.tokens


