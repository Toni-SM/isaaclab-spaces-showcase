Install

```bash
/home/toni/Documents/RL/isaac-sim_IsaacLab/isaaclab.sh -p -m pip install -e exts/direct_spaces_showcase
```
Tasks

```bash
/home/toni/Documents/RL/isaac-sim_IsaacLab/isaaclab.sh -p scripts/list_envs.py
```

Run

```bash
/home/toni/Documents/RL/isaac-sim_IsaacLab/isaaclab.sh -p scripts/skrl/train.py --task Spaces-Box-Box-Cartpole-Direct-v0
```

<style type="text/css">
    table {
        width: 100%;
    }
    td {
        border-color: gray;
        border-style: solid;
        border-width: 2px;
    }
    .rot90 {
        transform: rotate(-90deg);
        margin: 0;
        padding: 0;
    }
</style>
<table class="tg">
<tbody>
  <tr>
    <td colspan="2" rowspan="2"></td>
    <td colspan="5" style="text-align: center">action space</td>
  </tr>
  <tr>
    <td><strong>Box</strong></td>
    <td><strong>Discrete</strong></td>
    <td><strong>MultiDiscrete*</strong></td>
    <td><strong>Dict</strong></td>
    <td><strong>Tuple</strong></td>
  </tr>
  <tr>
    <td class="rot90", rowspan="5">observation</td>
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

* MultiDiscrete is currently supported in the skrl's [develop](https://github.com/Toni-SM/skrl/tree/develop) branch.
