def is_deadlock(processes):
    resource_requirements = []
    for i in processes:
        if i=="Listen to Music":
            resource_requirements.append([0,1,1])
        elif i=="Read File":
            resource_requirements.append([1,0,1])
        elif i=="Delete File":
            resource_requirements.append([1,0,1])
        elif i=="Write File":
            resource_requirements.append([0,0,1])
        elif i=="Plug Device":
            resource_requirements.append([1,1,0])
    n = len(processes)
    
    # Initialize available resources with 3 instances of each type
    available_resources = [3, 3, 3]
    
    # Initialize a list to track whether each process is satisfied
    process_satisfied = [False] * n
    
    while True:
        # Check if there are any processes that can be satisfied
        for i in range(n):
            if not process_satisfied[i]:
                # Try to allocate resources for the process
                if all(available_resources[j] >= resource_requirements[i][j] for j in range(3)):
                    # If resources are available, allocate them to the process
                    for j in range(3):
                        available_resources[j] += resource_requirements[i][j]
                    process_satisfied[i] = True

        # Check if all processes are satisfied or no further progress can be made
        if all(process_satisfied) or not any(not process_satisfied[i] for i in range(n)):
            break
    
    # If all processes are satisfied, there is no deadlock
    if all(process_satisfied):
        return False
    else:
        return True

