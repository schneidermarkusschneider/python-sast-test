import subprocess

class CommandHelper:
    def prepare_command(self, command_data, options):
        if options.get('shell_mode'):
            return {'cmd': command_data, 'use_shell': True}
        return {'cmd': command_data, 'use_shell': False}

    def execute_system_command(self, prepared_command):
        if prepared_command['use_shell']:
            result = subprocess.run(prepared_command['cmd'], shell=True, capture_output=True, text=True)
        else:
            result = subprocess.run(prepared_command['cmd'].split(), capture_output=True, text=True)
        return {'output': result.stdout, 'error': result.stderr}
