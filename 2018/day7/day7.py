for fichier in ["test", "input"]:
    print(f"\n\033[92m*** FICHIER {fichier}.txt ***\033[0m")
    data = [line.strip() for line in open(f"2018/day7/{fichier}.txt", "r") if line.strip() != ""]

    print("\033[93m--- Part One ---\033[0m")

    stepsConstraints = {}
    steps = set()
    for line in data:
        _step, stepBefore, _must, _be, _finished, _before, _step, stepAfter, _can, _begin = line.split(" ")
        stepsConstraints[stepAfter] = stepsConstraints.get(stepAfter, [])
        stepsConstraints[stepAfter].append(stepBefore)
        steps.add(stepBefore)
        steps.add(stepAfter)

    step_order = []
    step_queue = [step for step in steps if (step not in stepsConstraints)]
    while step_queue:
        step = step_queue.pop(0)
        step_order.append(step)
        
        step_queue += [stepNeed for stepNeed, step_done in stepsConstraints.items() if all((done in step_order) for done in step_done) and (stepNeed not in step_order) and (stepNeed not in step_queue)]
        step_queue.sort()


    print(f'Step order: {"".join(step_order)}')
    



    print("\n\033[93m--- Part Two ---\033[0m")

    workers = 2 if (fichier == "test") else 6
    time = 0 if (fichier == "test") else 60

    workers_jobs = [0] * workers
    workers_times = [0] * workers
    totalTime = 0
    
    step_order = []
    step_queue = [step for step in steps if (step not in stepsConstraints)]
    while len(step_order) < len(steps):

        for i in range(len(workers_times)):
            if workers_times[i] > 0:
                workers_times[i] -= 1
                if workers_times[i] == 0:
                    step_order.append(workers_jobs[i])
                    workers_jobs[i] = 0

        step_queue += [stepNeed for stepNeed, step_done in stepsConstraints.items() if all((done in step_order) for done in step_done) and (stepNeed not in step_order) and (stepNeed not in step_queue) and (stepNeed not in workers_jobs)]
        step_queue.sort()

        while step_queue and not(all(workers_jobs)):
            step = step_queue.pop(0)

            for i in range(len(workers_jobs)):
                if workers_jobs[i] == 0:
                    workers_jobs[i] = step
                    workers_times[i] = time + ord(step) - 64
                    break

        # print(f"[DEBUG] : totalTime: {totalTime} - workers_jobs: {workers_jobs} - workers_times: {workers_times} - step_queue: {step_queue} - step_order: {step_order}")
        # input()
                
        totalTime += 1


    print(f"Total time: {totalTime - 1}")