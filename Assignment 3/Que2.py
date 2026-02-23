# Q2. Write a program to input any alphabet and check whether it is vowel or consonant.

alphabet=input("Enter an alphabet: ")
if(alphabet.lower() in ['a','e','i','o','u']):
    print("The alphabet is a vowel.")
else:
    print("The alphabet is a consonant.")