#
# @JBData31@gmail.com 2021-05
#
# @see http://github.com/nwhitehead/pyfluidsynth
# addon to link libfluidsynth.so.3 (fluidsynth 2.2.1)
#
from ctypes import CFUNCTYPE
from fluidsynth import find_library, cfunc, c_void_p, c_int, c_char_p

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
def initFluidSynth():
  return  find_library('fluidsynth')

#
#
#
if __name__ == '__main__':
  pass 
