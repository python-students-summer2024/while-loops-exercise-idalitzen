def get_starting_number():
    while True:
        get_number=input("How many bottles of beer on the wall? ").strip()
        if get_number.isnumeric():
            get_number=int(get_number)
            if get_number>=1:
                return get_number
            else:
                print("Invalid response")
        else:
            print("Invalid response")



def sing(get_starting_number):
        get_starting_number=int(get_starting_number)
        for i in range(get_starting_number):
            if get_starting_number>=2:
                print(f" {get_starting_number} bottles of beer on the wall, {get_starting_number} bottles of beer.")
                get_starting_number=get_starting_number-1
                if get_starting_number==1:
                    continue
                else:
                    print(f"Take one down, pass it around, {get_starting_number} bottles of beer on the wall.")
            elif get_starting_number==1:
                print(f"Take one down, pass it around, {get_starting_number} bottle of beer on the wall.")
                print(f" {get_starting_number} bottle of beer on the wall, {get_starting_number} bottle of beer.")
                print("Take it down, pass it around, no more bottles of beer on the wall!")

