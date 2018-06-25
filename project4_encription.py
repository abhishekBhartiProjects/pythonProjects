alphabet = 'abcdefghijklmnopqrstuvwxyz'
message = raw_input('Please enter a message: ')
key = int(raw_input('Enter encription key (number between 1 to 25): '))
newMessage = ''

def encript(message, key):
    encriptedMessage = ''

    for character in message:
        if character in alphabet:
            position = alphabet.find(character)

            newPosition = (position + key) % 26
            newCharacter = alphabet[newPosition]
            encriptedMessage += newCharacter
        else:
            encriptedMessage += character

    return (encriptedMessage)

def decript(encriptedMessage, key):
    decriptedMessage = ''

    for character in encriptedMessage:
        if character in alphabet:
            position = alphabet.find(character)
            newPosition = (26 + (position - key)) % 26
            newCharacter = alphabet[newPosition]
            decriptedMessage += newCharacter
        else:
            decriptedMessage += character

    return (decriptedMessage)


encriptedMessage = encript(message, key)
decriptedMessage = decript(encriptedMessage, key)

print('Encripted message: '+ encriptedMessage)
print('Decript to original message: '+ decriptedMessage)



