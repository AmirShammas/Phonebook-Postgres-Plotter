import random
import peewee
import local_settings
from database_manager import DatabaseManager


database_manager = DatabaseManager(
    database_name=local_settings.DATABASE['name'],
    user=local_settings.DATABASE['user'],
    password=local_settings.DATABASE['password'],
    host=local_settings.DATABASE['host'],
    port=local_settings.DATABASE['port'],
)


class Order(peewee.Model):
    user = peewee.CharField(max_length=255, null=False, verbose_name='User')
    product = peewee.CharField(
        max_length=255, null=False, verbose_name='Product')
    month = peewee.IntegerField(null=False, verbose_name='Month')
    price = peewee.IntegerField(null=False, verbose_name='Price')
    count = peewee.IntegerField(null=False, verbose_name='Count')
    total_price = peewee.IntegerField(null=False, verbose_name='TotalPrice')

    def save(self, *args, **kwargs):
        self.total_price = self.price * self.count
        super().save(*args, **kwargs)

    class Meta:
        database = database_manager.db
        table_name = 'OrderTB'


class OrderManager:
    def create_orders():
        database_manager.create_tables(models=[Order])
        for _ in range(500):
            Order.create(user=f"user{random.randint(1, 10)}", product=f"product{random.randint(1, 10)}", month=random.randint(
                1, 12), price=random.randint(1000, 10000), count=random.randint(1, 20))
