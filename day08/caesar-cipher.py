alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to descript: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))


def encrypt(original_text: str, shift_amount: int) -> str:
    encrypt_text = ""

    for letter in original_text:
        position = alphabet.index(
            letter) + shift_amount  # position of each letter in the alphabet a=0, b=1 + shift_amount

        if position > 25:  # starts in a=0 and z=25
            position -= 25
            encrypt_text += alphabet[position - 1]  # starts in zero
        else:
            encrypt_text += alphabet[position]

    return f"Here's the encoded result: {encrypt_text}"


print(encrypt(original_text=text, shift_amount=shift))
