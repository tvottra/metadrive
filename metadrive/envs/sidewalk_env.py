from metadrive.component.navigation_module.node_network_navigation import NodeNetworkNavigation
from metadrive.envs import BaseEnv
from metadrive.manager.sidewalk_map_manager import SidewalkMapManager
from metadrive.manager.traffic_manager import TrafficMode
from metadrive.obs.observation_base import DummyObservation
import logging

SIDEWALK_DEFAULT_CONFIG = dict(
    vehicle_config=dict(
        # navigation_module=NodeNetworkNavigation,
        # Vehicle model. Candidates: "s", "m", "l", "xl", "default". random_agent_model makes this config invalid
        vehicle_model="default",
        # If set to True, the vehicle can go backwards with throttle/brake < -1
        enable_reverse=False,
        # Whether to show the box as navigation points
        show_navi_mark=False,
        # Whether to show a box mark at the destination
        show_dest_mark=True,
        # Whether to draw a line from current vehicle position to the designation point
        show_line_to_dest=False,
        # Whether to draw a line from current vehicle position to the next navigation point
        show_line_to_navi_mark=False,
    ))


class SidewalkEnv(BaseEnv):
    @classmethod
    def default_config(cls):
        my_config = super(SidewalkEnv, cls).default_config()
        my_config.update(SIDEWALK_DEFAULT_CONFIG)
        return my_config

    def setup_engine(self):
        super(SidewalkEnv, self).setup_engine()
        self.engine.register_manager("map_manager", SidewalkMapManager())

    def reward_function(self, agent):
        return 0, {}

    def cost_function(self, agent):
        return 0, {}

    def done_function(self, agent):
        return False, {}

    def get_single_observation(self):
        return DummyObservation()


if __name__ == "__main__":
    config = dict(use_render=True,
                  # if you have a screen and OpenGL suppor, you can set use_render=True to use 3D rendering
                  manual_control=True,  # we usually manually control the car to test environment
                  log_level=logging.CRITICAL,
                  )

    env = SidewalkEnv(config)
    env.reset()
    try:
        while True:
            obs, reward, termination, truncate, info = env.step(env.action_space.sample())
    finally:
        env.close()
