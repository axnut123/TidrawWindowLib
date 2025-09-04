from twlnew import *
from ti_system import *
def main():
  w=WinBaseObject()
  w.CreateWindow(210,210,210,"TWL2.0",60,25,140)
  w.SetAPPInfo("1.0.0","Your org here.","Public usage.","Example")
  s1=1
  s2=1
  st=120
  while True:
    w.DrawWindow()
    set_color(210,0,0)
    draw_text(250,20,"esc to quit")
    set_color(0,0,0)
    draw_text(st,120,s1*"["+"Press enter."+s2*"]")
    k=get_key()
    if k=="esc":w.TerminateProcess(0)
    elif k=="enter":
      s1+=1
      s2+=1
      st-=4
    elif k=="-" and s1!=0:
      s1-=1
      s2-=1
      st+=4
    w.WinUpdate()
    clear()
if __name__=="__main__":
  main()