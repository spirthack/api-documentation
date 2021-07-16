# CGameRules

{% hint style="info" %}
You can access GameRules class through [EntityList.GetGameRules](EntityList.md)
{% endhint %}

## Functions

## m_bFreezePeriod

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | bool | Is timeout active |

```lua
local is_freezed = EntityList.GetGameRules():m_bFreezePeriod()
print(is_freezed)
```

## m_bIsValveDS

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | bool | Is player on a valve server |

```lua
local valve_ds = EntityList.GetGameRules():m_bIsValveDS()
print(valve_ds)
```

## m_fRoundStartTime

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | float | Round start time |

```lua
local round_start_time = EntityList.GetGameRules():m_fRoundStartTime()
print(round_start_time)
```

## m_gamePhase

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | int | Game phase |

```lua
local game_phase = EntityList.GetGameRules():m_gamePhase()
print(game_phase)
```

## m_iNumConsecutiveCTLoses

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | int | Number of consecutive CT loses |

```lua
local ct_loses = EntityList.GetGameRules():m_iNumConsecutiveCTLoses()
print(ct_loses)
```

## m_iNumConsecutiveTerroristLoses

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | int | Number of consecutive T loses |

```lua
local t_loses = EntityList.GetGameRules():m_iNumConsecutiveTerroristLoses()
print(t_loses)
```

## m_iRoundTime

### Return value:

| Name | Type | Description |
| :--- | :--- | :--- |
| value | int | Round time |

```lua
local round_time = EntityList.GetGameRules():m_iRoundTime()
print(round_time)
```
