
def strataPy_output(Vs_all,depth_all):
    """
    This function generates input files for pyStrata from Vs and depth data.

    Parameters:
    Vs_all (list of lists): Each sublist contains Vs values for one profile.
    depth_all (list of lists): Each sublist contains depth values for one profile.

    The function creates a directory named "pyStrata_inputs" if it doesn't exist.
    Then, for each profile, it creates a Python file in this directory.
    The filename is "pyStrata_input{i}.py", where {i} is the profile number.
    Each file imports the pystrata module and defines a profile with the given Vs and depth values.
    """

    import os

    num_profiles = len(Vs_all)
    directory = "pyStrata_inputs"
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(1, num_profiles+1):
        filename = os.path.join(directory, "pyStrata_input{}.py".format(i))
        # Calculate the thickness of each layer
        thickness = [depth_all[i-1][j+1] - depth_all[i-1][j] for j in range(len(depth_all[i-1])-1)]
        # Eliminate layer of bedrock
        Vs = Vs_all[i-1][:-1]
        num_layers = len(Vs)
    

        with open(filename, 'w') as f:
            f.write("import pystrata\n")
            f.write("profile = pystrata.site.Profile(\n")
            f.write("    [")
            for i in range(num_layers):
                if i == num_layers-1:
                    f.write("\tpystrata.site.Layer(pystrata.site.SoilType('Rock', 18.0, None, 0.05), %.4f, %.4f)\n" % (thickness[i-1], Vs[i-1]))
                else:
                    f.write("\tpystrata.site.Layer(pystrata.site.SoilType('Soil', 18.0, None, 0.05), %.4f, %.4f),\n" % (thickness[i-1], Vs[i-1]))
            f.write("])\n")
    
