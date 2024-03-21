from custom_models import database_manager
from option_manager import OptionManager


if __name__ == "__main__":
    repeat = 1
    while repeat != 0:
        try:
            OptionManager.display_options()
            option = OptionManager.get_option()
            OptionManager.validate_option(option)
        except Exception as error:
            print("Error: ", error)
        finally:
            if database_manager.db:
                database_manager.db.close()
                print("Database connection is closed !!")
            repeat = int(input(
                'Do you want to continue? Enter 0 to exit the program, or any other number to continue: '))
