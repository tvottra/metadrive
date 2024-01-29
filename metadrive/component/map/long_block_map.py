from metadrive.component.map.pg_map import PGMap
from metadrive.component.pgblock.first_block import PGBlock
from metadrive.component.pgblock.pg_block import BaseBlock

class LongBlockMap(PGMap):
    def _generate(self, map_config):
        length = map_config.get("length", 100)  # you can adjust the length as needed
        width = map_config.get("width", 10)  # you can adjust the width as needed

        parent_node_path, pg_physics_world = self.engine.worldNP, self.engine.physics_world
        last_block = PGBlock(
            self.road_network,
            self._global_network,
            parent_node_path,
            pg_physics_world,
            map_config[self.LANE_WIDTH],
            map_config[self.LANE_NUM],
            self.random_seed
        )
        self.blocks.append(last_block)

        # for _ in range(length):
        #     last_block = BaseBlock(
        #         self.road_network,
        #         self._global_network,i
        #         last_block.get_socket(index=0),
        #         parent_node_path,
        #         pg_physics_world,
        #         map_config[self.LANE_WIDTH],
        #         map_config[self.LANE_NUM],
        #         self.random_seed
        #     )
        #     self.blocks.append(last_block)
