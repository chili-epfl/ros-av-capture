#### ROS package dependencies
 - audio_capture
 - usb_cam
 - rosbag_recorder

#### Usage

 - Clone this repo in the `src` directory of your catkin workspace
 - Run `catkin_make` from the root of your catkin workspace
 - Run `catkin_make -DCMAKE_INSTALL_PREFIX=/opt/ros/<distro> install` or source `devel/setup.bash`
 - To start the capture nodes and recording server, run `roslaunch av_capture av_capture.launch`

#### Config

The boolean arguments `publish_audio` and `publish_video` can be used to disable video or audio capture, and are set to true by default.
The capture parameters can be edited in `launch/webcam.launch` and `launch/audio.launch`.
