totalsize = 0
import os

for filename in os.listdir('/Users/danielseite/Documents'):
    totalsize += os.path.getsize(os.path.join('/Users/danielseite/Documents', filename))

print(totalsize)
