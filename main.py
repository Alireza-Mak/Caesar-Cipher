from caesar_cipher_art import logo, creator
from caesar_cipher_method import encodeOrDecode
import os

end_of_program = False

while not end_of_program:
  print(logo)
  type =input ("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  while not (type == "encode" or  type  == "decode"):
    type =input ("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  
  message =input ("Type your message:\n").lower()
  shift =int(input ("Type the shift:\n"))
  print(f"Here's the encoded result: {encodeOrDecode(message,shift,type)}")

  resetProgram =input ("Type 'yes' if you wnat to go again. Otherwise type 'no:\n")
  while resetProgram != "yes" and resetProgram !="no":
    resetProgram =input ("Type 'yes' if you wnat to go again. Otherwise type 'no:\n")
  if(resetProgram =="no"):
    end_of_program = True
    os.system('cls')
    print(f"\n👋👋 Good bye. 👋👋\nCreated by:\n{creator}")




