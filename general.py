import os

# each website I crawl is a seperate project ( folder )

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('creating project '+directory)
        os.makedirs(directory)

# create queue and crawled files (if not created)
def create_data_files(project_name,base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name +'/crawled.txt'

    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')


# Creates a new file
def write_file(path,data):
    f = open(path,'w')
    f.write(data)
    f.close()

# Add data onto an existing file
def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data+'\n')

# Delete the contents of a file
def delete_file_content(path):
    with open(path,'w'):
        pass # i.e do nothing
