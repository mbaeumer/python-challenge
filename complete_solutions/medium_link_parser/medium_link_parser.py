
# open file
# loop through each line
# if it is a medium link, edit it

def read_links_from_file():
    links = []
    filename='/Users/martinbaumer/Documents/links/work-mac/2022/links_2022_w26_work_medium.txt'
    try:
      with open(filename, 'r') as file:
          for line in file:
              links.append(line)
    except FileNotFoundError as e:
        print("File could not be found")
    return links

def reparse_links(linkList):
    parsedlinks = []
    for link in linkList:
        if "medium.com" in link and "source=email" in link:
            print("valid link. Index = %d" % (link.find("source=email")))
            parsedlinks.append(link[0:link.find("?source=email")])
    return parsedlinks

def write_file(parsedLinks):
    filename = '/Users/martinbaumer/Documents/links/work-mac/2022/links_2022_w26_work_medium2.txt'
    with open(filename, 'w') as file:
        for link in parsedLinks:
            file.write(link)
            file.write("\n")


if __name__ == '__main__':
    originalList = read_links_from_file()
    parsedLinks = reparse_links(originalList)
    write_file(parsedLinks)

