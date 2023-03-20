def action_a():
    do_a()
    do_b()
    ask_for_c("a1", player=0)
    do_c()
    ask_for_d("a2", player=1)
    do_d()
    ask_for_e("a3", player=0)
    do_e()


def ask_for(actionsubname, player):
    history.append(game)
    state.current_player = player
    state.currenct_action = actionsubname
    action = model(state)
    state, reward, done = env.step(action)
    states.append(state)
    actions.append(action)
    rewards.append(reward)


def get_trajectories():
    state_history = []
    action_history = []
    reward_history = []
    for g in range(num_games):
        states = []
        actions = []
        rewards = []
        state, reward, done = env.reset()
        while not done:
            action = model(state)
            state, reward, done = env.step(action)
            states.append(state)
            actions.append(action)
            rewards.append(reward)


def action_a1():
    do_a()
    do_b()
    state.current_player = 0
    state.options = get_options()
    state.next_action = "a2"


def action_a2():
    do_c()
    state.current_player = 1
    state.options = get_options()
    state.next_action = "a3"


def action_a3():
    do_d()
    state.current_player = 0
    state.options = get_options()
    state.next_action = "a4"


def action_a4():
    do_e()


def get_trajectories():
    state_history = []
    action_history = []
    reward_history = []
    for g in range(num_games):
        states = []
        actions = []
        rewards = []
        state, reward, done = env.reset()
        while not done:
            action = model(state)
            state, reward, done = env.step(action)
            states.append(state)
            actions.append(action)
            rewards.append(reward)

    return states, actions, rewards


def train():
    for e in range(epochs):
        loses = []
        for state, reward in mini_batch_histories:
            action = model(state)
            loss = loss_func(action, reward)
            zero_grad()
            loss.backward()
            optimizer.step()
            losses.append(loss.item)

        print(np.mean(losses))
