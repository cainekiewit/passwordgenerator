from random import randint
   
def load_pass():
    #declare variables to read and store data from the text file
    pass_store = []
    count = 0

    #store password list
    with open("password_store.txt", "r") as st:
        for line in st:
            pass_store.append(decrypt(line))
    print("Loaded.")
    return pass_store

def view_pass():
    #declare variables to read and store data from the text file
    pass_store = []
    count = 0

    #store password list
    with open("password_store.txt", "r") as st:
        for line in st:
            pass_store.append(decrypt(line))
    print("Loaded.")
    while len(pass_store) > count:
        print(pass_store[count])
        count += 1
    
    return pass_store

#function that will return a password and accepts the length of the password as a parameter
def pass_generate():
    length = int(input("Enter the password length:\n"))
    count = 0
    password = ""

    #chars to use in the generation of the password
    alphanumeric = "a/b/c/d/e/f/g/h/i/j/k/l/m/n/o/p/q/r/s/t/u/v/w/x/y/z".split("/")
    alphanumeric += ("a/b/c/d/e/f/g/h/i/j/k/l/m/n/o/p/q/r/s/t/u/v/w/x/y/z".upper()).split("/")
    alphanumeric += "1/2/3/4/5/6/7/8/9/0".split("/")

    #generate password
    while count < length:
        password += str(alphanumeric[randint(0, 61)])
        count += 1
   
    return password

#will store the password under a given name
def store_pass():
    print("Loading...")
    pass_store = load_pass()    
    #add new passwords to password list variable
    pass_store.append(input("Enter the name of the password:\n"))
    pass_store.append(pass_generate())

    #declare variables used to write to the text file
    temp_store = "";
    count = 0
    safe = open("password_store.txt", "w", encoding = "utf-8-sig")

    #create a string to write to the text file
    while count < len(pass_store):
        if str(pass_store[count]).endswith("\n"):
            temp_store += encrypt(str(pass_store[count]))
        else:
            temp_store += encrypt(str(pass_store[count]))+"\n"
        count += 1
    
    #write to text file and close
    safe.write(temp_store)
    safe.close()
    print("Password stored")

def load_cipher():
    key = "zy,xw,vu,ts,rq,po,nm,lk,ji,hg,fe,dc,ba,12,34,56,78,90,!@,&#,.$,{},[],()".split(",")
    key += "UNCONFIRMED,MEANINGLESS,yz,wx,uv,st,qr,op,mn,kl,ij,gh,ef,cd,ab,21,43,65,87,09,@!".split(",")
    key += "#&,$.,}{,][,)(,unconfirmed,meaningless,@@,..,&&,**,^^,!!,$$,%%,##,??".split(",")

    key_dic = {}
    count = 0
    for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890":
        key_dic.update({char:key[count]})
        count += 1
    return key_dic

def load_decipher():
    cipher = load_cipher()
    
    #switch key around
    count = 0
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    de_key = {}
    for each in cipher:
        de_key.update({cipher[each]:alphabet[count]})
        count += 1
    return de_key
    
def encrypt(message):
    #cipher text
    cipher = load_cipher()
    text_no_spaces = message.split(" ")
    temp = ""
    encrypted_text = []
    count = 0
    while len(text_no_spaces) > count:
        for char in text_no_spaces[count]:
            temp += cipher[char]
        encrypted_text.append(temp)
        temp = ""
        count += 1

    encrypted_text = " ".join(encrypted_text)
    return encrypted_text

def decrypt(message):
    decipher = load_decipher()
    
    #decipher text
    text_no_spaces = message.split(" ")
    temp = ""
    decrypted_text = []
    count = 0
    cipher_count = 0
    text_blocks = []
    
    while len(text_no_spaces) > count:
        for char in text_no_spaces[count]:
            temp += char
            if temp in decipher:
                text_blocks.append(decipher[temp])
                temp = ""
                cipher_count = 0
            else:
                cipher_count += 1
        decrypted_text.append("".join(text_blocks))
        count += 1
        text_blocks = []
        cipher_count = 0
        temp = ""
    decrypted_text = " ".join(decrypted_text)
    return decrypted_text

def menu():
    option = "re"
    while option == "re":
        
        print("Instructions for using Password Generator Beta:")
        print("-"*80)
        print("'gen' : Generate a new password")
        print("'dec' : Decrypt message encrypted with this program")
        print("'enc' : Encrypt a message")
        print("'view': View encrypted passwords")
        print("'quit': Quit the program")
        option = input("Enter what you would like to do: ")

        if option == "gen":
            option = "re"
            store_pass()

        elif option == "dec":
            option = "re"
            print(decrypt(input("Enter a message you would like to decrypt")))
            
        elif option == "enc":
            option = "re"
            print(encrypt(input("Enter a message you would like to encrypt")))
            
        elif option == "view":
            view_pass()
            while option.lower() != "yes":
                option = input("Enter 'yes' when you are done viewing.")
            option = "re"
        elif option == "quit":
            print("Come again soon.")
        else:
            print("*"*80)
            print("You entered an invalid option, please look at the instructions and try again")
            print("-"*80)
            option = "re"

menu()
