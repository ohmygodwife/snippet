# -*- coding: utf-8 -*- 
import angr
import claripy

def add_cond(state, argv1):
  for byte in argv1.chop(8):
#        state.add_constraints(byte != '\x00') # null
    # '\0' || '\x20' - '\x7e'
    cond = state.solver.Or(
            byte == '\0', 
            state.solver.And(
               byte >= ord(' '), byte <= ord('~')))
    state.add_constraints(cond)
#    state.add_constraints(byte <= '~') # '\x7e'

def main():
  proj = angr.Project("./ais3_crackme")
  argv1 = claripy.BVS("argv1",100*8)
  state = proj.factory.entry_state(args=["",argv1])
#  add_cond(state, argv1)
  simgr = proj.factory.simgr(state)
  simgr.explore(find=0x400602)
  print simgr.one_found.solver.eval(argv1, cast_to=str)

def test():
    assert main() == 'ais3{I_tak3_g00d_n0t3s}'

if  __name__=="__main__":
  main()