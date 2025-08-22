# Sample render tasks: (shot_name, frame_count)
render_tasks = [
    ("shot001", 60),
    ("shot002", 340),
    ("shot003", 90),
    ("shot004", 240),
]
# 1. List comprehension - filter shots with more than 100 frames
long_shots = [name for (name, frames) in render_tasks if frames > 100]
# 2. Dictionary comprehension - calculate render time (frame_count * 0.5 minutes)
render_times = {name: frames * 0.5 for (name, frames) in render_tasks}
# Print results
print("Shots with more than 100 frames:")
print(long_shots)
print("\nEstimated Render Times (in minutes):")
print(render_times)
