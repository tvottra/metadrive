import metadrive.component.map.pg_map as pg_map
from metadrive.envs import BaseEnv
from metadrive.obs.observation_base import DummyObservation
import logging

# ======================================== new content ===============================================
import cv2
from metadrive.component.map.sidewalk_map import SidewalkMap
from metadrive.manager.base_manager import BaseManager
from metadrive.component.pgblock.first_block import FirstPGBlock

class SidewalkMapManager(BaseManager):

    def __init__(self):
        super(SidewalkMapManager, self).__init__()
        self.current_map = None
        self.sidewalk_map_config = dict(
            type=pg_map.BigGenerateMethod.BLOCK_SEQUENCE,
            config='S',
            lane_width=80,
            lane_num=2,
            exit_length=100,
        )

    def reset(self):
        self.current_map = pg_map.PGMap(map_config=self.sidewalk_map_config)
        self.current_map.attach_to_world()

    def before_reset(self):
        if self.current_map:
            self.current_map.detach_from_world()
            self.current_map = None

    def destroy(self):
        # clear all maps when this manager is destroyed
        super(SidewalkMapManager, self).destroy()
        if self.current_map:
            self.current_map.destroy()


# Expand the default config system, specify where to spawn the car
# MY_CONFIG = dict(agent_configs={"default_agent": dict(spawn_lane_index=(FirstPGBlock.NODE_1, FirstPGBlock.NODE_2, 0))})
