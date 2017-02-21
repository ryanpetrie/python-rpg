import pytmx

def _animate_properties(tilemap, time):
    # Animate each tile property dictionary.
    for gid, props in tilemap.tile_properties.iteritems():
        # If there is no animation data, skip this tile.
        if 'frames' not in props or len(props['frames']) < 2:
            continue

        # 1. Keep track of current_frame and time_in_frame.
        if 'current_frame' not in props:
            props['current_frame'] = 0
        if 'time_in_frame' not in props:
            props['time_in_frame'] = 0

        # 2. Each game frame, add the time the frame took to time_in_frame.
        props['time_in_frame'] += time

        # 3. While time_in_frame is larger than the duration of current_frame:
        frames = props['frames']
        current_frame_duration = frames[props['current_frame']].duration
        while props['time_in_frame'] > current_frame_duration:
            # a. Subtract duration of current_frame from time_in_frame.
            props['time_in_frame'] -= current_frame_duration

            # b. Move current_frame to the next frame.
            props['current_frame'] = (props['current_frame'] + 1) % len(frames)
            current_frame_duration = frames[props['current_frame']].duration
            
        
def _animate_tile_data(tilemap):
    # For each layer:
    for layer_number in xrange(len(tilemap.layers)):
        layer = tilemap.layers[layer_number]

        # For each tile in the layer:
        for x, y, gid in layer:
            props = tilemap.get_tile_properties(x, y, layer_number)
            # If there is no animation data, skip this tile.
            if 'frames' not in props or len(props['frames']) < 2:
                continue

            # Get the gid for the current frame.
            frames = props['frames']
            frame = frames[props['current_frame']]
            gid = frame.gid

            # Set the tile data using the gid.
            # TODO: This will break get_tile_properties!
            layer.data[y][x] = gid
            

def animate_tilemap(tilemap, time):
    _animate_properties(tilemap, time)
    _animate_tile_data(tilemap)
