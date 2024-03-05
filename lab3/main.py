def validate_input(text):
    for char in text:
        if not ('А' <= char <= 'Я' or 'а' <= char <= 'я' or char == ' '):
            return False
    return True

def vigenere_cipher(text, key, mode):
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    result = ''
    key_length = len(key)
    key = key.upper()
    text = text.upper().replace(' ', '')

    for i, char in enumerate(text):
        if mode == 'encrypt':
            shift = alphabet.index(char) + alphabet.index(key[i % key_length])
            result += alphabet[shift % len(alphabet)]
        elif mode == 'decrypt':
            shift = alphabet.index(char) - alphabet.index(key[i % key_length])
            result += alphabet[shift % len(alphabet)]
        else:
            raise ValueError("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
    return result

def main():
    while True:
        choice = input("Выберите операцию: \n1 - Зашифровать \n2 - Расшифровать \n3 - Выход: ")
        if choice == '1':
            message = input("Введите сообщение на русском языке: ")
            if not validate_input(message):
                print("Сообщение должно содержать только русские буквы и пробелы.")
                continue
            key = input("Введите ключ (длина ключа не менее 7 символов): ")
            if len(key) < 7:
                print("Длина ключа должна быть не менее 7 символов.")
                continue
            print("Зашифрованное сообщение:", vigenere_cipher(message, key, 'encrypt'))
        elif choice == '2':
            ciphertext = input("Введите криптограмму: ")
            key = input("Введите ключ (длина ключа не менее 7 символов): ")
            if len(key) < 7:
                print("Длина ключа должна быть не менее 7 символов.")
                continue
            print("Расшифрованное сообщение:", vigenere_cipher(ciphertext, key, 'decrypt'))
        elif choice == '3':
            print("До свидания!")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()
