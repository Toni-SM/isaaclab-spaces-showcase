from __future__ import annotations

import torch

from isaaclab.envs import DirectRLEnv, DirectRLEnvCfg
from isaaclab.envs.utils.spaces import sample_space
from isaaclab.scene import InteractiveSceneCfg
from isaaclab.sim import SimulationCfg
from isaaclab.utils import configclass


@configclass
class EmptyEnvCfg(DirectRLEnvCfg):
    # env
    decimation = 2
    episode_length_s = 5.0
    observation_space = 2
    action_space = 1
    state_space = 0

    # simulation
    sim: SimulationCfg = SimulationCfg(dt=1 / 120, render_interval=decimation)

    # scene
    scene: InteractiveSceneCfg = InteractiveSceneCfg(num_envs=4096, env_spacing=4.0, replicate_physics=True)


class EmptyEnv(DirectRLEnv):
    cfg: EmptyEnvCfg

    def __init__(self, cfg: EmptyEnvCfg, render_mode: str | None = None, **kwargs):
        super().__init__(cfg, render_mode, **kwargs)

        self.observation_sample = sample_space(
            self.single_observation_space["policy"], device=self.device, batch_size=self.num_envs
        )
        self.reward_sample = torch.ones_like(self.episode_length_buf, dtype=torch.float32)
        self.terminated_sample = torch.zeros_like(self.episode_length_buf, dtype=torch.bool)

    def _pre_physics_step(self, actions: torch.Tensor) -> None:
        self.actions = actions

    def _apply_action(self) -> None:
        pass

    def _get_observations(self) -> dict:
        return {"policy": self.observation_sample}

    def _get_rewards(self) -> torch.Tensor:
        return self.reward_sample

    def _get_dones(self) -> tuple[torch.Tensor, torch.Tensor]:
        truncated = self.episode_length_buf >= self.max_episode_length - 1
        return self.terminated_sample, truncated
