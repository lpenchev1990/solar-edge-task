from django.core.management.base import BaseCommand
from pymongo import MongoClient
from my_app.models import MySQLModel  # Замести с модела си
from django.conf import settings
from mapSitemaps.models import ShopSitemap, ShopLink

class Command(BaseCommand):
    help = "Синхронизира данни от MySQL към MongoDB"

    def handle(self, *args, **kwargs):
        self.stdout.write("Започва синхронизацията...")

        # MongoDB клиент
        mongo_client = settings.MONGO_CLIENT
        mongo_db = mongo_client[settings.MONGO_DB_NAME]
        mongo_collection = mongo_db['my_collection']  # Замести с твоята колекция

        # Извличане на данни от MySQL
        data = ShopSitemap.objects.all().values()
        if not data:
            self.stdout.write("Няма данни за обработка.")
            return

        # Обработка и запис в MongoDB
        for record in data:
            print(record)

#             processed_data = self.process_data(record)
#             mongo_collection.update_one(
#                 {"_id": processed_data["_id"]},  # Уникален идентификатор
#                 {"$set": processed_data},
#                 upsert=True
#             )

        self.stdout.write("Синхронизацията приключи успешно.")

    def process_data(self, record):
        # Трансформирай данните тук, ако е нужно
        record["_id"] = record["id"]  # Например, използвай `id` като `_id`
        del record["id"]
        return record
