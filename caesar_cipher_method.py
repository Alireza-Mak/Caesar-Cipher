from caesar_cipher_word import alphabet

def encodeOrDecode(message,shift, type):
  messageArray = []
  resultMessage=''
  for letter in message:
    messageArray.append(letter)
  
  for letter in messageArray:
    if letter in alphabet:
      indexLetter = alphabet.index(letter)

      if type =="encode":
        finalIndex = indexLetter + shift
      else:
        finalIndex = indexLetter - shift

      if finalIndex > len(alphabet) -1:
        finalIndex = finalIndex % len(alphabet) 
      elif finalIndex < 0:
        finalIndex = finalIndex % len(alphabet) - len(alphabet)
      resultMessage += alphabet[finalIndex]    
    elif letter ==" ":
      resultMessage += " "  
    else:
      resultMessage += letter 
      
  
  return resultMessage

