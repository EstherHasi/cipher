
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)

def main():
    text = input('Enter your message: ')
    custom_key=input('Enter your key: ')

    encryption = encrypt(text,custom_key)
    print(f'\nEncrypted text: {encryption}')
    print(f'Key: {custom_key}')
    decryption = decrypt(encryption, custom_key)
    input(f'/nDo you want to see your original message?')
    print(f'/nDecrypted text: {decryption}\n')

if __name__ == '__main__':
    main()


