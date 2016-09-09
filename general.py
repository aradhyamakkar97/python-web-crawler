import os

# each website I crawl is a seperate project ( folder )

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('creating project '+directory)
        os.makedirs(directory)
