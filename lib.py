import re, sys, collections

def die(*args):
  if args:
    print(*args)
  sys.exit(-1)

def replace_prefix(s, prefix, replacement):
  if not s.startswith(prefix):
    die('chomp: {} does not start with {}'.format(s, prefix))
  return replacement + s[len(prefix):]

def fmt_cmd(s):
  s = s.strip()
  s = re.sub('\n', ' ', s)
  s = re.sub(' +', ' ', s)
  return s

def print_count(l):
  c = collections.Counter(l)
  for name, count in c.most_common():
    print('{0: <5} {1}'.format(count, name))
