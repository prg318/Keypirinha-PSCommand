# Keypirinha Plugin: PSCommand

This is PSCommand, a plugin for the
[Keypirinha](http://keypirinha.com) launcher.

PSCommand is a fork of the [Command Keypirinha plugin](https://github.com/bantya/Keypirinha-Command).

This plugin provides an easy way to execute powershell commands from Keypirinha.
## Install:

Since PSCommand is not in the PackageControl repository yet, perform a manual installation:

    Download the latest plugin file from [here](https://github.com/bantya/Keypirinha-PSCommand/releases/latest).

    Once the `Command.keypirinha-package` file is downloaded,
    move it to the `InstalledPackage` folder located at:

    - `Keypirinha\portable\Profile\InstalledPackages` in **Portable mode**
    - **Or** `%APPDATA%\Keypirinha\InstalledPackages` in **Installed mode** (the
    final path would look like
    `C:\Users\%USERNAME%\AppData\Roaming\Keypirinha\InstalledPackages`)

**NOTE:** You may have to manually restart Keypirinha to see the package activated.

## Configuration:

To use an alternate powershell binary, configure the `shell` variable.
To open the configuration, use the following keypirinha menu item:

    Configure Package -> PSCommand

Here's an example of a custom powershell path:

```ini
[main]
shell = C:\MyPowershellFolder\pwsh.exe
```


## Usage:

Invoke Keypirinha and put the command to be executed in following format:
```
[>] [command (can contain spaces)]
-OR-
[>>] [command (can contain spaces)]

e.g.

> echo 'Hello World'
>> ping google.com
```

### Difference between > and >>:

Running any command with `>>` will close the shell after completion of the command.

In case of `>`, shell will be kept open.

### Actions

- **Keep Open**: Do not close the prompt after running the command.
- **Close CMD**: Close the prompt after running the command.

*NOTE: These actions have first preference, if applied with a command.*

## License

MIT, that's it.


## Credits

- PSCommand fork author: [prg318](https://github.com/prg318)
- Original Command author: [bantya](https://github.com/bantya)
