letter_dict = {"S": {"a": "Saturday", "u": "Sunday"}, "F": "Friday",
               "M": "Monday", "T": {"u": "Tuesday", "h": "Thursday"}, "W": "Wednesday"}

input_str = input("please input:") 
input_list = input_str.split()

if len(input_list) == 1:
    letter = input_list[0] 
    if letter in letter_dict: 
        result = letter_dict[letter] 
        if isinstance(result, dict): 
            print("please input second letter:") 
            second_letter = input() 
            if second_letter in result: 
                print(result[second_letter]) 
            else: 
                print("data error") 
        else: 
                print(result) 
    else: print("data error")
else: print("data error")
