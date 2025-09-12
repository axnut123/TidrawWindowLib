#Copyrights (C) Haoriwa, All rights reserved.
#Ti Window Lib 2.0-TWL2.0
#use OOP to easly create a window application.
import sys
from ti_system import *
def version(gettype=0):
  """Get version, arg(s): 1.give 0 to get version tuple. give 1 to get copyright str."""
  if gettype==0:return 1,0,1
  elif gettype==1:return "Copyright (C) Haoriwa all rights reserved"
  else:raise ValueError("Unknown arguments.")
class WinBaseObject:
  """Window base class."""
  def __init__(self,winx=0,winy=0,winmaxx=0,winmaxy=0,linebold="thin",linestyle="solid",winbarred=None,winbargreen=None,winbarblue=None,title=None,ver=None,company=None,copyrights=None,originalname=None,textcolorred=None,textcolorgreen=None,textcolorblue=None):
    self.winbarred=winbarred
    self.winbargreen=winbargreen
    self.winbarblue=winbarblue
    self.linebold=linebold
    self.linestyle=linestyle
    self.winx=winx
    self.winy=winy
    self.winmaxx=winmaxx
    self.winmaxy=winmaxy
    self.title=title
    self.ver=ver
    self.company=company
    self.copyrights=copyrights
    self.originalname=originalname
    self.textcolorred=textcolorred
    self.textcolorgreen=textcolorgreen
    self.textcolorblue=textcolorblue
  def GetWindowInfo(self):
    """Get window info. no arg needed."""
  def CreateWindow(self,winbarred,winbargreen,winbarblue,title,textcolorred,textcolorgreen,textcolorblue,linebold="thin",linestyle="solid",winx=0,winy=0,winmaxx=0,winmaxy=0):
    """For create a window. 8 args needed. winbarred:window title bar red,winbargreen:window title bar green,winbarblue:window title bar blue,title:text for title,textred:red,textgreen:green,textblue:blue.optional args:linebold(str)=thin:(thin,thick),linestyle(str)=solid:(solid,dotted,dashed),winx=0:minimum x,winy=0:minimum y,winmaxx=0:maxium x,winmaxy=0:maxiun y."""
    self.winbarred=winbarred
    self.winbargreen=winbargreen
    self.winbarblue=winbarblue
    self.title=title
    self.winx=winx
    self.winy=winy
    self.winmaxx=winmaxx
    self.winmaxy=winmaxy
    self.textcolorred=textcolorred
    self.textcolorgreen=textcolorgreen
    self.textcolorblue=textcolorblue
    self.linebold=linebold
    self.linestyle=linestyle
    set_pen(self.linebold,self.linestyle)
    set_window(self.winx,self.winmaxx,self.winy,self.winmaxy)
    return 0
  def DrawWindow(self):
    """Draw the window that created."""
    set_color(self.winbarred,self.winbargreen,self.winbarblue)
    fill_rect(0,0,320,22)
    set_color(0,0,0)
    draw_line(0,22,320,22)
    set_color(self.textcolorred,self.textcolorgreen,self.textcolorblue)
    draw_text(5,20,self.title)
    return 0
  @staticmethod
  def WinUpdate():
    """Update screen."""
    paint_buffer()
  @staticmethod
  def TerminateProcess(code=None):
    """Terminate app. 1 optional arg. give quit code."""
    sys.stdout.write("APP exit with code:%s."%(code))
    raise SystemExit(code)
  def SetAPPInfo(self,ver,company,copyrights,originalname):
    """Set a info for your app. 4 args needed and must be string. version, company, copyright info, original name for app"""
    self.ver=ver
    self.company=company
    self.copyrights=copyrights
    self.originalname=originalname
  def GetAPPInfo(self,gettype="ver"):
    """Get the info that set by SetAPPInfo method. same pattern for SetAPPInfo."""
    if gettype=="ver":return self.ver
    elif gettype=="company":return self.company
    elif gettype=="copyrights":return self.copyrights
    elif gettype=="originalname":return self.originalname
    else:raise ValueError("Unknown arguments.")
class WinWidgetsObject:
  """Window widgets object."""
  def __init__(self):pass
  class ToolBar:
    def __init__(self,toolbarenb=False,toolbarred=None,toolbargreen=None,toolbarblue=None,tbid=None):
      self.toolbarenb=toolbarenb
      self.toolbarred=toolbarred
      self.toolbargreen=toolbargreen
      self.toolbarblue=toolbarblue
      self.tbid=tbid
    def CreateToolBar(self,toolbarenb,toolbarred,toolbargreen,toolbarblue):
      self.toolbarenb=toolbarenb
      self.toolbarred=toolbarred
      self.toolbargreen=toolbargreen
      self.toolbarblue=toolbarblue
    def AllocToolBarText(self,tbid):
      """Allocate a ID for text. tbid:give a id."""
      self.tbid=tbid
    def SetToolBarText(self,tbid,text,x,y,r,g,b,draw=False):
      """Setup a toolbar text. tbid for toolbar text id, your text with x,y,r,g,b arguments and count for text."""
      if self.tbid==tbid and draw:
        set_color(r,g,b)
        draw_text(x,y,text)
    def DrawToolBar(self):
      """Render toolbar. no argument."""
      if self.toolbarenb:
        set_color(self.toolbarred,self.toolbargreen,self.toolbarblue)
        fill_rect(0,22,320,22)
        set_color(0,0,0)
        draw_line(0,44,320,44)
  def SetText(self,x,y,text,r,g,b):
    """Setup a text, arguments: x,y,text,r,g,b."""
    set_color(r,g,b)
    draw_text(x,y,text)
    return 0
  def SetShape(self,shapetype,x,y,r,g,b,maxx=None,maxy=None,rd=None,filled=None):
    """Setup a shape, arguments:shapetype(circle,rect,line),x,y,r,g,b,maxx(default:None,used by rect),maxy(default:None,used by rect.),rd(default:None,used by circle.),filled[bool](default:None,used by rect and circle.)"""
    set_color(r,g,b)
    if shapetype=="circle":
      if filled:
        fill_circle(x,y,rd)
      else:
        draw_circle(x,y,rd)
      return 0
    elif shapetype=="rect":
      if filled:
        fill_rect(x,y,maxx,maxy)
      else:
        draw_rect(x,y,maxx,maxy)
      return 0
    elif shapetype=="line":
      draw_line(x,y,maxx,maxy)
      return 0