# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

import gymnasium as gym

from omni.isaac.lab_assets.cartpole import CARTPOLE_CFG

from omni.isaac.lab.assets import ArticulationCfg
from omni.isaac.lab.envs import DirectRLEnvCfg
from omni.isaac.lab.scene import InteractiveSceneCfg
from omni.isaac.lab.sim import SimulationCfg
from omni.isaac.lab.utils import configclass


@configclass
class CartpoleBaseEnvCfg(DirectRLEnvCfg):
    # env
    decimation = 2
    episode_length_s = 5.0
    state_space = 0

    # simulation
    sim: SimulationCfg = SimulationCfg(dt=1 / 120, render_interval=decimation)

    # robot
    robot_cfg: ArticulationCfg = CARTPOLE_CFG.replace(prim_path="/World/envs/env_.*/Robot")
    cart_dof_name = "slider_to_cart"
    pole_dof_name = "cart_to_pole"

    # scene
    scene: InteractiveSceneCfg = InteractiveSceneCfg(num_envs=4096, env_spacing=4.0, replicate_physics=True)

    # control
    max_effort = 100.0  # [N]

    # reset
    max_cart_pos = 3.0  # the cart is reset if it exceeds that position [m]
    initial_pole_angle_range = [-0.25, 0.25]  # the range in which the pole angle is sampled from on reset [rad]

    # reward scales
    rew_scale_alive = 1.0
    rew_scale_terminated = -2.0
    rew_scale_pole_pos = -1.0
    rew_scale_cart_vel = -0.01
    rew_scale_pole_vel = -0.005

@configclass
class BoxBoxEnvCfg(CartpoleBaseEnvCfg):
    """
    * Observation space (``~gymnasium.spaces.Box`` with shape (4,))

        ===  ====
        Idx  Observation
        ===  ====
        0    Pole DOF position
        1    Pole DOF velocity
        2    Cart DOF position
        3    Cart DOF velocity
        ===  ===

    * Action space (``~gymnasium.spaces.Box`` with shape (1,))

        ===  ===
        Idx  Action
        ===  ===
        0    Cart DOF effort scale: [-1, 1]
        ===  ===
    """
    # spaces
    observation_space = 4  # also: [4] or gym.spaces.Box(low=float("-inf"), high=float("inf"), shape=(4,))
    action_space = 1  # also: [1] or gym.spaces.Box(low=-1.0, high=1.0, shape=(1,))

@configclass
class BoxDiscreteEnvCfg(CartpoleBaseEnvCfg):
    """
    * Observation space (``~gymnasium.spaces.Box`` with shape (4,))

        ===  ====
        Idx  Observation
        ===  ====
        0    Pole DOF position
        1    Pole DOF velocity
        2    Cart DOF position
        3    Cart DOF velocity
        ===  ===

    * Action space (``~gymnasium.spaces.Discrete`` with 3 elements)

        ===  ===
        N    Action
        ===  ===
        0    Negative maximum cart DOF effort
        1    Zero cart DOF effort
        2    Positive maximum cart DOF effort
        ===  ===
    """
    # spaces
    observation_space = 4  # also: [4] or gym.spaces.Box(low=float("-inf"), high=float("inf"), shape=(4,))
    action_space = {3}  # also: gym.spaces.Discrete(3)

@configclass
class DictBoxEnvCfg(CartpoleBaseEnvCfg):
    """
    * Observation space (``~gymnasium.spaces.Dict`` with 2 constituent spaces)

        ================  ====
        Key               Observation
        ================  ====
        joint-positions   DOF positions
        joint-velocities  DOF velocities
        ================  ===

    * Action space (``~gymnasium.spaces.Box`` with shape (1,))

        ===  ===
        Idx  Action
        ===  ===
        0    Cart DOF effort scale: [-1, 1]
        ===  ===
    """
    observation_space = gym.spaces.Dict({
        "joint-positions": gym.spaces.Box(low=float("-inf"), high=float("inf"), shape=(2,)),
        "joint-velocities": gym.spaces.Box(low=float("-inf"), high=float("inf"), shape=(2,)),
    })  # also: {"joint-positions": 2, "joint-velocities": 2}

    action_space = gym.spaces.Box(low=-1.0, high=1.0, shape=(1,))  # also: 1 or [1]
