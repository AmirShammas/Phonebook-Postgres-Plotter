from custom_models import Order
from peewee import fn
import matplotlib.pyplot as plt


class DiagramManager:
    def create_params(option: int):

        x_labels = ['Month', 'Month', 'Month', 'Month',
                    'Product', 'Product', 'Month', 'Month']
        x_label = x_labels[option - 2]
        y_labels = ['Count', 'Mean Price', 'Count', 'Total Price',
                    'Count', 'Count', 'Orders Number', 'Total Price']
        y_label = y_labels[option - 2]
        titles = ['Count/Month for selected product', 'Mean Price/Month for selected product', 'Count/Month for selected user', 'Total Price/Month for selected user',
                  'Count/Product for selected user', 'Count/Product for 1 year', 'Orders Number/Month for 1 year', 'Total Price/Month for 1 year']
        title = titles[option - 2]

        if option == 2:
            selected_product = input("Please enter the product's name: ")
            if Order.select().where(Order.product == selected_product).exists():
                query = Order.select(Order.month, fn.SUM(Order.count).alias('total_count')).where(
                    (Order.product == selected_product) & Order.month.between(1, 12)).group_by(Order.month).order_by(Order.month)
            else:
                print("The product's code is not correct !!")

        elif option == 3:
            selected_product = input("Please enter the product's name: ")
            if Order.select().where(Order.product == selected_product).exists():
                query = Order.select(Order.month, fn.AVG(Order.price).alias('mean_price')).where(
                    (Order.product == selected_product) & Order.month.between(1, 12)).group_by(Order.month).order_by(Order.month)
            else:
                print("The product's code is not correct !!")

        elif option == 4:
            selected_user = input("Please enter the user's code: ")
            if Order.select().where(Order.user == selected_user).exists():
                query = Order.select(Order.month, fn.SUM(Order.count).alias('total_count')).where(
                    (Order.user == selected_user) & Order.month.between(1, 12)).group_by(Order.month).order_by(Order.month)
            else:
                print("The user's code is not correct !!")

        elif option == 5:
            selected_user = input("Please enter the user's code: ")
            if Order.select().where(Order.user == selected_user).exists():
                query = Order.select(Order.month, fn.SUM(Order.total_price).alias('total_price')).where(
                    (Order.user == selected_user) & Order.month.between(1, 12)).group_by(Order.month).order_by(Order.month)
            else:
                print("The user's code is not correct !!")

        elif option == 6:
            selected_user = input("Please enter the user's code: ")
            if Order.select().where(Order.user == selected_user).exists():
                query = Order.select(Order.product, fn.SUM(Order.count).alias('total_count')).where(
                    (Order.user == selected_user) & Order.month.between(1, 12)).group_by(Order.product).order_by(fn.SUM(Order.count))
            else:
                print("The user's code is not correct !!")

        elif option == 7:
            query = Order.select(Order.product, fn.SUM(Order.count).alias('total_count')).where(
                Order.month.between(1, 12)).group_by(Order.product).order_by(fn.SUM(Order.count).desc()).limit(5)

        elif option == 8:
            query = Order.select(Order.month, fn.COUNT(Order.id).alias(
                'orders_number')).group_by(Order.month).order_by(Order.month)

        elif option == 9:
            query = Order.select(Order.month, fn.SUM(Order.total_price).alias(
                'total_price')).group_by(Order.month).order_by(Order.month)

        return query, x_label, y_label, title

    def display_plot(x_label, y_label, title, results):
        x_s = []
        y_s = []
        for result in results:
            x = result[0]
            y = result[1]
            x_s.append(x)
            y_s.append(y)
        plt.bar(x_s, y_s, width=0.2)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()
