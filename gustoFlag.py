###########
# GustoObsFlag
###########
from enum import IntFlag


class GustoSeqFlag(IntFlag):
    """
    Define flags which reflect the quality or processing of an observation.  Observations refer to a
    calibratable set of integrations (for example a full OTF scan including the HOTs and REFs)

    usage:
    # produce a level_1a processed flag
    level_1a = GustoSeqFlag(level_1a)

    # a processed level flag in header

    processed_flag = processed_level |

    """
    incomplete = IntFlag(1) #, 'incomplete_obs'
    level_1a = IntFlag(2)  # 'level_1a_processed'
    level_1b = IntFlag(4)   # 'level_1b_processed'
    level_1c = IntFlag(8) #  'level_1c_processed'
    badbaselines = IntFlag(16) # 'baseline_issues'


class GustoBbtypeFlag(IntFlag):
    """

    Define Flags which impact entire integrations

    """
    corrupt = IntFlag(1) 
    problem = IntFlag(2) 
    ignore = IntFlag(4) 


class GustoMixerFlag(IntFlag):
    """

    Define Flags which impact individual mixers

    """
    underpumped = IntFlag(1)  
    problem = IntFlag(2)  


class GustoChannelFlag(IntFlag):
    """

    Define Flags which impact individual spectrometer channels, can appear at any channel of any integration

    """
    spike = IntFlag(1) #, 'spike'
    data_ool = IntFlag(2) #, 'out_of_limit'
    possible_line = IntFlag(4) #, 'potential_line'
    bad_channel = IntFlag(8) #, 'unknown_problem'
