from CC import alphabet

# Write Code 💻


def caeser(start_Text, shift_Amount, ciper_Action):
    final_Text = ""
    shift_Amount %= len(alphabet)

    if ciper_Action == "decode":
        shift_Amount *= -1

    for char in start_Text:
        if char in alphabet:
            start_index = alphabet.index(char)
            shifted_Index = start_index + shift_Amount
            final_Text += alphabet[shifted_Index]
        else:
            final_Text += char

    print(f"\n\nKaede : Your {ciper_Action}d Text's Result -> {final_Text}\n")


is_Continue = True

while is_Continue:
    action = input(
        "\n\nKaede : Type 'encode' To Encrypt, Type 'decode' To Decrypt Text -> ")
    text = input("\n\nKaede : Type Your Message -> ").lower()
    shift = int(input("\n\nKaede : Type The Shift Number -> "))

    caeser(start_Text=text, shift_Amount=shift, ciper_Action=action)

    continue_Program = input(
        "\nKaede : Would You Like To Restart The Program? Y/N -> ")

    if continue_Program == "y":
        is_Continue = True

    else:
        is_Continue = False
        print("\n\nKaede : GoodBye ~ \n\n")
