from custom_models import database_manager, OrderManager
from diagram_manager import DiagramManager


class OptionManager:
    def display_options():
        print("-------------------------------------------------------", "\n",
              "** OPTIONS **", "\n",
              "-------------------------------------------------------", "\n",
              "1) Create Order table", "\n",
              "2) Plot count/month for selected product in 1 year", "\n",
              "3) Plot mean_price/month for selected product in 1 year", "\n",
              "4) Plot count/month for selected user in 1 year", "\n",
              "5) Plot total_price/month for selected user in 1 year", "\n",
              "6) Plot count/product for selected user in 1 year", "\n",
              "7) Plot 5 best_seller products in 1 year", "\n",
              "8) Plot orders_number/month for 1 year", "\n",
              "9) Plot total_price/month for 1 year", "\n",
              "-------------------------------------------------------")

    def get_option():
        option = int(input("Please select a number between 1 to 9: "))
        return option

    def validate_option(option: int):
        options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if (option in options) & (option == 1):
            OrderManager.create_orders()
            print("Table created !!")

        elif (option in options) & (option != 1):
            query, x_label, y_label, title = DiagramManager.create_params(
                option)
            results = database_manager.db.execute(query)
            DiagramManager.display_plot(x_label, y_label, title, results)
            print("Plot displayed !!")

        else:
            print("Invalid input! Please try again!")
