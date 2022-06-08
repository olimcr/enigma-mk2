#https://en.wikipedia.org/wiki/Enigma_rotor_details#Rotor_wiring_tables
firstRotor=[10,7,4,17,15,24,21,19,3,1,13,9,6,18,22,20,16,14,5,23,11,2,12,26,25,8] #rotor I 1941
secondRotor=[14,20,26,16,19,6,2,15,11,13,23,18,3,10,4,9,22,12,1,5,25,21,24,8,7,17] #rotor II 1941
thirdRotor=[10,22,9,21,2,8,20,3,4,25,1,11,5,17,26,16,15,19,7,24,14,18,13,23,6,12] #rotor III 1941
reflector=[5,10,13,26,1,12,25,24,22,2,23,6,3,18,17,21,15,14,20,19,16,9,11,8,7,4] #Reflector A unknown date

def push_array(rotorNum):
    global firstRotor
    global secondRotor
    global thirdRotor
    match rotorNum:
        case 1:
            firstRotor = firstRotor[-1:] + firstRotor[:-1]
        case 2:
            secondRotor = secondRotor[-1:] + secondRotor[:-1]
        case 3:
            thirdRotor = thirdRotor[-1:] + thirdRotor[:-1]

#first turnover notch from q-r second from e-f and third from v-w
#https://en.wikipedia.org/wiki/Enigma_rotor_details#Turnover_notch_positions

def rotate_rotor(rotorNum):
    match rotorNum:
        case 1:
            push_array(1)
            if(firstRotor[0]==18):
                rotate_rotor(2)
        case 2:
            push_array(2)
            if(secondRotor[0]==6):
                rotate_rotor(3)
        case 3:
            push_array(3)

def char_to_number(char):
    return ord(char)-96

def number_to_char(number):
    return chr(number+96)

def input_validation(inputString):
    outputString=""
    for i in range(len(inputString)):
        if(ord(inputString[i])>96 and ord(inputString[i])<123):
            outputString+=inputString[i]
    return outputString

testString=input("Enter lowercase string to encrypt: ")
testString=input_validation(testString)
outputString=""
for i in range(len(testString)):
    charNumber=char_to_number(testString[i])
    charNumber=firstRotor[charNumber-1]
    charNumber=secondRotor[charNumber-1]
    charNumber=thirdRotor[charNumber-1]
    charNumber=reflector[charNumber-1]
    charNumber=thirdRotor.index(charNumber)
    charNumber=secondRotor.index(charNumber+1)
    charNumber=firstRotor.index(charNumber+1)
    rotate_rotor(1)
    outputString+=(number_to_char(charNumber+1))
    i+=1

print(outputString)
