project('MesonBuildTest', 'cpp')

list_all_cpps_command = run_command('python', 'list_files_with_ext.py', '.cpp')
if list_all_cpps_command.returncode() == 1
    error('if statement')
    fallback_command = run_command('list_files_with_ext.py', '.cpp')
    all_cpps = fallback_command.stdout().strip().split('\n') 
else
    all_cpps = list_all_cpps_command.stdout().strip().split('\n')
endif


executable('hello-world.exe', all_cpps) 
