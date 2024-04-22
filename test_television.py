import pytest
from television import Television

def test_power():
    tv = Television()
    assert not tv._Television__status  # Initial state is off
    tv.power()
    assert tv._Television__status  # Power turned on
    tv.power()
    assert not tv._Television__status  # Power turned off

def test_mute():
    tv = Television()
    assert not tv._Television__muted  # Initial state is not muted
    tv.mute()
    assert tv._Television__muted  #x Muted
    tv.mute()
    assert not tv._Television__muted  # Unmuted

def test_channel_up():
    tv = Television()
    assert tv._Television__channel == 0
    tv.channel_up()
    assert tv._Television__channel == 1

    for _ in range(3):
        tv.channel_up()
    assert tv._Television__channel == 0

def test_channel_down():
    tv = Television()
    assert tv._Television__channel == 0
    tv.channel_down()
    assert tv._Television__channel == 3
    for _ in range(3):
        tv.channel_down()
    assert tv._Television__channel == 2

def test_volume_up():
    tv = Television()
    assert tv._Television__volume == 0
    tv.volume_up()
    assert tv._Television__volume == 1
    for _ in range(2):
        tv.volume_up()
    assert tv._Television__volume == 2

def test_volume_down():
    tv = Television()
    assert tv._Television__volume == 0
    tv.volume_down()
    assert tv._Television__volume == 0
    tv.volume_up()
    tv.volume_down()
    assert tv._Television__volume == 0

def test_str():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()  # Turn on power
    tv.channel_up()  # Increase channel
    tv.volume_up()  # Increase volume
    assert str(tv) == "Power = True, Channel = 1, Volume = 1"

