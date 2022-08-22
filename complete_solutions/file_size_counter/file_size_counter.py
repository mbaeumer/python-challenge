import glob
from os import stat
from os.path import isdir


def count_total_file_size(base_dir, recursive):
    if recursive:
        files = glob.glob(base_dir + '/**/*.*', recursive=True)
    else:
        files = glob.glob(base_dir + '/*.*', recursive=False)

    total_size = 0
    for file in files:
        total_size = total_size + get_file_stats(file)
    filesize_in_megabytes = total_size % 1024
    print("Total file size of %s: %d" % (base_dir, filesize_in_megabytes))
    print("Total number of files of %s: %d" % (base_dir, len(files)))

def get_file_stats(filename):
    filesize = 0
    try:
        if not isdir(filename):
            statresult = stat(filename)
            filesize = statresult.st_size
    except FileNotFoundError as e:
      filesize = 0
    return filesize

if __name__ == '__main__':
    count_total_file_size('/Users/martinbaumer/Documents', False)
    count_total_file_size('/Users/martinbaumer/Downloads', True)
    count_total_file_size('/Users/martinbaumer/Desktop', False)
