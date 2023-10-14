from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    VERB = 1   #verbo x
    NOUN = 2   #sustantivo  
    ARTICLE = 3  #articulo  
    ADJECTIVE = 4  #adjetivo 
    PREPOSITION = 5 #preposicion 
    CONJUNCTION = 6  #conjucion 
    PRONOUN = 7 #pronombres    
    ADVERB = 8 #advervios  
    PUNCTUATION = 9 #puntuacion  
    UNKNOW = 10 
    
    def __str__(self) -> str:
        return self.name

@dataclass
class Token:
    token_type: TokenType
    lexeme: str
    
    def __repr__(self) -> str:
        return f'{self.token_type}("{self.lexeme}")'
