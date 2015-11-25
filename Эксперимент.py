def time_length(start_time, end_time):
    start_time = [int(a) for a in start_time.split(":")]
    end_time = [int(a) for a in end_time.split(":")]

    if end_time == [0, 0, 0]:
        end_time = (24, 0, 0)

    time_length_s = abs(end_time[0] * 3600 + end_time[1] * 60 + end_time[2] - start_time[0] * 3600 - start_time[1] * 60 - start_time[2])

    time_length_h = time_length_s // 3600
    time_length_m = (time_length_s - time_length_h * 3600) // 60
    time_length_s -= time_length_h * 3600 + time_length_m * 60

    return "{:01}:{:02}:{:02}".format(time_length_h, time_length_m, time_length_s)

with open('task.in') as fin:
    start_time = fin.readline()
    end_time = fin.readline()

    with open('task.out', 'w') as fout:
        print(time_length(start_time, end_time), file=fout)
