def get_inputtype(input):
    """
    Get input types based on input file format
    
    :param input:input file
    :return: type 

    """
    type = "Wrong Type"
    if input.split("/")[-1].split(".")[-1] == "mol2":
        type = "mol2"
    elif input.split("/")[-1].split(".")[-1] == "pdb":
        type = "pdb"
    elif input.split("/")[-1].split(".")[-1] == "sdf":
        type = "sdf"
    elif input.split("/")[-1].split(".")[-1] == "smi":
        type = "smile"
    print("Input Type:" +type)

    return type