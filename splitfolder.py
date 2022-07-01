import splitfolders

splitfolders.ratio("D:/data/data", output="split", seed=111, 
                  ratio=(0.8, 0.15, 0.05), group_prefix=None, move=False)