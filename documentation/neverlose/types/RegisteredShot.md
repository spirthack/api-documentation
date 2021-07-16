# RegisteredShot

{% hint style="info" %}
You can access `RegisteredShot` instance through `ragebot_shot` [callback](../other/callbacks.md)
{% endhint %}

{% hint style="info" %}
Miss reasons:
| Value | Description |
| :--- | :--- |
| 0 | Hit |
| 1 | Resolver |
| 2 | Spread |
| 3 | Occlusion |
| 4 | Prediction error |
{% endhint %}

## Fields:

| Name | Type | Description |
| :--- | :--- | :--- |
| hitchance | int | Chance to hit target |
| backtrack | int | How many ticks was backtracked |
| hitgroup | int | HitGroup |
| damage | int | Damage |
| target_index | int | Target ent index |
| reason | int | Miss reason |
| spread_degree | float | Spread angle |
