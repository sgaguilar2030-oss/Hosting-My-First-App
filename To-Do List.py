# To-Do list

todo_list = []

while True:   # <-- LOOP STARTS HERE :P
    print("\nWelcome to To-Do List! (>'v'<) Select a number from the options below:")
    print("1 = Add a to-do")
    print("2 = Remove a to-do")
    print("3 = Edit a to-do")
    print("4 = Show current to-do list")
    print("5 = End program")
    
    response = int(input("\nSelect a number: "))

    # ADD A TO-DO
    if response == 1:
        print("\nHow many to-dos would you like to add? (Min. = 1, Max. = 3): ")
        add_todo_number = int(input("Enter: "))

        if 1 <= add_todo_number <= 3:
            for i in range(add_todo_number):
                add = input("Enter a to-do: ")
                todo_list.append(add)

            ask = int(input("\nShow To-Do list? (1 = yes, 2 = no): "))
            if ask == 1:
                print("\nCurrent To-Do List:")
                for index, item in enumerate(todo_list, start=1):
                    print(f"{index}. {item}")
        else:
            print("\nInvalid number of items. o(TヘTo)")

    # REMOVE A TO-DO
    elif response == 2:
        if len(todo_list) == 0:
            print("\nNo items to remove. (┬┬﹏┬┬)")
        else:
            print("\nCurrent To-Do List:")
            for index, item in enumerate(todo_list, start=1):
                print(f"{index}. {item}")
            remove_num = int(input("Enter the number to remove: "))
            if 1 <= remove_num <= len(todo_list):
                todo_list.pop(remove_num - 1)
                print("Item removed! (～￣▽￣)～")
            else:
                print("Invalid number. ＞﹏＜")

    # EDIT A TO-DO
    elif response == 3:
        if len(todo_list) == 0:
            print("\nNo items to edit. (┬┬﹏┬┬)")
        else:
            print("\nCurrent To-Do List:")
            for index, item in enumerate(todo_list, start=1):
                print(f"{index}. {item}")
            edit_num = int(input("Enter the number to edit: "))
            if 1 <= edit_num <= len(todo_list):
                new_text = input("Enter new text: ")
                todo_list[edit_num - 1] = new_text
                print("Item updated! ( •̀ ω •́ )✧")
            else:
                print("Invalid number. ＞﹏＜")

    # SHOW LIST
    elif response == 4:
        print("\nCurrent To-Do List:")
        if len(todo_list) == 0:
            print("No to-dos yet.")
        else:
            for index, item in enumerate(todo_list, start=1):
                print(f"{index}. {item}")

    # END PROGRAM
    elif response == 5:
        print("\nGoodbye! q(≧▽≦q)")
        break   # <-- LOOP ENDS HERE :P

    else:
        print("\nInvalid input. Please try again. 〒▽〒")
