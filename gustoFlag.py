###########
# GustoObsFlag
###########
import numpy as np
from flags import Flags


class GustoObsFlag(Flags):
    """
    Define flags which reflect the quality or processing of an observation.  Observations refer to a
    calibratable set of integrations (for example a full OTF scan including the HOTs and REFs)
    """
    flag1 = 1, 'incomplete_obs'
    flag2 = 2, 'corrupt_obs'
    flag3 = 4, 'level_1a_processed'
    flag4 = 8, 'level_1b_processed'
    flag5 = 16, 'level_1c_processed'
    flag6 = 32, 'baseline_corrected'


class GustoChannelFlag(Flags):
    """
    Define Flags which impact individual spectrometer channels, can appear at any channel of any integration
    """
    flag1 = 1, 'spike'
    flag2 = 2, 'out_of_limit'
    flag3 = 4, 'potential_line'
    flag4 = 8, 'unknown_problem'

class GustoIntegrationFlag(Flags):
    """
    Define flags reflecting the quality of an individual integration.  This could be for example the quality
    of a "HOT" integration
    """
    flag1 = 1, 'corrupt_data'
    flag2 = 2, 'mixer_under_pumped'
    flag3 = 4, 'unknown_problem'