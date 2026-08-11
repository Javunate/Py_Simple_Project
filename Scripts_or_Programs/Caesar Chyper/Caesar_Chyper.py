class main:
    def __init__(self, key:dict):
        self.key = key
    
    def getinput(self):
        new_str = str(input("\nEnter String: "))
        if new_str.isalpha():
            new_str = new_str.lower()
            self.new_str = new_str
        else:
            print("Invalid Input")
    
    def encrypt(self):
        output = ""
        for c in self.new_str:
            for k,v in self.key.items():
                if k==c:
                    output +=v
                else:
                    continue
        self.encrypted_string = output
        return(output)
    
    def decript(self):
        output = ""
        for c in self.new_str:
            for k,v in self.key.items():
                if v==c:
                    output +=k
                else:
                    continue
        self.decripted_string = output
        return(output)
    
    def selector(self):
        while True:
            print("Type 0 To exit\n")
            print("-------Select Method-------")
            select = input("1. Encrypt\n2. Decrypt\n-> ")
            if select == "1":
                main.getinput()
                print(main.encrypt(),"\n")
            elif select == "2":
                main.getinput()
                print(main.decript(),"\n")
            elif select != "0":
                print("Invalid Input\n")
            else:
                break

if __name__ == "__main__":
    key={"a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i", "g": "j", "h": "k", "i": "l", "j": "m", "k": "n", "l": "o", "m": "p", "n": "q", "o": "r", "p": "s", "q": "t", "r": "u", "s": "v", "t": "w", "u": "x", "v": "y", "w": "z", "x": "a", "y": "b", "z": "c"}
    main= main(key=key)
    main.selector()
    quit