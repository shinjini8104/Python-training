from collections import deque

def run_tasks(task_times, slice_time):
    q = deque()
    for i, t in enumerate(task_times):
        q.append([i + 1, t])

    runs = 0

    while q:
        task_id, remaining = q.popleft()

        if remaining > slice_time:
            print("Task", task_id, "runs for", slice_time, "units.")
            q.append([task_id, remaining - slice_time])
        else:
            print("Task", task_id, "runs for", remaining, "units.")

        runs += 1

    print("Total runs taken:", runs)


# Test Case
tasks = [10, 5, 8]
time_slice = 4

print("Output:\nTest Case 1:")
run_tasks(tasks, time_slice)
