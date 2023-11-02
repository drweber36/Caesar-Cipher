# *** Message Encoder / Decoder Version 1.0 *** #


num_to_letter = dict(zip(range(26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
letter_to_num = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(26)))

# Get the users decision: encode or decode
def user_decision():
    while True:
        print()
        print("Would you like to Encode a message or Decode?")
        print()
        user_choice = input("Enter e / d: ").strip().lower()
        if user_choice == "e" or user_choice == "d":
            return user_choice
        else:
            print("Please enter a valid input (e / d).")  

# Encode 
def initiate_encoder():
    plaintext_encode = input("Enter the message you would like to decode: ")
    print()
    key = int(input("Enter the key for this message (1 - 26): "))
    cipher_message = ""
    for c in plaintext_encode.upper():
        if c.isalpha():
            cipher_message += num_to_letter[(letter_to_num[c] + key)%26]
        else:
            cipher_message += c
    return cipher_message

# Decode
def initiate_decoder():
    plaintext_decode = input("Enter the message you would like to decode, as well as the key for this message (1 - 26): ")
    print()
    key = int(input("Enter the key for this message (1 - 26): "))
    decipher_message = ""
    for c in plaintext_decode.upper():
        if c.isalpha():
            decipher_message += num_to_letter[(letter_to_num[c] - key)%26]
        else:
            decipher_message += c
    return decipher_message
   
# main function to run encode or decode functions
def main ():
    user_choice = user_decision()
    if user_choice == "e":
        result = initiate_encoder()
    elif user_choice == "d":
        result = initiate_decoder()
    else:
        result = "Invalid Choice"
    
    print("Message:", result)

main()


