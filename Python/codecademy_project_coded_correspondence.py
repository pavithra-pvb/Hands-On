alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
translated_message = ""
for letter in message:
    if not letter in punctuation:
        letter_value = alphabet.find(letter)
        translated_message += alphabet[(letter_value + 10) % 26]
    else:
        translated_message += letter
print(translated_message)

message_for_v = "hey vishal! This is a super cool cipher, thanks for showing me! What else you got?"
translated_message = ""
for letter in message_for_v:
    if not letter in punctuation:
        letter_value = alphabet.find(letter)
        translated_message += alphabet[(letter_value - 10) % 26]
    else:
        translated_message += letter
print(translated_message)


# both of these functions need the strings `alphabet` and `punctuation` defined before being run
def decoder(message, offset):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value + offset) % 26]
        else:
            translated_message += letter
    return translated_message


def coder(message, offset):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value - offset) % 26]
        else:
            translated_message += letter
    return translated_message


message_one = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."

# Now we'll print the output of `decoder` for the first message with an offset of 10
print(decoder(message_one, 10))

# Now we know what offset to use for the second message, so we use that to solve.
message_two = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

print(decoder(message_two, 14))

coded_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

# The easiest way to break this code is to simply brute force though all of the possible shifts.
# We'll only need to try 25 different shifts, so it's not computationally expensive. Then we can
# look through all of the outputs and look for the one that in english, and we've decoded our message!
for i in range(1,26):
    print("offset: " + str(i))
    print("\t " + decoder(coded_message, i) + "\n")


def vigenere_decoder(coded_message, keyword):
    letter_pointer = 0
    keyword_final = ''
    for i in range(0,len(coded_message)):
        if coded_message[i] in punctuation:
            keyword_final += coded_message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)
    translated_message = ''
    for i in range(0,len(coded_message)):
        if not coded_message[i] in punctuation:
            ln = alphabet.find(coded_message[i]) - alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += coded_message[i]
    return translated_message

message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = "friends"

print(vigenere_decoder(message, keyword))

def vigenere_coder(message, keyword):
    letter_pointer = 0
    keyword_final = ''
    for i in range(0,len(message)):
        if message[i] in punctuation:
            keyword_final += message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)
    translated_message = ''
    for i in range(0,len(message)):
        if message[i] not in punctuation:
            ln = alphabet.find(message[i]) + alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += message[i]
    return translated_message

message_for_v = "thanks for teaching me all these cool ciphers! you really are the best!"
keyword = "besties"

print(vigenere_coder(message_for_v,keyword))
print(vigenere_decoder(vigenere_coder(message_for_v, keyword), keyword))