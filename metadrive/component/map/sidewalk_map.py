from metadrive.component.map.pg_map import PGMap
from metadrive.component.pgblock.first_block import PGBlock

class SidewalkMap(PGMap):
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
        last_block.construct_from_config(
            {
                "block_index": 0,
                "position": (0, 0),
                "heading": 0,
                "length": length,
                "width": width,
                "drivable_area_indices": [0, 1, 2, 3],
                "block_objects": []
            }
        )
        

