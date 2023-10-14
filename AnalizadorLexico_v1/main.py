from scanner import EnglishScanner

def main():
    text_bruto = str(input('Ingrese texto: '))
    text = text_bruto.lower()
    s = EnglishScanner(text)
    tokens = s.scanAll()
    print(tokens)
    
if __name__ == '__main__':
    main()
