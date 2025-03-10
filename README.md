# Spaces showcase tasks for Isaac Lab

Install (optional)

```bash
python -m pip install -e exts/spaces_showcase
```

List tasks

```bash
python scripts/list_envs.py
```

Run a task

```bash
python scripts/skrl/train.py --task Spaces-Showcase-<OBSERVATION>-<ACTION>-Cartpole-Direct-v0
```

### Showcased spaces

<table>
<tbody>
  <tr>
    <td colspan="2" rowspan="2"></td>
    <td colspan="5">action space</td>
  </tr>
  <tr>
    <td><strong>Box</strong></td>
    <td><strong>Discrete</strong></td>
    <td><strong>MultiDiscrete*</strong></td>
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
    <td><strong>Discrete</strong></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td><strong>MultiDiscrete</strong></td>
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

* MultiDiscrete action space is currently supported only on the skrl's [develop](https://github.com/Toni-SM/skrl/tree/develop) branch.
