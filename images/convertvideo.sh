#!/bin/bash

# USAGE:
#
# $0 start_time duration file_name_without_extension
# 
# Example: COnvert from 53 seconds to 1:30
# ../convertvideo.sh 00:00:53 00:00:37 bintrain_4_worldinfo  
# or
# ../convertvideo.sh 53 37 bintrain_4_worldinfo  

ffmpeg\
    -ss $1 -t $2\
    -i "${3}.mkv"\
    -filter:v "crop=1120:700:400:200,scale=800:-1,setpts=0.25*PTS"\
    -r 30\
    -an "${3}.mp4"
