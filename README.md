# Spaces showcase tasks for Isaac Lab

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
    <td><strong>Dict</strong></td>
    <td><strong>Tuple</strong></td>
  </tr>
  <tr>
    <td rowspan="5"><p>observation space</td>
    <td><strong>Box</strong></td>
    <td>x</td>
    <td>x</td>
    <td>x</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Discrete&nbsp;<sup>(1)</sup></strong></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td><strong>MultiDiscrete&nbsp;<sup>(1)</sup></strong></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Dict</strong></td>
    <td>x</td>
    <td>x</td>
    <td>x</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Tuple</strong></td>
    <td>x</td>
    <td>x</td>
    <td>x</td>
    <td></td>
    <td></td>
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
    <td><strong>Dict</strong></td>
    <td><strong>Tuple</strong></td>
  </tr>
  <tr>
    <td rowspan="5"><p>observation space</td>
    <td><strong>Box</strong></td>
    <td>x</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Discrete&nbsp;<sup>(1)</sup></strong></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td><strong>MultiDiscrete&nbsp;<sup>(1)</sup></strong></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Dict</strong></td>
    <td>x</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td><strong>Tuple</strong></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody></table>

<hr>

Notes: The following features are currently supported only on the skrl's [develop](https://github.com/Toni-SM/skrl/tree/develop) branch:

<sup>(1)</sup> `Discrete` and `MultiDiscrete` observation spaces.

<sup>(2)</sup> `MultiDiscrete` action space.
