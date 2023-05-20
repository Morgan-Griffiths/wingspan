state = {
    'players': [
        {'cards': [1,2,3,4,5], 'food': [1,2,3,4,5]}
    ]
}
stack = [(0,'discardfood'), (0,'discard')]

def discard(player_id, stack, state, answer):
    if answer == 'skip':
        return None
    if answer:
        state['players'][player_id]['cards'].remove(int(answer))

    if len(state['players'][player_id]['cards']) == 0:
        return None
    else:
        return (player_id, 'discard'), f"pick a card to discard {state['players'][0]['cards']}"

def discardfood(player_id, stack, state, answer):
    if answer:
        state['players'][player_id]['food'].remove(int(answer))

    numcards = len(state['players'][player_id]['cards'])
    numfood = len(state['players'][player_id]['food'])
    if numfood > 5 - numcards:
        return (player_id, 'discardfood'), 'discard another food'
    else:
        stack.append((2, 'nextthing'))
        stack.append((2, 'nextthing'))
        return None
    
def nextthing(player_id, stack, state, answer):
    print('!nextthing!!!!')
    return None

action_lookup = {
    'discardfood': discardfood,
    'discard': discard,
    'nextthing': nextthing,
}

def run(stack, state, answer):
    while stack:
        current = stack.pop()
        if result := action_lookup[current[1]](current[0], stack, state, answer):
            action, description = result
            print(result)
            stack.append(action)
            return description
        answer = None


answer = None
while question := run(stack, state, answer):
    print(state, stack)
    answer = input(question).strip()

print(state, stack)
print('done')
print(state)







# ef action_a():
#     do_a()
#     do_b()
#     ask_for_c("a1", player=0)
#     do_c()
#     ask_for_d("a2", player=1)
#     do_d()
#     ask_for_e("a3", player=0)
#     do_e()


# def ask_for(actionsubname, player):
#     history.append(game)
#     state.current_player = player
#     state.currenct_action = actionsubname 
#     action = model(state)
#     state, reward, done = env.step(action)
#     states.append(state)
#     actions.append(action)
#     rewards.append(reward)


# def get_trajectories():
#     state_history = []
#     action_history = []
#     reward_history = []
#     for g in range(num_games):
#         states = []
#         actions = []
#         rewards = []
#         state, reward, done = env.reset()
#         while not done:
#             action = model(state)
#             state, reward, done = env.step(action)
#             states.append(state)
#             actions.append(action)
#             rewards.append(reward)


# def action_a1():
#     do_a()
#     do_b()
#     state.current_player = 0
#     state.options = get_options()
#     state.next_action = "a2"


# def action_a2():
#     do_c()
#     state.current_player = 1
#     state.options = get_options()
#     state.next_action = "a3"


# def action_a3():
#     do_d()
#     state.current_player = 0
#     state.options = get_options()
#     state.next_action = "a4"


# def action_a4():
#     do_e()


# def get_trajectories():
#     state_history = []
#     action_history = []
#     reward_history = []
#     for g in range(num_games):
#         states = []
#         actions = []
#         rewards = []
#         state, reward, done = env.reset()
#         while not done:
#             action = model(state)
#             state, reward, done = env.step(action)
#             states.append(state)
#             actions.append(action)
#             rewards.append(reward)

#     return states, actions, rewards


# def train():
#     for e in range(epochs):
#         loses = []
#         for state, reward in mini_batch_histories:
#             action = model(state)
#             loss = loss_func(action, reward)
#             zero_grad()
#             loss.backward()
#             optimizer.step()
#             losses.append(loss.item)

#         print(np.mean(losses))
