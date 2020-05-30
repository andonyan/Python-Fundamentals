electrons = int(input())
electrons_per_shell = []
while electrons > 0:
    if electrons - (2 * ((len(electrons_per_shell) + 1) ** 2)) > 0:
        electrons_per_shell.append(2 * (len(electrons_per_shell) + 1) ** 2)
        electrons = electrons - (2 * (len(electrons_per_shell)  ** 2))
    else:
        electrons_per_shell.append(electrons)
        electrons = 0
else:
    print(electrons_per_shell)