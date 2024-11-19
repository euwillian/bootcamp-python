alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(original_text: str, shift_amount: int) -> str:
    encrypt_text = ""

    for letter in original_text:
        if not letter.isalpha():
            encrypt_text += letter
            continue

        position = alphabet.index(
            letter) + shift_amount  # position of each letter in the alphabet a=0, b=1 + shift_amount

        if position > 25:  # starts in a=0 and z=25
            position %= len(alphabet)  # position = position % 26
            encrypt_text += alphabet[position - 1]  # starts in zero
        else:
            encrypt_text += alphabet[position]

    return f"Here's the encoded result: {encrypt_text}"


def decrypt(original_text: str, shift_amount: int) -> str:
    decrypt_text = ""

    for letter in original_text:
        if not letter.isalpha():
            decrypt_text += letter
            continue

        position = alphabet.index(
                letter) - shift_amount  # position of each letter in the alphabet a=0, b=1 - shift_amount

        if position < 0:
            position += len(alphabet)
            decrypt_text += alphabet[position + 1]
        else:
            decrypt_text += alphabet[position]

    return f"Here's the decoded result: {decrypt_text}"


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to descript: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    if direction == "encode":
        print(encrypt(original_text=text, shift_amount=shift))  # hello = khoor // 3
    elif direction == "decode":
        print(decrypt(original_text=text, shift_amount=shift))  # khoor = hello // 3
    elif direction == "exit":
        break
    else:
        print("Invalid option!")
