# match-case example

user_name = "Dave"

match user_name:
    case "Dave":
        print("\nGet off my computer Dave!")
    case "angela_catlady_87":
        print("\nI know it is you, Dave! Go Away!")
    case "Codecademy":
        print("\nAccess Granted")
    case default:
        print("\nUsername not recognized")