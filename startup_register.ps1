$script = "powershell.exe -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$HOME\1man.army\scripts\batch_launcher.ps1`""
$task = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c $script"
$trigger = New-ScheduledTaskTrigger -AtLogOn
Register-ScheduledTask -TaskName "1manarmyBoot" -Action $task -Trigger $trigger -RunLevel Highest -Force
