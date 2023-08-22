katz_deli = []

def line(katz_deli):
    if not katz_deli:
        line_message = "The line is currently empty."
        print(line_message)
    else:
        line_message = "The line is currently:"
        # # for index, customer in enumerate(katz_deli, start=1):
        #     line_message += f" {index}. {customer}"
        for i in range(len(katz_deli)): 
            line_message += f" {i + 1}. {katz_deli[i]}"
        print(line_message)

def take_a_number(katz_deli, new_customer):
    katz_deli.append(new_customer)
    position = len(katz_deli)
    print(f"Welcome, {new_customer}. You are number {position} in line.")

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
        return
    
    serving_customer = katz_deli.pop(0)
    print(f"Currently serving {serving_customer}.")