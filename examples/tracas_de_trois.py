#
# @JBData31@gmail.com 2021-06
# Part author Nicolas Bertrand
#
import logging as Logging
import copy as Copy

from music21 import defaults, metadata, stream, instrument, midi, duration, meter, tempo, clef, chord, articulations
from music21.note import Note, Rest
from music21.chord import Chord

from drumsnotes import Snare, HiHat, OpenHiHat, PedalHiHat, Kick, Crash, Ride, HighTom, MiddleTom, LowTom
from drumsnotes import drumsPart, showDrums, StreamPlayer2

#
#
#
Logging.basicConfig(level=Logging.INFO)
Logging.warning('Watch out!')

aPart0 = drumsPart(time=meter.TimeSignature('3/4'), metronome=tempo.MetronomeMark(number=100))
aPart0.metadata = metadata.Metadata()
aPart0.metadata.title = 'Tracas de Trois by music21.drumsnotes'
aPart0.metadata.composer = 'Nicolas BERTRAND'
# add a dummy Instrument to avoid musescore warn
aInstrument = instrument.Instrument()
# aInstrument.midiChannel = 9, 10, whatever
aPart0.insert(aInstrument)
#

# A
aMeasureA0 = stream.Measure()
aMeasureA0.append(Chord([Kick(duration=duration.Duration(1.0))]))
aMeasureA0.append(Snare(duration=duration.Duration(0.5)))
aMeasureA0.append(Snare(duration=duration.Duration(0.5)))
aMeasureA0.append(Snare(duration=duration.Duration(0.5)))
aMeasureA0.append(Snare(duration=duration.Duration(0.5)))
aPart0.repeatAppend(aMeasureA0, 3)

aMeasureA3 = stream.Measure()
aMeasureA3.append(Chord([Kick(duration=duration.Duration(1.0))]))
aNote0 = Snare(duration=duration.Duration(1.0))
aNote0.articulations=[articulations.Accent()]
aMeasureA3.append(aNote0)
#aMeasureA3.append(Snare(duration=duration.Duration(1.0), articulations=[articulations.StrongAccent()]))
aMeasureA3.append(Rest(duration=duration.Duration(0.5)))
aMeasureA3.append(Snare(duration=duration.Duration(0.5)))
aPart0.append(aMeasureA3)

# B
aMeasureB0 = stream.Measure()
aMeasureB0.append(Chord([Kick(duration=duration.Duration(1.0))]))
aNote0 = Snare(duration=duration.Duration(1.0))
aNote0.articulations=[articulations.Accent()]
aMeasureB0.append(aNote0)
aMeasureB0.append(Snare(duration=duration.Duration(0.5)))
aMeasureB0.append(Snare(duration=duration.Duration(0.5)))
aPart0.append(aMeasureB0)

aMeasureB1 = stream.Measure()
aMeasureB1.append(Chord([Kick(duration=duration.Duration(1.0))]))
aMeasureB1.append(Snare(duration=duration.Duration(1.0)))
aMeasureB1.append(Snare(duration=duration.Duration(0.25)))
aMeasureB1.append(Snare(duration=duration.Duration(0.25)))
aMeasureB1.append(Snare(duration=duration.Duration(0.25)))
aMeasureB1.append(Snare(duration=duration.Duration(0.25)))
aPart0.append(aMeasureB1)

aMeasureB2 = Copy.deepcopy(aMeasureB0)
aPart0.append(aMeasureB2)

aMeasureB3 = Copy.deepcopy(aMeasureA3)
aPart0.append(aMeasureB3)

# C
aMeasureC0 = stream.Measure()
aChord0 = Chord([Snare(), Kick()])
aChord0.articulations=[articulations.Accent()]
aMeasureC0.append(aChord0)
aMeasureC0.append(Snare())
aMeasureC0.append(Snare())
aNote0 = Snare()
aNote0.articulations=[articulations.Accent()]
aMeasureC0.append(aNote0)
aMeasureC0.append(Snare())
aMeasureC0.append(Snare())
aPart0.repeatAppend(aMeasureC0, 3)

aMeasureC3 = Copy.deepcopy(aMeasureA3)
aPart0.append(aMeasureC3)

# D
aMeasureD0 = stream.Measure()
aMeasureD0.append(Chord([Kick(duration=duration.Duration(1.0))]))
aMeasureD0.append(Snare(duration=duration.Duration(0.5)))
aMeasureD0.append(Snare(duration=duration.Duration(0.5)))
aMeasureD0.append(Kick(duration=duration.Duration(0.5)))
aMeasureD0.append(Kick(duration=duration.Duration(0.5)))
aPart0.append(aMeasureD0)

aMeasureD1 = stream.Measure()
aMeasureD1.append(Snare(duration=duration.Duration(1.0)))
aNote0 = Snare(duration=duration.Duration(1.0))
aNote0.articulations=[articulations.Accent()]
aMeasureD1.append(aNote0)
aMeasureD1.append(Kick(duration=duration.Duration(1.0)))
aPart0.append(aMeasureD1)

aMeasureD2 = Copy.deepcopy(aMeasureD0)
aPart0.append(aMeasureD2)

aMeasureD3 = stream.Measure()
aMeasureD3.append(Snare(duration=duration.Duration(1.0)))
aNote0 = Snare(duration=duration.Duration(1.0))
aNote0.articulations=[articulations.Accent()]
aMeasureD3.append(aNote0)
aMeasureD3.append(Rest(duration=duration.Duration(0.5)))
aMeasureD3.append(Snare())
aPart0.append(aMeasureD3)

# E
aMeasureE0 = stream.Measure()
aMeasureE0.append(Kick(duration=duration.Duration(1.0)))
aMeasureE0.append(PedalHiHat(duration=duration.Duration(1.0)))
aMeasureE0.append(Snare(duration=duration.Duration(1.0)))
aPart0.append(aMeasureE0)

aMeasureE1 = stream.Measure()
aMeasureE1.append(Kick(duration=duration.Duration(1.0)))
aMeasureE1.append(PedalHiHat(duration=duration.Duration(1.0)))
aMeasureE1.append(Snare())
aMeasureE1.append(Snare())
aPart0.append(aMeasureE1)

aMeasureE2 = stream.Measure()
aMeasureE2.append(Kick(duration=duration.Duration(1.0)))
aMeasureE2.append(PedalHiHat(duration=duration.Duration(1.0)))
aMeasureE2.append(Snare(duration=duration.Duration(0.25)))
aMeasureE2.append(Snare(duration=duration.Duration(0.25)))
aMeasureE2.append(Snare(duration=duration.Duration(0.25)))
aMeasureE2.append(Snare(duration=duration.Duration(0.25)))
aPart0.append(aMeasureE2)

aMeasureE3 = stream.Measure()
aNote0 = Snare(duration=duration.Duration(1.0))
aNote0.articulations=[articulations.Accent()]
aMeasureE3.append(aNote0)
aMeasureE3.append(Chord([Kick(duration=duration.Duration(1.0)), Crash(duration=duration.Duration(1.0))]))
aMeasureE3.append(Rest(duration=duration.Duration(1.0)))
aPart0.append(aMeasureE3)

showDrums(aPart0)

aPart0.write('midi', fp='../_midi/tracas_de_trois.mid')
Logging.info('tracas_de_trois mid written in _midi.')

player = StreamPlayer2(soundfont='../_soundfont/PNS_Drum_Kit.SF2')
player.setMidiStream(aPart0)
player.play()
player.stop()

