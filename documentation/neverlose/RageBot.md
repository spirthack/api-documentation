# RageBot

{% hint style="info" %}
Hitboxes:

```text
    0. head
    1. neck
    2. pelvis
    3. stomach
    4. lower chest
    5. chest
    6. upper chest
    7. right thigh
    8. left thigh
    9. right calf
    10. left calf
    11. right foot
    12. left foot
    13. right hand
    14. left hand
    15. right upper arm
    16. right forearm
    17. left upper arm
    18. left forearm
```

{% endhint %}

## Functions

## OverrideMinDamage

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| index | int | Entity index |
| value | int | New mindamage |

```lua
RageBot.OverrideMinDamage(1, 10)
```

## OverrideHitchance

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| index | int | Entity index |
| value | int | New hitchance |

```lua
RageBot.OverrideHitchance(1, 10)
```

## ForceSafety

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| index | int | Entity index |

```lua
RageBot.ForceSafety(1)
```

## SetTargetPriority

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| index | int | Entity index |
| priority | int | Arbitrary numerical priority value - higher value = higher priority |

```lua
RageBot.SetTargetPriority(1, 100)
```

## SetHitboxPriority

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| index | int | Entity index |
| hitbox | int | Hitbox index |
| priority | int | Arbitrary numerical priority value - higher value = higher priority |

```lua
RageBot.SetHitboxPriority(1, 0, 100)
```

## ForceHitboxSafety

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| index | int | Entity index |
| hitbox | int | Hitbox index |

```lua
RageBot.ForceHitboxSafety(1, 0)
```

## EnableHitbox

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| index | int | Entity index |
| hitbox | int | Hitbox index |
| state | bool | Hitbox state |

```lua
RageBot.EnableHitbox(1, 0, false)
```

## EnableMultipoints

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| index | int | Entity index |
| hitbox | int | Hitbox index |
| state | bool | Multipoint state |

```lua
RageBot.EnableMultipoints(1, 0, false)
```

## IgnoreTarget

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| index | int | Entity index |

```lua
RageBot.IgnoreTarget(1)
```
