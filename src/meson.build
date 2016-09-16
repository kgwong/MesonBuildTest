project('MesonBuildTest', 'cpp')

list_all_cpps_command = run_command('python', 'list_files_with_ext.py', '.cpp')
all_cpps = list_all_cpps_command.stdout().strip().split('\n')
executable('hello-world.exe', all_cpps) 
