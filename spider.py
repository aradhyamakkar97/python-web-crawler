from urllib.request import urlopen
from link_finder import LinkFinder
from genera import *


class Spider:

    #class variables (shares among all instances)

    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self):
