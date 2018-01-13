#!/usr/bin/python

def generate_heading(level, text):
  result = ""
  i = 0
  while i < level:
    result = result + "#"
    i = i + 1
  result = result + " " + text
  return result 

def generate_bullet_list(list):
  result = "\n\n"
  for item in list:
    result = result + "* " + item + "\n"
  result = result + "\n"
  return result

def generate_italic_text(text):
  result = "__" + text + "__"
  return result

def generate_bold_text(text):
  result = "**" + text + "**"
  return result
 
def generate_code_snippet(text):
  start = "{% highlight python %}\n"
  end = "{% endhighlight %}"
  result = start + text + "\n" + end + "\n"
  return result
