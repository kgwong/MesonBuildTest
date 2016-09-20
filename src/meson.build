project('MesonBuildTest', 'cpp')

windows_list_all_cpps_command = run_command('python', 'list_files_with_ext.py', '.cpp')
if windows_list_all_cpps_command.returncode() == 1
    fallback_command = run_command('list_files_with_ext.py', '.cpp')
    all_cpps = fallback_command.stdout().strip().split('\n') 
else
    all_cpps = windows_list_all_cpps_command.stdout().strip().split('\n')
endif

gtest = subproject('gtest')
sdl = subproject('sdl2')

executable('hello-world.exe', all_cpp, dependencies : [gtest, sdl])
