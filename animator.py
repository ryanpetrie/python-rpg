import pytmx

def animate_tilemap(tilemap, time):
    # Animate each tile property dictionary.
    for gid, props in tilemap.tile_properties.iteritems():
        animate_tile_properties(props, time)

def reset_animation(props):
    if not props:
        return
    props['current_frame'] = 0
    props['time_in_frame'] = 0

def animate_tile_properties(props, time):
    # If there is no animation data, skip this tile.
    if 'frames' not in props or len(props['frames']) < 2:
        return

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
            
# Get an animated tile image. Also animate if animation_time > 0.
def get_animated_tile_image(tilemap, x, y, layer, animation_time = 0):
    props = tilemap.get_tile_properties(x, y, layer)
    # If there is no animation data, return get_tile_image.
    if not props or 'frames' not in props or len(props['frames']) < 2:
        return tilemap.get_tile_image(x, y, layer)

    if 'current_frame' not in props:
        reset_animation(props)

    # Animate if requested.
    if animation_time > 0:
        animate_tile_properties(props, animation_time)

    # Get the gid for the current frame.
    frames = props['frames']
    frame = frames[props['current_frame']]
    return tilemap.images[frame.gid]
