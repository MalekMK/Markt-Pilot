import asyncio
import csv
import logging
from utils import main

logger = logging.getLogger('websockets.client')
logger.disabled = True
asyncio.get_event_loop().run_until_complete(main())
