#Copyright (C) Haoriwa 2024-2025
#All rights reserved.
#using MIT license,under LICENSE.txt.
"""TiWindowLib. easy to create a 
gui program. No OOP, only functions.
free to use for personal, organization and 
community.
to use TWL, use given function to 
recall.
-------------------------strcture:
WindowBase gets title, and draw window frame.
got an argument for dark frame,True or False.
WindowElementDraw gets elements id and 
display.
WindowMain is main function. has an argument
for keep window when stop. 1 is keep, 0 is clear.
"""
#==start============================
from ti_draw import *
from time import *
from ti_system import *
from random import *
import sys
import gc
#=================================
def Cinfo(info=1):
  return {
        1:"TWL 1.2 Build 4",
        2:"By axnut123",
        3:sys.version}.get(info)

def WindowBase(title="Twl",dark=False):  
#Basic window frame, your elements will be here.
  if dark==True:
    set_color(10,10,10)
    fill_rect(0,0,320,22)
    set_color(255,255,255)
    draw_line(0,22,320,22)
    draw_text(5,20,title)
    draw_text(29,20,str(Cinfo(1)))
  else:
    set_color(220,220,220)
    fill_rect(0,0,320,22)
    set_color(30,30,30)
    draw_line(0,22,320,22)
    draw_text(5,20,title)
    draw_text(29,20,str(Cinfo(1)))
  set_color(220,10,10)
  draw_text(235,20,"esc to quit")
  return 0

def TerminateProcess(code=None):
  gc.collect()
  raise SystemExit(code)

def WindowElementDraw(elementid):
  if elementid==1:
    set_color(0,0,0)
    draw_text(10,40,"Click enter!")
  return 0

def WindowMain(keepwindow=0):
  """this is a standard template for Twl."""
  key="0"
  use_buffer()
  clear()
  WindowBase("Twl/",False)
  WindowElementDraw(1)
  while key!="esc":
    key=str(get_key())
    if keepwindow==1:
      pass
    else:
      if key=="esc":
        TerminateProcess()
    if key=="enter":
      set_color(randint(0,255),randint(0,255),randint(0,255))
      fill_rect(0,23,320,300)
      set_color(0,0,0)
    paint_buffer()
  return 0

#=execution section====================
if __name__=="__main__":
  WindowMain()
