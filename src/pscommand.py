import os
import re
import subprocess
import keypirinha as kp
import keypirinha_util as kpu

class PSCommand(kp.Plugin):
    _debug = True

    SECTION_MAIN = 'main'

    REGEX_INPUT = r'^(>{1,2})\s(.+)'

    ITEM_COMMAND = kp.ItemCategory.USER_BASE + 1

    def __init__(self):
        super().__init__()

    def on_config_changed(self):
        self.dbg("on_config_changed called!")
        self._read_config()

    def _read_config(self):
        settings = self.load_settings()
        self._shell = settings.get("shell", "main", fallback="C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe")
        self.dbg("Shell is now: {}".format(self._shell))

    def on_start(self):
        self._read_config()

        actions = []

        actions.append(self._set_action('keep_open', 'Keep Open', 'Run the command and keep shell open.'))
        actions.append(self._set_action('close_cmd', 'Close shell', 'Close shell after running the command.'))

        self.set_actions(self.ITEM_COMMAND, actions)

    def on_catalog(self):
        self.on_start()

    def on_suggest(self, user_input, items_chain):
        input = re.search(self.REGEX_INPUT, user_input)

        if input is None:
            return None

        if len(input.groups()) != 2:
            pass
        else:
            operator = input.group(1)
            command = input.group(2)

        suggestion = [self._set_suggestion(operator + '@' + command)]

        self.set_suggestions(suggestion)

    def on_execute(self, item, action):
        if item.category() != self.ITEM_COMMAND:
            return

        prompt = self._shell

        [operator, command] = self._split_target(item.target())

        close = None
        if operator == '>':
            close = '-NoExit'

        if action and action.name() == "keep_open":
            close = '-NoExit'

        if os.path.isfile(prompt):
            try:
                cmd = [prompt]
                if close:
                    cmd.append(close)
                cmd.append('-Command')
                cmd.append(command)
                self.dbg("Running {}".format(cmd))
                subprocess.Popen(cmd, cwd = os.path.dirname(prompt))
            except Exception as e:
                print('Exception: CMD - (%s)' % (e))
        else:
            print('Error: Could not find \"%s\" executable.\n\nYou may need to modify the PATH' % (prompt))

    def on_activated(self):
        pass

    def on_deactivated(self):
        pass

    def on_events(self, flags):
        pass

    def _set_action(self, name, label, desc):
        return self.create_action(
            name = name,
            label = label,
            short_desc = desc
        )

    def _set_suggestion(self, target):
        [operator, command] = self._split_target(target)

        close_msg = ''
        if operator == '>>':
            close_msg = ' and close shell.'

        return self.create_item(
            category = self.ITEM_COMMAND,
            label = operator + ' ' + command,
            short_desc = 'Run \'' + command + '\' command' + close_msg,
            target = target,
            args_hint = kp.ItemArgsHint.FORBIDDEN,
            hit_hint = kp.ItemHitHint.IGNORE
        )

    def _split_target(self, target):
        return target.split('@')
