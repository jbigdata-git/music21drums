#
# @JBData31@gmail.com 2021-04
#
import logging as Logging

from music21 import defaults, metadata, stream, instrument, midi, duration, meter, tempo, clef, chord, articulations
from music21.note import Note, Rest
from music21.chord import Chord 

#from music21drums.utils import *
from music21drums.drumsnotes import Snare, HiHat, OpenHiHat, PedalHiHat, Kick, Crash, Ride, HighTom, MiddleTom, LowTom
from music21drums.drumsnotes import drumsPart, showDrums 

#
#
#
Logging.basicConfig(level=Logging.INFO)
Logging.warning('Watch out!')

aPart0 = drumsPart()
aPart0.metadata = metadata.Metadata()
aPart0.metadata.title = 'Drumsnotes tutorial'
aPart0.metadata.composer = 'jbdata31@gmail.com'

# add a dummy Instrument to avoid musecore warn
aInstrument = instrument.Instrument()
aInstrument.midiChannel = 6 
aPart0.insert(aInstrument)
#
aMeasure0 = stream.Measure()
aMeasure0.append(Chord([Crash(), Kick()]))
aMeasure0.append(HiHat())
aMeasure0.append(Chord([HiHat(), Snare()]))
aMeasure0.append(HiHat())
aMeasure0.append(Chord([Crash(), Kick()]))
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
aMeasure0.append(Chord([HiHat(), Kick()]))
aMeasure0.append(OpenHiHat())
aMeasure0.append(Chord([HiHat(), Snare(), Kick()]))
aMeasure0.append(OpenHiHat())
aMeasure0.append(Chord([HiHat(), Kick()]))
aMeasure0.append(OpenHiHat())
aMeasure0.append(Chord([HiHat(), Snare(), Kick()]))
aMeasure0.append(Chord([HiHat(), Kick()]))
aPart0.append(aMeasure0)

aMeasure0 = stream.Measure()
aMeasure0.append(Chord([HiHat(duration=duration.Duration(0.25)), Kick(duration=duration.Duration(0.25))]))
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
aMeasure0.append(Snare())
aMeasure0.append(Chord([PedalHiHat(), Snare()]))
aMeasure0.append(Chord([Kick(), HighTom()]))
aMeasure0.append(Chord([Kick(), MiddleTom()]))
aMeasure0.append(Chord([Kick(), Ride(), LowTom()]))
aPart0.append(aMeasure0)

#aPart0.show()
#aPart0.show('text')
showDrums(aPart0)

aPart0.write('midi', fp='_midi/tuto_drumsnotes.mid')
Logging.info('tuto_drumsnotes.mid written in _midi.')
#aMidi = open_midi('_midi/tuto_drumsnotes.mid', False)
#list_instruments(aMidi)
