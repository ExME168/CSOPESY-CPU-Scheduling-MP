import fcfs as FCFSModule

def printBanner():
    print("=========================================================================================================")
    print('\033[0;34m' + "░█████╗░██████╗░██╗░░░██╗  ░██████╗░█████╗░██╗░░██╗███████╗██████╗░██╗░░░██╗██╗░░░░░██╗███╗░░██╗░██████╗░")
    print("██╔══██╗██╔══██╗██║░░░██║  ██╔════╝██╔══██╗██║░░██║██╔════╝██╔══██╗██║░░░██║██║░░░░░██║████╗░██║██╔════╝░")
    print("██║░░╚═╝██████╔╝██║░░░██║  ╚█████╗░██║░░╚═╝███████║█████╗░░██║░░██║██║░░░██║██║░░░░░██║██╔██╗██║██║░░██╗░")
    print("██║░░██╗██╔═══╝░██║░░░██║  ░╚═══██╗██║░░██╗██╔══██║██╔══╝░░██║░░██║██║░░░██║██║░░░░░██║██║╚████║██║░░╚██╗")
    print("╚█████╔╝██║░░░░░╚██████╔╝  ██████╔╝╚█████╔╝██║░░██║███████╗██████╔╝╚██████╔╝███████╗██║██║░╚███║╚██████╔╝")
    print("░╚════╝░╚═╝░░░░░░╚═════╝░  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░░╚═════╝░╚══════╝╚═╝╚═╝░░╚══╝░╚═════╝░"+ '\033[0m')
    print("=========================== by Fadrigo, A.; Sibal, M.; Tan, P. -- CSOPESY S11 ===========================")
    print('\033[0;34m' + "Algorithims:\n" + '\033[0m'  + "   0.) First-Come-First-Serve (FCFS)\n   1.) Shortest-Job First (SJF)\n   2.) Shortest-Remaining-Time-First (SRTF)\n   3.) Round-Robin (RR)")
    print('\033[0;34m' + "Usage:" + '\033[0m'  + "[X - Algorithm Number] [Y - Number of Processes] [Z - Time Slice]")
    print('\033[0;34m'  + "Constraints:\n" + '\033[0m'  +   "   0 ≤ X ≤ 4\n   3 ≤ Y ≤ 100\n   1 ≤ Z ≤ 100")
    print("\n")

def getProcesses(procLen):
    procList = []
    print("Write ", procLen, " processes.")
    print("Process Input Format: [A - Process ID] [B - Arrival Time] [C - Burst Time]")

    for i in range(procLen):
        process = list(map(int,input(">> ").strip().split(' ')))
        procList.append(process)
    
    return procList

def main():
    try:
        terminated = False
        printBanner()
        
        while(not terminated):
            algID, procLen, timeSlice = list(map(int,input(">> ").strip().split(' ')))
            if algID == 0:
                processes = getProcesses(procLen)
                FCFSModule.computeFCFS(processes, timeSlice)
            elif algID == 1:
                print("SJF")
            elif algID == 2:
                print("SRTF")
            elif algID == 3:
                print("RR")
            elif algID == 4:
                print("Program Terminated ...")
                terminated = True
            else:
                print("ERROR: Invalid Input")

        exit()

    except Exception as err:
        print(f"{type(err).__name__} was raised: {err}")
    

if __name__ == "__main__":
    main()
