#
# @JBData31@gmail.com 2021-05
#
# @see http://web.mit.edu/music21/
# @see http://sites.google.com/site/soundfonts4u/
#
import logging as Logging
import unittest
import copy as Copy

from music21 import mainTest, metadata, stream, instrument, clef, meter, tempo, duration, articulations
from music21.note import Note
from music21.chord import Chord

from player import StreamPlayer2

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
  aPart.show('musicxml')

#
#
#
class TestExternal(unittest.TestCase):

  #
  #
  #
  def testTuto(self):
    aPart0 = drumsPart()
    aPart0.metadata = metadata.Metadata()
    aPart0.metadata.title = 'music21drumsnotes'
    aPart0.metadata.composer = 'jbdata31@gmail.com'

    # add a dummy Instrument to avoid musescore warn
    aInstrument = instrument.Instrument()
    # aInstrument.midiChannel = 9, 10, whatever
    aPart0.insert(aInstrument)
    #
    aMeasure0 = stream.Measure()
    aMeasure0.append(Chord([Crash(), Kick()]))
    aMeasure0.append(HiHat())
    aMeasure0.append(Chord([HiHat(), Snare()]))
    aMeasure0.append(HiHat())
    aMeasure0.append(Chord([Ride(), Kick()]))
    aMeasure0.append(HiHat())
    aMeasure0.append(Chord([HiHat(), Snare()]))
    aMeasure0.append(Chord([HiHat(), Kick()]))
    aPart0.append(aMeasure0)

    aMeasure0 = stream.Measure()
    aMeasure0.append(Chord([HiHat(), Kick()]))
    aMeasure0.append(HiHat())
    aMeasure0.append(Chord([HiHat(), Snare()]))
    aMeasure0.append(Chord([HiHat(), Kick()]))
    aMeasure0.append(OpenHiHat())
    aMeasure0.append(Chord([HiHat(), Kick()]))
    aMeasure0.append(Chord([HiHat(), Snare()]))
    aMeasure0.append(HiHat())
    aPart0.append(aMeasure0)

    aMeasure0 = stream.Measure()
    aMeasure0.append(Chord([HiHat(), Kick()]))
    aMeasure0.append(HiHat())
    aMeasure0.append(Chord([HiHat(), Snare()]))
    aMeasure0.append(Chord([HiHat(), Kick()]))
    aMeasure0.append(Chord([HiHat(), Kick()]))
    aMeasure0.append(OpenHiHat())
    aMeasure0.append(Chord([HiHat(), Snare()]))
    aMeasure0.append(HiHat())
    aPart0.append(aMeasure0)

    aMeasure0 = stream.Measure()
    aMeasure0.append(Snare())
    aMeasure0.append(Snare(duration=duration.Duration(0.25)))
    aMeasure0.append(Snare(duration=duration.Duration(0.25)))
    aMeasure0.append(Chord([HighTom(), PedalHiHat()]))
    aMeasure0.append(HighTom(duration=duration.Duration(0.25)))
    aMeasure0.append(HighTom(duration=duration.Duration(0.25)))
    aMeasure0.append(Chord([MiddleTom(), PedalHiHat()]))
    aMeasure0.append(MiddleTom(duration=duration.Duration(0.25)))
    aMeasure0.append(MiddleTom(duration=duration.Duration(0.25)))
    aMeasure0.append(Chord([LowTom(), PedalHiHat()]))
    aMeasure0.append(LowTom(duration=duration.Duration(0.25)))
    aMeasure0.append(Chord([Ride(duration=duration.Duration(0.25)), LowTom(duration=duration.Duration(0.25))]))
    aPart0.append(aMeasure0)

    aMeasure0 = stream.Measure()
    aMeasure0.append(Chord([HiHat(articulations=[articulations.Accent()]), Kick()]))
    aNote0 = OpenHiHat()
    aNote0.articulations = [articulations.Accent()]
    aMeasure0.append(aNote0)
    #aMeasure0.append(OpenHiHat())
    aMeasure0.append(Chord([HiHat(), Snare(), Kick()]))
    aNote0 = OpenHiHat()
    aNote0.articulations = [articulations.Accent()]
    aMeasure0.append(aNote0)
    #aMeasure0.append(OpenHiHat())
    aMeasure0.append(Chord([HiHat(), Kick()]))
    aNote0 = OpenHiHat()
    aNote0.articulations = [articulations.Accent()]
    aMeasure0.append(aNote0)
    #aMeasure0.append(OpenHiHat())
    aMeasure0.append(Chord([HiHat(), Snare(), Kick()]))
    aMeasure0.append(Chord([HiHat(), Kick()]))
    aPart0.repeatAppend(aMeasure0, 2)

    aMeasure0 = stream.Measure()
    aMeasure0.append(Chord([Crash(duration=duration.Duration(0.25)), Kick(duration=duration.Duration(0.25))]))
    aMeasure0.append(HiHat(duration=duration.Duration(0.25)))
    aMeasure0.append(OpenHiHat(duration=duration.Duration(0.25)))
    aMeasure0.append(HiHat(duration=duration.Duration(0.25)))
    aMeasure0.append(Chord([Snare(duration=duration.Duration(0.25)), Kick(duration=duration.Duration(0.25))]))
    aMeasure0.append(HiHat(duration=duration.Duration(0.25)))
    aMeasure0.append(OpenHiHat(duration=duration.Duration(0.25)))
    aMeasure0.append(HiHat(duration=duration.Duration(0.25)))
    aMeasure0.append(Chord([HiHat(duration=duration.Duration(0.25)), Kick(duration=duration.Duration(0.25))]))
    aMeasure0.append(HiHat(duration=duration.Duration(0.25)))
    aMeasure0.append(OpenHiHat(duration=duration.Duration(0.25)))
    aMeasure0.append(HiHat(duration=duration.Duration(0.25)))
    aMeasure0.append(Chord([Snare(duration=duration.Duration(0.25)), Kick(duration=duration.Duration(0.25))]))
    aMeasure0.append(HiHat(duration=duration.Duration(0.25)))
    aMeasure0.append(OpenHiHat(duration=duration.Duration(0.25)))
    aMeasure0.append(HiHat(duration=duration.Duration(0.25)))
    aPart0.append(aMeasure0)

    aMeasure0 = stream.Measure()
    aMeasure0.append(Snare())
    aMeasure0.append(Chord([PedalHiHat(duration=duration.Duration(0.25)), Snare(duration=duration.Duration(0.25))]))
    aMeasure0.append(HighTom(duration=duration.Duration(0.25)))
    aMeasure0.append(MiddleTom(duration=duration.Duration(0.25)))
    aMeasure0.append(LowTom(duration=duration.Duration(0.25)))
    aNote0 = LowTom()
    aNote0.articulations = [articulations.Accent()]
    aMeasure0.append(aNote0)
    #aMeasure0.append(LowTom(articulations = [articulations.Accent()]))
    aMeasure0.append(Chord([PedalHiHat(), Snare()]))
    aMeasure0.append(Chord([Kick(), HighTom()]))
    aMeasure0.append(Chord([Kick(), MiddleTom()]))
    aMeasure0.append(Chord([Kick(), Ride(), LowTom()]))
    aPart0.append(aMeasure0)

    showDrums(aPart0)

    aPart0.write('midi', fp='../_midi/test_drumsnotes.mid')
    Logging.info('test_drumsnotes.mid written in _midi.')

    player = StreamPlayer2(soundfont='../_soundfont/PNS_Drum_Kit.SF2')
    player.setMidiStream(aPart0)
    player.play()
    player.stop()

#
# Main
#
if __name__ == '__main__':
  Logging.basicConfig(level=Logging.INFO)
  mainTest(TestExternal)
