MORSE_CODE_DICT = { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.','0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-', ' ':'/'}
is_running = True

def text_to_morse(text):
    morse_text = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_text += MORSE_CODE_DICT[char] + ' '
        else:
            morse_text+='/' # indicates a space
    return morse_text


def morse_to_text(morse_text):
    morse_text=morse_text.split(' ')
    text=''
    for code in morse_text:
        for key,value in MORSE_CODE_DICT.items():
            if code == value :
                text += key
    return text



def main():
    global is_running
    print("Choose an option:")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")
    print("3. Exit")

    choice = input()

    if choice == '1':
        text_input = input("Enter the text: ")
        morse_output = text_to_morse(text_input)
        print(f"Morse Code: {morse_output}")
    elif choice == '2':
        morse_input = input("Enter the Morse code (use '/' for space): ")
        text_output = morse_to_text(morse_input)
        print(f"Text: {text_output}")
    elif choice == '3':
        print("Goodbye!")
        is_running=False  
    else:
        print("Invalid choice. Please enter '1' or '2'.")

while is_running:
    main()
