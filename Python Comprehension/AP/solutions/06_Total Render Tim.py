# Sample render logs (frame, time in seconds)
render_logs = [
    (1001, 3.2),
    (1002, 2.9),
    (1003, 3.5),
]

# Generator expression - sum render times
total_time = sum(time for _, time in render_logs)

# Print result
print("Total Render Time:")
print(total_time)
