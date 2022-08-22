import sys

# open file
# loop through each line
# if it is a medium link, edit it

def check_args(args):
    try:
      if len(args)!=2:
        raise RuntimeError
    except RuntimeError as re:
        print("Provide exactly one argument")

def read_links_from_file(filename):
    links = []
    try:
      with open(filename, 'r') as file:
          for line in file:
              links.append(line)
    except FileNotFoundError as e:
        print("File could not be found")
    return links

def reparse_links(linkList):
    totalLinks = 0
    mediumLinks = 0
    parsedlinks = []
    for link in linkList:
        totalLinks = totalLinks + 1
        if "medium.com" in link and "source=email" in link:
            parsedlinks.append(link[0:link.find("?source=email")])
            mediumLinks = mediumLinks + 1
        else:
            parsedLinks.append(link)
    print("total number of rows processed: %d; number of medium links: %d" % (totalLinks, mediumLinks))
    return parsedlinks

def write_file(parsedLinks, filename):
    with open(filename, 'w') as file:
        for link in parsedLinks:
            file.write(link)
            file.write("\n")
    print("saved data to file: %s" % (filename))


if __name__ == '__main__':
    check_args(sys.argv)
    originalList = read_links_from_file(sys.argv[1])
    parsedLinks = reparse_links(originalList)
    write_file(parsedLinks, sys.argv[1])

