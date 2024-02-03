#!/usr/bin/python
import musicalbeeps

def play():
    player = musicalbeeps.Player(volume=1.0,
                                 mute_output=False)

    # Examples:

    # To play an A on default octave n°4 for 0.2 seconds
    #player.play_note("A", 0.2)

    player.play_note("e5", 0.4)
    player.play_note("b4", 0.2)
    player.play_note("c5", 0.2)
    player.play_note("d5", 0.4)
    player.play_note("c5", 0.2)
    player.play_note("c5", 0.2)

    player.play_note("a4", 0.4)
    player.play_note("a4", 0.2)
    player.play_note("c5", 0.2)
    player.play_note("e5", 0.2)
    player.play_note("d5", 0.4)
    player.play_note("c5", 0.2)

    player.play_note("b4", 0.4)
    player.play_note("b4", 0.2)
    player.play_note("c5", 0.2)
    player.play_note("d5", 0.4)
    player.play_note("e5", 0.2)

    player.play_note("c5", 0.4)
    player.play_note("a4", 0.4)
    player.play_note("a4", 0.4)

    player.play_note("pause", 0.4)
    player.play_note("pause", 0.2)

    player.play_note("d5", 0.4)
    player.play_note("f5", 0.2)
    player.play_note("a5", 0.4)
    player.play_note("g5", 0.2)
    player.play_note("f5", 0.2)

    player.play_note("d5", 0.4)
    player.play_note("f5", 0.2)
    player.play_note("a5", 0.2)
    player.play_note("g5", 0.2)
    player.play_note("f5", 0.2)

    player.play_note("e5", 0.6)
    player.play_note("c5", 0.2)
    player.play_note("e5", 0.4)
    player.play_note("d5", 0.2)
    player.play_note("c5", 0.2)

    player.play_note("b4", 0.4)
    player.play_note("b4", 0.2)
    player.play_note("c5", 0.2)
    player.play_note("d5", 0.4)
    player.play_note("e5", 0.4)

    player.play_note("c5", 0.4)
    player.play_note("a4", 0.4)
    player.play_note("a4", 0.4)

    pause: .4

    E4: .8
    C4: .8

    D4: .8
    B3: .8

    C4: .8
    A3: .8

    G3  #:.8
    B3: .8

    E4: .8
    C4: .8

    D4: .8
    B3: .8

    C4: .4
    E4: .4
    A4: .4
    A4: .4

    G4  #:1.6

    E5: .4
    B4: .2
    C5: .2
    D5: .4
    C5: .2
    B4: .2

    A4: .4
    A4: .2
    C5: .2
    E5: .4
    D5: .2
    C5: .2

    B4: .4
    B4: .2
    C5: .2
    D5: .4
    E5: .4

    C5: .4
    A4: .4
    A4: .4
    pause: .4

    pause: .2
    D5: .4
    F5: .2
    A5: .4
    G5: .2
    F5: .2

    E5: .6
    C5: .2
    E5: .4
    D5: .2
    C5: .2

    B4: .4
    B4: .2
    C5: .2
    D5: .4
    E5: .4

    C5: .4
    A4: .4
    A4: .4
    pause: .4

def playtwo():
    player = musicalbeeps.Player(volume=1.0,
                                 mute_output=False)

    player.play_note("g5", 0.4)
    player.play_note("b5b", 0.4)
    player.play_note("c5", 0.8)
    player.play_note("g5", 0.4)
    player.play_note("g5", 0.4)
    player.play_note("d5b", 0.2)
    player.play_note("c5", 0.8)

    player.play_note("pause", 0.2)
    player.play_note("g5", 0.4)
    player.play_note("b5b", 0.4)
    player.play_note("c5", 0.8)
    player.play_note("g5", 0.4)
    player.play_note("g5", 0.4)
    player.play_note("d5b", 0.2)
    player.play_note("c5", 0.8)
if __name__ =='__main__':
    playtwo()
