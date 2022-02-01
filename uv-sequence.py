selection = cmds.ls(sl=True)
firstObject = selection[0]

for i in range(1, len(selection)):
    # uvs = 2 (transfer uvs 'all')
    # sampleSpace = 2 (component)
    cmds.transferAttributes(selection[0], selection[i], uvs = 2, sampleSpace = 2)