def play_video(url, frame_rate, speed=1.0):
  video_playback_speed = frame_rate * speed
  frame = get_next_frame(url, video_playback_speed)
  show_next_frame(frame)