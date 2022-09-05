
def sets_demo():
  # create a set
  first_set = {"one", "two", "three"}
  print(first_set)
  second_set=set(("one", "two", "three"))
  print(second_set)

  # add a new item
  first_set.add("four")
  print(first_set)

  # duplicates not allowed
  first_set.add("four")
  print(first_set)

  # different data types are allowed
  first_set.add(5)
  print(first_set)

if __name__ == '__main__':
    sets_demo()