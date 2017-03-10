import argparse
import os
import os.path
import time
import sys
from subprocess import Popen

# Parse the arguments
parser = argparse.ArgumentParser(description='Tile the first num-pages horizontally into a JPEG image.')
parser.add_argument("-paper", type=str, default='paper.pdf', help='The pdf to convert.')
parser.add_argument("-num-pages", type=int, default=8, help='Determines how many pages to convert')
parser.add_argument("-timeout", type=int, default=15, help='Determined how long to wait before quiting')
args = parser.parse_args()

# Generate the workspace folders
os.system('mkdir -p tmp') # for intermediate files

fullpath = args.paper
outpath = fullpath.replace('.pdf', '.jpg')

if os.path.isfile(outpath):
    print 'skipping %s, the file already exists.' % (fullpath, )
    sys.exit(0)

# erase previous intermediate files tmp/test-*.png
index = 0
while True:
    f = 'tmp/test-%d.png' % index
    if not os.path.isfile(f):
        break
    cmd = 'rm %s' % f
    os.system(cmd)

# spawn async convert commands.
pp = Popen(['convert', "%s[0-%d]" % (fullpath, args.num_pages-1), "-thumbnail", "x156", "tmp/test.png"])
t0 = time.time()
while time.time() - t0 < args.timeout: # give it 15 seconds deadline
    ret = pp.poll()
    if not (ret is None):
        # process terminated
        break
    time.sleep(0.1)
ret = pp.poll()
if ret is None:
    # we did not terminate in 5 seconds
    pp.terminate() # give up

if not os.path.isfile('tmp/test-0.png'):
    # failed to render pdf
    print 'could not render pdf.'
else:
    cmd = "montage -mode concatenate -quality 80 -tile x1 tmp/test-*.png %s" % outpath
    os.system(cmd)

# Delete the tmp folder
os.system('rm -rf tmp')
