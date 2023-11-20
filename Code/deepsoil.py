
def write_file(filename, num_layers, thickness, Vs):
    with open(filename, 'w') as f:
        f.write("[FILE_VERSION]:[1]\n")
        f.write("[ANALYSIS_DOMAIN]:[TIME+FREQUENCY]\n")
        f.write("\t[MAX_ITERATIONS]:[15] [COMPLEX_MOD]:[SHAKE_FI] [EFFECTIVE_SSR]:[0.65]\n")
        f.write("[ANALYSIS_TYPE]:[NONLINEAR]\n")
        f.write("[SHEAR_TYPE]:[VELOCITY]\n")
        f.write("[MAX_ITERATIONS]:[5]\n")
        f.write("[ERROR_TOL]:[1E-05]\n")
        f.write("[STEP_CONTROL]:[FLEXIBLE] [MAX_STRAIN_INC]:[5E-06] [INTERPOLATION]:[ZERO_PADDED]\n")
        f.write("[VISCOUS_DAMPING]:[RAYLEIGH_2] [RAYLEIGH_TYPE]:[FREQUENCIES] [0.8] [9]\n")
        f.write("[DAMPING_UPDATE]:[TRUE]\n")
        f.write("[STEP_CONTROL]:[FLEXIBLE] [MAX_STRAIN_INC]:[5E-06] [INTERPOLATION]:[ZERO_PADDED]\n")
        f.write("[NUM_LAYERS]:[%d]\n" % num_layers)
        f.write("[WATER_TABLE]:[1]\n")

        for i in range(1, num_layers+1):
            f.write("[LAYER]:[%d]\n" % i)
            f.write("\t[THICKNESS]:[%.2f] [WEIGHT]:[18.8] [SHEAR]:[%.2f] [SS_DAMP]:[0.03]\n" % (thickness[i-1], Vs[i-1]))
            f.write("\t[MODEL]:[MKZ] [REFERENCE_STRAIN]:[0.00127] [REFERENCE_STRESS]:[0.3] [BETA]:[1.34] [S]:[1] [B]:[0] [D]:[0]\n")
            f.write("\t[MRDF]:[NONE]\n")
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
    