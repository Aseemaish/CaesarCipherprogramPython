def caesar(text, shift, direction):     #Caesar function combined with encrypt and decrypt
    if shift > 26:      #checking if the shift is greater than 26
        shift = shift % 26      #getting the remainder of the shift divided by 26 so as to get the shift within the range of 26
    new_text = ""   #creating an empty string
    for letter in text:     #looping through the text
        if letter in alphabet:      #checking if the letter is in the alphabet
            new_index = 0       #setting the new_index to 0
            position = alphabet.index(letter)       #getting the position of the letter in the alphabet list
            if direction == "encode":       #checking if the direction is encode
                new_index = position + shift        #adding the shift to the position
            elif direction == "decode":     #checking if the direction is decode
                new_index = position - shift        #subtracting the shift from the position
                if new_index < 0:       #checking if the new_index is less than 0
                    new_index += 26     #adding 26 to the new_index
            new_text += alphabet[new_index]        #adding the new_index to the new_text
        else:
            new_text += letter      #adding the letter to the new_text
    return new_text     #returning the new_text
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
# def encrypt(text, shift): Encrypt function alone
#     new_text = ""     creating an empty string
#     for letter in text:   looping through the text
#         if letter in alphabet:    #checking if the letter is in the alphabet
#             position = alphabet.index(letter)   #getting the position of the letter in the alphabet list
#             new_index = position + shift  #adding the shift to the position
#         new_text += alphabet[new_index]   #adding the new_index to the new_text
#     return new_text   #returning the new_text
#
#
# def decrypt(text, shift):     #Decrypt function alone
#     new_text = ""     #creating an empty string
#     for letter in text:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             new_index = position - shift  #subtracting the shift from the position
#             if new_index < 0:     #checking if the new_index is less than 0
#                 new_index += 26       #adding 26 to the new_index
#             new_text += alphabet[new_index]
#     return new_text


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

cont = True
while cont:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    print(caesar(text, shift, direction))
    yorn = input("Do you want to continue? (yes/no): ")
    if yorn == "no":
        cont = False
        print("Goodbye!")
