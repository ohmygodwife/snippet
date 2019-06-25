# -*- coding: utf-8 -*- 
import angr
import claripy
import sys

proj = angr.Project('./xctf_re1',  load_options={'auto_load_libs': False})

def input():
  passwd_len = int(sys.argv[1])
  
  state = proj.factory.entry_state(add_options=angr.options.unicorn) #with unicorn 54sec, without 58sec
  # Constrain the first x bytes to be non-null and non-newline:
  for _ in xrange(passwd_len):
    k = state.posix.files[0].read_from(1)
    state.se.add(k >= 32)
    state.se.add(k < 127)

  # Constrain the last byte to be a newline
  k = state.posix.files[0].read_from(1)
  state.se.add(k == 10)

  # Reset the symbolic stdin's properties and set its length.
  state.posix.files[0].seek(0)
  state.posix.files[0].length = passwd_len + 1
  
  simgr = proj.factory.simgr(state)
  simgr.explore(find=lambda s:"correct!" in s.posix.dumps(1))
  print simgr.one_found.posix.dumps(0)

def hook():
  flag = claripy.BVS("argv1",100*8)
  class my_scanf_for_s(angr.SimProcedure):
    def run(self, fmt, ptr):
      self.state.memory.store(ptr, flag)
  proj.hook_symbol('__isoc99_scanf', my_scanf_for_s(), replace=True)
  
  simgr = proj.factory.simgr()
  simgr.explore(find=lambda s:"correct!" in s.posix.dumps(1))
  print simgr.one_found.solver.eval(flag, cast_to = str)
  
def main():
  input()
#  hook()

'''
  for pp in simgr.found:
    out = pp.posix.dumps(1)
    print out
#    inp = pp.posix.files[0].all_bytes()
#    print pp.solver.eval(inp,cast_to = str)
    print pp.solver.eval(flag, cast_to = str)
''' 

def test():
    assert main() == '9563'

if  __name__=="__main__":
  main()