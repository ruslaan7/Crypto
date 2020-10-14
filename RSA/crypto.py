def encrypt(word, e, n):
    encrypt_data = []

    for symbol in word:
        encrypt_data.append(pow(ord(symbol), e, n))
    return encrypt_data


def decrypt(encrypt_data, d, n):

    message = ''
    for symbol in encrypt_data:
        message += chr(pow(symbol, d, n))
    return message
