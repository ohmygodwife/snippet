import angr
import logging

def main():
    p = angr.Project("defcamp_r200", auto_load_libs=False)
    sm = p.factory.simulation_manager()

    # merge all states every time we hit the bottom of the outer loop
    sm.use_technique(angr.exploration_techniques.ManualMergepoint(0x4007FD, wait_counter=9999))
    # avoid the antidebug traps (dead loop), go to puts("Nice!")
    # 000000000040085D                 jmp     short loc_40085D
    # 0000000000400882                 jmp     short loc_400882
    sm.use_technique(angr.exploration_techniques.Explorer(find=0x400936, avoid=(0x40085D, 0x400882)))
    # go!
    sm.run()
    return sm.one_found.posix.dumps(0).split('\n')[0]

def test():
    assert main() == 'rotors'

if __name__ == '__main__':
#    logging.getLogger('angr.manager').setLevel('DEBUG')
#    logging.getLogger('angr.exploration_techniques.manual_mergepoint').setLevel('DEBUG')
    print main()
