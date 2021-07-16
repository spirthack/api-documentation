# Callbacks

{% hint style="info" %}
To register a callback, you can call [Cheat.RegisterCallback](../classes/Cheat.md#registercallback) function.
{% endhint %}

## List of all callbacks:

## `draw`

This callback will be executed in game thread, it allows you do draw any primitives and has safe access to any game functions

```lua
Cheat.RegisterCallback("draw", function()
    Render.Text("Hello world, it's me", Vector2.new(10.0, 15.0), Color.new(1.0, 1.0, 1.0), 16)
end)
```

## `pre_prediction`

CreateMove callback before cheat prediction, if you need to modify something before prediction
and/or ragebot/antiaims/etc, you can do it there

### Parameters passed in callback:

| Name | Type | Description |
| :--- | :--- | :--- |
| command | C_UserCmd | Createmove command |

```lua
Cheat.RegisterCallback("pre_prediction", function(cmd)
    cmd.forwardmove = 120
end)
```

## `prediction`

CreateMove callback inside cheat prediction, if you need to modify something inside prediction
and/or before ragebot/antiaims/etc, you can do it there

### Parameters passed in callback:

| Name | Type | Description |
| :--- | :--- | :--- |
| command | C_UserCmd | Createmove command |

```lua
Cheat.RegisterCallback("pre_prediction", function(cmd)
    AntiAim.OverridePitch(90) -- UP
end)
```

## `createmove`

CreateMove callback after cheat prediction

### Parameters passed in callback:

| Name | Type | Description |
| :--- | :--- | :--- |
| command | C_UserCmd | Createmove command |

```lua
Cheat.RegisterCallback("pre_prediction", function(cmd)
    print("My forwardmove is " .. tostring(cmd.forwardmove))
end)
```

## `events`

This callback will be executed whenever new game event will be executed

### Parameters passed in callback:

| Name | Type | Description |
| :--- | :--- | :--- |
| event | IGameEvent | Event |

{% hint style="info" %}
A list of events can be found [here](https://wiki.alliedmods.net%20Counter-Strike:_Global_Offensive_Events).
{% endhint %}

```lua
cheat.RegisterCallback("events", function(event)
    if event:GetName() ~= "player_death" then return end

    print(tostring(event:GetInt("userid")) .. " was killed by " .. tostring(event:GetInt("attacker")))
end)
```

## `destroy`

This callback will be called before script unload, so you can revert changes inside this callback

```lua
Cheat.RegisterCallback("destroy", function()
    print("Bye-bye")
end)
```

## `frame_stage`

This callback will be executed on every frame stage.

### Parameters passed in callback:

| Name | Type | Description |
| :--- | :--- | :--- |
| stage | number | Stage number |

{% hint style="info" %}
A list of stages can be found [here](source_engine_enums.md#stages).
{% endhint %}

```lua
Cheat.RegisterCallback("frame_stage", function(stage)
    if stage ~= 5 then return end
    print("render_start")
end)
```

## `console`

This callback will be executed whenever the user enters something into the console

### Parameters passed in callback:

| Name | Type | Description |
| :--- | :--- | :--- |
| text | string | Text |

```lua
Cheat.RegisterCallback("console", function(text)
    print("Input text was: '" .. text .. "'")
end)
```

## `registered_shot`

This callback will be executed whenever server registers ragebot shot

### Parameters passed in callback:

| Name | Type | Description |
| :--- | :--- | :--- |
| shot | RegisteredShot | Information about shot |

```lua
Cheat.RegisterCallback("registered_shot", function(shot)
    print("[SHOT] hc: " .. tostring(shot.hitchange) .. " | backtrack: " .. tostring(shot.backtrack) .. " | hitgroup: " .. tostring(shot.hitgroup) .. " | damage: " .. tostring(shot.damage) .. " | target: " .. tostring(shot.target_index))
end)
```

## `ragebot_shot`

This callback will be executed whenever ragebot shoot

### Parameters passed in callback:

| Name | Type | Description |
| :--- | :--- | :--- |
| shot | RagebotShot | Information about shot |

```lua
Cheat.RegisterCallback("ragebot_shot", function(shot)
    print("[SHOT] hc: " .. tostring(shot.hitchange) .. " | backtrack: " .. tostring(shot.backtrack) .. " | hitgroup: " .. tostring(shot.hitgroup) .. " | damage: " .. tostring(shot.damage) .. " | target: " .. tostring(shot.target_index))
end)
```

## `fire_bullet`

This callback will be executed when other players shooting

### Parameters passed in callback:

| Name | Type | Description |
| :--- | :--- | :--- |
| shot | DT_FireBullets | Information about bullet |

```lua
Cheat.RegisterCallback("fire_bullet", function(bullet)
    print(tostring(bullet.m_iPlayer) .. " is shooting")
end)
```

## `override_view`

This callback will be executed when game is calculating view

### Parameters passed in callback:

| Name | Type | Description |
| :--- | :--- | :--- |
| setup | CViewSetup | View setup |

```lua
Cheat.RegisterCallback("override_view", function(setup)
    print("field of view is " .. tostring(setup.fov))
end)
```
