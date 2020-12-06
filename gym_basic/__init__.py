from gym.envs.registration import register

register(
    id='basic-v0',
    entry_point='gym_basic.envs:BasicEnv',
)

register(
    id='basic-v2',
    entry_point='gym_basic.envs:BasicEnv2',
)