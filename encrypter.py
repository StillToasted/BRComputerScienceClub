# ==========================================
# PART 1: CAESAR CIPHER ENCRYPTION
# ==========================================

message = "HELLO WORLD"
shift = 3


def encrypt(message, shift):
    result = ""

    for char in message:

        if char.isalpha():

            # TODO 1:
            # Convert the character into its ASCII value.

            # TODO 2:
            # Shift the letter forward by 'shift' positions.
            # Hint: Use % 26 to wrap around the alphabet.

            # TODO 3:
            # Convert the new ASCII value back to a letter
            # and append it to result.

            pass

        else:
            result += char

    return result


encrypted = encrypt(message, shift)

print("Original:", message)
print("Encrypted:", encrypted)
