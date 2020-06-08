import os

def delete_line(original_file, line_number):
    """ Delete a line from a file at the given line number """
    is_skipped = False
    current_index = 0
    dummy_file = original_file + '.bak'
    # Open original file in read only mode and dummy file in write mode
    with open(original_file, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Line by line copy data from original file to dummy file
        for line in read_obj:
            # If current line number matches the given line number then skip copying
            if current_index != line_number:
                write_obj.write(line)
            else:
                is_skipped = True
            current_index += 1
 
    # If any line is skipped then rename dummy file as original file
    if is_skipped:
        os.remove(original_file)
        os.rename(dummy_file, original_file)
    else:
        os.remove(dummy_file)

#delete_line("try.txt", 2)

def isQuot(tweet):
  val = False
  for char in tweet:
    if (char == '"'):
      val = True
  return val 

def sh(script, msg=0):
  os.system("bash -c '%s'" % script)

def prepare_tweet():
  tweet = '' 

  f = open("/Users/gabe/bash_stuff/haikuBot/haikus.txt", "r")

  lines = 0
  for line in f:
    tweet += line
    lines += 1
    if lines == 3:
      break
    delete_line("/Users/gabe/bash_stuff/haikuBot/haikus.txt", 0) 
    delete_line("/Users/gabe/bash_stuff/haikuBot/haikus.txt", 0) 
  f.close()
  
  tweet = tweet[:-1] 
  print(tweet)
  return tweet

tweet = prepare_tweet()
val = isQuot(tweet)

while val:
  tweet = prepare_tweet()
  val = isQuot(tweet)

command = 'twurl -d "status=' + tweet + '" /1.1/statuses/update.json | jq >> ~/bash_stuff/haikuBot/log.txt'
sh(command)

