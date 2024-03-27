alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encrypt(plain_text, shift_key):
    cipher_text=""
    for char in plain_text:
        if char == ' ':
            cipher_text+=' '
            continue
        pos= alphabet.index(char)
        new_pos= (pos+shift_key)%26
        cipher_text += alphabet[new_pos]

    print(f"Your encrypted message is ={cipher_text}")    

def decrypt(encrypt_text, shift_key):
    plain_text=""
    for char in encrypt_text:
        if char == ' ':
            plain_text+=' '
            continue
        pos= alphabet.index(char)
        new_pos= (pos - shift_key)%26
        plain_text += alphabet[new_pos]

    print(f"Your decrypted message is ={plain_text}") 

end=True
while end:
    e_ord=input("If you want to do encryption then type encryption and if you you want to decrypt your message then type decryption: \n")
    message = input("Enter your message:\n")
    key = int(input("Enter your shift key:\n"))

    if e_ord=="encryption":
        encrypt(message, key)
    elif e_ord=="decryption":
        decrypt(message, key)
    again = input("type yes if you want to do again otherwise no:\n")
    if again=='no':
        end=False
        print("Ok Bye!!")
    
