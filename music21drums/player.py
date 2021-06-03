#
# @JBData31@gmail.com 2021-05
#
# @install apt-get install fluidsynth libfluidsynth-dev, pip install pyFluidSynth 
# @see http://www.fluidsynth.org/api/fluidsettings.xml
# @see http://sites.google.com/site/soundfonts4u/
#
import logging as Logging
import time
import random
import unittest

from ctypes import CFUNCTYPE
from fluidsynth import FLUID_OK, FLUID_FAILED, c_void_p, c_int, c_char_p
from fluidsynth import new_fluid_settings, fluid_settings_setstr, new_fluid_synth, new_fluid_audio_driver, fluid_synth_sfload, delete_fluid_audio_driver, delete_fluid_synth, delete_fluid_settings, fluid_synth_set_reverb_level, fluid_synth_set_chorus
from fluidsynth2 import initFluidSynth 
from fluidsynth2 import new_fluid_player, fluid_is_soundfont, fluid_is_midifile, fluid_player_add, fluid_player_add_mem, fluid_player_play, fluid_player_join, delete_fluid_player, fluid_player_set_playback_callback, fluid_player_set_tick_callback, fluid_midi_event_get_pitch, fluid_synth_reverb_on, fluid_synth_chorus_on 

from music21 import mainTest, defaults, corpus
from music21.exceptions21 import Music21Exception
from music21.midi import translate as midiTranslate

#
#
#
class StreamPlayer2Exception(Music21Exception):
  pass

#
# StreamPlayer2 class
#
class StreamPlayer2():

  #
  # @Constructor
  # @param driver: "alsa" | "jack" | "portaudio".
  # @param soundfount: Soundfont file path.
  #
  def __init__(self, driver='alsa', soundfont='/usr/share/sounds/sf2/FluidR3_GM.sf2'):
    Logging.basicConfig(level=Logging.INFO)

    self._midi = None
    fluidlib = initFluidSynth()
    if fluidlib is None:
      raise StreamPlayer2Exception('libfluidsynth.so not found.')
    Logging.info(f'{fluidlib} lib loaded.')
    self.settings = new_fluid_settings()
    result = fluid_settings_setstr(self.settings, 'audio.driver'.encode(), driver.encode())
    Logging.info(f'Fluidsynth settings [{driver}, {soundfont}] done with result {result}.')
    self.synth = new_fluid_synth(self.settings)

    self.player = new_fluid_player(self.synth)
    self._setSoundFont(soundfont)
    Logging.info(f'Audio player created with id {self.player}.')

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
    if not self._midi is None:
      raise StreamPlayer2Exception('midi file is already set.')
    self._midi = filename
    return fluid_player_add(self.player, filename.encode())

  #
  #
  #
  def setMidiStream(self, stream):
    if not self._midi is None:
      raise StreamPlayer2Exception('midi stream is already set.')
    streamMidiFile = midiTranslate.streamToMidiFile(stream)
    streamMidiWritten = streamMidiFile.writestr()
    self._midi = streamMidiFile

    return fluid_player_add_mem(self.player, streamMidiWritten, len(streamMidiWritten))
    
  #
  #
  #
  def play(self):
    if self._midi is None:
      raise StreamPlayer2Exception('midi not set, use setMidiFile or setMidiStream.')
    self.adriver = new_fluid_audio_driver(self.settings, self.synth)
    Logging.info(f'Audio driver thread started with id {self.adriver}.')
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
  def testBachDetune(self):
    b = corpus.parse('bwv66.6')
    keyDetune = []
    for i in range(127):
      keyDetune.append(random.randint(-30, 30))
    for n in b.flat.notes:
      n.pitch.microtone = keyDetune[n.pitch.midi]
    player = StreamPlayer2(driver='alsa', soundfont='/usr/share/sounds/sf2/FluidR3_GM.sf2')
    player.setMidiStream(b)
    player.play()
    player.stop()

  #
  #
  #
  def testMidiDrums(self):
    player = StreamPlayer2(soundfont='../_soundfont/PNS_Drum_Kit.SF2')
    player.setMidiFile('../_midi/tuto_drumsnotes.mid')
    try:
      player.setMidiFile('../_midi/tuto_drumsnotes.mid')
    except StreamPlayer2Exception as ex:
      Logging.info(f'{ex} test done.')
    player.play()
    player.stop()

  #
  # tick_callback requires fluidsynth 2.2.X.
  #
  def testCallback(self):

    #
    # @warn don't use logging api otherwise coredump
    #
    def _playback_callback(data, event):
      print(f' _playback_callback [{data}, {event}, {type(event)}].')
      return FLUID_OK

    #
    # @warn don't use logging api otherwise coredump
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
    #fluid_player_set_playback_callback(player.getFluidSynthPlayer(), CFUNCTYPE(c_int, c_void_p, c_void_p)(_playback_callback), 'a dummy str') 
    fluid_player_set_tick_callback(player.getFluidSynthPlayer(), CFUNCTYPE(c_int, c_void_p, c_int)(_tick_callback), None) 
    player.play()
    player.stop()

  #
  # effects need special soundfont
  #
  def testSpecialEffect(self):
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
  mainTest(TestExternal)
