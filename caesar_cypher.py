alphabet=['a','b','c','d','e',"f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
    
def caesar(original_text,shift_amount,encode_or_decode):
    output_text=""
    if encode_or_decode=='decode':
                shift_amount*=-1 
                
    for ltr in original_text:
        if ltr not in alphabet:
            output_text+=ltr
        else:
             
            shifted_position=alphabet.index(ltr)+shift_amount
            shifted_position%=len(alphabet)
            output_text+=alphabet[shifted_position]
    print(f'Here is your {encode_or_decode}d message {output_text}')
    
should_continue=True
while should_continue:
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt\n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type your shift number:\n")) 
           
    caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)
    restart=input("Would you like to go again Type 'yes' to continue and 'no' to stop\n").lower()
    if restart=='no':
        should_continue=False
        print('Goodbye')
    
    
