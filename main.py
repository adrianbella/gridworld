# distribution over the states
grid_map = [[0, 0, 0, 0], [0, 1, 2, 5], [1, 2, 3, 6], [2, 3, 3, 7],
            [4, 0, 5, 8], [4, 1, 6, 9], [5, 2, 7, 10], [6, 3, 7, 11],
            [8, 4, 9, 12], [8, 5, 10, 13], [9, 6, 11, 14], [10, 7, 11, 15],
            [12, 8, 13, 12], [12, 9, 14, 13], [13, 10, 15, 14], [0, 0, 0, 0]]
# V(s) values
v_list = [0.0, 0.0, 0.0, 0.0,
          0.0, 0.0, 0.0, 0.0,
          0.0, 0.0, 0.0, 0.0,
          0.0, 0.0, 0.0, 0.0]
# probability of the actions [left,up,right,down]
policy = [[0.0, 0.0, 0.0, 0.0], [0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25],
          [0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25],
          [0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25],
          [0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25], [0.0, 0.0, 0.0, 0.0]]
# error threshold
Theta = 0.001
# reward for all steps
r = -1.0


def policy_evaluation():
    delta = 0.0

    for state_index in range(len(v_list)):  # Loop for each s in S
        vk_s_old = v_list[state_index]  # v <- V(s)
        v_list[state_index] = calcualte_Bellman(state_index)  # Sum_{s',r} p(s',r|s,pi(s))[r+gamma*V(s')]
        delta = max(delta, abs(vk_s_old - v_list[state_index]))  # delta <- max(delta,|v-V(s)|)

    if delta < Theta:  # if true, the v_(s) function is optimal
        print 'Delta < Theta is true!'


def calcualte_Bellman(state_index):
    summ = 0.0

    for i in range(len(grid_map[state_index])):
        summ += policy[state_index][i] * (r + v_list[grid_map[state_index][i]])

    return summ


def policy_improvement():
    is_policy_stable = True  # policy-stable <- true

    for state_index in range(len(v_list)):
        old_policy_s = policy[state_index]  # old-action <- pi(s)
        policy[state_index] = calcualte_best_action(
            state_index)  # pi(s) <- argmax_a\sum_{s',r}p(s',r|s,a)[r+\gammaV(s')]
        for i in range(len(old_policy_s)):
            if old_policy_s[i] != policy[state_index][i]:
                is_policy_stable = False

    if is_policy_stable:  # if the policy didn't change, we find the optimal policy
        print 'we find the optimal policy:'


def calcualte_best_action(state_index):
    max_v = -1000.0
    best_action_indexes = []
    for i in range(len(grid_map[state_index])):
        if max_v < v_list[grid_map[state_index][i]]:
            max_v = v_list[grid_map[state_index][i]]
            best_action_indexes = []
            best_action_indexes.append(i)
        elif max_v == v_list[grid_map[state_index][i]]:
            best_action_indexes.append(i)

    result = [0.0, 0.0, 0.0, 0.0]

    if state_index == 0 or state_index == 15:  # in case of terminated states the probability distribution is always 0
        return result

    for i in best_action_indexes:
        result[i] = 1.0 / float(len(best_action_indexes))

    return result


def policy_iteration(iteration):
    current_iterationcount = 0

    while iteration > current_iterationcount:
        policy_evaluation()
        policy_improvement()
        current_iterationcount += 1
        print 'v_(s) current value after', current_iterationcount, ' iterations:'
        print v_list[0:4]
        print v_list[4:8]
        print v_list[8:12]
        print v_list[12:16]
        print 'policy current value after', current_iterationcount, ' iterations:'
        print policy[0:4]
        print policy[4:8]
        print policy[8:12]
        print policy[12:16]


def value_iteration(iteration):
    current_iterationcount = 0

    while iteration > current_iterationcount:
        delta = 0  # delta <- 0

        for state_index in range(len(v_list)):  # loop for each s \in S
            v_old_value = v_list[state_index]
            v_list[state_index] = calculate_Bellman_optimality_equation(
                state_index)  # max_a Sum_{s',r} p(s',r|s,pi(s))[r+gamma*V(s')]
            delta = max(delta, abs(v_old_value - v_list[state_index]))  # delta <- max(delta,|v-V(s)|)

        if delta < Theta:  # if true, the v_(s) function is optimal
            print 'Delta < Theta is true!'
            print 'The value function is optimal!'
            calculate_policy_to_current_v_s()
            return

        current_iterationcount += 1

        print 'v_(s) current value after', current_iterationcount, ' iterations:'
        print v_list[0:4]
        print v_list[4:8]
        print v_list[8:12]
        print v_list[12:16]

    calculate_policy_to_current_v_s()


def calculate_policy_to_current_v_s():
    for state_index in range(len(v_list)):
        policy[state_index] = calcualte_best_action(
            state_index)  # pi(s) = argmax \summ_{s',r} p(s',r|s,a)[r + \gamma v(s')]


def calculate_Bellman_optimality_equation(state_index):
    max_value = -1000.0

    for i in range(len(grid_map[state_index])):
        current_v_s = policy[state_index][i] * (r + v_list[grid_map[state_index][i]])
        if current_v_s > max_value:
            max_value = current_v_s

    if state_index == 0 or state_index == 15:  # in case of terminated states the v_s is always 0
        return 0.0

    return max_value


if __name__ == '__main__':

    is_intervall_contains = False
    is_iterationtype_correct = False
    Type = 0

    while is_iterationtype_correct != True:
        Type = input('Enter the desired iteration type number (1 = policy iteration, 2 = value iteration): ')
        if Type == 1 or Type == 2:
            is_iterationtype_correct = True
        else:
            print 'You should enter ''1'' or ''2''!'

    while is_intervall_contains != True:
        iterations = input('Enter the desired count of iterations [1;100]: ')
        if iterations < 1 or iterations > 100:
            print 'The given number is out of the intervall!'
        else:
            is_intervall_contains = True

    if Type == 1:
        policy_iteration(iterations)
    elif Type == 2:
        value_iteration(iterations)
    else:
        print "You should choose one of the iteration types!"

    print 'Main function is over:'
    print '-----------------------------------------------------END-----------------------------------------------------'
    print 'Final v_(s): '
    print v_list[0:4]
    print v_list[4:8]
    print v_list[8:12]
    print v_list[12:16]
    print 'Final policy:'
    print policy[0:4]
    print policy[4:8]
    print policy[8:12]
    print policy[12:16]
