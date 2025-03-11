# Spaces showcase tasks for Isaac Lab

This project is a showcase for the definition and use of the different observation and action spaces available at Isaac Lab.

Currently, only the Isaac Lab's Direct workflow supports the definition of other spaces for observation and action other than `Box`.
See [Isaac Lab's documentation](https://isaac-sim.github.io/IsaacLab/main/source/api/lab/isaaclab.envs.html#isaaclab.envs.DirectRLEnvCfg.observation_space) for more information.

> Models defined for the tasks are just an example of what can be done with **skrl**, visit [skrl's Model instantiators](https://skrl.readthedocs.io/en/latest/api/utils/model_instantiators.html) for more details.

## Setup

Install (**optional**, because the scripts will automatically add the project to the PYTHONPATH if it is not installed).

```bash
python -m pip install -e source/spaces_showcase
```

List available tasks.

```bash
python scripts/list_envs.py
```

## Showcased spaces

### Cartpole task

Train a task for a specific observation and action space type.

```bash
python scripts/skrl/train.py --task Spaces-Showcase-<OBSERVATION>-<ACTION>-Cartpole-Direct-v0 --headless
```

<table>
<tbody>
  <tr>
    <td colspan="2" rowspan="2"></td>
    <td colspan="5">action space</td>
  </tr>
  <tr>
    <td><strong>Box</strong></td>
    <td><strong>Discrete</strong></td>
    <td><strong>MultiDiscrete&nbsp;<sup>(2)</sup></strong></td>
  </tr>
  <tr>
    <td rowspan="5"><p>observation space</td>
    <td><strong>Box</strong></td>
    <td>x</td>
    <td>x</td>
    <td>x</td>
  </tr>
  <tr>
    <td><strong>Discrete&nbsp;<sup>(1)</sup></strong></td>
    <td>x</td>
    <td>x</td>
    <td>x</td>
  </tr>
  <tr>
    <td><strong>MultiDiscrete&nbsp;<sup>(1)</sup></strong></td>
    <td>x</td>
    <td>x</td>
    <td>x</td>
  </tr>
  <tr>
    <td><strong>Dict</strong></td>
    <td>x</td>
    <td>x</td>
    <td>x</td>
  </tr>
  <tr>
    <td><strong>Tuple</strong></td>
    <td>x</td>
    <td>x</td>
    <td>x</td>
  </tr>
</tbody></table>

### Cartpole-Camera task

Train a task for a specific observation and action space type.

```bash
python scripts/skrl/train.py --task Spaces-Showcase-<OBSERVATION>-<ACTION>-Cartpole-Camera-Direct-v0 --enable_cameras --headless
```

<table>
<tbody>
  <tr>
    <td colspan="2" rowspan="2"></td>
    <td colspan="5">action space</td>
  </tr>
  <tr>
    <td><strong>Box</strong></td>
    <td><strong>Discrete</strong></td>
    <td><strong>MultiDiscrete&nbsp;<sup>(2)</sup></strong></td>
  </tr>
  <tr>
    <td rowspan="5"><p>observation space</td>
    <td><strong>Box</strong></td>
    <td>x</td>
    <td>x</td>
    <td>x</td>
  </tr>
  <tr>
    <td><strong>Discrete&nbsp;<sup>(1)</sup></strong></td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td><strong>MultiDiscrete&nbsp;<sup>(1)</sup></strong></td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td><strong>Dict</strong></td>
    <td>x</td>
    <td><small>in progress</small></td>
    <td><small>in progress</small></td>
  </tr>
  <tr>
    <td><strong>Tuple</strong></td>
    <td><small>in progress</small></td>
    <td><small>in progress</small></td>
    <td><small>in progress</small></td>
  </tr>
</tbody></table>

<hr>

Notes: The following features are currently supported only on the skrl's [develop](https://github.com/Toni-SM/skrl/tree/develop) branch:

<sup>(1)</sup> One-hot encoding of `Discrete` and `MultiDiscrete` observation spaces.

<sup>(2)</sup> `MultiDiscrete` action space (`MultiCategoricalMixin` model instantiator).
