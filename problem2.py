import os

def find_files(suffix, path):
    result = []
    try:
      list_dir = os.listdir(path)
      for item in list_dir:
          if os.path.isfile(path + '/' + item):
              if item.endswith(suffix):
                  result.append(path + '/' + item)
          else:
              result.extend(find_files(suffix, path + '/' + item))

      return result
    except:
        return 'directory not exist'

print(find_files('.c', 'testdir'))

## Test Case 1 - find all files with .h extension
assert find_files('.h', 'testdir') == ['testdir/subdir1/a.h', 'testdir/subdir3/subsubdir1/b.h', 'testdir/subdir5/a.h', 'testdir/t1.h']

## Test Case 2 - find all files with .xyz extension
assert find_files('.xyz', 'testdir') == []

## Test Case 3 - find all files in unexisted directory
assert find_files('.c', 'examdir') == 'directory not exist'

