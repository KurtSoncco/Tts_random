
def write_file(filename, num_layers, thickness, Vs):
    with open(filename, 'w') as f:
        f.write("[FILE_VERSION]:[1]\n")
        f.write("[ANALYSIS_DOMAIN]:[FREQUENCY]\n")
        f.write("[ANALYSIS_TYPE]:[EQUIVALENT_LINEAR]\n")
        f.write("[SHEAR_TYPE]:[VELOCITY]\n")
        f.write("[MAX_ITERATIONS]:[15]\n")
        f.write("[ERROR_TOL]:[1E-05]\n")
        f.write("[COMPLEX_MOD]:[SHAKE_FI]\n")
        f.write("[EFFECTIVE_SSR]:[0.65]\n")
        f.write("[DYNAMIC_CURVES]:[NL_PARAMETERS]\n")
        f.write("[NUM_LAYERS]:[%d]\n" % num_layers)
        f.write("[WATER_TABLE]:[1]\n")

        for i in range(1, num_layers+1):
            f.write("[LAYER]:[%d]\n" % i)
            f.write("\t[THICKNESS]:[%.4f] [WEIGHT]:[18.8] [SHEAR]:[%.4f] [SS_DAMP]:[0.03]\n" % (thickness[i-1], Vs[i-1]))
            f.write("\t[MODEL]:[GQ] [STRENGTH]:[234] [THETA1]:[-9.97] [THETA2]:[10.8000000000001] [THETA3]:[0.891250938133747] [THETA4]:[1] [THETA5]:[0.99] [A]:[1]\n")
            f.write("\t[MRDF]:[DARENDELI] [P1]:[0.865] [P2]:[0.05]\n")
            if i == 1:
                f.write("\t[OUTPUT]:[TRUE]\n")
            else:
                f.write("\t[OUTPUT]:[FALSE]\n")
            

        f.write("[LAYER]:[TOP_OF_ROCK]\n")
        f.write("\t[OUTPUT]:[FALSE]\n")
        f.write("[HALFSPACE]:[RIGID]\n")
        f.write("[RS_TYPE]:[FREQUENCY] [RS_DAMPING]:[0.05]\n")
        f.write("[ACCELERATION_HISTORY]:[EXTERNAL] [DEEPSOILACCELINPUT.TXT]\n")
        f.write("[UNITS]:[METRIC]\n")
        f.write("[LAYER_NAMES]:[%d]\n" % num_layers)
        for i in range(1, num_layers+1):
            f.write("\t[LAYER_NAMES]:[%d][Layer?%d]\n" % (i, i))

import os

def deepsoil_input(Vs_all,depth_all):
    num_profiles = len(Vs_all)
    directory = "deepsoil_inputs"
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(1, num_profiles+1):
        filename = os.path.join(directory, "deepsoil_input{}.dp".format(i))
        # Calculate the thickness of each layer
        thickness = [depth_all[i-1][j+1] - depth_all[i-1][j] for j in range(len(depth_all[i-1])-1)]
        # Eliminate layer of bedrock
        Vs = Vs_all[i-1][:-1]
        num_layers = len(Vs)
        write_file(filename, num_layers, thickness, Vs)
    