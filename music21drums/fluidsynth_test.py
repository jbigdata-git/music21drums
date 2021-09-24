#
# @author JBData31@gmail.com 2021-05
#
# @see https://www.fluidsynth.org/api/fluidsettings.xml
# @see /usr/local/lib/python3.8/dist-packages/fluidsynth.py

import time
import random
import unittest

import fluidsynth
from fluidsynth import lib, FLUID_OK, FLUID_FAILED, cfunc, c_void_p, c_int, c_char_p
from fluidsynth import new_fluid_settings, fluid_settings_setstr, new_fluid_synth, new_fluid_audio_driver, fluid_synth_sfload, delete_fluid_audio_driver, delete_fluid_synth, delete_fluid_settings, fluid_synth_set_reverb_level, fluid_synth_set_chorus
from ctypes import CFUNCTYPE
from ctypes.util import find_library

from music21 import defaults, corpus
from music21.exceptions21 import Music21Exception
from music21.midi import translate as midiTranslate

#
# pyFluidSynth adds
#
new_fluid_player = cfunc('new_fluid_player', c_void_p,
                         ('synth', c_void_p, 1))

fluid_is_soundfont = cfunc('fluid_is_soundfont', c_int,
                           ('filename', c_char_p, 1))

fluid_is_midifile = cfunc('fluid_is_midifile', c_int,
                          ('filename', c_char_p, 1))

fluid_player_add = cfunc('fluid_player_add', c_int,
                          ('player', c_void_p, 1),
                          ('midifile', c_char_p, 1))

fluid_player_add_mem = cfunc('fluid_player_add_mem', c_int,
                          ('player', c_void_p, 1),
                          ('buffer', c_void_p, 1),
                          ('len', c_int, 1 ))

fluid_player_play = cfunc('fluid_player_play', c_int,
                          ('player', c_void_p, 1))

fluid_player_join = cfunc('fluid_player_join', c_int,
                          ('player', c_void_p, 1))

delete_fluid_player = cfunc('delete_fluid_player', None,
                            ('player', c_void_p, 1))

fluid_player_set_playback_callback = cfunc('fluid_player_set_playback_callback', c_int,
                                           ('player', c_void_p, 1),
                                           ('handler', CFUNCTYPE(c_int, c_void_p, c_void_p), 1),
                                           ('handler_data', c_void_p, 1))

fluid_player_set_tick_callback = cfunc('fluid_player_set_tick_callback', c_int,
                                       ('player', c_void_p, 1),
                                       ('handler', CFUNCTYPE(c_int, c_void_p, c_int), 1),
                                       ('handler_data', c_void_p, 1))

fluid_midi_event_get_pitch = cfunc('fluid_midi_event_get_pitch', c_int,
                                   ('fluid_midi_event_t', c_void_p, 1))

fluid_synth_reverb_on = cfunc('fluid_synth_reverb_on', c_int,
                              ('synth', c_void_p, 1),
                              ('fx_group', c_int, 1),
                              ('on', c_int, 1))

fluid_synth_chorus_on = cfunc('fluid_synth_chorus_on', c_int,
                              ('synth', c_void_p, 1),
                              ('fx_group', c_int, 1),
                              ('on', c_int, 1))

#
#
#
class StreamPlayer2Exception(Music21Exception):
  pass

#
# StreamPlayer2 class
#
#class StreamPlayer2(fluidsynth.Synth):
class StreamPlayer2():

  #
  # @Constructor
  # @param driver: "alsa" | "jack" | "portaudio".
  # @param soundfount: Soundfont file path.
  #
  #def __init__(self, *arguments, **keywords):
  def __init__(self, driver='alsa', soundfont='/usr/share/sounds/sf2/FluidR3_GM.sf2'):
    #super().__init__(*arguments, **keywords)

    self._midiFile = None
    fluidlib = find_library('fluidsynth')
    if fluidlib is None:
      raise StreamPlayer2Exception('libfluidsynth.so not found.')
    print(f'Fluidsynth lib loaded {fluidlib}.')
    self.settings = new_fluid_settings()
    result = fluid_settings_setstr(self.settings, 'audio.driver'.encode(), driver.encode())
    print(f'Fluidsynth settings [{driver}, {soundfont}] done with result {result}.')
    self.synth = new_fluid_synth(self.settings)

    result = fluid_synth_chorus_on(self.synth, -1, True)
    print(f'Set chorus on with result {result}.')
    result = fluid_synth_set_chorus(self.synth, 50, 5.0, 2.5, 10.0, 1)
    print(f'Set chrorus params with result {result}.')

    self.player = new_fluid_player(self.synth)
    self._setSoundFont(soundfont)
    print(f'Audio player created with id {self.player}.')

  #
  # private use
  #
  def _setSoundFont(self, filename):
    return fluid_synth_sfload(self.synth, filename.encode(), 1)

  #
  #
  #
  def getFluidSynth(self):
    return self.synth 

  #
  #
  #
  def getFluidSynthPlayer(self):
    return self.player

  #
  #
  #
  def setMidiFile(self, filename):
    if not self._midiFile is None:
      raise StreamPlayer2Exception('StreamPlayer2 has already a midi file')
    self._midiFile = filename
    return fluid_player_add(self.player, filename.encode())

  #
  #
  #
  def setMidiStream(self, stream):
    streamMidiFile = midiTranslate.streamToMidiFile(stream)
    streamMidiWritten = streamMidiFile.writestr()

    return fluid_player_add_mem(self.player, streamMidiWritten, len(streamMidiWritten))
    
  #
  #
  #
  def play(self):
    self.adriver = new_fluid_audio_driver(self.settings, self.synth)
    print(f'Audio driver thread started with id {self.adriver}.')
    fluid_player_play(self.player);
    fluid_player_join(self.player);

  #
  #
  #
  def stop(self):
    delete_fluid_audio_driver(self.adriver);
    delete_fluid_player(self.player);
    delete_fluid_synth(self.synth);
    delete_fluid_settings(self.settings);

