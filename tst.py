import inspect
from logger import PlacedTradesLogger

logger = PlacedTradesLogger('DEL')

print(logger.__doc__)
print('---')
print(logger.create_log_file.__doc__)