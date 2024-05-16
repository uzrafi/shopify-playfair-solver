# Program to solve Playfair Cipher
# Author: Uzair Rafi

def create_playfair_grid(key):
    # Remove duplicate characters from the key and replace J with I
    key = "".join(dict.fromkeys(key.replace("J", "I")))

    # Create the initial matrix with the key
    matrix = list(key)

    # Fill remaining grid with alphabet, if char not in matrix
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in matrix:
            matrix.append(char)

    # Shape into 5x5 grid
    matrix = [matrix[i:i+5] for i in range(0, 25, 5)]

    return matrix

def find_position(matrix, char):
    for row_idx, row in enumerate(matrix):
        if char in row:
            return row_idx, row.index(char)
    raise ValueError(f"'{char}' is not in the matrix")

def decrypt(ciphertext, key):
    # Create Playfair matrix
    matrix = create_playfair_grid(key)

    # Decrypt the ciphertext
    text = ""
    for i in range(0, len(ciphertext), 2):
        pair = ciphertext[i:i+2]
        
        # Convert 'J' to 'I'
        pair = pair.replace("J", "I")

        # Find positions of pairs in matrix
        row1, col1 = find_position(matrix, pair[0])
        row2, col2 = find_position(matrix, pair[1])

        # Decrypt pairs
        if row1 == row2:
            text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            text += matrix[row1][col2] + matrix[row2][col1]

    return text

key = "SUPERSPY"
encrypted_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

decrypted_text = decrypt(encrypted_text, key)
print(decrypted_text.replace('X', ''))
