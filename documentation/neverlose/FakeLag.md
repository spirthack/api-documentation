# FakeLag

## Functions

## Choking

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | bool | Is chocking packet |

```lua
local chocking = FakeLag.Choking()
```

## ForceSend

### Choke this tick, and send packet on next tick.

```lua
FakeLag.ForceSend()
```

## SentPackets

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | int | How many packets sent in row. |

```lua
local sent_packets_num = FakeLag.SentPackets()
```

## SetState

### Parameters:

| Name | Type | Description |
| :--- | :--- | :--- |
| state | bool | Set packet state False - choke packet True - send packet |

```lua
FakeLag.SetState(false)
```
