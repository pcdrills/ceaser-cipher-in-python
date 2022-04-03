print("\t CEASER CIPHER ENCRYPTION")
print('''--------------------------------------
****** * Welcome to Ceaser Cipher Encrption Program * ***********
----> written by pcdrills -> github.com/pcdrills
----> You Input a Number and the program checks if it's prime or not
--------------------------------------------------------------------------''')

# formula for all general cases below
# encrypting formula    c = (x + n) mod 26      -- c=encryted letter, x=plaintext letter, n=numberofshifts
# decryting formula     c = (x – n) mod 26      -- c=encryted letter, x=plaintext letter, n=numberofshifts


#this function handles all the encryption and decryption. the ceaser_option determines wether to encrypt or decrypt
#takes in plain text and the key

def ceaser(ceaser_option, p_text, key):
    if ceaser_option == 'encode':
        print('Encrypting.....')
    elif ceaser_option == 'decode':
        print('Decrypting.....')
    else:
        print(f"invalid command: {command}")
        return
    shifted_text = ''
    for letter in p_text:
        print(letter, '/', end='')
        if(letter == ' '):
            shifted_text += ' '
        elif letter in alphabet:
            index_of_letter = alphabet.index(letter)        #find index of letter in alphabet
            if ceaser_option == 'encode':
                shift_index = (index_of_letter + key) % 26  #calculate the index after the shift - - for encrypt
            else:
                shift_index = (index_of_letter - key) % 26  #calculate the index after the shift -- for decrypt
            shifted_letter = alphabet[shift_index]    #find the letter at the shift index
            shifted_text += shifted_letter        #sum up the letters after shifting
            print(shifted_letter, '\\', end='')
        else:
            print("Some letter(s) you input isn't in the alphabet")
            break;
    if ceaser_option == 'encode':
        print('\nEncryption complete.....')
        print(f"Text Value is: {shifted_text}")
    elif ceaser_option == 'decode':
        print('Decryption complete.....')
        print(f"Text Value is: {shifted_text}")
    print(".............................................................")


#this function just displays the help
def helping():
    print(''' Type 'encode' to encrypt , type 'decode' to decrypt\n 
    ==> means you should input a command commands (help, decode, encode)
    -->: means you should input your phrase (for both encrption and decrption)
    ))>: means you should input your key
    encode -- use encode to encryt a message
    decode -- use decode to decrypt a cipher text (encrypted message)
    help -- to display this help
    quit -- to exit the program
    Nb: encryption and decryption key must be a number
    ''')

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print("Available options are: help, encode, decode, quit")

quit = False
while not quit:
    command = input("==> ").lower()
    ceasercommands = ['encode', 'decode']
    if command in ceasercommands:
        option = command
        plain_text = input("input text/phrase: -->: ").lower()
        key = int(input("Enter key ))>: "))
        ceaser(option, plain_text, key)
        command=''
    elif command == 'help':
        helping()
    elif command == 'quit':
        print("Quiting...")
        quit == True
        break

    else:
        print("Command not found, type 'help' to get the guide")

print("--------------------pcdrills--------------------------")
