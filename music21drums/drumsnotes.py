#
# @JBData31@gmail.com 2021-04
#
import copy as Copy

from music21 import stream, clef, meter, tempo, duration, articulations
from music21.note import Note

#
# Partition init
#
def drumsPart():
  return stream.Part([clef.PercussionClef(), meter.TimeSignature('4/4'), tempo.MetronomeMark(number=80)])

#
# Base class
#
class DrumsNote(Note):

  #
  # Constructor
  #
  def __init__(self, *arguments, **keywords):
    if 'duration' not in keywords:
      keywords.update({'duration': duration.Duration(0.5)})
    super().__init__(*arguments, **keywords) 

#
# Snare
#
class Snare(DrumsNote) :

  #
  # Constructor
  #
  def __init__(self, *arguments, **keywords):
    super().__init__(38, *arguments, **keywords) 

#
# Kick
#
class Kick(DrumsNote):

  #
  # Constructor
  #
  def __init__(self, *arguments, **keywords):
    super().__init__(35, *arguments, **keywords)
    self.articulations = [articulations.StrongAccent()]

#
# HiHat
#
class HiHat(DrumsNote):

  #
  # Constructor
  #
  def __init__(self, *arguments, **keywords):
    super().__init__(42, *arguments, **keywords) 

#
# HiHat
#
class OpenHiHat(DrumsNote):

  #
  # Constructor
  #
  def __init__(self, *arguments, **keywords):
    super().__init__(46, *arguments, **keywords) 

#
# HiHat
#
class PedalHiHat(DrumsNote):

  #
  # Constructor
  #
  def __init__(self, *arguments, **keywords):
    super().__init__(44, *arguments, **keywords) 

#
# Crash 
#
class Crash(DrumsNote):

  #
  # Constructor
  #
  def __init__(self, *arguments, **keywords):
    super().__init__(49, *arguments, **keywords) 

#
# Ride 
#
class Ride(DrumsNote):

  #
  # Constructor
  #
  def __init__(self, *arguments, **keywords):
    super().__init__(51, *arguments, **keywords) 

#
# Tom  
#
class HighTom(DrumsNote):

  #
  # Constructor
  #
  def __init__(self, *arguments, **keywords):
    super().__init__(50, *arguments, **keywords) 

#
# Tom  
#
class MiddleTom(DrumsNote):

  #
  # Constructor
  #
  def __init__(self, *arguments, **keywords):
    super().__init__(47, *arguments, **keywords) # 48

#
# Tom  
#
class LowTom(DrumsNote):

  #
  # Constructor
  #
  def __init__(self, *arguments, **keywords):
    super().__init__(45, *arguments, **keywords) 

#
#
#
def _note2drumsnote(pNote):
  if isinstance(pNote, Snare):
    pNote.name = 'B4'
  elif isinstance(pNote, Kick):
    pNote.name = 'D4'
  elif isinstance(pNote, HiHat):
    pNote.name = 'G5'
    pNote.notehead = 'x'
  elif isinstance(pNote, OpenHiHat):
    pNote.name = 'G5'
    pNote.notehead = 'circle-x'
  elif isinstance(pNote, PedalHiHat):
    pNote.name = 'D4'
    pNote.notehead = 'x'
  elif isinstance(pNote, Crash):
    pNote.name = 'A5'
    pNote.notehead = 'x'
    pNote.articulations = [articulations.Accent()]
  elif isinstance(pNote, Ride):
    pNote.name = 'B5'
    pNote.notehead = 'x'
  elif isinstance(pNote, HighTom):
    pNote.name = 'E5'
  elif isinstance(pNote, MiddleTom):
    pNote.name = 'D5'
  elif isinstance(pNote, LowTom):
    pNote.name = 'F4'

#
#
#
def showDrums(pPart):
  aPart = Copy.deepcopy(pPart)
  #for aNote in aPart.getElementsByClass('Note'):
  for aNote in aPart.recurse().notes:
    aClassName = type(aNote).__name__
    print(type(aNote), aClassName)
    if (aNote.isNote):
      _note2drumsnote(aNote)
    if (aNote.isChord):
      isCrash = False
      for aNote2 in aNote._notes:
        _note2drumsnote(aNote2)
        if isinstance(aNote2, Crash):
          isCrash = True
      if isCrash:
        aNote.articulations = [articulations.Accent()]
  aPart.show()

#
# Main
#
if __name__ == '__main__':
  pass
