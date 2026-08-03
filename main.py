if __name__ == "__main__": #checking if the script is independently run
    print("Conduit - The Middle Man")

    main_loop_bool_checker = True

    while main_loop_bool_checker:
        main_user_input = input("Enter Command: ")

        if main_user_input == "quit":
            main_loop_bool_checker = False;
        else:
            import core.validator #importing the validator python script from the core repository
            core.validator.first_phase_checker(main_user_input) #calling the function declared in the validator script, the raw user input is entirely parsed to the function
