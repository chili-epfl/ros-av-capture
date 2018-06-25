import argparse
import rosbag

parser = argparse.ArgumentParser(description='Extract mp3 file from audio topic in ros bag.')
parser.add_argument('bagfile', help='ros bag file to use as input')
parser.add_argument('outfile', help='destination of output')
args = parser.parse_args()

bag = rosbag.Bag(args.bagfile)
output = open(args.outfile, 'w')

for topic, msg, t in bag.read_messages(topics=['/audio/audio']):
    output.write(''.join(msg.data))

bag.close()
output.close()
