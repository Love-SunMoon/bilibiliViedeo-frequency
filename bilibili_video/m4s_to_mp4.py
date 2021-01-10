# -*- coding: utf-8 -*-
# coding=utf-8
import json
import os
import sys

file_path = os.path.dirname(sys.argv[0])


def read_video_path(path):
    return os.listdir(path)


def read_file_name(path):
    with open(path + "\\entry.json", encoding="utf-8") as f:
        return json.loads(f.read())["page_data"]["part"]


def m4s_to_mp4(path, name, save_path):
    # save_path = os.path.abspath(os.path.realpath(os.path.dirname(__file__))) + "\\video\\"
    # save_path = r"F:/html+css/"
    ffmpeg_path = file_path + "\\ffmpeg.exe"
    audio_path = path + "\\80\\audio.m4s"
    video_path = path + "\\80\\video.m4s"
    cmd = "{} -i {} -i {} {}{}.mp4".format(ffmpeg_path, audio_path, video_path, save_path, name)
    os.system(cmd)


if __name__ == "__main__":
    try:
        with open(file_path + "/config.txt", encoding="gbk") as f:
            config = f.read()
            if '\\' in config:
                config = config.replace('\\', "\\\\")
            config = eval(config)

    except UnicodeDecodeError:
        with open(file_path + "/config.txt", encoding="utf-8") as f:
            config = f.read()
            if '\\' in config:
                config = config.replace('\\', "\\\\")
            if config.find("{"):
                config = config[config.find("{"):]
            config = eval(config)
    print("运行时非常占用cpu，如有需要请关闭其他应用在运行")
    print("执行会花费较长时间请耐心等待")
    input("任意键继续")
    dir_path = config["视频目录"]
    save_path = config["保存目录"]
    dir_path += "\\"
    save_path += "\\"
    for i in read_video_path(dir_path):
        video_name = read_file_name(dir_path + i)
        m4s_to_mp4(dir_path + i, video_name, save_path)
        print("成功转换视频" + video_name)
    input("程序执行完成，任意键退出")
