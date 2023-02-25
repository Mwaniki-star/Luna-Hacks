# convert integer to roman numerals
def int_to_roman(num: int)->str:
    roman_num={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
    roman=''

    for value,symbol in roman_num.items():
        while num>=value:
            roman+=symbol
            num-=value
    return roman

    # Convert Roman numerals to Integer.
def roman_to_int(roman: str)->int:
    roman_num={'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
    
    num=0
    prev_value=0

    for symbol in roman:
        curr_value=roman_num[symbol]
        num+=curr_value
        if curr_value>prev_value:
            num-=2*prev_value
        prev_value=curr_value
    return num

            # Prompt user to enter input and convert to other formart
while True:
    user_choice=input("Enter '1' to convert an integer to roman number or '2' to convert roman number to interger: ")
    if user_choice=='1':
        num=int(input("ENTER INTEGER TO CONVERT TO ROMAN NUMBER:"))
        roman= int_to_roman(num)
        print(f"{num} TO ROMAN NUMBER IS {roman}")
        break
    elif user_choice=='2':
        roman=input("ENTER ROMAN NUMBER TO CONVERT TO INTEGER:")
        num= roman_to_int(roman)
        print(f"{roman} TO INTEGER IS {num}")
        break
    else:
        print("Invalid input. Please Enter '1' or '2'")


