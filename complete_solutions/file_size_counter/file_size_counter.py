import glob
from os import stat
from os.path import isdir

def show_menu():
    menu_options = {
        1: 'Quick overview',
        2: 'Detailed overview',
        3: 'Exit'
    }

    while (True):
        print("Main menu")
        print("---------")
        for k in menu_options.keys():
            print(k, "-", menu_options[k])
        try:
            userinput = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number")
            continue

        if userinput == 1:
            show_quick_overview()
        elif userinput == 2:
            try:
                folder = get_folder_selection()
                show_detailed_overview(folder)
            except ValueError:
                continue
        else:
            exit(0)

def get_folder_selection():
    folder_options = {
        1: '/Users/martinbaumer/Documents',
        2: '/Users/martinbaumer/Downloads',
        3: '/Users/martinbaumer/Desktop',
        4: 'back to main menu'
    }
    while (True):
        print("Select a folder")
        print("---------")
        for k in folder_options.keys():
            print(k, "-", folder_options[k])
        try:
            userinput = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number")
            continue

        if userinput == 4:
            raise ValueError
        else:
            return folder_options[userinput]

def show_quick_overview():
    count_total_file_size('/Users/martinbaumer/Documents', False)
    count_total_file_size('/Users/martinbaumer/Downloads', False)
    count_total_file_size('/Users/martinbaumer/Desktop', False)

def get_files_in_directory(base_dir, recursive):
    if recursive:
        return glob.glob(base_dir + '/**/*.*', recursive=True)
    else:
        return glob.glob(base_dir + '/*.*', recursive=False)


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

def show_detailed_overview(folder):
    print('This is a detailed overview on %s'% (folder))

    largest_file = get_largest_file(folder)
    print('Largest file: %s, file size: %d' % (largest_file , get_file_stats(largest_file) % 1024))

    smallest_file = get_smallest_file(folder)
    print('Smallest file: %s, file size: %d' % (smallest_file, get_file_stats(smallest_file) % 1024))

def get_largest_file(base_dir):
    files = get_files_in_directory(base_dir, False)
    max_file_size = 0
    largest_file = ''
    for file in files:
        if get_file_stats(file) > max_file_size:
            largest_file = file
            max_file_size = get_file_stats(file)
    return largest_file

def get_smallest_file(base_dir):
    files = get_files_in_directory(base_dir, False)
    min_file_size = 30000000
    smallest_file = ''
    for file in files:
        if get_file_stats(file) < min_file_size:
            smallest_file = file
            min_file_size = get_file_stats(file)
    return smallest_file

if __name__ == '__main__':
    show_menu()
