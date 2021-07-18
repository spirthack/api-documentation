# Doubletap Speed

> Author: [@elleqt](https://github.com/elleqt)
>
> Name: `Doubletap speed`
>
> Description: `Doubletap speed`

```lua
local sv_maxusrcmdprocessticks = g_CVar:FindVar("sv_maxusrcmdprocessticks")

cheat.RegisterCallback("prediction", function()

    sv_maxusrcmdprocessticks:SetInt(17)
    exploits.OverrideDoubleTapSpeed(15)

end)

cheat.RegisterCallback("destroy", function()
	sv_maxusrcmdprocessticks:SetInt(16)
    exploits.OverrideDoubleTapSpeed(13)
end)
```