#
#
#
class TestExternal(unittest.TestCase):

  #
  #
  #
  def _testBachDetune(self):
    b = corpus.parse('bwv66.6')
    keyDetune = []
    for i in range(127):
      keyDetune.append(random.randint(-30, 30))
    for n in b.flat.notes:
      n.pitch.microtone = keyDetune[n.pitch.midi]
    #sp = StreamPlayer(b)
    #sp.play()
    player = StreamPlayer2(driver='alsa')
    #player.setSoundFont('/usr/share/sounds/sf2/FluidR3_GM.sf2')
    player.setMidiStream(b)
    player.play()
    player.stop()

  #
  #
  #
  def _testMidiDrums(self):
    player = StreamPlayer2(soundfont='../_soundfont/PNS_Drum_Kit.SF2')
    player.setMidiFile('../_midi/tuto_drumsnotes.mid')
    try:
      player.setMidiFile('../_midi/tuto_drumsnotes.mid')
    except StreamPlayer2Exception:
      # Test
      pass
    player.play()
    player.stop()
    #player.setSoundFont('/usr/share/sounds/sf2/FluidR3_GM.sf2')
    #player.setMidiFile('../_midi/novelette.mid')
    #player.play()
    #player.stop()

  #
  # 
  #
  def testPlayCallback(self):
    #
    #
    #
    def _playback_callback(data, event):
      print(f' _playback_callback [{data}, {event}, {type(event)}].')
      return FLUID_OK

    b = corpus.parse('bwv66.6')
    keyDetune = []
    for i in range(127):
      keyDetune.append(random.randint(-30, 30))
    for n in b.flat.notes:
      n.pitch.microtone = keyDetune[n.pitch.midi]
    player = StreamPlayer2(driver='alsa')
    player.setMidiStream(b)
    fluid_player_set_playback_callback(player.getFluidSynthPlayer(), CFUNCTYPE(c_int, c_void_p, c_void_p)(_playback_callback), 'A dummy str') 
    player.play()
    player.stop()

  #
  # tick_callback requires fluidsynth 2.2.X.
  #
  def testTickCallback(self):
    #
    #
    #
    def _tick_callback(data, tick):
      print(f' _tick_callback [{data}, {tick}].')
      return FLUID_OK

    b = corpus.parse('bwv66.6')
    keyDetune = []
    for i in range(127):
      keyDetune.append(random.randint(-30, 30))
    for n in b.flat.notes:
      n.pitch.microtone = keyDetune[n.pitch.midi]
    player = StreamPlayer2(driver='alsa')
    player.setMidiStream(b)
    fluid_player_set_tick_callback(player.getFluidSynthPlayer(), CFUNCTYPE(c_int, c_void_p, c_int)(_tick_callback), 'A dummy str') 
    player.play()
    player.stop()

  #
  # effects need special soundfont
  #
  def _testSpecialEffect(self):
    player = StreamPlayer2(soundfont='/usr/share/sounds/sf2/FluidR3_GM.sf2')
    player.setMidiFile('../_midi/novelette.mid')
    """
    synth = player.getFluidSynth()
    result = fluid_synth_reverb_on(synth, -1, True)
    print(f'Set reverb on with result {result}.')
    result = fluid_synth_set_reverb_level(synth, 0.9)
    print(f'Set reverb level with result {result}.')
    result = fluid_synth_chorus_on(synth, -1, True)
    print(f'Set chorus on with result {result}.')
    result = fluid_synth_set_chorus(synth, 50, 5.0, 2.5, 10.0, 1)
    print(f'Set chrorus params with result {result}.')
    """
    player.play()
    player.stop()
 
#
#
#
if __name__ == '__main__':
    import music21
    music21.mainTest(TestExternal)
