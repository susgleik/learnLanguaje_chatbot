from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    VERB = 1   #verbo x
    NOUN = 2   #sustantivo  x
    ARTICLE = 3  #articulo  x
    ADJECTIVE = 4  #adjetivo x
    PREPOSITION = 5 #preposicionx 
    CONJUNCTION = 6  #conjucion x
    PRONOUN = 7 #pronombres  x  
    ADVERB = 8 #advervios  x
    PUNCTUATION = 9 #puntuacion  x
    UNKNOW = 10 
    
    def __str__(self) -> str:
        return self.name

@dataclass
class Token:
    token_type: TokenType
    lexeme: str
    
    def __repr__(self) -> str:
        return f'{self.token_type}("{self.lexeme}")'
