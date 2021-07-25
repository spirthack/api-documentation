# Doubletap Speed

> Author: [@elleqt](https://github.com/elleqt)
>
> Name: `Doubletap speed`
>
> Description: `Doubletap speed`

```lua
local sv_maxusrcmdprocessticks = g_CVar:FindVar("sv_maxusrcmdprocessticks")
sv_maxusrcmdprocessticks:SetInt(16)

cheat.RegisterCallback("prediction", function()
    exploits.OverrideDoubleTapSpeed(14)
end)

cheat.RegisterCallback("destroy", function()
    sv_maxusrcmdprocessticks:SetInt(16)
    exploits.OverrideDoubleTapSpeed(13)
end)
```
