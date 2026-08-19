import os
import sys
import argparse
from utilities import backup
import time

version_str = '1.1.0'
parser = argparse.ArgumentParser()

parser.add_argument('-i',
                    '--sourcePath',
                    help='absolute path, must be a file or directory',
                    required=True)
parser.add_argument('-o',
                    '--destinationPath',
                    help='absolute path, must be a directory',
                    required=True)
parser.add_argument('-s',
                    '--silent',
                    help='if set, no console output',
                    action='store_true')
parser.add_argument('-a',
                    '--autosave',
                    type=int,
                    choices=(15, 300, 600, 900, 1800),
                    help='if set, enables automatic backup',),

args = parser.parse_args()

if args.silent:
    sys.stdout = open(os.devnull, 'w')

print(f"AGTDarkShadow04's NMS Backup Utility v{version_str}")
print('\nTHE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,\n'
      'INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n'
      'FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.\n'
      'IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,\n'
      'DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,\n'
      'TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE\n'
      'OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n')

while True:
    print('Starting backup...')
    if backup(args.sourcePath, args.destinationPath):
        print('Backup complete!')
        if not args.autosave:
            exit(0)
        else:
            print(f'\nWaiting {args.autosave} seconds ({int(args.autosave / 60)} minutes)...\n')
            time.sleep(args.autosave)
    else:
        print('Backup failed.')
        exit(1)
