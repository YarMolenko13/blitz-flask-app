from app import manager
from main import *


# python manager.py db init - для иницилизации 
# python manager.py db migrate - для создания миграции
# python manager.py db upgrade - для применения изменений


if __name__ == '__main__':
	manager.run()