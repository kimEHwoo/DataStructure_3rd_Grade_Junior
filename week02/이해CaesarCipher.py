class CaesarCipher:
  ''' Class for doing encryption and decryption using a Caesar Cipher'''

  def __init__(self, shift):
    ''' Construct Caesar cipher using given integer shift for rotation'''

    encoder = [None] * 26           # temp array for encryption
    decoder = [None] * 26           # temp array for decryption
    for k in range(26):
      encoder[k] = chr((k+shift) % 26 + ord('A'))   # Encrypt each character by shifting it by 'shift' positions
      decoder[k] = chr((k-shift) % 26 + ord('A'))   # Decrypt each character by shifting it back by 'shift' positions
    self._forward = ''.join(encoder)      # store as string for encryption
    self._backward = ''.join(decoder)     # store as string for decryption
    # +ord('A')를 한 이유
    # ASCHII CODE 에서 A에 해당하는 수자를 더해줘야
    # 나머지 알파벳의 숫자들이 맞아지기 때문이다.

  def encrypt(self, message):
    ''' return string representing encrypted message'''
    return self._transform(message, self._forward)   # Use the encryption key to encrypt the message

  def decrypt(self, secret):
    ''' return string representing decrypted message'''
    return self._transform(secret, self._backward)  # Use the decryption key to decrypt the secret message

  def _transform(self, original, code):
    ''' Utility to perform transformation based on given code string'''
    msg = list(original)    # Convert the message to a list of characters
    for k in range(len(msg)):
      if msg[k].isupper():
        j = ord(msg[k]) - ord('A')  # Get the index of the character in the alphabet (0 to 25)
        msg[k] = code[j]            # Replace this character with the corresponding character from the code
    return ''.join(msg)   # Convert the list of characters back to a string and return it
    # 대문자만 인덱스로 변환, 소문자는 암호화, 복호화 x'


if __name__ =='__main__':
  cipher = CaesarCipher(3)    # Create a CaesarCipher object with a shift of 3
  message = "THE EAGLES IN play; MEET AT JOE'S"    # Message to be encrypted
  coded = cipher.encrypt(message)    # Encrypt the message
  print('Secret:', coded)    # Print the encrypted message
  answer = cipher.decrypt(coded)    # Decrypt the encrypted message
  print('Message:', answer)    # Print the decrypted message
