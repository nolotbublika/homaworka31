
import multiprocessing


class WarehouseManager:
    def __init__(self):
        self.data = {}

    def process_request(self, request):
        product, action, quantity = request
        if action == "receipt":
            self.data[product] = self.data.get(product, 0) + quantity
        elif action == "shipment":
            if product in self.data:
                self.data[product] = max(0, self.data[product] - quantity)

    def run(self, requests):
        processes = []
        for request in requests:
            p = multiprocessing.Process(target=self.process_request, args=(request,))
            processes.append(p)
            p.start()
        for p in processes:
            p.join()

# Создаем менеджера склада
manager = WarehouseManager()

# Множество запросов на изменение данных о складских запасах
requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]

# Запускаем обработку запросов
manager.run(requests)

# Выводим обновленные данные о складских запасах
print(manager.data)


