"""
Please feel free to run this script to enjoy a journey by keyboard!
Remember to press H to see help message!

Note: This script require rendering, please following the installation instruction to setup a proper
environment that allows popping up an window.
"""
import argparse
import logging
import random

import cv2
import numpy as np

from metadrive import envs
from metadrive.component.sensors.rgb_camera import RGBCamera
from metadrive.constants import HELP_MESSAGE

if __name__ == "__main__":
    config = dict(use_render=True, # if you have a screen and OpenGL suppor, you can set use_render=True to use 3D rendering  
                   manual_control=True, # we usually manually control the car to test environment
                   log_level=logging.CRITICAL)
    
    env = envs.SidewalkEnv(config)
    env.reset()
    try:
        while True:
             obs, reward, termination, truncate, info = env.step(env.action_space.sample())
    finally:
        env.close()
