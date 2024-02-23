from metadrive.envs import BaseEnv
from metadrive.manager.sidewalk_map_manager import SidewalkMapManager
from metadrive.obs.observation_base import DummyObservation
import logging


class SidewalkEnv(BaseEnv):

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
    
if __name__=="__main__":
    config = dict(use_render=True, # if you have a screen and OpenGL suppor, you can set use_render=True to use 3D rendering  
                   manual_control=True, # we usually manually control the car to test environment
                   log_level=logging.CRITICAL)
    
    env = SidewalkEnv(config)
    env.reset()
    try:
        while True:
             obs, reward, termination, truncate, info = env.step(env.action_space.sample())
    finally:
        env.close()
