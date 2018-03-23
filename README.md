#### ROS package dependencies
 - audio_capture
 - rosbag
 - usb_cam

#### Usage

 - Open a terminal and `cd` into your catkin workspace `src` directory
 - Clone this repo to a directory called `av_capture` (`git clone https://github.com/chili-epfl/ros-av-capture.git av_capture`)
 - Run `catkin_make` from the root of your catkin workspace
 - Source `devel/setup.bash`
 - To start capturing, use `roslaunch av_capture av_capture.launch`

#### Config

By default, output is saved to a bagfile in /tmp. This can be changed through the argument `output_dir`. E.g. to save the output in `/home/user`, use `roslaunch av_capture av_capture.launch output_dir:=/home/user`.

The boolean arguments `capture_audio` and `capture_video` can be used to disable video or audio capture. They are set to true by default. In the same way, `publish_audio` and `publish_video` can be used to disable the nodes that publish audio or video.

The capture parameters can be edited in `launch/webcam.launch` and `launch/audio.launch`.

The audio can be extracted from a bag file using `scripts/extract_mp3.py`. Pass `--help` for usage information.

The video frames can be extracted to the current directory by running `rosrun image_view extract_images _sec_per_frame:=0.01 _image_transport:=compressed image:=/usb_cam/image_raw` and then, in a seperate terminal, playing the bag file (`rosbag play $BAGFILE`).
