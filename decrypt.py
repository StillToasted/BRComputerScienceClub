# ==========================================
# PART 2: CAESAR CIPHER DECRYPTION
# ==========================================

def decrypt(message, shift):
    result = ""

    for char in message:

        if char.isalpha():

            # TODO 4:
            # Convert the character into its ASCII value.

            # TODO 5:
            # Shift the letter BACKWARDS.

            # TODO 6:
            # Convert the ASCII value back to a letter
            # and append it to result.

            pass

        else:
            result += char

    return result


decrypted = decrypt(encrypted, shift)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
