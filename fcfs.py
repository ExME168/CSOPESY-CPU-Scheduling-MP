def computeFCFS(processes, procLen):
    print("FCFS")
    print("Processes: ")

    first_proc_AT = processes[0][1]
    start_time = first_proc_AT
    
    for i in range(procLen):
        proc_ID, AT, BT = processes[i]
        end_time = start_time + BT
        print(f"{proc_ID} start time: {start_time} end time: {end_time} | Waiting time: *")
        
        if(i != procLen-1):
            next_proc_AT = processes[i+1][1]

        if(next_proc_AT > end_time):
            start_time = end_time
            end_time = next_proc_AT
            print(f"CPU IDLE start time: {start_time} end time: {end_time} | Waiting time: *")
            start_time = end_time
        else:
            start_time = end_time