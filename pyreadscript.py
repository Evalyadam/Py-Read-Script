import os

encryption_map = {
    "a": "bh", "b": "ih", "c": "rh", "d": "kh", "e": "oh", "f": "uh", "g": "mh", "h": "yh", "i": "ah",
    "j": "sh", "k": "wh", "l": "zh", "m": "qh", "n": "xh", "o": "ch", "p": "th", "q": "ph", "r": "nh",
    "s": "gh", "t": "lh", "u": "dh", "v": "fh", "w": "jh", "x": "eh", "y": "bh", "z": "vh",
    "A": "B1", "B": "I1", "C": "R1", "D": "K1", "E": "O1", "F": "U1", "G": "M1", "H": "Y1", "I": "A1",
    "J": "S1", "K": "W1", "L": "Z1", "M": "Q1", "N": "X1", "O": "C1", "P": "T1", "Q": "P1", "R": "N1",
    "S": "G1", "T": "L1", "U": "D1", "V": "F1", "W": "J1", "X": "E1", "Y": "B1", "Z": "V1",
    "0": "10", "1": "11", "2": "12", "3": "13", "4": "14", "5": "15", "6": "16", "7": "17", "8": "18",
    "9": "19", "!": "s!", "@": "s@", "#": "s#", "$": "s$", "%": "s%", "^": "s^", "&": "s&", "*": "s*",
    "(": "s(", ")": "s)", "-": "s-", "_": "s_", "=": "s=", "+": "s+", "[": "s[", "]": "s]", "{": "s{",
    "}": "s}", "\\": "s\\", "|": "s|", ";": "s;", ":": "s:", "'": "s'", "\"": "s\"", ",": "s,", ".": "s.",
    "<": "s<", ">": "s>", "/": "s/", "?": "s?", "`": "s`", "~": "s~", " ": "s "
}

# Create a reverse encryption map for decryption
decryption_map = {v: k for k, v in encryption_map.items()}

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def encrypt_text(text):
    encrypted_text = []
    for char in text:
        if char in encryption_map:
            encrypted_text.append(encryption_map[char])
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def decrypt_text(text):
    decrypted_text = []
    i = 0
    while i < len(text):
        for key_length in range(2, 4):  # Because keys are 2 or 3 characters long
            part = text[i:i+key_length]
            if part in decryption_map:
                decrypted_text.append(decryption_map[part])
                i += key_length
                break
        else:
            decrypted_text.append(text[i])
            i += 1
    return ''.join(decrypted_text)

def encrypt_file(input_file, output_file):
    text = read_file(input_file)
    encrypted_text = encrypt_text(text)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(encrypted_text)

def decrypt_and_execute_file(encrypted_file):
    text = read_file(encrypted_file)
    decrypted_text = decrypt_text(text)
    
    exec(decrypted_text)

def main():
    encrypt_or_decrypt = input("(E)ncrypt or (D)ecrypt (and run)? ").strip().lower()
    eod_choices = ["e", "d"]
    if encrypt_or_decrypt not in eod_choices:
        print("Invalid choice.")
        return

    if encrypt_or_decrypt == eod_choices[0]:  # Encrypt
        filename = input("Filename to encrypt: ").strip()
        if os.path.isfile(filename):
            base, _ = os.path.splitext(filename)
            output_file = f"{base}.pyreadscript"
            encrypt_file(filename, output_file)
            print(f"Encrypted content written to {output_file}")
        else:
            print(f"File {filename} does not exist.")
    elif encrypt_or_decrypt == eod_choices[1]:  # Decrypt and run
        filename_dnr = input("Filename to decrypt and execute: ").strip()
        if os.path.isfile(filename_dnr):
            decrypt_and_execute_file(filename_dnr)
        else:
            print(f"File {filename_dnr} does not exist.")

if __name__ == "__main__":
    main()
