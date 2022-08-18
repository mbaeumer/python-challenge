import glob
import os


def count_total_file_size(base_dir):
    files = glob.glob(base_dir + '/**/*.*', recursive=True)
    total_size = 0
    for file in files:
        total_size = total_size + get_file_stats(file)
    filesize_in_megabytes = total_size % 1024
    print("Total file size: %d" % (filesize_in_megabytes))

def get_file_stats(filename):
  statresult = os.stat(filename)
  return statresult.st_size

if __name__ == '__main__':
    count_total_file_size('/Users/martinbaumer/Documents/fxlink-builds')
