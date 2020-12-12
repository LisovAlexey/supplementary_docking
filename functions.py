from pathlib import Path

from pymol import cmd


def copy_to_file(file, wf):
    with file.open("r") as rf:
        for line in rf.readlines():
            wf.write(line)


def merge_mols(path_str):
    try:
        path = Path(path_str)
    except Exception as e:
        print(e)
        print("Wrong path string :", path_str)
        return

    if not path.is_dir():
        print("Error! No such directory", path)
        return

    outname = "merged_ligands"
    output_file = path / (outname + ".mol2")

    with output_file.open("w") as wf:
        for file in path.iterdir():
            if file.suffix == ".mol2" and file.stem != outname:
                copy_to_file(file, wf)

    print("Success! File saved to:", output_file)

    cmd.load(str(output_file))
    return path


cmd.extend("merge_mols", merge_mols)
